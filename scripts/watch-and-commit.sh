#!/usr/bin/env bash
# File Watcher for Auto-Commit
# Monitors file changes and automatically commits them at specified intervals

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AUTO_COMMIT_SCRIPT="$SCRIPT_DIR/auto-commit.sh"
WATCH_INTERVAL=300  # Default: 5 minutes (300 seconds)
CONFIG_FILE="${AUTO_COMMIT_CONFIG:-$SCRIPT_DIR/auto-commit-config.sh}"

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

print_info() {
    echo -e "${BLUE}[$(date +'%Y-%m-%d %H:%M:%S')]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[$(date +'%Y-%m-%d %H:%M:%S')]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[$(date +'%Y-%m-%d %H:%M:%S')]${NC} $1"
}

usage() {
    cat << EOF
Usage: $0 [OPTIONS]

Watches for file changes and auto-commits at specified intervals

OPTIONS:
    -i SECONDS    Watch interval in seconds (default: 300 = 5 minutes)
    -m MESSAGE    Custom commit message prefix
    -P            Don't auto-push (commit only)
    -h            Show this help message

EXAMPLES:
    $0                          # Watch with 5-minute intervals
    $0 -i 60                    # Watch with 1-minute intervals
    $0 -i 600 -P                # Watch every 10 minutes, don't push
    $0 -m "Work session:"       # Custom commit message prefix

USAGE:
    Run this script and leave it running in the background.
    It will check for changes every WATCH_INTERVAL seconds.
    Press Ctrl+C to stop watching.

EOF
}

# Parse arguments - use array for safety
declare -a AUTO_COMMIT_ARGS_ARRAY=()
CUSTOM_MESSAGE=""

while getopts "i:m:Ph" opt; do
    case $opt in
        i) WATCH_INTERVAL="$OPTARG" ;;
        m) CUSTOM_MESSAGE="$OPTARG" ;;
        P) AUTO_COMMIT_ARGS_ARRAY+=("-P") ;;
        h) usage; exit 0 ;;
        \?) echo "Invalid option: -$OPTARG"; usage; exit 1 ;;
    esac
done

# Add custom message to args array if provided
if [ -n "$CUSTOM_MESSAGE" ]; then
    AUTO_COMMIT_ARGS_ARRAY+=("-m" "$CUSTOM_MESSAGE")
fi

# Validate watch interval
if ! [[ "$WATCH_INTERVAL" =~ ^[0-9]+$ ]]; then
    echo "Error: Watch interval must be a positive number"
    exit 1
fi

if [ "$WATCH_INTERVAL" -lt 10 ]; then
    print_warning "Watch interval is very short ($WATCH_INTERVAL seconds). Consider using a longer interval."
fi

# Check if auto-commit script exists
if [ ! -f "$AUTO_COMMIT_SCRIPT" ]; then
    echo "Error: Auto-commit script not found at $AUTO_COMMIT_SCRIPT"
    exit 1
fi

# Make sure auto-commit script is executable
chmod +x "$AUTO_COMMIT_SCRIPT"

# Cleanup on exit
cleanup() {
    print_info "Stopping file watcher..."
    exit 0
}

trap cleanup SIGINT SIGTERM

# Main watch loop
main() {
    print_info "Starting file watcher..."
    print_info "Watch interval: $WATCH_INTERVAL seconds"
    print_info "Auto-commit script: $AUTO_COMMIT_SCRIPT"
    print_info "Press Ctrl+C to stop"
    echo
    
    local iteration=0
    
    while true; do
        iteration=$((iteration + 1))
        print_info "Check #$iteration - Looking for changes..."
        
        # Check if there are any changes
        if [ -n "$(git status --porcelain)" ]; then
            print_info "Changes detected. Running auto-commit..."
            
            # Run auto-commit script with safe argument expansion
            if "$AUTO_COMMIT_SCRIPT" "${AUTO_COMMIT_ARGS_ARRAY[@]}"; then
                print_success "Auto-commit completed successfully"
            else
                print_warning "Auto-commit failed or was cancelled"
            fi
        else
            print_info "No changes detected"
        fi
        
        echo
        print_info "Next check in $WATCH_INTERVAL seconds..."
        sleep "$WATCH_INTERVAL"
    done
}

main
