# 🔄 Auto Sync Agent

## Overview

The Auto Sync Agent is an automated GitHub Actions workflow that continuously pulls changes from the remote repository and pushes local changes. It acts as a "git employee" that keeps your branches synchronized without manual intervention.

---

## 🎯 What It Does

The agent automatically:
1. **Pulls** the latest changes from the remote branch
2. **Commits** any local changes with automatic commit messages
3. **Pushes** the changes back to the remote repository
4. **Detects conflicts** and creates issues when manual intervention is needed
5. **Reports status** of each sync operation

---

## ⚙️ Configuration

### Automatic Schedule
- **Runs every 30 minutes** by default
- Configured via cron: `*/30 * * * *`
- Can be adjusted in `.github/workflows/auto-sync-agent.yml`

### Manual Trigger
You can manually run the sync from GitHub:
1. Go to **Actions** → **Auto Sync Agent**
2. Click **Run workflow**
3. Optional: Specify a branch name
4. Optional: Enable force push (use with caution)

---

## 🚀 Usage

### Basic Usage (Automatic)

The agent runs automatically every 30 minutes. No action needed!

### Manual Sync

**Via GitHub UI:**
```
Actions → Auto Sync Agent → Run workflow
```

**Via GitHub CLI:**
```bash
# Sync current branch
gh workflow run auto-sync-agent.yml

# Sync specific branch
gh workflow run auto-sync-agent.yml -f branch=main

# Force push (use with caution)
gh workflow run auto-sync-agent.yml -f force_push=true
```

---

## 📋 How It Works

### Step-by-Step Process

1. **Checkout Repository**
   - Fetches the full repository history
   - Uses GitHub token for authentication

2. **Pull Latest Changes**
   - Fetches from origin
   - Attempts rebase first (cleaner history)
   - Falls back to merge if rebase fails
   - Detects and reports conflicts

3. **Check Local Changes**
   - Scans for uncommitted files
   - Counts commits ahead/behind remote
   - Reports status

4. **Commit Local Changes**
   - Adds all changes (`git add -A`)
   - Creates timestamped commit
   - Skips if no changes detected

5. **Push to Remote**
   - Pushes committed changes
   - Uses `--force-with-lease` if requested
   - Reports success or failure

6. **Conflict Handling**
   - Creates GitHub issue if conflicts detected
   - Provides manual resolution steps
   - Adds labels for tracking

---

## 🛡️ Safety Features

### Conflict Detection
If the agent encounters merge conflicts:
- ✅ Stops the sync process
- ✅ Creates a GitHub issue with resolution steps
- ✅ Adds labels: `auto-sync`, `conflict`, `needs-attention`
- ✅ Provides the workflow run link for debugging

### Force Push Protection
- Only available via manual trigger
- Uses `--force-with-lease` (safer than `--force`)
- Prevents accidental overwrites
- Requires explicit user approval

### Branch Protection
- Respects protected branch rules
- Won't force push to protected branches
- Requires appropriate permissions

---

## 📊 Sync Reports

After each run, the agent generates a report:

```markdown
## 🔄 Auto Sync Report

**Branch:** main
**Time:** 2024-12-04 12:00:00 UTC

✅ **Pulled:** Changes from remote
✅ **Committed:** Local changes saved
✅ **Pushed:** Changes to remote

### Branch Status
- Commits behind: 0
- Commits ahead: 2
```

---

## 🔧 Customization

### Change Sync Frequency

Edit `.github/workflows/auto-sync-agent.yml`:

```yaml
on:
  schedule:
    # Every 15 minutes
    - cron: '*/15 * * * *'
    
    # Every hour
    - cron: '0 * * * *'
    
    # Every 6 hours
    - cron: '0 */6 * * *'
```

### Customize Commit Messages

Edit the commit step:

```yaml
- name: Commit local changes
  run: |
    git commit -m "Your custom message" \
               -m "Additional details"
```

### Add Pre-Commit Hooks

Add validation before committing:

```yaml
- name: Run tests before commit
  run: |
    npm test  # or your test command
    
- name: Commit local changes
  if: success()
  run: |
    git add -A
    git commit -m "Auto-sync: Changes validated"
```

---

## 🚨 Troubleshooting

### Issue: "Push failed - may need to pull first"

**Cause:** Someone else pushed to the branch between pull and push.

**Solution:**
1. The next scheduled run will retry
2. Or manually trigger the workflow again
3. Or pull and push manually:
   ```bash
   git pull origin <branch>
   git push origin <branch>
   ```

### Issue: "Conflicts detected"

**Cause:** Remote and local changes conflict.

**Solution:**
1. Check for the auto-created GitHub issue
2. Follow the resolution steps in the issue:
   ```bash
   git pull origin <branch>
   # Resolve conflicts in your editor
   git add .
   git commit
   git push origin <branch>
   ```

### Issue: "Permission denied"

**Cause:** Insufficient GitHub token permissions.

**Solution:**
1. Go to **Settings** → **Actions** → **General**
2. Under "Workflow permissions", ensure:
   - ✅ Read and write permissions enabled
   - ✅ Allow GitHub Actions to create and approve pull requests

### Issue: "Workflow not running"

**Cause:** Workflow may be disabled or schedule not triggering.

**Solution:**
1. Check **Actions** → **Auto Sync Agent** is enabled
2. Manually trigger once to "wake it up"
3. Check GitHub Actions limits (minutes used)

---

## 💡 Best Practices

