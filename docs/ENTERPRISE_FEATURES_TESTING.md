# GitHub Copilot Enterprise Features Testing Guide

## Overview
This guide helps you verify that all GitHub Copilot Enterprise features you've paid for are working correctly. If any test fails, there may be a configuration or permissions issue.

## Your Subscription
You have a **GitHub Copilot Enterprise** subscription, which includes all Business features plus additional enterprise-specific capabilities.

## Feature Testing Checklist

Use this checklist to verify all your paid features are working:

---

## 🎯 Core Copilot Features (Available to All Tiers)

### ✅ Code Completions
**What it is**: AI-powered code suggestions as you type

**How to test**:
1. Open VS Code or your IDE
2. Create a new file (e.g., `test.js`)
3. Start typing a function: `function calculateSum(`
4. Wait for Copilot suggestions to appear
5. Press Tab to accept

**Expected Result**: Gray text suggestions appear as you type

**If it fails**: 
- Check Copilot is enabled in your IDE
- Verify your Copilot subscription is active
- Check you're signed into the correct GitHub account

---

### ✅ Copilot Chat
**What it is**: Conversational AI assistance in your IDE

**How to test**:
1. In VS Code: Press `Ctrl+Shift+I` (Windows/Linux) or `Cmd+Shift+I` (Mac)
2. Type a question: "How do I read a file in Node.js?"
3. Review the response

**Expected Result**: Copilot Chat panel opens and responds to your question

**If it fails**:
- Install GitHub Copilot Chat extension
- Verify Copilot is enabled
- Check network connectivity

---

## 💼 Business Features (Included in Your Enterprise Plan)

### ✅ Organization-Wide Access
**What it is**: Copilot access for all organization members

**How to test**:
1. Go to GitHub → Your Organization → Settings → Copilot
2. Check "User access" section
3. Verify members have access

**Expected Result**: Organization members can enable Copilot

**If it fails**:
- Verify you're an organization owner
- Check billing is current
- Review organization policies

---

### ✅ Policy Management
**What it is**: Control Copilot usage across your organization

**How to test**:
1. Go to Organization → Settings → Copilot → Policies
2. Check available policy options:
   - Suggestions matching public code
   - Content exclusions
   - IDE configurations

**Expected Result**: You can view and modify organization policies

**If it fails**:
- Verify you're an organization owner
- Check you have Copilot Business/Enterprise subscription
- Contact GitHub Support if settings are missing

---

### ✅ Content Exclusions
**What it is**: Exclude specific files/repositories from Copilot

**How to test**:
1. Organization → Settings → Copilot → Content exclusion
2. Add a test exclusion pattern: `**/secrets/**`
3. Save

**Expected Result**: Exclusion is saved and applied

**If it fails**:
- Verify organization ownership
- Check subscription level
- Review enterprise policies (they may override org settings)

---

## 🏢 Enterprise-Only Features (What You're Paying For)

### ✅ Enterprise Policies (Top Priority)
**What it is**: Enterprise-wide Copilot governance across all organizations

**How to test**:
1. Click your profile picture → Enterprise
2. Select your enterprise
3. Go to Policies → Copilot
4. Review available policies:
   - Copilot in GitHub.com
   - Copilot in the IDE
   - Copilot on mobile
   - Custom agents
   - AI models

**Expected Result**: You see enterprise-level policy controls

**If it fails**:
- ❌ **YOU SHOULD HAVE THIS** - You paid for Enterprise
- Verify you're an enterprise owner (not just org owner)
- Check if you have multiple enterprises (select correct one)
- Contact GitHub Support - this is a billing/provisioning issue

**Policy Options You Should Have**:
```
✅ Enabled everywhere (force on for all orgs)
✅ Disabled (force off for all orgs)
✅ Allow organizations to decide (flexible)
```

---

### ✅ Custom Agents (YOUR KEY ISSUE)
**What it is**: Create specialized AI assistants for repositories

**How to test**:
1. Enterprise → Policies → Copilot → Custom agents
2. Check current setting
3. Change to "Enabled everywhere" or "Allow organizations to decide"
4. Save

