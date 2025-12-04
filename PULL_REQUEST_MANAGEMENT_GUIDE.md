# Pull Request Management Guide

## 🎯 Quick Start: You Have 84 Open PRs - What Now?

You're new to GitHub and have **84 open pull requests**. Don't panic! This guide will help you understand what they are, which ones to merge, and how to manage them going forward.

---

## 📚 What is a Pull Request?

A **Pull Request (PR)** is a proposal to merge changes from one branch into another (usually into `main`). Think of it as:
- A **package of changes** waiting for approval
- A **draft** that hasn't been published yet
- A **checkpoint** before changes become permanent

### When Should You Merge a PR?

✅ **Merge when:**
- The work is complete and tested
- The changes are ready to be permanent
- You've reviewed the changes and they look good

❌ **Don't merge when:**
- Work is still in progress (marked `[WIP]` or `draft`)
- You're not sure what the PR does
- Changes conflict with other work

---

## 🔍 Understanding Your 84 PRs

Looking at your repository, most PRs were created by **GitHub Copilot** (AI assistant) and fall into these categories:

### 1. **Documentation PRs** (Most of them)
- Adding guides, READMEs, setup instructions
- Generally safe to merge if content looks good

### 2. **Feature PRs** (Game content, automation)
- New game scenes, expedition content
- Automation workflows, AI agents
- **Review carefully** before merging

### 3. **Infrastructure PRs** (GitHub setup, workflows)
- GitHub Actions, security scanning
- **Important** - can affect how your repo works

### 4. **Draft PRs** (`[WIP]` in title)
- Work in progress, not ready to merge
- **Don't merge these yet**

---

## 🚦 Decision Framework: What To Do With Each PR

### Step 1: Categorize Your PRs

Run this command to see all PRs grouped by status:

```bash
cd /home/runner/work/Aethromoor/Aethromoor
git branch -a | grep copilot
```

### Step 2: Make Decisions

For each PR, ask yourself:

| Question | Action |
|----------|--------|
| Is it marked `[WIP]` or `draft`? | **Wait** - keep open |
| Does the title describe something you want? | **Review** → Maybe merge |
| Is it outdated (created months ago)? | **Close** if no longer relevant |
| Does it conflict with main branch? | **Review conflicts** or close |
| Is it a duplicate of another PR? | **Close** the duplicate |

---

## ✅ Recommended Actions for Your 84 PRs

Based on analysis of your PRs, here's a suggested plan:

### **Phase 1: Quick Wins (Merge Ready)**
These PRs are documentation/guides that are safe to merge:

- **PR #86** - Enterprise automation validation checklist
- **PR #101** - Collaboration playthrough blueprints
- **PR #118** - AI comm log entries

**Action:** Review and merge these first (3 PRs)

### **Phase 2: Close Obsolete/Duplicate PRs**
These are likely outdated or superseded:

- Any PR marked `[WIP]` from more than 2 weeks ago
- Duplicate documentation PRs (multiple README updates)
- PRs that conflict with already-merged changes

**Action:** Close with a comment explaining why (estimated ~30 PRs)

### **Phase 3: Review Feature PRs**
These need careful review before merging:

- **PR #92, #116** - Game content (expeditions, scenes)
- **PR #95, #107, #108** - AI automation features
- **PR #119, #120** - Workflow improvements

**Action:** Review each, test if possible, then merge or request changes (~20 PRs)

### **Phase 4: Infrastructure PRs**
These affect your repository's core functionality:

- GitHub Actions workflows
- Security scanning
- Branch protection rules

**Action:** Review very carefully, test in a staging environment if possible (~10 PRs)

### **Phase 5: Keep Open**
These are actively being worked on:

- Current `[WIP]` PRs with recent activity
- PRs you're actively collaborating on

**Action:** Keep open, update regularly (~10 PRs)

---

## 🔄 Push vs Pull: When to Use Each

### **Git Pull** (`git pull`)
**Use when:** You want to get the latest changes FROM GitHub TO your computer

```bash
git pull origin main
```

**When to do it:**
- Before you start working each day
- When someone else (or an AI) has made changes
- To update your local copy with remote changes

### **Git Push** (`git push`)
**Use when:** You want to send your changes FROM your computer TO GitHub

```bash
git push origin branch-name
```

**When to do it:**
- After you've committed changes locally
- When you want to create/update a PR
- To back up your work to GitHub

### **The Workflow**

