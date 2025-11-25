# Inbox Automation Quick Start Guide

## 🎯 What's Automated?

Your Avalon repository now has **automated inbox management**! Here's what happens automatically:

### When Someone Opens an Issue:
✅ **Auto-labeled** based on keywords (bug, feature, lore, automation, etc.)  
✅ **Auto-categorized** by content type (game, docs, lore, automation)  
✅ **Welcomed** if they're a first-time contributor  
✅ **Guided** with helpful links and context  

### When Someone Opens a PR:
✅ **Auto-labeled** based on changed files  
✅ **Size-tagged** (XS, S, M, L, XL)  
✅ **Welcomed** if first-time contributor  
✅ **Reminded** to link related issues  

### Automatically Managed:
✅ **Stale issues** marked after 60 days of inactivity  
✅ **Stale PRs** marked after 30 days of inactivity  
✅ **Auto-closed** after 14 additional days (unless pinned)  
✅ **Notifications** summarize changes and releases  

## 📝 How to Use

### Creating an Issue:

1. Go to **Issues** → **New Issue**
2. Choose a template:
   - **Bug Report** - Report game bugs
   - **Feature Request** - Suggest improvements
   - **Lore Question** - Ask about worldbuilding
   - **Automation Setup** - Automation topics
   - **Task** - General tasks

3. Fill out the form - structured fields help automation!
4. Submit - automation takes care of the rest

### Creating a PR:

1. Push your changes to a branch
2. Open a pull request
3. The system automatically:
   - Labels it based on files changed
   - Adds a size label
   - Welcomes you if it's your first PR
   - Reminds you to link issues

### Keeping Items Active:

To prevent auto-closure, add these labels:
- `pinned` - Keep open indefinitely
- `in-progress` - Currently being worked on
- `security` - Security-related
- `help-wanted` - Seeking contributors

## 🏷️ Label System

### Auto-Applied Labels:

**By Content:**
- `bug` - Bug reports
- `enhancement` - Feature requests
- `documentation` - Documentation changes
- `game-content` - Game-related
- `lore-writing` - Lore and writing
- `automation` - Automation topics
- `question` - Questions

**By Size (PRs only):**
- `size/XS` - < 10 lines
- `size/S` - 10-49 lines
- `size/M` - 50-199 lines
- `size/L` - 200-499 lines
- `size/XL` - 500+ lines

### Manual Labels (for maintainers):

**Priority:**
- `pinned` - Don't auto-close
- `security` - Security issues
- `in-progress` - Being worked on

**Community:**
- `help-wanted` - Seeking help
- `good-first-issue` - Good for newcomers
- `needs-review` - Awaiting review

**Status:**
- `needs-triage` - Needs categorization
- `wontfix` - Won't be addressed
- `duplicate` - Duplicate issue
- `stale` - Inactive

## 🔔 Notifications

The system creates summaries when:
- Code is pushed to main branch
- Releases are published
- Milestones are completed

Check the **Actions** tab to see workflow runs!

## 🎮 Game-Specific Features

### Bug Reports:
- Select which game version (HTML/ChoiceScript)
- Identify the scene where bug occurred
- Structured reproduction steps
- Auto-labeled with `bug` and `needs-triage`

### Feature Requests:
- Categorize by type (game, lore, technical, etc.)
- Priority rating
- Auto-labeled with `enhancement`

### Lore Questions:
- Topic area selection
- Context provision
- Auto-labeled with `lore-writing` and `question`

## ⚙️ For Maintainers

### Daily Tasks:
- Review new issues (check `needs-triage` label)
- Verify auto-labels are accurate
- Respond to questions
- Update priorities

### Weekly Tasks:
- Review `in-progress` items
- Check stale warnings
- Update milestones
- Review automation effectiveness

### Monthly Tasks:
- Audit label usage
- Update workflow rules if needed
- Review closed stale items
- Adjust timeframes if necessary

### Managing Stale Items:

**To Keep Open:**
- Add comment (resets timer)
- Add `pinned` label (never goes stale)
- Add `in-progress` label (exempt from stale)

**To Close:**
- Let stale timer expire
- Or manually close with explanation

## 🔗 Integrations (Ready to Enable)

### Discord Notifications:
1. Create Discord webhook
2. Add as repository secret `DISCORD_WEBHOOK`
3. Uncomment section in `notifications.yml`
4. Get notified on Discord for pushes, releases, etc.

### Email Notifications:
- Configure in repository settings
- Or add email action to workflows
- Customize message templates

### Zapier Integration:
- Connect GitHub to Zapier
- Use triggers: issue created, PR merged, release published
- See `AUTOMATION_GUIDE.md` for workflow ideas

## 📚 Documentation

Full documentation:
- **Detailed Guide:** [docs/INBOX_AUTOMATION_CONFIG.md](../docs/INBOX_AUTOMATION_CONFIG.md)
- **Integration Ideas:** [docs/AUTOMATION_GUIDE.md](../docs/AUTOMATION_GUIDE.md)
- **Project Roadmap:** [docs/PROJECT_ROADMAP.md](../docs/PROJECT_ROADMAP.md)

Workflow files:
- `.github/workflows/issue-triage.yml` - Issue automation
- `.github/workflows/pr-automation.yml` - PR automation
- `.github/workflows/stale-management.yml` - Stale management
- `.github/workflows/notifications.yml` - Notification system

Issue templates:
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/lore_question.yml`
- `.github/ISSUE_TEMPLATE/automation.yml`
- `.github/ISSUE_TEMPLATE/task.md`

## 🆘 Troubleshooting

**Issue not auto-labeled?**
- Check if keywords match (see workflow files)
- Verify labels exist in repository
- Review Actions tab for errors

**Stale bot marked active issue?**
- Add comment to reset timer
- Add `pinned` or `in-progress` label
- Check last activity date

**Workflow not running?**
- Check Actions tab for errors
- Verify repository permissions
- Check YAML syntax

**Need help?**
- Open an issue using Automation template
- Check workflow run logs in Actions tab
- See full docs in `INBOX_AUTOMATION_CONFIG.md`

## ✨ Tips

1. **Use templates** - They enable better automation
2. **Link issues to PRs** - Use "Closes #123" in PR description
3. **Keep issues updated** - Prevents premature closure
4. **Use labels consistently** - Helps organization
5. **Check Actions tab** - See what automation is doing
6. **Review summaries** - Check workflow run summaries

---

**Quick Links:**
- [Open an Issue](../../issues/new/choose)
- [View Open Issues](../../issues)
- [View Pull Requests](../../pulls)
- [Actions Dashboard](../../actions)
- [Full Documentation](../docs/INBOX_AUTOMATION_CONFIG.md)

---

*Inbox automation powered by GitHub Actions*  
*Last updated: November 2025*
