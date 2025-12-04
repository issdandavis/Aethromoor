#!/bin/bash

# GitHub Copilot Access Checker and Setup Assistant
# This script helps diagnose and guide you through fixing Copilot access issues

set -e

echo "=========================================="
echo "GitHub Copilot Access Diagnostic Tool"
echo "=========================================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check if gh CLI is installed
if ! command -v gh &> /dev/null; then
    echo -e "${RED}✗ GitHub CLI (gh) is not installed${NC}"
    echo ""
    echo "Please install it first:"
    echo "  macOS:   brew install gh"
    echo "  Linux:   See https://github.com/cli/cli/blob/trunk/docs/install_linux.md"
    echo "  Windows: See https://github.com/cli/cli#windows"
    exit 1
fi

echo -e "${GREEN}✓ GitHub CLI is installed${NC}"
echo ""

# Check authentication status
echo "Checking GitHub authentication..."
if ! gh auth status &> /dev/null; then
    echo -e "${RED}✗ Not authenticated with GitHub${NC}"
    echo ""
    echo "Please run: gh auth login"
    exit 1
fi

# Get current user
CURRENT_USER=$(gh api user --jq '.login')
echo -e "${GREEN}✓ Authenticated as: ${CURRENT_USER}${NC}"
echo ""

# Check Copilot access for current user
echo "Checking Copilot access..."
COPILOT_STATUS=$(gh api /user/copilot_seat_management 2>&1 || echo "NO_ACCESS")

if [[ "$COPILOT_STATUS" == *"NO_ACCESS"* ]] || [[ "$COPILOT_STATUS" == *"404"* ]]; then
    echo -e "${RED}✗ Current account (${CURRENT_USER}) does NOT have Copilot access${NC}"
    HAS_COPILOT=false
else
    echo -e "${GREEN}✓ Current account (${CURRENT_USER}) HAS Copilot access${NC}"
    HAS_COPILOT=true
fi
echo ""

# Check organization memberships
echo "Checking organization memberships..."
ORGS=$(gh api /user/orgs --jq '.[].login' 2>/dev/null || echo "")

if [ -z "$ORGS" ]; then
    echo -e "${YELLOW}⚠ Not a member of any organizations${NC}"
    echo ""
    echo "To enable Copilot for multiple accounts:"
    echo "  1. Create a GitHub Organization (https://github.com/organizations/new)"
    echo "  2. Add both accounts as members"
    echo "  3. Purchase Copilot Business for the organization"
    echo "  4. Assign Copilot seats to both accounts"
else
    echo -e "${GREEN}✓ Member of these organizations:${NC}"
    for org in $ORGS; do
        echo "  - $org"
        
        # Check if organization has Copilot
        ORG_COPILOT=$(gh api "/orgs/$org/copilot/billing" 2>&1 || echo "NO_ACCESS")
        if [[ "$ORG_COPILOT" == *"NO_ACCESS"* ]] || [[ "$ORG_COPILOT" == *"404"* ]]; then
            echo -e "    ${RED}✗ Organization does NOT have Copilot enabled${NC}"
        else
            echo -e "    ${GREEN}✓ Organization has Copilot enabled${NC}"
        fi
    done
fi
echo ""

# Generate action plan
echo "=========================================="
echo "ACTION PLAN"
echo "=========================================="
echo ""

if [ "$HAS_COPILOT" = false ]; then
    echo -e "${YELLOW}Your current account needs Copilot access.${NC}"
    echo ""
    echo "Choose ONE of these options:"
    echo ""
    echo "OPTION 1: Individual Subscription ($10/month)"
    echo "  1. Visit: https://github.com/settings/copilot"
    echo "  2. Click 'Get access to GitHub Copilot'"
    echo "  3. Choose 'Individual' plan"
    echo "  4. Add payment method"
    echo ""
    echo "OPTION 2: Organization Subscription (Recommended for multiple accounts)"
    if [ -z "$ORGS" ]; then
        echo "  1. Create organization: https://github.com/organizations/new"
        echo "  2. Set up Copilot Business: https://github.com/organizations/[ORG]/settings/copilot"
        echo "  3. Invite your second account to the organization"
        echo "  4. Assign Copilot seats to both accounts"
    else
        echo "  For organization: ${ORGS}"
        echo "  1. Visit: https://github.com/organizations/${ORGS}/settings/copilot"
        echo "  2. Set up Copilot Business plan"
        echo "  3. Grant access to your accounts"
    fi
    echo ""
    echo "OPTION 3: Ask Organization Admin"
    echo "  If someone else manages your organization (like 'isdandavis2'):"
    echo "  1. Contact them and request Copilot access"
    echo "  2. Provide your GitHub username: ${CURRENT_USER}"
    echo ""
else
    echo -e "${GREEN}✓ Current account has Copilot access!${NC}"
    echo ""
    echo "To enable Copilot for your SECOND account:"
    echo ""
    if [ -z "$ORGS" ]; then
        echo "Since you're not in an organization, you need to:"
        echo "  EITHER: Create an organization and add both accounts"
        echo "  OR: Purchase individual Copilot for the second account"
    else
        echo "If ${ORGS} manages Copilot:"
        echo "  1. Log in as organization owner"
        echo "  2. Visit: https://github.com/organizations/${ORGS}/settings/people"
        echo "  3. Invite your second account"
        echo "  4. Visit: https://github.com/organizations/${ORGS}/settings/copilot"
        echo "  5. Grant access to the second account"
    fi
fi

echo ""
echo "=========================================="
echo "IDE SETUP"
echo "=========================================="
echo ""
echo "After getting Copilot access, configure your IDE:"
echo ""
echo "VS Code:"
echo "  1. Install 'GitHub Copilot' extension"
echo "  2. Press F1 → 'GitHub: Sign In'"
echo "  3. Choose account with Copilot access"
echo "  4. Reload window (F1 → 'Developer: Reload Window')"
echo ""
echo "JetBrains IDEs:"
echo "  1. Settings → Plugins → Search 'GitHub Copilot'"
echo "  2. Install and restart"
echo "  3. Settings → Version Control → GitHub → Add account"
echo "  4. Sign in with account that has Copilot"
echo ""

echo "=========================================="
echo "VERIFICATION"
echo "=========================================="
echo ""
echo "After setup, verify Copilot works:"
echo "  1. Visit: https://github.com/settings/copilot"
echo "  2. Should show Copilot features, not 'Get access'"
echo "  3. In IDE, open a code file"
echo "  4. Start typing - you should see Copilot suggestions"
echo "  5. Test Copilot Chat (if available)"
echo ""

echo "For detailed help, see:"
echo "  - docs/GITHUB_COPILOT_ENTERPRISE_SETUP.md"
echo "  - docs/COPILOT_TROUBLESHOOTING.md"
echo ""
echo "=========================================="
