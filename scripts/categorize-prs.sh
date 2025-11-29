#!/bin/bash
# PR Categorization Helper
# This script helps you understand what each PR does

echo "════════════════════════════════════════════════"
echo "  📋 PR CATEGORIZATION HELPER"
echo "════════════════════════════════════════════════"
echo ""

# Check if gh CLI is installed
if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI (gh) not found!"
    echo ""
    echo "Please install it from: https://cli.github.com/"
    echo ""
    echo "Or use the web interface at: https://github.com/issdandavis/Aethromoor/pulls"
    exit 1
fi

echo "✅ GitHub CLI found!"
echo ""

# Check authentication
if ! gh auth status &> /dev/null; then
    echo "❌ Not authenticated with GitHub"
    echo ""
    echo "Run: gh auth login"
    exit 1
fi

echo "✅ Authenticated with GitHub"
echo ""
echo "════════════════════════════════════════════════"
echo ""

# Count total PRs
TOTAL_PRS=$(gh pr list --state open --limit 1000 --json number | jq '. | length')

echo "📊 PR SUMMARY"
echo "─────────────────────────────────────────────────"
echo "Total Open PRs: $TOTAL_PRS"
echo ""

# Count draft PRs
DRAFT_COUNT=$(gh pr list --state open --draft --limit 1000 --json number | jq '. | length')
echo "Draft/WIP PRs: $DRAFT_COUNT"
echo ""

echo "════════════════════════════════════════════════"
echo ""

# Categorize by title keywords
echo "📁 CATEGORIZATION BY TYPE"
echo "─────────────────────────────────────────────────"
echo ""

echo "📚 DOCUMENTATION PRs:"
gh pr list --state open --limit 1000 --json number,title,isDraft | \
  jq -r '.[] | select(.title | test("(?i)(readme|documentation|guide|doc)")) | "  #\(.number) - \(.title) \(if .isDraft then "[DRAFT]" else "" end)"'
echo ""

echo "⚙️ AUTOMATION/WORKFLOW PRs:"
gh pr list --state open --limit 1000 --json number,title,isDraft | \
  jq -r '.[] | select(.title | test("(?i)(automation|workflow|ci|github actions)")) | "  #\(.number) - \(.title) \(if .isDraft then "[DRAFT]" else "" end)"'
echo ""

echo "🤖 AI/COPILOT PRs:"
gh pr list --state open --limit 1000 --json number,title,isDraft | \
  jq -r '.[] | select(.title | test("(?i)(ai|copilot|agent|enterprise)")) | "  #\(.number) - \(.title) \(if .isDraft then "[DRAFT]" else "" end)"'
echo ""

echo "🎮 GAME CONTENT PRs:"
gh pr list --state open --limit 1000 --json number,title,isDraft | \
  jq -r '.[] | select(.title | test("(?i)(choicescript|expedition|scene|content|spark|familiar)")) | "  #\(.number) - \(.title) \(if .isDraft then "[DRAFT]" else "" end)"'
echo ""

echo "🔧 INFRASTRUCTURE/SETUP PRs:"
gh pr list --state open --limit 1000 --json number,title,isDraft | \
  jq -r '.[] | select(.title | test("(?i)(setup|infrastructure|config|saml)")) | "  #\(.number) - \(.title) \(if .isDraft then "[DRAFT]" else "" end)"'
echo ""

echo "════════════════════════════════════════════════"
echo ""

# Show oldest PRs
echo "⏰ OLDEST OPEN PRs (May be outdated):"
echo "─────────────────────────────────────────────────"
gh pr list --state open --limit 10 | head -10
echo ""

echo "════════════════════════════════════════════════"
echo ""

# Show draft PRs
echo "✏️ DRAFT PRs (Work in Progress):"
echo "─────────────────────────────────────────────────"
gh pr list --state open --draft --limit 100
echo ""

echo "════════════════════════════════════════════════"
echo ""

echo "💡 SUGGESTED NEXT STEPS:"
echo "─────────────────────────────────────────────────"
echo ""
echo "1. Review the categories above"
echo "2. For each PR, decide:"
echo "   - ✅ Merge it (if work is complete and good)"
echo "   - 🗑️  Close it (if outdated or duplicate)"
echo "   - ⏸️  Keep open (if still needed)"
echo ""
echo "3. Common commands:"
echo "   - View PR: gh pr view PR_NUMBER"
echo "   - Merge PR: gh pr merge PR_NUMBER --squash --delete-branch"
echo "   - Close PR: gh pr close PR_NUMBER --comment 'Reason for closing'"
echo "   - Mark ready: gh pr ready PR_NUMBER"
echo ""
echo "4. Start with:"
echo "   - Documentation PRs (usually safe to merge)"
echo "   - Close obvious duplicates"
echo "   - Review draft PRs to see if they're still needed"
echo ""

echo "════════════════════════════════════════════════"
echo ""
echo "📋 For detailed guidance, see:"
echo "   - PULL_REQUEST_MANAGEMENT_GUIDE.md"
echo "   - PR_CLEANUP_TRACKER.md"
echo "   - GIT_PUSH_PULL_GUIDE.md"
echo ""
echo "════════════════════════════════════════════════"