**Expected Result**: Custom agents can be enabled

**If it fails**:
- ❌ **YOU SHOULD HAVE THIS** - This is an Enterprise feature you paid for
- If this option is missing, contact GitHub Support immediately
- If it's grayed out, check you're logged in as enterprise owner
- If it says "disabled," you just need to enable it (not a billing issue)

**After enabling**:
1. Wait 5-10 minutes
2. Go to your repository
3. Navigate to `.github/agents/`
4. Verify agents are available in Copilot Chat

---

### ✅ GitHub Models Integration
**What it is**: Access to different AI models (GPT-4, Claude, etc.)

**How to test**:
1. Enterprise → Policies → Copilot
2. Look for "AI models" or "GitHub Models" section
3. Check available models and settings

**Expected Result**: You can configure which AI models are available

**If it fails**:
- ❌ **YOU SHOULD HAVE THIS** - Enterprise feature
- Verify enterprise ownership
- Contact GitHub Support if missing

**Available models should include**:
- GPT-4 (various versions)
- Claude (various versions)  
- Other supported models

---

### ✅ GitHub Copilot in GitHub.com
**What it is**: Use Copilot directly on GitHub.com (not just IDE)

**How to test**:
1. Go to GitHub.com
2. Navigate to any repository
3. Look for Copilot icon in the interface
4. Click to open Copilot panel
5. Ask a question about the repository

**Expected Result**: Copilot panel opens on GitHub.com

**If it fails**:
- Check Enterprise → Policies → Copilot in GitHub.com is enabled
- Verify you're in an organization with Copilot access
- Try different browser (clear cache)

---

### ✅ Copilot Pull Request Summaries
**What it is**: AI-generated PR descriptions and summaries

**How to test**:
1. Create or open a pull request
2. Look for Copilot suggestions in PR description
3. Click "Generate PR summary" or similar button

**Expected Result**: Copilot generates PR summary automatically

**If it fails**:
- Check enterprise/org policies allow this
- Verify in a repository with Copilot access
- May need to enable in repository settings

---

### ✅ Copilot Knowledge Bases (Beta/Preview)
**What it is**: Create custom knowledge bases for your organization

**How to test**:
1. Enterprise or Organization → Settings
2. Look for "Copilot" → "Knowledge bases" or similar
3. Check if you can create/manage knowledge bases

**Expected Result**: Knowledge base management interface available

**If it fails**:
- May be in beta/preview - check if you need to enable preview features
- Verify enterprise subscription
- Contact GitHub Support to enable preview access

---

### ✅ Advanced Security Integration
**What it is**: Copilot Autofix for security vulnerabilities

**How to test**:
1. Enterprise → Policies → Advanced Security
2. Check "Copilot Autofix" setting
3. Enable if available

**Expected Result**: Copilot can suggest fixes for security issues

**If it fails**:
- Verify GitHub Advanced Security is enabled
- Check enterprise policies allow it
- May require additional GHAS license

---

### ✅ Usage Analytics and Reporting
**What it is**: Detailed usage metrics across organization

**How to test**:
1. Enterprise → Insights
2. Look for Copilot usage reports
3. Check metrics like:
   - Active users
   - Acceptance rates
   - Organization trends

**Expected Result**: Detailed analytics dashboard

**If it fails**:
- ❌ **YOU SHOULD HAVE THIS** - Enterprise feature
- Verify enterprise ownership
- Check if data is still being collected (may take 24-48 hours)

---

### ✅ Audit Logs for Copilot
**What it is**: Track Copilot usage and policy changes

**How to test**:
1. Enterprise → Audit log
2. Filter by "copilot" events
3. Review Copilot-related activities

**Expected Result**: Copilot events appear in audit log

**If it fails**:
- Verify enterprise ownership
- Check if any Copilot activities have occurred recently
- May take time for events to appear

---

### ✅ IP Indemnification
**What it is**: Legal protection for Copilot-generated code

**Status**: Automatic with Enterprise subscription

**How to verify**:
1. Review your GitHub Enterprise contract
2. Check GitHub's Legal documentation
3. Verify in billing settings

