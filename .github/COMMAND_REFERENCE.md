# AI Organizer Bot - Command Reference

## Quick Command Guide

All commands are issued via issue or PR comments starting with `/ai-`

### Issue Organization

```markdown
/ai-organize triage-all
  → Triages all open issues, applies labels, assigns to projects

/ai-organize clean-stale
  → Closes stale issues after warning period

/ai-organize sync-labels
  → Ensures consistent label taxonomy across repository

/ai-organize update-milestones
  → Reviews and updates milestone assignments
```

### Code Review

```markdown
/ai-review pr <number>
  → Review specific pull request

/ai-review pr <number> --focus security
  → Focus review on security issues

/ai-review pr <number> --focus performance
  → Focus review on performance issues

/ai-review all-open-prs
  → Review all open pull requests
```

### Task Execution

```markdown
/ai-task create feature <name>
  → Create new feature branch with boilerplate

/ai-task create bugfix <issue-number>
  → Create bugfix branch from issue

/ai-task generate tests <file>
  → Generate test cases for file

/ai-task generate docs <module>
  → Generate documentation for module
```

### Code Operations

```markdown
/ai-refactor <file>
  → Refactor specified file

/ai-optimize <function>
  → Optimize specific function

/ai-document <module>
  → Add documentation to module

/ai-test <component>
  → Generate tests for component

/ai-migrate <from> <to>
  → Migrate code from old to new pattern
```

### Workflow Operations

```markdown
/ai-run test
  → Run test suite

/ai-run build
  → Run build process

/ai-run deploy <environment>
  → Deploy to specified environment (staging/production)

/ai-run release <version>
  → Create new release with version
```

### Repository Management

```markdown
/ai-organize branches
  → Clean up merged/stale branches

/ai-organize dependencies
  → Update outdated dependencies

/ai-organize security
  → Review and fix security vulnerabilities

/ai-organize performance
  → Analyze and optimize performance
```

### Agent Management

```markdown
/ai-agent create <name>
  → Create new AI agent

/ai-agent list
  → List all active agents

/ai-agent disable <name>
  → Disable specific agent

/ai-agent enable <name>
  → Enable specific agent
```

### Analytics & Reporting

```markdown
/ai-report weekly
  → Generate weekly activity report

/ai-report security
  → Generate security audit report

/ai-report performance
  → Generate performance metrics report

/ai-report contributors
  → Generate contributor statistics
```

## Command Flags

Most commands support these flags:

```markdown
--dry-run          → Preview without executing
--force            → Skip confirmations
--verbose          → Detailed output
--silent           → Minimal output
--async            → Run asynchronously
--priority <level> → Set priority (low/normal/high/critical)
```

## Examples

### Complete Feature Development

```markdown
Comment: /ai-task create feature user-dashboard --from main

Bot creates:
- feature/user-dashboard branch
- Basic file structure
- Initial tests
- Draft PR

Comment: /ai-test src/dashboard --coverage 80

Bot generates:
- Comprehensive test suite
- Edge case tests
- Integration tests

Comment: /ai-review pr 123 --focus all

Bot reviews:
- Code quality
- Security
- Performance
- Best practices

Comment: /ai-deploy staging --wait

Bot deploys:
- Builds application
- Runs tests
- Deploys to staging
- Verifies deployment
```

### Issue Cleanup

```markdown
Comment: /ai-organize triage-all --dry-run

Bot shows:
- 15 issues to label
- 8 issues to assign
- 3 issues to close
- Proposed changes

Comment: /ai-organize triage-all --force

Bot executes:
- Applies labels
- Assigns to projects
- Closes stale issues
- Posts summary
```

### Security Audit

```markdown
Comment: /ai-organize security --scan-all

Bot performs:
- Dependency vulnerability scan
- Code security analysis
- Secret detection
- Permission audit
- Generates report
```

## Advanced Usage

### Chained Commands

```markdown
/ai-task create feature auth && /ai-test src/auth && /ai-review pr
```

### Conditional Execution

```markdown
/ai-deploy staging if tests pass
/ai-review pr 123 unless already reviewed
```

### Scheduled Commands

```markdown
schedule: "0 0 * * 1"  # Every Monday
command: /ai-organize triage-all
```

### Batch Operations

```markdown
/ai-review prs --label needs-review --max 10
/ai-organize issues --state open --older-than 30d
```

## Custom Commands

Define custom commands in `.github/config/commands.yml`:

```yaml
custom_commands:
  - name: full-release
    command: /ai-release
    steps:
      - run_tests
      - bump_version
      - update_changelog
      - create_tag
      - build_artifacts
      - deploy_production
      - announce
    
  - name: weekly-maintenance
    command: /ai-maintain
    steps:
      - clean_branches
      - update_dependencies
      - run_security_scan
      - generate_report
```

## Response Codes

Bot responses include status indicators:

```markdown
✅ Success - Task completed
🔄 In Progress - Task running
⏸️ Paused - Waiting for input
❌ Failed - Task failed
⚠️ Warning - Completed with warnings
ℹ️ Info - Information only
```

## Rate Limits

Commands are rate limited:

- **10 commands per minute** per user
- **100 commands per hour** per repository
- **Priority commands** bypass normal limits
- **Admin users** have higher limits

## Permissions

Command authorization levels:

| Command Type | Required Permission |
|-------------|---------------------|
| Read operations | Triage |
| Write operations | Write |
| Deploy operations | Maintain |
| Admin operations | Admin |

## Getting Help

```markdown
/ai-help
  → Show available commands

/ai-help <command>
  → Show detailed help for command

/ai-status
  → Show bot status and active tasks

/ai-queue
  → Show task queue
```

## Troubleshooting

```markdown
/ai-debug <task-id>
  → Show debug info for task

/ai-retry <task-id>
  → Retry failed task

/ai-cancel <task-id>
  → Cancel running task
```

## Best Practices

1. **Be Specific**: Use flags to narrow scope
2. **Dry Run First**: Preview changes with `--dry-run`
3. **Monitor Output**: Check bot responses
4. **Use Async**: For long-running tasks
5. **Review Before Deploy**: Always review before production
6. **Combine Commands**: Chain related operations
7. **Set Priorities**: Use `--priority` for urgent tasks

## Support

For issues or questions:
- Check bot logs in Actions tab
- Review webhook deliveries
- Create issue with `ai-bot-support` label
- See `.github/AI_BOT_README.md` for docs

---

**Pro Tip**: Type `/ai-` in a comment to see autocomplete suggestions for available commands!
