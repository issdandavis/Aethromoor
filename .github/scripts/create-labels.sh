#!/bin/bash

# Script to create GitHub labels for the Avalon repository
# This supports the automated workflows and project organization

echo "Creating GitHub labels for Avalon repository..."

# Note: This script requires GitHub CLI (gh) to be installed and authenticated
# Run: gh auth login

# Check if gh is installed
if ! command -v gh &> /dev/null; then
    echo "Error: GitHub CLI (gh) is not installed"
    echo "Install from: https://cli.github.com/"
    exit 1
fi

# Check if authenticated
if ! gh auth status &> /dev/null; then
    echo "Error: Not authenticated with GitHub CLI"
    echo "Run: gh auth login"
    exit 1
fi

# Function to create label
create_label() {
    local name=$1
    local color=$2
    local description=$3
    
    echo "Creating label: $name"
    gh label create "$name" --color "$color" --description "$description" 2>/dev/null || \
    gh label edit "$name" --color "$color" --description "$description" 2>/dev/null
}

# Priority Labels
create_label "priority: critical" "d73a4a" "Critical issue requiring immediate attention"
create_label "priority: high" "ff9800" "High priority issue"
create_label "priority: medium" "ffc107" "Medium priority issue"
create_label "priority: low" "00e676" "Low priority issue"

# Type Labels
create_label "bug" "d73a4a" "Something isn't working"
create_label "enhancement" "a2eeef" "New feature or request"
create_label "documentation" "0075ca" "Improvements or additions to documentation"
create_label "question" "d876e3" "Further information is requested"
create_label "duplicate" "cfd3d7" "This issue or pull request already exists"
create_label "invalid" "e4e669" "This doesn't seem right"
create_label "wontfix" "ffffff" "This will not be worked on"

# Content Labels
create_label "game-content" "7057ff" "Related to game scenes and gameplay"
create_label "lore" "c5def5" "Related to worldbuilding and lore"
create_label "writing" "bfd4f2" "Related to narrative and writing"
create_label "choicescript" "f9d0c4" "Related to ChoiceScript implementation"

# Technical Labels
create_label "github-actions" "000000" "Related to GitHub Actions workflows"
create_label "security" "d73a4a" "Security-related issue or improvement"
create_label "dependencies" "0366d6" "Pull requests that update a dependency file"
create_label "tests" "0e8a16" "Related to testing"
create_label "automation" "fbca04" "Related to automation and CI/CD"

# Size Labels (for PRs)
create_label "size: XS" "c2e0c6" "Extra small PR (< 10 lines)"
create_label "size: S" "7cfc00" "Small PR (< 50 lines)"
create_label "size: M" "ffa500" "Medium PR (< 200 lines)"
create_label "size: L" "ff4500" "Large PR (< 500 lines)"
create_label "size: XL" "8b0000" "Extra large PR (500+ lines)"

# Status Labels
create_label "status: in progress" "1d76db" "Work is currently in progress"
create_label "status: blocked" "b60205" "Blocked by dependencies or issues"
create_label "status: needs review" "fbca04" "Needs review from maintainers"
create_label "status: ready to merge" "0e8a16" "Approved and ready to merge"

# AI & Collaboration Labels
create_label "ai-generated" "e99695" "Content or code generated with AI assistance"
create_label "ai-review" "f9d0c4" "Needs AI review or validation"
create_label "good first issue" "7057ff" "Good for newcomers"
create_label "help wanted" "008672" "Extra attention is needed"

# Project-Specific Labels
create_label "phase-1" "0052cc" "Phase 1 development tasks"
create_label "phase-2" "5319e7" "Phase 2 development tasks"
create_label "phase-3" "b60205" "Phase 3 development tasks"
create_label "polish" "fef2c0" "Polish and refinement work"
create_label "beta-testing" "ff9800" "Related to beta testing"

echo ""
echo "✅ Labels created successfully!"
echo ""
echo "To view all labels, run: gh label list"
echo "To delete a label, run: gh label delete <label-name>"
