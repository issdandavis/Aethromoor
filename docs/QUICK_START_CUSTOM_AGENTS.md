# Quick Start: Enable Custom Agents (Administrator Guide)

## TL;DR - I'm the Administrator

If you're seeing **"Custom models have been disabled by your enterprise policy administrators"** and you ARE the administrator, here's what you need to do:

## 🚀 Quick Fix (5 Minutes)

### Step 1: Verify Your Permission Level
```
Are you an Enterprise Owner? → Follow Enterprise Path
Are you an Organization Owner? → Follow Organization Path  
Are you just a Repo Admin? → You need help from above
```

### Step 2A: Enterprise Owner Path

**Go here**: GitHub.com → (Profile Photo) → Enterprise → Policies → Copilot

**Change this setting**:
- Find: **"Custom agents"** under AI Controls
- Current: Probably set to "Disabled" ❌
- Change to: **"Allow organizations to decide"** ✅ or **"Enabled everywhere"** ✅

**Click**: Save

**Wait**: 5-10 minutes for the change to propagate

✅ **Done!** Custom agents are now enabled.

---

### Step 2B: Organization Owner Path (No Enterprise)

**Go here**: GitHub.com → Your Org → Settings → Copilot

**Enable this**:
- Find: **"Custom agents"** section
- Toggle: **Enable custom agents** ✅
- Choose: Which repositories can use them

**Click**: Save

**Wait**: 5-10 minutes

✅ **Done!** Your organization can now use custom agents.

---

## Step 3: Verify It Works

1. **Go to this repository**: `.github/agents/`
2. **Check file exists**: `my-agent.agent.md` ✅
3. **Ensure it's on main branch** (merge PR if needed)
4. **Wait 5-10 minutes** after merging
5. **Test in Copilot Chat**:
   ```
   @avalon-lore-steward help me organize lore files
   ```

## 🔧 Troubleshooting

### "I can't find the Enterprise/Organization settings"

**You might not have the required permissions.**

| You See This | You Are | You Can Do |
|-------------|---------|------------|
| Enterprise → Policies → Copilot | Enterprise Owner | Enable for all orgs ✅ |
| Org → Settings → Copilot | Org Owner | Enable for your org ✅ |
| Repo → Settings only | Repo Admin | Create agent files only (need help from above) ⚠️ |
| Nothing above | Contributor | Contact your admin ❌ |

**Fix**: Ask someone with higher permissions, or check if you're logged into the correct GitHub account.

### "Settings are grayed out"

**Cause**: Your organization is under enterprise management, and the enterprise policy is blocking changes.

**Fix**: You need to be an Enterprise Owner to change this, or ask the Enterprise Owner to change the policy.

### "Agent doesn't appear in Copilot"

**Common fixes**:
- ✅ Wait 10 minutes after merging to main
- ✅ Verify `description` field exists in YAML frontmatter
- ✅ Check file is in `.github/agents/` directory
- ✅ Ensure Copilot subscription is Business or Enterprise (not Individual)
- ✅ Refresh VS Code / GitHub interface

## 📍 Direct Links

**Enterprise Settings** (if you have access):
```
https://github.com/enterprises/YOUR-ENTERPRISE/policies/copilot
```

**Organization Settings** (if you have access):
```
https://github.com/organizations/YOUR-ORG/settings/copilot
```

Replace `YOUR-ENTERPRISE` and `YOUR-ORG` with your actual names.

## 🎯 What Exactly You're Enabling

When you enable custom agents, you're allowing:
- ✅ Repository-specific AI assistants (like our Avalon Lore Steward)
- ✅ Organization-wide shared agents
- ✅ Specialized agents with domain knowledge
- ✅ Custom instructions and boundaries for AI behavior

This does **NOT** give unrestricted AI access - you control what agents can do through their configuration files.

## 🔒 Security Note

Custom agents:
- Can only use tools you explicitly allow in their configuration
- Follow boundaries you define in their `.agent.md` files
- Don't have access to secrets unless you explicitly give them
- Are scoped to repositories or organizations you control

**This is safe to enable** if you want specialized AI assistance for your projects.

## 📚 Full Documentation

For complete details, see:
- [`docs/CUSTOM_AGENTS_SETUP.md`](./CUSTOM_AGENTS_SETUP.md) - Complete setup guide
- [GitHub Official Docs](https://docs.github.com/en/copilot/reference/custom-agents-configuration) - Technical reference

## Still Stuck?

### Check Your Subscription
```
GitHub → Settings → Copilot → Check subscription type
```
- ✅ GitHub Copilot Business
- ✅ GitHub Copilot Enterprise  
- ❌ GitHub Copilot Individual (doesn't support custom agents)

### Verify Enterprise/Org Structure
```bash
# Are you in an enterprise?
GitHub → Profile → Switch context → See if Enterprise shows up

# Which org owns this repo?
GitHub → Repository → Settings → Check org name at top
```

### Contact Points
1. **Check permissions**: Ask your GitHub admin if you're not sure of your role
2. **Enterprise policy**: Enterprise Owners can see and change policies
3. **GitHub Support**: Contact with your enterprise/org details if nothing works

---

**Quick Checklist**:
- [ ] I verified my permission level (Enterprise Owner / Org Owner)
- [ ] I navigated to the correct settings page
- [ ] I changed "Custom agents" to "Enabled" or "Allow organizations to decide"
- [ ] I saved the changes
- [ ] I waited 10 minutes
- [ ] I verified the `.agent.md` file is on the main branch
- [ ] I tested in Copilot Chat

If all checked ✅ and it still doesn't work → See full documentation or contact GitHub Support.

---

**Last Updated**: November 2025  
**For**: Avalon Repository Administrators
