# GitHub Copilot Enterprise Access Setup Guide

## Problem Overview

This guide addresses common issues with GitHub Copilot access in enterprise and multi-account scenarios, particularly when setting up "AI employees" or multiple collaborative accounts.

---

## Quick Diagnosis

### Check Your Current Access

1. **Visit Copilot Settings**: https://github.com/settings/copilot
   - If you see Copilot features → ✅ Access enabled
   - If you see "Get access to GitHub Copilot" → ❌ No access

2. **Check Organization Membership**: https://github.com/settings/organizations
   - Verify you're a member of the organization that manages Copilot
   - Check if your role allows Copilot access

3. **Check Which Account is Active**:
   - Visit https://github.com/settings/profile
   - Note the username displayed

---

## Enterprise Setup Process

### For Organization Owners/Admins

#### Step 1: Enable Copilot for Your Organization

1. Go to your organization settings: `https://github.com/organizations/[YOUR-ORG]/settings/copilot`
2. Click **"Set up a plan"** or **"Manage access"**
3. Choose a plan:
   - **Copilot Business**: For team collaboration ($19/user/month)
   - **Copilot Enterprise**: For advanced features ($39/user/month)

#### Step 2: Assign Seats to Users

1. Navigate to organization settings → **Copilot**
2. Click **"Grant access"** or **"Add people"**
3. Search for and select the accounts you want to enable:
   - `issdandavis-netizen`
   - Any other accounts you manage
4. Click **"Add to organization"** if they aren't members yet
5. Enable Copilot access for each user

#### Step 3: Configure Policies

1. Under **Copilot settings**:
   - ✅ Enable "Allow Copilot to use code snippets for suggestions"
   - ✅ Enable "Allow Copilot Chat"
   - ✅ Enable "Allow Copilot in the CLI"
   - ✅ Enable "Copilot Extensions" (for AI agents)

---

## Multi-Account Management

### For Users Managing Multiple Accounts

#### Scenario: Two Personal Accounts Need Copilot

If both accounts are yours:

1. **Option A: Organization Approach** (Recommended)
   - Create a GitHub Organization
   - Add both accounts as members
   - Purchase Copilot Business for the organization
   - Assign seats to both accounts

2. **Option B: Separate Subscriptions**
   - Purchase Copilot Individual for each account ($10/month each)
   - Each account manages its own subscription

#### Setting Up an Organization for AI Collaboration

```bash
# Steps to create an organization:
# 1. Go to: https://github.com/organizations/new
# 2. Choose organization name (e.g., "your-ai-team")
# 3. Select account type (Free or Business)
# 4. Complete setup wizard
```

---

## Troubleshooting Common Issues

### Issue 1: "Extension Not Installed" Error

**Error Message**: `You tried referencing a copilot extension 'issdandavis-netizen' that's not installed`

**Solution**:
- This suggests trying to use a Copilot extension that doesn't exist
- Check available extensions: https://github.com/marketplace?type=apps&copilot_app=true
- Copilot extensions are different from user accounts
- To install an extension:
  1. Go to GitHub Marketplace
  2. Find the Copilot extension
  3. Click "Install"
  4. Grant necessary permissions

### Issue 2: IDE Not Recognizing Copilot Access

**Symptoms**: Copilot works on github.com but not in VS Code/IDE

**Solution**:
1. **Sign out of GitHub in your IDE**:
   ```
   VS Code: Press F1 → "GitHub: Sign Out"
   JetBrains: File → Settings → Version Control → GitHub → Remove account
   ```

2. **Sign back in with the correct account**:
   ```
   VS Code: Press F1 → "GitHub: Sign In"
   JetBrains: File → Settings → Version Control → GitHub → Add account
   ```

3. **Verify Copilot extension is installed**:
   ```
   VS Code: Extensions panel → Search "GitHub Copilot"
   JetBrains: Settings → Plugins → Search "GitHub Copilot"
   ```

4. **Reload the IDE**:
   ```
   VS Code: Press F1 → "Developer: Reload Window"
   JetBrains: File → Invalidate Caches / Restart
   ```

### Issue 3: Account Has Access But Features Are Limited

**Check**:
- Which plan is active? (Individual vs Business vs Enterprise)
- Are specific features enabled by organization policy?
- Go to: `https://github.com/settings/copilot` to see detailed status

### Issue 4: Cannot Add Second Account to Organization

**Requirements**:
- Both accounts must have verified email addresses
- Second account must accept the organization invitation
- Organization must have available Copilot seats

**Steps**:
1. Organization Owner: Settings → People → Invite member
2. Enter the email for the second account
3. Second account: Check email and accept invitation
4. Organization Owner: Settings → Copilot → Assign seat to new member

---

## Setting Up AI Agents with GitHub

### GitHub Copilot Extensions for AI Employees

GitHub now supports Copilot Extensions, which allow AI agents to work within your development workflow.

#### Available Patterns:

