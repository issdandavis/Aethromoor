#!/usr/bin/env bash
# Auto-commit script for Avalon repository
# This script automatically commits and pushes changes to help streamline workflow

set -euo pipefail

# Configuration
CONFIG_FILE="${AUTO_COMMIT_CONFIG:-$(dirname "$0")/auto-commit-config.sh}"
DEFAULT_BRANCH="main"
DEFAULT_MESSAGE_PREFIX="Auto-commit:"
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Load configuration if exists
if [ -f "$CONFIG_FILE" ]; then
    source "$CONFIG_FILE"
fi

# Default configuration values (can be overridden in config file)
: ${COMMIT_MESSAGE_PREFIX:=$DEFAULT_MESSAGE_PREFIX}
: ${AUTO_PUSH:=true}
: ${DRY_RUN:=false}
: ${INCLUDE_UNTRACKED:=true}
: ${MAX_FILE_SIZE_MB:=10}
: ${EXCLUDE_PATTERNS:="*.log *.tmp node_modules/ .env"}

# Function to print colored output
print_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to check if we're in a git repository
check_git_repo() {
    if ! git rev-parse --git-dir > /dev/null 2>&1; then
        print_error "Not a git repository!"
        exit 1
    fi
}

# Function to check for large files
check_file_sizes() {
    local max_size_bytes=$((MAX_FILE_SIZE_MB * 1024 * 1024))
    local large_files=()
    
    while IFS= read -r file; do
        if [ -f "$file" ]; then
            # Portable file size check - try different methods
            local size=0
            if [ -n "$(command -v stat)" ]; then
                # Try BSD stat first (macOS)
                size=$(stat -f%z "$file" 2>/dev/null || true)
                # If that failed, try GNU stat (Linux)
                if [ -z "$size" ] || [ "$size" = "0" ]; then
                    size=$(stat -c%s "$file" 2>/dev/null || echo 0)
                fi
            else
                # Fallback using ls
                size=$(ls -l "$file" 2>/dev/null | awk '{print $5}' || echo 0)
            fi
            
            if [ "$size" -gt "$max_size_bytes" ]; then
                # Portable size formatting
                local size_mb=$((size / 1024 / 1024))
                large_files+=("$file (${size_mb}MB)")
            fi
        fi
    done < <(git diff --name-only --cached)
    
    if [ ${#large_files[@]} -gt 0 ]; then
        print_warning "Large files detected (>${MAX_FILE_SIZE_MB}MB):"
        printf '%s\n' "${large_files[@]}"
        read -p "Continue anyway? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            return 1
        fi
    fi
    return 0
}

# Function to display usage
usage() {
    cat << EOF
Usage: $0 [OPTIONS]

Auto-commit script for Avalon repository

OPTIONS:
    -m MESSAGE    Custom commit message (default: auto-generated with timestamp)
    -n            Dry run - show what would be committed without committing
    -p            Push after commit (default: true)
    -P            Don't push after commit
    -u            Include untracked files (default: true)
    -U            Don't include untracked files
    -h            Show this help message

EXAMPLES:
    $0                              # Auto-commit all changes with timestamp
    $0 -m "Update lore files"       # Custom commit message
    $0 -n                           # Dry run to see what would be committed
    $0 -U -P                        # Commit tracked files only, don't push

CONFIGURATION:
    Create scripts/auto-commit-config.sh to set defaults:
        COMMIT_MESSAGE_PREFIX="Auto:"
        AUTO_PUSH=true
        INCLUDE_UNTRACKED=true
        MAX_FILE_SIZE_MB=10
        EXCLUDE_PATTERNS="*.log *.tmp"

EOF
}

# Parse command line arguments
CUSTOM_MESSAGE=""
while getopts "m:npPuUh" opt; do
    case $opt in
        m) CUSTOM_MESSAGE="$OPTARG" ;;
        n) DRY_RUN=true ;;
        p) AUTO_PUSH=true ;;
        P) AUTO_PUSH=false ;;
        u) INCLUDE_UNTRACKED=true ;;
        U) INCLUDE_UNTRACKED=false ;;
        h) usage; exit 0 ;;
        \?) print_error "Invalid option: -$OPTARG"; usage; exit 1 ;;
    esac
done

# Main execution
main() {
    print_info "Starting auto-commit process..."
    
    # Check if we're in a git repository
    check_git_repo
    
    # Check for changes
    if [ -z "$(git status --porcelain)" ]; then
        print_info "No changes to commit. Working tree clean."
        exit 0
    fi
    
    # Show current status
    print_info "Current repository status:"
    git status --short
    echo
    
    # Add files to staging
    if [ "$INCLUDE_UNTRACKED" = true ]; then
        if [ "$DRY_RUN" = true ]; then
            print_info "[DRY RUN] Would add all files (including untracked)"
        else
            print_info "Adding all files (including untracked)..."
            git add -A
        fi
    else
        if [ "$DRY_RUN" = true ]; then
            print_info "[DRY RUN] Would add tracked files only"
        else
            print_info "Adding tracked files only..."
            git add -u
        fi
    fi
    
    # Check if anything is staged
    if [ -z "$(git diff --cached --name-only)" ]; then
        print_info "No changes staged for commit."
        exit 0
    fi
    
    # Show what will be committed
    print_info "Files to be committed:"
    git diff --cached --name-status
    echo
    
    # Check file sizes
    if ! check_file_sizes; then
        print_error "Commit cancelled due to file size concerns."
        exit 1
    fi
    
    # Generate commit message
    if [ -n "$CUSTOM_MESSAGE" ]; then
        COMMIT_MSG="$CUSTOM_MESSAGE"
    else
        # Auto-generate message based on changed files (cache the diff output)
        local cached_files=$(git diff --cached --name-only)
        local changed_files=$(echo "$cached_files" | wc -l | tr -d ' ')
        COMMIT_MSG="${COMMIT_MESSAGE_PREFIX} Updated ${changed_files} file(s) at ${TIMESTAMP}"
    fi
    
    # Commit changes
    if [ "$DRY_RUN" = true ]; then
        print_info "[DRY RUN] Would commit with message: '$COMMIT_MSG'"
    else
        print_info "Committing changes..."
        if git commit -m "$COMMIT_MSG"; then
            print_success "Changes committed successfully!"
            print_info "Commit message: $COMMIT_MSG"
        else
            print_error "Commit failed!"
            exit 1
        fi
    fi
    
    # Push changes
    if [ "$AUTO_PUSH" = true ]; then
        if [ "$DRY_RUN" = true ]; then
            print_info "[DRY RUN] Would push to remote repository"
        else
            print_info "Pushing to remote repository..."
            local current_branch=$(git rev-parse --abbrev-ref HEAD)
            if git push origin "$current_branch"; then
                print_success "Changes pushed successfully to $current_branch!"
            else
                print_warning "Push failed. You may need to pull first or check permissions."
                print_info "Run: git push origin $current_branch"
                exit 1
            fi
        fi
    else
        print_info "Skipping push (AUTO_PUSH=false)"
        print_info "To push manually, run: git push"
    fi
    
    print_success "Auto-commit process completed!"
}

# Run main function
main
