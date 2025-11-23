# AI Organizer Bot - Complete Automation System

## Overview

The AI Organizer Bot is a comprehensive GitHub App that provides full automation capabilities across your entire GitHub organization. It can handle any task you request, from code reviews to issue management to creating new AI agents.

## Features

### 🤖 AI Agent Management
- **Auto-create specialized AI agents** for different tasks
- **Dynamic agent assignment** based on issue type and labels
- **Multi-agent collaboration** for complex tasks
- **Agent templates** for common scenarios

### 📋 Issue & Project Management
- **Automatic issue triaging** and labeling
- **Smart assignment** to appropriate team members or AI agents
- **Priority detection** and escalation
- **Automated project board updates**

### 🔄 Workflow Automation
- **Intelligent CI/CD management**
- **Automated code review** and suggestions
- **Pull request automation** (merging, conflict resolution)
- **Release management** and versioning

### 🔐 Security & Compliance
- **Automated security scanning** integration
- **Dependency updates** via Dependabot
- **Code scanning alerts** management
- **Secret scanning** and remediation

### 📊 Analytics & Reporting
- **Automated status reports**
- **Team productivity analytics**
- **Code quality metrics**
- **Custom dashboard generation**

## Setup Instructions

### 1. Register the GitHub App

Use the manifest file to create the app:

```bash
# Navigate to: https://github.com/settings/apps/new
# Or for organization: https://github.com/organizations/YOUR_ORG/settings/apps/new

# Upload the github-app-manifest.json or manually configure:
```

**Required Settings:**
- **App Name**: AI Organizer Bot
- **Homepage URL**: https://github.com/issdandavis
- **Callback URL**: Your webhook endpoint
- **Webhook Secret**: Generate a secure secret (save this!)
- **Permissions**: All selected in manifest
- **Events**: All events subscribed

### 2. Install the App

1. After creation, click "Install App"
2. Select repositories (recommended: All repositories)
3. Authorize the installation

### 3. Configure Webhook Endpoint

You'll need a server to receive webhooks. Options:

**Option A: GitHub Actions (Serverless)**
- Use the provided workflow files
- No external server needed
- Limited to GitHub Actions capabilities

**Option B: External Service**
- Deploy webhook handler (see `webhook-server/` directory)
- Configure your webhook URL in the app settings
- More flexible but requires hosting

### 4. Set Up Environment Variables

Create repository secrets:

```yaml
GITHUB_APP_ID: Your app ID
GITHUB_APP_PRIVATE_KEY: Your private key (PEM format)
GITHUB_APP_INSTALLATION_ID: Installation ID
WEBHOOK_SECRET: Your webhook secret
OPENAI_API_KEY: For AI features (optional)
ANTHROPIC_API_KEY: For Claude features (optional)
```

## Usage

### Creating AI Agents via Issues

Create a new issue with the label `ai-agent-request`:

```markdown
**Agent Name**: Code Reviewer Agent
**Purpose**: Review all pull requests for code quality
**Triggers**: On pull request opened/updated
**Capabilities**: Code analysis, comment on PRs, suggest improvements
**Permissions**: Read code, write comments
```

The bot will automatically:
1. Create a new agent configuration file
2. Set up the necessary workflows
3. Activate the agent
4. Reply with agent details

### Requesting Automated Tasks

Use issue commands:

```markdown
/ai-task Create a new feature branch for user authentication
/ai-review Review PR #123 for security vulnerabilities
/ai-deploy Deploy to staging environment
/ai-report Generate weekly productivity report
/ai-organize Triage all open issues and assign to appropriate projects
```

### Agent Types

The system includes pre-configured agent templates:

1. **Code Review Agent** - Automated code reviews
2. **Issue Triager** - Categorize and assign issues
3. **Documentation Agent** - Maintain docs
4. **Test Agent** - Write and run tests
5. **Security Agent** - Security scanning and fixes
6. **Release Agent** - Manage releases
7. **Dependency Agent** - Update dependencies
8. **Custom Agent** - Create your own

## Agent Configuration Files

Agents are configured in `.github/agents/`:

```markdown
---
name: code-reviewer
description: Reviews pull requests automatically
triggers:
  - pull_request.opened
  - pull_request.synchronize
permissions:
  contents: read
  pull_requests: write
capabilities:
  - code_analysis
  - comment_creation
  - review_approval
---

# Agent Behavior

This agent reviews all pull requests for:
- Code quality
- Security vulnerabilities
- Best practices
- Performance issues

It will automatically comment on PRs with findings.
```

## Webhook Events

The bot subscribes to all GitHub events:

### Repository Events
- `push`, `pull_request`, `issues`, `release`
- `create`, `delete`, `fork`, `star`
- `repository`, `repository_dispatch`

