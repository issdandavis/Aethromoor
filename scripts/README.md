# GitHub Copilot Access Fix - Scripts

## Quick Start

Run this script to diagnose and fix your Copilot access issues:

```bash
./scripts/check-copilot-access.sh
```

This will:
1. Check if you're authenticated with GitHub
2. Verify your current Copilot access status
3. List your organization memberships
4. Provide step-by-step instructions to fix access issues

## What This Script Does

The script **cannot automatically fix** Copilot access (GitHub doesn't allow that), but it **will tell you exactly what to do** to fix it yourself.

## Prerequisites

1. **Install GitHub CLI**:
   ```bash
   # macOS
   brew install gh
   
   # Linux (Debian/Ubuntu)
   sudo apt install gh
   
   # Linux (Fedora/RHEL)
   sudo dnf install gh
   
   # Windows
   winget install GitHub.cli
   ```

2. **Authenticate with GitHub**:
   ```bash
   gh auth login
   ```
   Choose:
   - GitHub.com
   - HTTPS
   - Yes (authenticate Git)
   - Login with a web browser

## Running the Diagnostic

```bash
cd /path/to/Avalon
./scripts/check-copilot-access.sh
```

The script will output:
- ✓ or ✗ for each check
- Your current GitHub username
- Whether you have Copilot access
- Your organization memberships
- Specific action plan to fix access

## Common Scenarios

### Scenario 1: No Copilot Access on Either Account

**What script will say**:
```
✗ Current account (your-username) does NOT have Copilot access
⚠ Not a member of any organizations
```

**Fix**:
1. Follow the "OPTION 1" or "OPTION 2" in the script output
2. Either buy individual Copilot or create an organization

### Scenario 2: One Account Has Access, Other Doesn't

**What to do**:
1. Run script while logged in as first account (has access)
2. Note which organization manages Copilot
3. Log in to GitHub web as organization owner
4. Add second account to organization
5. Assign Copilot seat to second account

### Scenario 3: Organization Exists But No Copilot

**What script will say**:
```
✓ Member of these organizations:
  - your-org
    ✗ Organization does NOT have Copilot enabled
```

**Fix**:
1. Visit: https://github.com/organizations/your-org/settings/copilot
2. Set up Copilot Business plan
3. Add payment method
4. Grant access to members

## Manual Steps (When Script Cannot Run)

If you can't run the script, follow these manual steps:

### Step 1: Check Your Current Access
1. Visit: https://github.com/settings/copilot
2. If you see Copilot features → ✅ You have access
3. If you see "Get access" → ❌ No access

### Step 2: For Account Without Access

**Option A - Individual Plan** ($10/month):
1. Visit: https://github.com/settings/copilot
2. Click "Get access to GitHub Copilot"
3. Choose "Individual" plan
4. Add payment method

**Option B - Organization Plan** (Best for 2+ accounts):
1. Create organization: https://github.com/organizations/new
2. Add both accounts as members
3. Enable Copilot Business: https://github.com/organizations/[ORG]/settings/copilot
4. Assign seats to both accounts

### Step 3: Verify in IDE

**VS Code**:
1. Install "GitHub Copilot" extension
2. F1 → "GitHub: Sign In"
3. Sign in with account that has Copilot
4. F1 → "Developer: Reload Window"
5. Open a code file and start typing

**JetBrains**:
1. Settings → Plugins → "GitHub Copilot"
2. Install and restart
3. Settings → Version Control → GitHub → Add account
4. Sign in with account that has Copilot
5. Open a code file and start typing

## Troubleshooting the Script

### "gh: command not found"
Install GitHub CLI first (see Prerequisites above)

### "Not authenticated with GitHub"
Run: `gh auth login`

### Script runs but shows wrong account
Switch accounts:
```bash
gh auth switch
# or
gh auth logout
gh auth login  # login with different account
```

### Want to check both accounts
Run the script twice:
```bash
# First account
gh auth login  # login as account 1
./scripts/check-copilot-access.sh

# Second account  
gh auth login  # login as account 2
./scripts/check-copilot-access.sh
```

## Additional Resources

- **Detailed Setup Guide**: `docs/GITHUB_COPILOT_ENTERPRISE_SETUP.md`
- **Troubleshooting Guide**: `docs/COPILOT_TROUBLESHOOTING.md`
- **GitHub Copilot Docs**: https://docs.github.com/en/copilot

## Important Notes

⚠️ **This script cannot**:
- Automatically purchase Copilot subscriptions
- Modify GitHub organization settings
- Grant Copilot access without proper permissions

✅ **This script can**:
- Diagnose your current setup
- Tell you exactly what's wrong
- Provide step-by-step instructions to fix it
- Save you time by checking everything at once

## Support

If the script doesn't help, contact GitHub Support:
1. Visit: https://support.github.com
2. Choose: "Copilot" → "Access and billing"
3. Provide:
   - Your GitHub username
   - Organization name (if applicable)
   - Error messages from the script
   - Screenshots of your settings pages

---

**Last Updated**: November 24, 2025  
**For**: Avalon Repository / Polly's Wingscroll Project