**Expected Result**: IP indemnification is included in your plan

**Note**: This is a legal feature, not a technical one to test

---

## 🧪 Testing Your Custom Agents (Specific to Your Issue)

Now let's test the custom agents in this repository:

### Test 1: Verify Agents Exist
```bash
# Check agent files exist
ls -la .github/agents/

# Expected output:
# my-agent.agent.md (Avalon Lore Steward)
# choicescript-converter.agent.md (ChoiceScript Converter)
```

### Test 2: Validate Agent Configuration
```bash
# Check agent file format
head -20 .github/agents/my-agent.agent.md

# Expected: YAML frontmatter with:
# - name: Avalon Lore Steward
# - description: (some description)
# - target: github-copilot
```

### Test 3: Enable Custom Agents at Enterprise Level
1. Go to: GitHub → Enterprise → Policies → Copilot
2. Find: "Custom agents" section
3. Current setting: Probably "Disabled" ❌
4. Change to: "Enabled everywhere" ✅
5. Click: Save
6. Wait: 10 minutes

### Test 4: Verify Agent Activation
1. Wait 10 minutes after enabling
2. Merge this PR to main branch
3. Wait another 5 minutes
4. Open VS Code Copilot Chat
5. Type: `@avalon-lore-steward`
6. Expected: Agent should auto-complete and be available

### Test 5: Use Custom Agent
```
# In Copilot Chat
@avalon-lore-steward Help me verify the timeline for Izack Thorne

# Expected Result:
# Agent responds with lore-specific guidance
# References IZACK_MASTER_CHRONICLE_UPDATED.txt
# Provides timeline validation
```

### Test 6: Test Second Agent
```
# In Copilot Chat
@choicescript-converter How do I convert an HTML scene to ChoiceScript?

# Expected Result:
# Agent provides ChoiceScript conversion guidance
# References proper syntax
# Suggests stat tracking implementation
```

---

## 📊 Feature Availability Matrix

| Feature | Individual | Business | Enterprise | You Should Have |
|---------|-----------|----------|------------|-----------------|
| Code completions | ✅ | ✅ | ✅ | ✅ YES |
| Copilot Chat | ✅ | ✅ | ✅ | ✅ YES |
| Org management | ❌ | ✅ | ✅ | ✅ YES |
| Policy controls | ❌ | ✅ | ✅ | ✅ YES |
| **Custom agents** | ❌ | ❌ | ✅ | ✅ **YES - YOU PAID FOR THIS** |
| **Enterprise policies** | ❌ | ❌ | ✅ | ✅ **YES - YOU PAID FOR THIS** |
| GitHub Models | ❌ | Limited | ✅ | ✅ YES |
| Usage analytics | ❌ | Org-level | Enterprise-level | ✅ YES |
| Audit logs | ❌ | Org-level | Enterprise-level | ✅ YES |
| IP indemnification | ❌ | ✅ | ✅ | ✅ YES |
| Advanced Security integration | ❌ | ❌ | ✅ | ✅ YES |

---

## 🚨 Red Flags - Contact GitHub Support If:

### Critical Issues (You Paid For These)
1. ❌ No "Enterprise" menu in your GitHub profile
2. ❌ No "Custom agents" option in Enterprise → Policies → Copilot
3. ❌ No "AI models" configuration in enterprise settings
4. ❌ No enterprise-level usage analytics
5. ❌ Custom agents still disabled after enabling in enterprise policies

### Verification Issues
1. ❌ Can't access Enterprise → Policies (you might not be enterprise owner)
2. ❌ Enterprise policies are grayed out (permission issue)
3. ❌ Billing shows "Business" instead of "Enterprise"

### How to Check Your Actual Subscription Level
```
1. Go to: https://github.com/settings/copilot
2. Check: "Your GitHub Copilot subscription"
3. Should say: "GitHub Copilot Enterprise" or show enterprise name
4. Billing: Should show enterprise-level features

OR

1. Profile → Enterprise → Settings → Billing
2. Check: Active Copilot subscription
3. Verify: Enterprise-level features are listed
```

---

