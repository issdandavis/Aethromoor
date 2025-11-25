# Inbox Automation Configuration

## Overview
This document details the automated inbox management system for the Avalon project. These automations help triage issues, manage pull requests, and keep the project organized.

## Implemented Automations

### 1. Issue Triage & Auto-Labeling (`issue-triage.yml`)
**Triggers:** When issues are opened, edited, or reopened

**Features:**
- Automatically labels issues based on keywords:
  - `bug` - Bug reports
  - `enhancement` - Feature requests
  - `documentation` - Documentation issues
  - `game-content` - Game-related issues
  - `lore-writing` - Lore/writing topics
  - `automation` - Automation-related issues
- Welcomes first-time contributors with helpful information
- Provides project context and guidelines

**How it works:**
1. Scans issue title and body for keywords
2. Applies appropriate labels automatically
3. Checks if user is first-time contributor
4. Posts welcome message with relevant links

### 2. PR Auto-Assignment & Notifications (`pr-automation.yml`)
**Triggers:** When pull requests are opened, ready for review, or reviewed

**Features:**
- Auto-labels PRs based on changed files
- Adds size labels (XS, S, M, L, XL) based on changes
- Welcomes first-time contributors
- Reminds about linking to related issues
- Categorizes changes (game content, lore, docs, automation)

**Size Labels:**
- `size/XS` - Less than 10 lines changed
- `size/S` - 10-49 lines changed
- `size/M` - 50-199 lines changed
- `size/L` - 200-499 lines changed
- `size/XL` - 500+ lines changed

### 3. Stale Issue Management (`stale-management.yml`)
**Triggers:** Daily at 00:00 UTC (or manual trigger)

**Features:**
- Marks inactive issues stale after 60 days
- Marks inactive PRs stale after 30 days
- Closes stale items after 14 additional days
- Respects exempt labels: `pinned`, `security`, `in-progress`, `help-wanted`
- Auto-removes stale label when activity resumes

**Exemptions:**
Issues/PRs with these labels won't be marked stale:
- `pinned` - Important, keep open
- `security` - Security-related
- `in-progress` - Actively being worked on
- `help-wanted` - Seeking contributors
- `needs-review` - Awaiting review

### 4. Notification System (`notifications.yml`)
**Triggers:** Push to main, releases, issues/PRs opened/closed

**Features:**
- Summarizes changes on push to main
- Categorizes updates (game, lore, docs, automation)
- Creates release announcements
- Detects milestone completion
- Provides job summaries

**Ready for Integration:**
- Discord webhooks (commented out, requires secret)
- Email notifications
- Social media posts
- Custom notification endpoints

## Issue Templates

### Available Templates:

1. **Bug Report** (`bug_report.yml`)
   - Structured bug reporting
   - Game version selection
   - Scene/area identification
   - Reproduction steps
   - Labels: `bug`, `needs-triage`

2. **Feature Request** (`feature_request.yml`)
   - Category selection
   - Problem/solution format
   - Priority rating
   - Alternative considerations
   - Labels: `enhancement`, `needs-triage`

3. **Lore Question** (`lore_question.yml`)
   - Topic area selection
   - Context provision
   - Reason tracking
   - Labels: `lore-writing`, `question`

4. **Automation Setup** (`automation.yml`)
   - Automation type selection
   - Request type categorization
   - Integration details
   - Security checklist
   - Labels: `automation`, `needs-triage`

5. **Task** (`task.md`)
   - General task template
   - Goal and acceptance criteria
   - AI loop planning

## Labels

### Automatically Applied:
- `bug` - Bug reports
- `enhancement` - Feature requests
- `documentation` - Documentation changes
- `game-content` - Game-related content
- `lore-writing` - Lore and writing
- `automation` - Automation topics
- `choicescript` - ChoiceScript specific
- `stale` - Inactive items
- `size/*` - PR size indicators

### Manual Labels (recommended):
- `pinned` - Don't auto-close
- `security` - Security issues
- `in-progress` - Currently being worked on
- `help-wanted` - Seeking contributors
- `good-first-issue` - Good for newcomers
- `needs-review` - Awaiting review
- `needs-triage` - Needs categorization
- `question` - Questions
- `wontfix` - Won't be addressed
- `duplicate` - Duplicate issue

## Configuration Files

### Workflow Files:
```
.github/workflows/
├── issue-triage.yml      # Auto-label and welcome for issues
├── pr-automation.yml     # Auto-label and welcome for PRs
├── stale-management.yml  # Mark and close stale items
└── notifications.yml     # Summary and notification system
```

### Template Files:
```
.github/ISSUE_TEMPLATE/
├── config.yml           # Issue template configuration
├── bug_report.yml       # Bug report form
├── feature_request.yml  # Feature request form
├── lore_question.yml    # Lore question form
├── automation.yml       # Automation issue form
└── task.md             # General task template
```

