# GitHub Configuration & Automation

This directory contains GitHub-specific configuration files for the Avalon project, including automated workflows, issue templates, and project automation.

## 📁 Directory Structure

```
.github/
├── workflows/                      # GitHub Actions workflows
│   ├── issue-triage.yml           # Auto-label and triage issues
│   ├── pr-automation.yml          # Auto-label and manage PRs
│   ├── stale-management.yml       # Mark and close stale items
│   ├── notifications.yml          # Notification system
│   ├── choicescript-tests.yml     # Game testing (existing)
│   └── jekyll-docker.yml          # Jekyll build (existing)
│
├── ISSUE_TEMPLATE/                # Issue templates
│   ├── config.yml                 # Template configuration
│   ├── bug_report.yml             # Bug report form
│   ├── feature_request.yml        # Feature request form
│   ├── lore_question.yml          # Lore question form
│   ├── automation.yml             # Automation issue form
│   └── task.md                    # General task template
│
├── INBOX_AUTOMATION_QUICKSTART.md # Quick start guide
└── README.md                      # This file
```

## 🤖 Automated Workflows

### Active Automations:

1. **Issue Triage** (`issue-triage.yml`)
   - Auto-labels issues based on content
   - Welcomes first-time contributors
   - Categorizes by type (bug, feature, lore, etc.)

2. **PR Automation** (`pr-automation.yml`)
   - Labels PRs based on changed files
   - Adds size labels (XS, S, M, L, XL)
   - Welcomes first-time contributors
   - Reminds about linking issues

3. **Stale Management** (`stale-management.yml`)
   - Marks inactive issues/PRs as stale
   - Auto-closes after additional inactivity
   - Respects exemption labels

4. **Notifications** (`notifications.yml`)
   - Summarizes commits to main
   - Announces releases
   - Detects milestone completion

### Existing Workflows:

5. **ChoiceScript Tests** (`choicescript-tests.yml`)
   - Tests game content changes
   - Placeholder for quicktest/randomtest

6. **Jekyll Build** (`jekyll-docker.yml`)
   - Builds Jekyll site
   - Runs on push/PR to main

## 📝 Issue Templates

When creating a new issue, users can choose from:

- **Bug Report** - Structured bug reporting with game version selection
- **Feature Request** - Categorized enhancement requests
- **Lore Question** - Questions about worldbuilding and story
- **Automation Setup** - Automation-related issues
- **Task** - General task tracking

All templates use YAML forms for structured data, enabling better automation.

## 🏷️ Labels

### Auto-Applied:
- `bug`, `enhancement`, `documentation`
- `game-content`, `lore-writing`, `automation`
- `choicescript`, `question`
- `size/XS`, `size/S`, `size/M`, `size/L`, `size/XL` (PRs only)
- `stale`

### Manual (for maintainers):
- `pinned`, `security`, `in-progress`
- `help-wanted`, `good-first-issue`, `needs-review`
- `needs-triage`, `wontfix`, `duplicate`

## 🚀 Quick Start

### For Users:
1. [Open an issue](../../issues/new/choose) - Choose a template
2. Fill out the form - Structured fields help automation
3. Submit - Automation handles the rest!

### For Contributors:
1. Create your branch
2. Make changes
3. Open a PR - Auto-labeling and size detection happen automatically
4. Link related issues with "Closes #123"

### For Maintainers:
1. Review `needs-triage` labeled items daily
2. Add `pinned` or `in-progress` to prevent auto-closure
3. Check Actions tab for workflow status
4. See [INBOX_AUTOMATION_CONFIG.md](../docs/INBOX_AUTOMATION_CONFIG.md) for details

## 📚 Documentation

- **Quick Start:** [INBOX_AUTOMATION_QUICKSTART.md](INBOX_AUTOMATION_QUICKSTART.md)
- **Full Guide:** [docs/INBOX_AUTOMATION_CONFIG.md](../docs/INBOX_AUTOMATION_CONFIG.md)
- **Integration Ideas:** [docs/AUTOMATION_GUIDE.md](../docs/AUTOMATION_GUIDE.md)

## ⚙️ Configuration

### Stale Timeframes:
- Issues: 60 days → mark stale → 14 days → auto-close
- PRs: 30 days → mark stale → 14 days → auto-close

### Exemptions:
Items with these labels won't go stale:
- `pinned`, `security`, `in-progress`, `help-wanted`, `needs-review`

### Notification Triggers:
- Push to main branch
- Release published
- Issue/PR opened or closed
- Milestone completed

## 🔌 External Integrations (Ready to Enable)

### Discord:
1. Create webhook in Discord server settings
2. Add as repository secret: `DISCORD_WEBHOOK`
3. Uncomment section in `notifications.yml`

### Email:
- Configure in repository settings
- Or add action to workflow files

### Zapier:
- Connect GitHub to Zapier account
- Use triggers: issue_created, release_published, etc.
- See AUTOMATION_GUIDE.md for workflow ideas

## 🛠️ Maintenance

### Daily:
- Review new issues (check Actions tab)
- Verify auto-labels are accurate
- Respond to first-time contributors

### Weekly:
- Review `in-progress` items
- Check stale warnings
- Update priorities and milestones

### Monthly:
- Audit label usage
- Review workflow effectiveness
- Adjust timeframes if needed

## 🆘 Troubleshooting

**Workflow not running?**
- Check Actions tab for errors
- Verify YAML syntax
- Check repository permissions

**Labels not applied?**
- Review workflow file for keyword matching
- Ensure labels exist in repository
- Check permissions include `issues: write`

**False positive on stale?**
- Add comment to reset timer
- Add `pinned` or `in-progress` label

## 📊 Monitoring

### Actions Dashboard:
Visit [Actions](../../actions) to see:
- Workflow run history
- Success/failure status
- Execution logs
- Job summaries

### Insights:
- Issue/PR statistics
- Label usage
- Contributor activity
- Community health

## 🔐 Security

- Never commit secrets to workflow files
- Use repository secrets for tokens/webhooks
- Keep permissions minimal (least privilege)
- Audit connected apps regularly
- Enable 2FA on all accounts

## 🌟 Contributing

To improve automation:
1. Open an issue using the Automation template
2. Describe the enhancement or fix
3. Test changes in a fork first
4. Submit PR with clear description

## 📜 License

These automation configurations are part of the Avalon project and follow the same license as the main repository.

---

**Need Help?**
- Read [INBOX_AUTOMATION_QUICKSTART.md](INBOX_AUTOMATION_QUICKSTART.md)
- Check [INBOX_AUTOMATION_CONFIG.md](../docs/INBOX_AUTOMATION_CONFIG.md)
- Open an issue with the Automation template

**Last Updated:** November 2025  
**Automation Status:** ✅ Active