### 1. Use for Development Branches
✅ **Good:** Feature branches, development branches  
❌ **Avoid:** Main/production branches without review

### 2. Review Before Enabling
- Test manually first
- Understand what will be auto-committed
- Consider impact on team workflow

### 3. Set Up Branch Protection
```
Settings → Branches → Add rule
- Require pull request reviews
- Require status checks
- Include administrators
```

### 4. Monitor Sync Activity
- Check **Actions** tab regularly
- Review auto-created issues
- Watch for conflict patterns

### 5. Combine with Other Automation
Works great with:
- Auto-formatters (Prettier, Black)
- Linters (ESLint, Pylint)
- Code generators
- AI agents (like the ones in this repo!)

---

## 🔗 Integration with Other Agents

The Auto Sync Agent works seamlessly with other automation in this repository:

### AI Scene Writer
- Scene writer creates new content
- Auto Sync commits and pushes it
- No manual intervention needed

### AI Content Polisher
- Content polisher improves scenes
- Auto Sync saves the changes
- Continuous improvement loop

### Agent Management
- Agents make changes
- Auto Sync keeps everything synchronized
- Team always has latest work

### Example Combined Workflow:
```
1. AI Scene Writer creates new scene (every 3 hours)
2. Auto Sync commits and pushes (30 min later)
3. AI Content Polisher improves it (every 4 hours)
4. Auto Sync commits and pushes (30 min later)
5. Repeat...
```

---

## 📚 Advanced Usage

### Sync Multiple Branches

Create separate workflow files:

```yaml
# .github/workflows/auto-sync-main.yml
on:
  schedule:
    - cron: '*/30 * * * *'
jobs:
  sync-main:
    steps:
      - uses: actions/checkout@v4
        with:
          ref: main
      # ... sync steps
```

### Add Notifications

Notify on Discord/Slack:

```yaml
- name: Notify Discord
  if: steps.status.outputs.has_changes == 'true'
  run: |
    curl -X POST "${{ secrets.DISCORD_WEBHOOK_URL }}" \
      -H "Content-Type: application/json" \
      -d '{"content": "🔄 Auto Sync: Changes pushed to ${{ steps.branch.outputs.name }}"}'
```

### Create Summary Comment

Add to pull requests:

```yaml
- name: Comment on PR
  uses: actions/github-script@v7
  with:
    script: |
      github.rest.issues.createComment({
        issue_number: context.issue.number,
        body: '🔄 Auto Sync completed successfully!'
      })
```

---

## 🔐 Security Considerations

### Token Security
- Uses `GITHUB_TOKEN` (automatic)
- Limited to repository scope
- No external secrets required

### What Gets Committed
The agent commits **everything** in the working directory:
- Modified files
- New files
- Deleted files (via `git add -A`)

### What Doesn't Get Committed
- Files in `.gitignore`
- Protected files (like in `.auth/keys.json`)
- Large files blocked by Git LFS

### Recommendations
1. Keep `.gitignore` updated
2. Don't store secrets in tracked files
3. Use the `.auth/` directory for sensitive data
4. Review sync reports regularly

---

## 📖 Related Documentation

- **Security Guide:** `docs/SECURITY.md`
- **GitHub Secrets Setup:** `docs/GITHUB_SECRETS_SETUP.md`
- **AI Autonomous Workflow:** `docs/AI_AUTONOMOUS_WORKFLOW.md`
- **Automation Guide:** `docs/AUTOMATION_GUIDE.md`

---

## 🆘 Getting Help

### Check Workflow Runs
```
Actions → Auto Sync Agent → Latest run
```

### View Sync History
```bash
git log --grep="Auto-sync" --oneline
```

### Disable Temporarily
```
Actions → Auto Sync Agent → ⋮ → Disable workflow
```

### Re-enable
```
Actions → Auto Sync Agent → Enable workflow
```

---

## 📝 Example Scenarios

### Scenario 1: Working with AI Agents

**Setup:**
1. AI agents create content automatically
2. Auto Sync commits every 30 minutes
3. Changes pushed to development branch
4. You review and merge to main

**Benefit:** Continuous progress without manual commits

### Scenario 2: Multi-Device Development

**Setup:**
1. Work on laptop, make changes
2. Don't commit, just save files
3. Auto Sync commits and pushes
4. Switch to desktop, changes are there

**Benefit:** Never forget to push changes

### Scenario 3: Team Collaboration

**Setup:**
1. Team members work on feature branch
2. Auto Sync keeps branch updated
3. Conflicts detected early
4. Issues created for resolution

**Benefit:** Reduced merge conflicts at PR time

---

## ✅ Quick Start Checklist

- [ ] Review the workflow file: `.github/workflows/auto-sync-agent.yml`
- [ ] Understand what will be auto-committed
- [ ] Check `.gitignore` is comprehensive
- [ ] Enable workflow permissions (Settings → Actions)
- [ ] Run manual test: `gh workflow run auto-sync-agent.yml`
- [ ] Monitor first few automatic runs
- [ ] Adjust schedule if needed
- [ ] Set up notifications (optional)
- [ ] Document for your team

---

## 🎉 You're All Set!

The Auto Sync Agent is now managing your git pull/push operations automatically. Sit back and let it handle the synchronization while you focus on building great features!

**Questions?** Create an issue with the `auto-sync` label.

---

**Created:** December 2024  
**Version:** 1.0.0  
**Maintainer:** @issdandavis  
**Repository:** Avalon/Aethromoor
