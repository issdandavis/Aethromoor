#!/bin/bash
# Auto Sync Agent - Quick Control Script

set -e

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_header() {
    echo -e "${BLUE}========================================${NC}"
    echo -e "${BLUE}  🔄 Auto Sync Agent Control${NC}"
    echo -e "${BLUE}========================================${NC}"
    echo ""
}

print_status() {
    echo -e "${GREEN}✓${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

show_help() {
    cat << EOF
Usage: $(basename "$0") [COMMAND]

Commands:
    status      Show current sync status
    manual      Trigger manual sync now
    enable      Enable automatic syncing
    disable     Disable automatic syncing
    schedule    Change sync schedule
    history     View recent sync commits
    help        Show this help message

Examples:
    $(basename "$0") status        # Check current status
    $(basename "$0") manual        # Run sync now
    $(basename "$0") history       # View sync history

For full documentation, see: docs/AUTO_SYNC_AGENT.md
EOF
}

check_gh_cli() {
    if ! command -v gh &> /dev/null; then
        print_error "GitHub CLI (gh) not found"
        echo "Install from: https://cli.github.com/"
        exit 1
    fi
}

show_status() {
    print_header
    echo "📊 Repository Status"
    echo ""
    
    # Current branch
    BRANCH=$(git branch --show-current)
    echo "Current branch: $BRANCH"
    
    # Git status
    if [[ -n $(git status --porcelain) ]]; then
        print_warning "Local changes detected:"
        git status --short
    else
        print_status "Working tree clean"
    fi
    
    echo ""
    
    # Check if behind/ahead
    git fetch origin --quiet
    BEHIND=$(git rev-list HEAD..origin/$BRANCH --count 2>/dev/null || echo "0")
    AHEAD=$(git rev-list origin/$BRANCH..HEAD --count 2>/dev/null || echo "0")
    
    echo "Branch sync status:"
    echo "  • Commits behind origin: $BEHIND"
    echo "  • Commits ahead of origin: $AHEAD"
    
    echo ""
    
    # Check workflow status
    echo "🤖 Auto Sync Agent Status"
    if gh workflow view auto-sync-agent.yml &>/dev/null; then
        STATUS=$(gh workflow view auto-sync-agent.yml --json state -q .state 2>/dev/null || echo "unknown")
        if [ "$STATUS" = "active" ]; then
            print_status "Workflow is enabled"
        else
            print_warning "Workflow is disabled"
        fi
        
        # Last run
        LAST_RUN=$(gh run list --workflow=auto-sync-agent.yml --limit 1 --json conclusion,startedAt -q '.[0] | "\(.conclusion) at \(.startedAt)"' 2>/dev/null || echo "No runs yet")
        echo "  • Last run: $LAST_RUN"
    else
        print_error "Workflow not found or GitHub CLI not authenticated"
        echo "  Run: gh auth login"
    fi
    
    echo ""
}

manual_sync() {
    print_header
    echo "🚀 Triggering Manual Sync"
    echo ""
    
    check_gh_cli
    
    BRANCH=$(git branch --show-current)
    echo "Branch: $BRANCH"
    echo ""
    
    read -p "Proceed with manual sync? (y/N) " -n 1 -r
    echo
    
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        gh workflow run auto-sync-agent.yml -f branch="$BRANCH"
        print_status "Sync triggered"
        echo ""
        echo "Monitor progress:"
        echo "  gh run watch"
        echo ""
        echo "Or visit: https://github.com/$(gh repo view --json nameWithOwner -q .nameWithOwner)/actions"
    else
        print_warning "Cancelled"
    fi
}

enable_workflow() {
    print_header
    echo "✅ Enabling Auto Sync Agent"
    echo ""
    
    check_gh_cli
    
    if gh workflow enable auto-sync-agent.yml; then
        print_status "Auto Sync Agent enabled"
        echo ""
        echo "The agent will now run every 30 minutes automatically."
        echo "View runs: gh run list --workflow=auto-sync-agent.yml"
    else
        print_error "Failed to enable workflow"
    fi
}

disable_workflow() {
    print_header
    echo "⏸️  Disabling Auto Sync Agent"
    echo ""
    
    check_gh_cli
    
    read -p "Are you sure you want to disable automatic syncing? (y/N) " -n 1 -r
    echo
    
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        if gh workflow disable auto-sync-agent.yml; then
            print_status "Auto Sync Agent disabled"
            echo ""
            echo "You can still trigger manual syncs with:"
            echo "  $(basename "$0") manual"
        else
            print_error "Failed to disable workflow"
        fi
    else
        print_warning "Cancelled"
    fi
}

change_schedule() {
    print_header
    echo "⏰ Change Sync Schedule"
    echo ""
    
    echo "Current schedule: Every 30 minutes"
    echo ""
    echo "Suggested schedules:"
    echo "  1) Every 15 minutes: */15 * * * *"
    echo "  2) Every 30 minutes: */30 * * * * (current)"
    echo "  3) Every hour:       0 * * * *"
    echo "  4) Every 2 hours:    0 */2 * * *"
    echo "  5) Every 6 hours:    0 */6 * * *"
    echo ""
    
    print_warning "To change the schedule, edit:"
    echo "  .github/workflows/auto-sync-agent.yml"
    echo ""
    echo "Find the 'schedule' section and update the cron expression."
    echo ""
    echo "Cron syntax: minute hour day month weekday"
    echo "Example: '*/30 * * * *' = every 30 minutes"
    echo ""
    echo "Learn more: https://crontab.guru/"
}

show_history() {
    print_header
    echo "📜 Recent Auto Sync Commits"
    echo ""
    
    # Show last 10 auto-sync commits
    git log --grep="Auto-sync" --oneline --decorate --graph -10 || {
        print_warning "No auto-sync commits found yet"
    }
    
    echo ""
}

# Main script logic
case "${1:-}" in
    status)
        show_status
        ;;
    manual)
        manual_sync
        ;;
    enable)
        enable_workflow
        ;;
    disable)
        disable_workflow
        ;;
    schedule)
        change_schedule
        ;;
    history)
        show_history
        ;;
    help|--help|-h)
        show_help
        ;;
    *)
        if [ -n "${1:-}" ]; then
            print_error "Unknown command: $1"
            echo ""
        fi
        show_help
        exit 1
        ;;
esac