1. **GitHub Apps as AI Agents**:
   - Create GitHub Apps to automate tasks
   - Apps can use GitHub API on behalf of users
   - Guide: https://docs.github.com/en/apps/creating-github-apps

2. **Copilot Extensions**:
   - Build custom Copilot extensions
   - Extend Copilot's capabilities with your own AI
   - Guide: https://docs.github.com/en/copilot/building-copilot-extensions

3. **Personal Access Tokens for Automation**:
   - Generate tokens for automated workflows
   - Settings → Developer settings → Personal access tokens → Fine-grained tokens
   - Assign specific repository permissions

#### Example: Setting Up an AI Agent Account

```bash
# 1. Create a new GitHub account for your AI agent
#    (e.g., "your-team-ai-agent")

# 2. Add it to your organization:
#    Organization Settings → People → Invite member

# 3. Assign appropriate permissions:
#    - Repository access (read/write as needed)
#    - Copilot access (if the AI needs code assistance)

# 4. Generate a Personal Access Token for the AI:
#    - Sign in as the AI account
#    - Settings → Developer settings → Personal access tokens
#    - Generate new token with necessary scopes
#    - Store securely (use GitHub Secrets or environment variables)

# 5. Configure your automation to use the token:
#    - In GitHub Actions: Use as a secret
#    - In local scripts: Use environment variables
```

---

## Step-by-Step: Enable Copilot for Both Your Accounts

### Recommended Approach: Organization-Based

1. **Create an Organization** (if you don't have one):
   - Go to: https://github.com/organizations/new
   - Name it (e.g., "issdandavis-workspace")
   - Choose "Free" to start

2. **Upgrade to Copilot Business**:
   - Organization Settings → Copilot → Set up plan
   - Choose "Copilot Business"
   - Enter payment information

3. **Add Both Accounts**:
   - Settings → People → Invite member
   - Invite your second account via email
   - Accept invitation from second account

4. **Assign Copilot Seats**:
   - Settings → Copilot → Grant access
   - Select both accounts
   - Save changes

5. **Verify Access**:
   - Log in as first account → https://github.com/settings/copilot
   - Should show "Managed by [organization-name]"
   - Repeat for second account

---

## Verification Checklist

After setup, verify everything works:

- [ ] Account 1 can access https://github.com/settings/copilot
- [ ] Account 2 can access https://github.com/settings/copilot
- [ ] Both accounts show Copilot is enabled
- [ ] VS Code/IDE recognizes Copilot for account 1
- [ ] VS Code/IDE recognizes Copilot for account 2
- [ ] Copilot Chat works in both accounts
- [ ] CLI Copilot works (`gh copilot suggest` or `gh copilot explain`)
- [ ] Organization dashboard shows both users with Copilot access

---

## Cost Breakdown

### Individual Plans
- **Copilot Individual**: $10/month per account
- **Two accounts**: $20/month total

### Organization Plans
- **Copilot Business**: $19/user/month
- **Two users**: $38/month total
- **Benefits**: Centralized management, organization policies

### Enterprise Plans
- **Copilot Enterprise**: $39/user/month
- **Two users**: $78/month total
- **Benefits**: All Business features + advanced code review, security features

---

## Contact GitHub Support

If you still can't enable access after following this guide:

1. **GitHub Support Portal**: https://support.github.com
2. **Choose topic**: "Copilot" → "Access and billing"
3. **Provide**:
   - Both account usernames
   - Organization name (if applicable)
   - Error messages you're seeing
   - Screenshots of settings pages

---

## Additional Resources

- **Official Copilot Docs**: https://docs.github.com/en/copilot
- **Copilot Business Setup**: https://docs.github.com/en/copilot/overview-of-github-copilot/about-github-copilot-business
- **Copilot Extensions**: https://docs.github.com/en/copilot/building-copilot-extensions
- **GitHub Organizations**: https://docs.github.com/en/organizations
- **GitHub Apps**: https://docs.github.com/en/apps

---

## Quick Command Reference

```bash
# Check GitHub CLI authentication
gh auth status

# Login to GitHub CLI
gh auth login

# Switch GitHub accounts
gh auth switch

# Check Copilot CLI
gh copilot --version

# Install Copilot CLI extension
gh extension install github/gh-copilot

# Use Copilot to explain code
gh copilot explain "your code or command"

# Use Copilot to suggest commands
gh copilot suggest "what you want to do"
```

---

## Notes for This Repository

This documentation is specific to the Avalon repository's needs for:
- Multi-account collaboration on narrative and game development
- Potential AI agent assistance with ChoiceScript conversion
- Enterprise-level tooling for multi-generational project management

**Repository-specific considerations**:
- Both accounts should have write access to this repository
- Copilot can assist with ChoiceScript scene expansion
- AI agents could help automate game.js → ChoiceScript conversion
- Consider using GitHub Actions with Copilot for automated testing

---

**Last Updated**: November 24, 2025  
**Maintained By**: issdandavis  
**For**: Avalon Repository / Polly's Wingscroll Project
