# GitHub Copilot Troubleshooting Guide

## Quick Fixes for Common Errors

---

## Error: "Extension Not Installed"

### Full Error Message
```
You tried referencing a copilot extension 'issdandavis-netizen' that's not installed. 
To learn more about installing extensions, visit https://gh.io/install-copilot-extensions
```

### What This Means
- You're trying to use a Copilot Extension that doesn't exist or isn't installed
- **Important**: Copilot Extensions are NOT the same as GitHub user accounts
- The username 'issdandavis-netizen' is a GitHub user, not a Copilot Extension

### Solutions

#### 1. If You're Trying to Use a Copilot Extension

**Browse Available Extensions**:
- Visit: https://github.com/marketplace?type=apps&copilot_app=true
- Examples:
  - Docker extension
  - Sentry extension
  - DataStax extension

**Install an Extension**:
1. Go to GitHub Marketplace
2. Find the extension you need
3. Click "Install" or "Set up a plan"
4. Grant necessary permissions to your account/organization

#### 2. If You're Trying to Enable Copilot Access

This error might appear if you're confusing:
- **Copilot Extensions** (third-party integrations)
- **Copilot Access** (enabling Copilot for your account)

**Enable Copilot for your account**:
1. Go to: https://github.com/settings/copilot
2. If you see "Get access", you need a subscription
3. Choose:
   - Individual plan: $10/month
   - Ask organization admin to assign a seat
   - Purchase through your organization

#### 3. If You're Setting Up an Organization

You may be trying to use an account name where an organization name should be used.

**Check**:
- Organization names and user names are different
- Organizations manage Copilot seats for multiple users
- Create an organization at: https://github.com/organizations/new

---

## Common Issues by Scenario

### Scenario 1: Two Accounts, Both Need Copilot

**Problem**: You have accounts `issdandavis-netizen` and another account, both need Copilot

**Solution Path A - Organization** (Best for collaboration):
```
1. Create a GitHub Organization
2. Add both accounts as members
3. Purchase Copilot Business for the organization
4. Assign Copilot seats to both accounts
Cost: $38/month for 2 users
```

**Solution Path B - Individual** (Simpler but separate):
```
1. Log into first account
2. Go to https://github.com/settings/copilot
3. Purchase Copilot Individual ($10/month)
4. Log into second account
5. Repeat steps 2-3
Cost: $20/month for 2 accounts
```

### Scenario 2: IDE Not Working with Copilot

**Problem**: Copilot works on GitHub.com but not in VS Code/JetBrains

**Diagnostic Steps**:
```bash
# 1. Check which account is logged in
# VS Code: Click account icon (bottom left)
# JetBrains: File → Settings → Version Control → GitHub

# 2. Verify Copilot extension is installed
# VS Code: Extensions → Search "GitHub Copilot"
# JetBrains: Plugins → Search "GitHub Copilot"

# 3. Check Copilot status in IDE
# VS Code: Open Command Palette (F1) → "GitHub Copilot: Status"
```

**Fix**:
```
1. Sign out of GitHub in your IDE
2. Sign back in with the account that has Copilot access
3. Reload/restart the IDE
4. Try generating code with Copilot
```

### Scenario 3: Organization Admin Setup

**Problem**: You're the organization owner and need to enable Copilot for team members

**Steps**:
```
1. Go to: https://github.com/organizations/[YOUR-ORG]/settings/copilot
2. Click "Set up a plan"
3. Choose Copilot Business ($19/user/month)
4. Add payment method
5. Go to "Grant access"
6. Search for team members by username
7. Click "Add" for each user
8. Save changes
```

**Verify**:
- Each user should now see Copilot enabled at https://github.com/settings/copilot
- Status should show "Managed by [organization-name]"

---

## Account vs Extension Clarification

### GitHub User Accounts
- **Example**: `issdandavis-netizen`, `octocat`
- **Purpose**: Individual or bot accounts that can:
  - Push code
  - Create pull requests
  - Comment on issues
  - Use Copilot (if enabled)

### Copilot Extensions
- **Example**: `docker`, `sentry`, `datastax`
- **Purpose**: Third-party integrations that extend Copilot's capabilities:
  - Query external services in Copilot Chat
  - Access specialized knowledge
  - Integrate with specific tools

### Key Difference
```
User Account: issdandavis-netizen
↓
Can have Copilot access enabled
↓
Can install Copilot Extensions
↓
Can use extensions in Copilot Chat

Extension: docker (example)
↓
Provides Docker knowledge to Copilot
↓
Available in Copilot Chat via @docker
↓
Requires installation from Marketplace
```

---

## Verification Commands

### Check Your Setup

```bash
# 1. Check GitHub CLI authentication
gh auth status
# Should show: Logged in to github.com as [your-username]

# 2. Check which accounts are configured
gh auth status --show-token
# (Don't share the token!)

# 3. Switch between accounts (if multiple configured)
gh auth switch

# 4. Check Copilot CLI is available
gh copilot --version
# If not installed:
gh extension install github/gh-copilot

# 5. Test Copilot CLI
gh copilot suggest "list files in current directory"
```

### Browser-Based Checks

```
Account 1:
1. Log into GitHub as issdandavis-netizen
2. Visit: https://github.com/settings/copilot
3. Should see Copilot features, not "Get access"

Account 2:
1. Log into GitHub as [second-account]
2. Visit: https://github.com/settings/copilot
3. Should see Copilot features, not "Get access"

Organization:
1. Log in as organization owner
2. Visit: https://github.com/organizations/[org]/settings/copilot
3. Should see both accounts with Copilot access
```

---

## Still Stuck?

### Information to Gather Before Contacting Support

1. **Account Information**:
   - Primary account username: _______________
   - Secondary account username: _______________
   - Organization name (if applicable): _______________

2. **Current Status**:
   - [ ] Account 1 has Copilot access (visit settings/copilot to check)
   - [ ] Account 2 has Copilot access
   - [ ] Organization exists and manages Copilot
   - [ ] Copilot works in IDE for account 1
   - [ ] Copilot works in IDE for account 2

3. **Error Messages**:
   - Copy exact error message
   - Screenshot of error (if visual)
   - Which tool shows the error (GitHub.com, VS Code, CLI, etc.)

4. **What You're Trying to Do**:
   - Enable Copilot for multiple accounts
   - Install a Copilot extension
   - Set up organization Copilot management
   - Other: _______________

### Contact Options

**GitHub Support**:
- Visit: https://support.github.com
- Choose: "Copilot" → "Access and billing"
- Include information from above

**Community Forums**:
- GitHub Community: https://github.community
- Stack Overflow: Tag `github-copilot`

**Documentation**:
- Copilot Docs: https://docs.github.com/en/copilot
- Organizations: https://docs.github.com/en/organizations

---

## Next Steps

After resolving access issues:

1. **Configure Your IDE**:
   - Install GitHub Copilot extension
   - Sign in with correct account
   - Test code suggestions

2. **Explore Copilot Features**:
   - Code completions
   - Copilot Chat
   - CLI assistance (`gh copilot`)
   - Copilot in Pull Requests

3. **Set Up Team Policies** (if using organization):
   - Configure code suggestions settings
   - Set up exclusions (if needed)
   - Enable/disable specific features

4. **For This Repository**:
   - Use Copilot for ChoiceScript conversion
   - Assist with game scene expansion
   - Help with narrative consistency checks

---

**Quick Reference**: See `docs/GITHUB_COPILOT_ENTERPRISE_SETUP.md` for detailed setup instructions.

---

**Last Updated**: November 24, 2025  
**For**: Avalon Repository / Polly's Wingscroll Project
