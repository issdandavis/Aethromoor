# 🔄 Auto Sync Agent - Quick Start

## What It Does

Automatically **pulls** changes from GitHub and **pushes** your local changes every 30 minutes. No more manual `git pull` or `git push` needed!

---

## ⚡ Quick Setup (2 minutes)

### 1. Enable the Workflow

**Option A: GitHub UI**
```
1. Go to Actions tab
2. Find "Auto Sync Agent"
3. Click "Enable workflow"
```

**Option B: Command Line**
```bash
gh workflow enable auto-sync-agent.yml
```

### 2. Test It

Trigger a manual sync to test:

```bash
# Using the control script
./scripts/auto-sync-control.sh manual

# Or using GitHub CLI
gh workflow run auto-sync-agent.yml
```

### 3. Done! 🎉

The agent now runs every 30 minutes automatically.

---

## 🎮 Usage

### Check Status
```bash
./scripts/auto-sync-control.sh status
```

### Manual Sync Now
```bash
./scripts/auto-sync-control.sh manual
```

### View Sync History
```bash
./scripts/auto-sync-control.sh history
```

### Disable Temporarily
```bash
./scripts/auto-sync-control.sh disable
```

---

## 📋 What Gets Synced

✅ **Pulls:**
- Latest changes from remote branch
- New commits from team members
- Updates to shared files

✅ **Commits & Pushes:**
- All your local changes
- New files you created
- Modified files

❌ **Never Commits:**
- Files in `.gitignore`
- Secret keys (`.env`, `.auth/keys.json`)
- Build artifacts

---

## 🔒 Safety Features

- **Conflict Detection** - Creates issue if conflicts found
- **Force Push Protection** - Requires manual approval
- **Branch Protection** - Respects protected branch rules
- **Automatic Reports** - Shows what was synced

---

## 🚨 Troubleshooting

### "Conflicts detected"
Check GitHub issues for auto-created conflict resolution guide.

### "Permission denied"
Enable write permissions:
```
Settings → Actions → General → Workflow permissions
✅ Read and write permissions
```

### "Workflow not running"
1. Check it's enabled in Actions tab
2. Manually trigger once
3. Check GitHub Actions minutes quota

---

## 📚 Full Documentation

**Complete Guide:** [docs/AUTO_SYNC_AGENT.md](docs/AUTO_SYNC_AGENT.md)

**Topics Covered:**
- How it works (step-by-step)
- Customization (change schedule, add hooks)
- Advanced usage (multi-branch, notifications)
- Security considerations
- Integration with other agents

---

## 💡 Pro Tips

1. **Review `.gitignore`** before enabling
2. **Test with a feature branch** first
3. **Monitor first few runs** in Actions tab
4. **Combine with other AI agents** for full automation

---

## 🆘 Quick Help

**Control Script:**
```bash
./scripts/auto-sync-control.sh help
```

**GitHub Actions:**
```
Repository → Actions → Auto Sync Agent
```

**Create Issue:**
Add `auto-sync` label for agent-related questions

---

**Ready?** Enable the workflow and let the agent handle your git sync! 🚀

For the complete guide with all features and customization options, see **[docs/AUTO_SYNC_AGENT.md](docs/AUTO_SYNC_AGENT.md)**.