### Code Events
- `check_run`, `check_suite`, `status`
- `deployment`, `deployment_status`
- `code_scanning_alert`, `secret_scanning_alert`

### Organization Events
- `organization`, `member`, `membership`
- `team`, `team_add`

### Project Events
- `project`, `project_card`, `project_column`
- `milestone`, `label`

## Workflow Integration

The bot works with GitHub Actions:

```yaml
# .github/workflows/ai-organizer.yml
name: AI Organizer Bot

on:
  issues:
    types: [opened, labeled]
  pull_request:
    types: [opened, synchronize]
  workflow_dispatch:

jobs:
  process-event:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: AI Bot Handler
        uses: ./.github/actions/ai-bot-handler
        with:
          event-type: ${{ github.event_name }}
          github-token: ${{ secrets.GITHUB_TOKEN }}
```

## API Integration

### GitHub GraphQL API

The bot uses GraphQL for efficient data fetching:

```graphql
query GetIssueDetails($owner: String!, $repo: String!, $number: Int!) {
  repository(owner: $owner, name: $repo) {
    issue(number: $number) {
      title
      body
      labels(first: 10) {
        nodes {
          name
        }
      }
      assignees(first: 5) {
        nodes {
          login
        }
      }
    }
  }
}
```

### AI Integration

Connect to AI services for intelligent automation:

```javascript
// Example: Using OpenAI for code review
const response = await openai.chat.completions.create({
  model: "gpt-4",
  messages: [
    {
      role: "system",
      content: "You are a code reviewer. Analyze this pull request for issues."
    },
    {
      role: "user",
      content: prDiff
    }
  ]
});
```

## Advanced Features

### Multi-Agent Workflows

Chain multiple agents for complex tasks:

```yaml
# .github/workflows/multi-agent-workflow.yml
name: Multi-Agent Task

on:
  issues:
    types: [labeled]

jobs:
  analyze:
    if: contains(github.event.issue.labels.*.name, 'complex-task')
    runs-on: ubuntu-latest
    steps:
      - name: Planner Agent
        # Creates execution plan
      - name: Code Agent
        # Implements changes
      - name: Test Agent
        # Tests changes
      - name: Review Agent
        # Reviews everything
      - name: Deploy Agent
        # Deploys if approved
```

### Custom Commands

Add custom slash commands:

```markdown
/ai-refactor <file> - Refactor code
/ai-optimize <function> - Optimize performance
/ai-document <module> - Generate documentation
/ai-test <component> - Write tests
/ai-migrate <from> <to> - Migrate code
```

### Scheduled Tasks

Automate recurring tasks:

```yaml
# Daily cleanup
on:
  schedule:
    - cron: '0 0 * * *'  # Midnight daily

jobs:
  cleanup:
    runs-on: ubuntu-latest
    steps:
      - name: Close stale issues
      - name: Update dependencies
      - name: Run security scans
      - name: Generate reports
```

## Security Best Practices

1. **Never commit secrets** - Use GitHub Secrets
2. **Validate webhooks** - Verify webhook signatures
3. **Least privilege** - Only grant necessary permissions
4. **Audit logs** - Enable and monitor
5. **Rate limiting** - Implement rate limits
6. **Input validation** - Sanitize all inputs

## Monitoring & Debugging

### Logs

View bot activity:
```bash
# GitHub Actions logs
gh run list --workflow=ai-organizer.yml

# Webhook deliveries
# Settings > Developer settings > GitHub Apps > AI Organizer Bot > Advanced
```

### Debugging

Enable debug mode:
```yaml
env:
  ACTIONS_STEP_DEBUG: true
  ACTIONS_RUNNER_DEBUG: true
```

## Troubleshooting

### Common Issues

**Bot not responding to events:**
- Check webhook delivery status
- Verify webhook URL is accessible
- Check event subscription settings

**Permission errors:**
- Review app permissions
- Ensure installation has access to repository
- Check token scope

**Rate limiting:**
- Implement exponential backoff
- Use GraphQL to reduce API calls
- Cache responses when possible

## Support & Resources

- **Documentation**: `.github/docs/ai-bot/`
- **Examples**: `.github/examples/`
- **Issues**: Report bugs via GitHub Issues
- **Community**: Discuss in Discussions

## Contributing

To add new agents or features:

1. Create agent config in `.github/agents/`
2. Add workflow in `.github/workflows/`
3. Update this README
4. Test thoroughly
5. Submit PR

## License

MIT License - See LICENSE file

## Credits

Built for the Avalon project by ISDanDavis
Powered by GitHub Apps, Actions, and AI

---

**Ready to automate everything? Install the AI Organizer Bot and let AI handle your GitHub tasks!**