## 🔧 Step-by-Step Enterprise Setup

### Week 1: Basic Setup
- [ ] Verify enterprise subscription is active
- [ ] Confirm you're enterprise owner
- [ ] Enable Copilot at enterprise level
- [ ] Configure basic policies

### Week 2: Custom Agents Setup
- [ ] Enable custom agents in enterprise policies
- [ ] Wait 10 minutes for propagation
- [ ] Verify agents appear in organization settings
- [ ] Test agents in a repository

### Week 3: Advanced Features
- [ ] Configure GitHub Models access
- [ ] Set up usage analytics monitoring
- [ ] Review audit logs
- [ ] Configure Advanced Security integration

### Week 4: Team Rollout
- [ ] Train team on custom agents
- [ ] Share agent documentation
- [ ] Gather feedback
- [ ] Iterate on agent configurations

---

## 📞 Support Contacts

### GitHub Support
**When to contact**: Missing enterprise features you paid for

**How to contact**:
1. Go to: https://support.github.com/
2. Select: "GitHub Copilot" → "Enterprise"
3. Describe: "Paid for Enterprise, missing [feature name]"
4. Include:
   - Enterprise name
   - Organization name
   - Account email
   - Specific missing feature

**What to ask for**:
- "I have GitHub Copilot Enterprise subscription but cannot access custom agents"
- "Please verify my enterprise has all paid features enabled"
- "Custom agents option missing from Enterprise → Policies"

### Quick Checks Before Contacting Support
1. ✅ Verify you're logged into correct account
2. ✅ Confirm you're enterprise owner (not just org owner)
3. ✅ Check billing is current and shows "Enterprise"
4. ✅ Wait 24 hours after subscription starts
5. ✅ Clear browser cache and retry

---

## 🎯 Your Specific Issue: Custom Agents

### Current Situation
- ❌ Error: "Custom models have been disabled by your enterprise policy administrators"
- ✅ You ARE the administrator
- ✅ You HAVE paid for Enterprise

### Root Cause
Custom agents are disabled by default in enterprise policies. You need to enable them.

### Solution
1. **Go to**: GitHub → Profile → Enterprise → Your Enterprise Name
2. **Navigate**: Policies → Copilot → Custom agents
3. **Change from**: "Disabled" ❌
4. **Change to**: "Enabled everywhere" ✅ or "Allow organizations to decide" ✅
5. **Save**: Click Save Changes
6. **Wait**: 10 minutes for changes to propagate
7. **Verify**: Custom agents now available in this repository

### If That Doesn't Work
1. Check you selected the correct enterprise (if you have multiple)
2. Verify you're enterprise owner: Enterprise → Settings → People → Your role
3. Clear browser cache and retry
4. Wait 24 hours (rare, but settings can take time)
5. Contact GitHub Support with: "Enterprise subscription, custom agents not enabling"

---

## ✅ Success Criteria

You'll know everything is working when:

- ✅ You can access Enterprise → Policies → Copilot
- ✅ Custom agents option is present and can be enabled
- ✅ After enabling, agents appear in Copilot Chat as `@agent-name`
- ✅ You can use `@avalon-lore-steward` in this repository
- ✅ You can use `@choicescript-converter` in this repository
- ✅ Usage analytics show Copilot activity
- ✅ Audit logs track Copilot policy changes
- ✅ All enterprise policies are configurable (not grayed out)

---

## 📝 Quick Reference Commands

### Check Your Subscription
```bash
# In terminal
gh copilot status

# Expected output should mention "Enterprise" tier
```

### Verify Agent Files
```bash
# List agent files
ls -la .github/agents/

# Validate YAML frontmatter
head -20 .github/agents/my-agent.agent.md
```

### Test in Copilot Chat
```
# Basic test
@workspace What is this repository about?

# Agent test (after enabling)
@avalon-lore-steward Help me with lore consistency

# Second agent test
@choicescript-converter Convert a scene to ChoiceScript
```

---

**Last Updated**: November 2025  
**Your Subscription**: GitHub Copilot Enterprise  
**Support**: If any enterprise feature is missing, contact GitHub Support immediately