## Customization

### Adding Discord Notifications:

1. Create a Discord webhook in your server settings
2. Add the webhook URL as a repository secret named `DISCORD_WEBHOOK`
3. Uncomment the Discord notification section in `notifications.yml`
4. Customize the message format as needed

Example:
```yaml
- name: Send Discord notification
  env:
    DISCORD_WEBHOOK: ${{ secrets.DISCORD_WEBHOOK }}
  if: env.DISCORD_WEBHOOK != ''
  run: |
    curl -H "Content-Type: application/json" \
      -d '{"content": "🚀 New update: ${{ github.event.head_commit.message }}"}' \
      $DISCORD_WEBHOOK
```

### Adding Email Notifications:

Use GitHub's built-in notification settings or add a workflow step:
```yaml
- name: Send Email
  uses: dawidd6/action-send-mail@v3
  with:
    server_address: smtp.gmail.com
    server_port: 465
    username: ${{ secrets.MAIL_USERNAME }}
    password: ${{ secrets.MAIL_PASSWORD }}
    subject: New Avalon Update
    body: ${{ github.event.head_commit.message }}
    to: subscribers@example.com
    from: Avalon Project
```

### Modifying Stale Timeframes:

Edit `stale-management.yml`:
- `days-before-issue-stale` - Days before marking issue stale (default: 60)
- `days-before-issue-close` - Days after stale before closing (default: 14)
- `days-before-pr-stale` - Days before marking PR stale (default: 30)
- `days-before-pr-close` - Days after stale before closing (default: 14)

### Adding Custom Labels:

Edit the workflow files to add new auto-labeling rules:
```yaml
- name: Label custom category
  if: contains(github.event.issue.body, 'your-keyword')
  uses: actions/github-script@v7
  with:
    script: |
      github.rest.issues.addLabels({
        issue_number: context.issue.number,
        owner: context.repo.owner,
        repo: context.repo.repo,
        labels: ['your-label']
      })
```

## Maintenance

### Weekly Tasks:
- Review `needs-triage` labeled items
- Ensure auto-labels are accurate
- Check for any failed workflow runs
- Update exemption labels as needed

### Monthly Tasks:
- Review stale items before auto-closure
- Update workflow rules based on patterns
- Adjust timeframes if needed
- Audit label usage

### As Needed:
- Add new issue templates for common patterns
- Customize notification messages
- Add new integrations (Discord, Zapier, etc.)
- Update automation rules

## Troubleshooting

### Workflow Not Running:
1. Check workflow file syntax (YAML validation)
2. Verify permissions in workflow file
3. Check repository settings > Actions > General
4. Review Actions tab for error messages

### Labels Not Applied:
1. Verify keyword matching in workflow
2. Check that labels exist in repository
3. Review workflow run logs
4. Ensure permissions include `issues: write`

### Stale Bot Issues:
1. Check exempt labels are spelled correctly
2. Verify schedule syntax
3. Review `operations-per-run` limit
4. Check for rate limiting

### Notifications Not Sending:
1. Verify secrets are set correctly
2. Check webhook URLs are valid
3. Review service-specific rate limits
4. Test with workflow_dispatch trigger

## Integration with Zapier

These GitHub automations complement the Zapier workflows described in `AUTOMATION_GUIDE.md`:

### GitHub → Zapier Triggers:
- New issue created → Create Trello card
- PR merged → Post to Discord
- Release published → Send email newsletter
- Issue labeled `bug` → Add to bug tracking sheet

### Zapier → GitHub Actions:
- Google Docs update → Trigger workflow
- Form submission → Create GitHub issue
- Calendar event → Update milestone

## Best Practices

1. **Keep workflows focused** - Each workflow should do one thing well
2. **Use meaningful labels** - Consistent labeling helps automation
3. **Monitor workflow runs** - Check Actions tab regularly
4. **Test changes** - Use workflow_dispatch for manual testing
5. **Document customizations** - Update this file when making changes
6. **Review permissions** - Only grant necessary permissions
7. **Protect secrets** - Never commit secrets to repository
8. **Use issue templates** - Structured data enables better automation

## Future Enhancements

Planned improvements:
- [ ] Auto-assign issues based on file paths
- [ ] Project board automation
- [ ] Automated changelog generation
- [ ] Community metrics dashboard
- [ ] Integration with game testing framework
- [ ] Automated lore consistency checks
- [ ] Beta tester management automation

## Support

For questions about inbox automations:
1. Check this documentation
2. Review workflow files in `.github/workflows/`
3. Open an automation issue using the template
4. Check GitHub Actions documentation

---

**Last Updated:** November 2025  
**Maintained By:** Avalon Project Team  
**Version:** 1.0