```bash
# 1. Start fresh
git pull origin main

# 2. Make changes to files
# (edit, create, delete files)

# 3. Stage changes
git add .

# 4. Commit changes
git commit -m "Describe what you changed"

# 5. Push to GitHub
git push origin branch-name
```

---

## 🤖 Automated PR Cleanup Script

Create this script to help manage PRs in bulk:

```bash
#!/bin/bash
# Save as: scripts/pr-cleanup.sh

echo "=== PR Cleanup Assistant ==="
echo ""
echo "This will help you review and close old PRs"
echo ""

# List all draft PRs
echo "Draft PRs (work in progress):"
gh pr list --state open --draft --limit 100

echo ""
echo "PRs older than 30 days:"
gh pr list --state open --search "created:<$(date -d '30 days ago' '+%Y-%m-%d')" --limit 100

echo ""
echo "To close a PR, run: gh pr close PR_NUMBER --comment 'Closing because...'"
```

---

## 📋 Best Practices Going Forward

### 1. **One Feature = One PR**
Don't let PRs pile up. Merge or close them regularly.

### 2. **Use Draft PRs**
Mark unfinished work as draft to avoid confusion:
```bash
gh pr create --draft --title "[WIP] My feature"
```

### 3. **Regular Cleanup**
Set a reminder to review PRs weekly:
- Monday: Review new PRs
- Friday: Merge or close old PRs

### 4. **Clear Titles**
Use descriptive PR titles:
- ✅ "Add expedition: Singing Dunes scene"
- ❌ "Update file"

### 5. **Close Unneeded PRs**
Don't feel bad about closing PRs! It's better than having 84 open.

```bash
gh pr close 123 --comment "Closing - work completed in PR #124"
```

---

## 🚀 Quick Action Plan (Next 30 Minutes)

### Step 1: Install GitHub CLI (if not installed)
```bash
# Check if installed
gh --version

# If not, install from: https://cli.github.com/
```

### Step 2: Review Your PRs
```bash
# List all open PRs
gh pr list --state open

# View a specific PR
gh pr view PR_NUMBER
```

### Step 3: Take Initial Actions
```bash
# Merge a ready PR
gh pr merge PR_NUMBER --squash --delete-branch

# Close an outdated PR
gh pr close PR_NUMBER --comment "No longer needed"

# Mark a PR as ready for review
gh pr ready PR_NUMBER
```

### Step 4: Create a Tracking Document
Create `PR_CLEANUP_TRACKER.md` to track your progress:

```markdown
# PR Cleanup Progress

## Summary
- Total PRs: 84
- Merged: 0
- Closed: 0
- Remaining: 84

## This Week's Actions
- [ ] Review Phase 1 PRs (documentation)
- [ ] Close duplicate/obsolete PRs
- [ ] Merge 5 ready PRs

## Notes
- Keep track of which PRs you've reviewed
- Mark date when you merge/close PRs
```

---

## 🆘 When You're Stuck

### Question: "I don't know if this PR is safe to merge"
**Answer:** 
1. Check the "Files changed" tab on GitHub
2. Look for file types:
   - `.md` files (documentation) = usually safe
   - `.yml` files (workflows) = review carefully
   - Game content files = test if possible
3. If still unsure, close it and create a new one when you need the feature

### Question: "Should I push or pull?"
**Answer:**
- **Pull first** (get latest changes)
- Make your changes
- **Push** (send your changes)

### Question: "What if I mess up?"
**Answer:**
- GitHub keeps history - you can undo almost anything
- Closed PRs can be reopened
- Merged PRs can be reverted
- When in doubt, ask for help!

---

## 📞 Getting Help

- **GitHub Docs:** https://docs.github.com/en/pull-requests
- **GitHub Community:** https://github.community/
- **Your repo has guides:**
  - `START_HERE.md`
  - `QUICK_START.md`
  - `CONTRIBUTING.md`

---

## 🎓 Key Takeaways

1. **84 PRs is manageable** - start with documentation PRs
2. **Pull** = get changes FROM GitHub
3. **Push** = send changes TO GitHub
4. **Merge** when work is complete
5. **Close** PRs that are outdated or no longer needed
6. **Don't be afraid** to close PRs - it's better than clutter
7. **Set a weekly routine** for PR management

---

**Remember:** You're the owner - you decide what gets merged. Start small, review carefully, and don't hesitate to close PRs that don't make sense. It's better to have 10 well-managed PRs than 84 confusing ones!
