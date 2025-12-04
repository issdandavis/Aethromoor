# AI Automation Guide for Avalon

This guide explains how AI automation is integrated into the Avalon game development project, enabling efficient collaboration between human developers and AI assistants.

## Table of Contents

- [Overview](#overview)
- [AI-Powered Features](#ai-powered-features)
- [Workflow Integration](#workflow-integration)
- [Custom Agents](#custom-agents)
- [Best Practices](#best-practices)
- [Configuration](#configuration)
- [Monitoring and Costs](#monitoring-and-costs)
- [Troubleshooting](#troubleshooting)

## Overview

The Avalon project leverages AI automation for:

- **Code Review**: Automated review of ChoiceScript scenes and JavaScript code
- **Documentation**: Keeping docs up-to-date and consistent
- **Lore Consistency**: Ensuring narrative canon across all content
- **Testing**: Automated validation of game logic and scenes
- **Development Assistance**: AI pair programming for new features

### Architecture

```
┌─────────────────────────────────────────────────────┐
│                  GitHub Repository                   │
├─────────────────────────────────────────────────────┤
│                                                       │
│  ┌──────────────┐    ┌──────────────┐              │
│  │  Pull Request │───▶│   Triggers   │              │
│  └──────────────┘    └──────┬───────┘              │
│                              │                       │
│                    ┌─────────▼──────────┐           │
│                    │  GitHub Actions     │           │
│                    │  Workflows          │           │
│                    └─────────┬──────────┘           │
│                              │                       │
│          ┌───────────────────┼───────────────────┐  │
│          │                   │                   │  │
│  ┌───────▼──────┐   ┌───────▼──────┐   ┌───────▼──────┐
│  │ Code Review  │   │   Docs       │   │    Lore      │
│  │   Agent      │   │   Agent      │   │   Checker    │
│  └──────┬───────┘   └──────┬───────┘   └───────┬──────┘
│         │                  │                   │       │
│         └──────────────────┼───────────────────┘       │
│                            │                           │
│                    ┌───────▼──────────┐                │
│                    │  AI Models       │                │
│                    │  (GPT-4, etc.)   │                │
│                    └───────┬──────────┘                │
│                            │                           │
│                    ┌───────▼──────────┐                │
│                    │  Results Posted  │                │
│                    │  as PR Comments  │                │
│                    └──────────────────┘                │
└─────────────────────────────────────────────────────┘
```

## AI-Powered Features

### 1. Automated Code Review

**What it does:**
- Reviews ChoiceScript scene files for syntax errors
- Checks JavaScript code quality and security
- Validates YAML workflow files
- Ensures lore consistency in narrative content

**Triggers:**
- New pull requests
- Updates to existing pull requests
- Manual workflow dispatch

**Configuration:**
- `.github/workflows/ai-code-review.yml`
- `.github/agents/code_review_agent.yml`

**Example Output:**
```markdown
## AI Code Review Results

### File: `choicescript_game/scenes/arrival.txt`

✅ No critical issues found

⚠️ Warnings:
- Line 45: Consider adding more context for player choice
- Line 78: Variable 'player_name' should match style guide

💡 Suggestions:
- Add more dialogue options for Polly
- Expand the description of Avalon Academy entrance
```

### 2. Documentation Assistant

**What it does:**
- Validates markdown syntax and structure
- Checks for broken links
- Ensures documentation completeness
- Auto-fixes formatting issues
- Validates spell

 and terminology

**Triggers:**
- Changes to `.md` files
- Manual workflow dispatch
- Weekly maintenance runs

**Configuration:**
- `.github/agents/documentation_agent.yml`

**Auto-fixes:**
- Trailing whitespace
- Inconsistent header formatting
- Simple spelling errors
- Broken internal links

### 3. Lore Consistency Checker

**What it does:**
- Validates character names against canon
- Checks magic system terminology
- Ensures timeline consistency
- Verifies location names

**Canonical References:**
- Character names from `lore/characters/`
- Magic terms from established lore
- Timeline from `docs/AETHERMOOR_CHRONICLES.md`

**Example Check:**
```python
# Canonical character names
CHARACTERS = {
    "Izack Thorne": ["Izack", "Izack Thorne", "Professor Thorne"],
    "Polly": ["Polly", "Polymnia", "Polymnia Aetheris"],
    "Aria Luminette": ["Aria", "Aria Luminette"],
    # ... more characters
}

# Will flag: "Isaac Thorne" (wrong spelling)
# Will accept: "Professor Thorne" (valid variant)
```

### 4. Continuous Integration (CI)

**What it does:**
- Validates ChoiceScript syntax
- Checks JavaScript code
- Runs documentation checks
- Verifies lore consistency
- Generates build summary

**Runs on:**
- Push to main branches
- All pull requests

**Configuration:**
- `.github/workflows/ci.yml`

## Workflow Integration

### Development Workflow

1. **Create Feature Branch**
   ```bash
   git checkout -b feature/new-expedition
   ```

2. **Make Changes**
   - Edit ChoiceScript scenes
   - Update documentation
   - Add lore content

3. **Create Pull Request**
   - AI Code Review runs automatically
   - Documentation checks validate markdown
   - Lore consistency verified

4. **Review Results**
   - Address any critical issues
   - Consider warnings and suggestions
   - Update based on feedback

5. **Merge**
   - All checks pass
   - Human review approved
   - Automated merge or manual merge

### AI-Assisted Development

#### Using AI for Scene Writing

```markdown
**Human:** Create a new expedition scene for the Crystal Caverns

**AI Assistant:**
- Reviews existing expeditions (Singing Dunes, Verdant Tithe, Rune Glacier)
- Maintains consistent structure
- Ensures lore accuracy
- Generates draft scene

**Human:** Reviews and refines the draft

**AI Code Review:** Validates syntax and consistency
```

#### Using AI for Bug Fixes

```markdown
**Human:** Reports bug in choice logic

**AI Assistant:**
- Analyzes the scene file
- Identifies the issue
- Proposes fix with explanation

**Human:** Reviews and applies fix

**CI Workflow:** Validates the fix
```

## Custom Agents

### Available Agents

#### 1. Avalon Lore Steward
**Purpose:** Narrative canon curator

**Capabilities:**
- Validates lore consistency
- Organizes narrative materials
- Maintains character information
- Ensures story continuity

**Usage:**
```yaml
# Triggered automatically on lore file changes
paths:
  - lore/**
  - writing_drafts/**
  - choicescript_game/scenes/**
```

#### 2. Code Review Agent
**Purpose:** Automated code quality

**Capabilities:**
- ChoiceScript syntax validation
- JavaScript quality checks
- Security vulnerability detection
- Style guide enforcement

**Usage:**
```yaml
# Triggered on PR creation/update
events:
  - pull_request
paths:
  - choicescript_game/**/*.txt
  - game/**/*.js
```

#### 3. Documentation Agent
**Purpose:** Documentation quality

**Capabilities:**
- Markdown validation
- Link checking
- Spelling and grammar
- Auto-formatting

**Usage:**
```yaml
# Triggered on doc changes
paths:
  - docs/**/*.md
  - *.md
```

### Creating Custom Agents

See [CUSTOM_AGENTS.md](CUSTOM_AGENTS.md) for detailed guide on creating new agents.

## Best Practices

### For Developers

1. **Review AI Feedback Critically**
   - AI suggestions are helpful but not infallible
   - Use your judgment on what to implement
   - Question recommendations that don't make sense

2. **Provide Context**
   - Add comments explaining complex logic
   - Document why certain choices were made
   - Help AI understand your intentions

3. **Iterative Improvement**
   - Address critical issues first
   - Consider warnings for next iteration
   - Use suggestions to improve quality

4. **Lore Consistency**
   - Always reference canonical lore documents
   - Flag any lore additions for review
   - Maintain character voice and consistency

### For AI Assistants

1. **Respect Canon**
   - Never contradict established lore
   - Reference source materials
   - Flag inconsistencies for human review

2. **Be Helpful, Not Prescriptive**
   - Offer suggestions, not commands
   - Explain reasoning behind recommendations
   - Accept that humans make final decisions

3. **Maintain Context**
   - Remember project structure
   - Understand ChoiceScript specifics
   - Keep Avalon narrative style

4. **Focus on Quality**
   - Prioritize functionality over perfection
   - Ensure code works before optimizing
   - Maintain readability

## Configuration

### Environment Variables

Required secrets (set in GitHub repository settings):

```bash
# Required
OPENAI_API_KEY=sk-...          # For GPT-4 access
GITHUB_TOKEN=ghp_...            # Automatically provided by GitHub

# Optional
ANTHROPIC_API_KEY=sk-ant-...    # For Claude access
DISCORD_WEBHOOK_URL=https://... # For notifications
SLACK_WEBHOOK_URL=https://...   # For notifications
```

### Agent Configuration

Edit `.github/agents/config.yml` to adjust:

- Agent priorities
- Rate limits
- Cost controls
- Execution order
- Notification settings

### Workflow Configuration

Customize workflows in `.github/workflows/`:

- `ai-code-review.yml` - Review automation
- `ci.yml` - Continuous integration
- Add custom workflows as needed

## Monitoring and Costs

### Cost Management

AI API usage has costs. Monitor and control:

1. **Rate Limits**
   ```yaml
   # In config.yml
   rate_limits:
     per_hour: 100
     per_day: 500
   ```

2. **Token Limits**
   ```yaml
   # In agent configs
   ai_config:
     max_tokens: 2000
   ```

3. **Cost Controls**
   ```yaml
   cost_controls:
     max_daily_cost: 5.00
     warning_threshold: 0.8
   ```

### Monitoring

Check AI usage:

1. **GitHub Actions**
   - View workflow runs
   - Check action logs
   - Monitor failures

2. **API Dashboards**
   - OpenAI usage dashboard
   - Anthropic console
   - Monitor costs daily

3. **Alerts**
   - Set up budget alerts
   - Monitor rate limit warnings
   - Track error rates

### Usage Optimization

Reduce costs:

1. **Targeted Triggers**
   - Only run on relevant files
   - Skip on documentation-only changes
   - Use path filters effectively

2. **Efficient Prompts**
   - Keep context concise
   - Limit token usage
   - Cache results when possible

3. **Manual Oversight**
   - Review automatically-generated content
   - Disable agents when not needed
   - Use manual workflow dispatch

## Troubleshooting

### Common Issues

#### 1. AI Review Not Running

**Problem:** Pull request created but no AI review appears

**Solutions:**
- Check workflow file paths match changed files
- Verify OPENAI_API_KEY secret is set
- Review GitHub Actions logs for errors
- Check rate limits haven't been exceeded

#### 2. Lore Consistency False Positives

**Problem:** AI flags correct lore as inconsistent

**Solutions:**
- Update canonical reference files
- Add valid variants to agent config
- Use exemptions for special cases

#### 3. High API Costs

**Problem:** Unexpected API usage charges

**Solutions:**
- Review and reduce max_tokens settings
- Add more aggressive path filters
- Disable less critical agents
- Use manual triggers instead of automatic

#### 4. Agent Conflicts

**Problem:** Multiple agents making contradictory suggestions

**Solutions:**
- Check agent execution order
- Review conflict resolution settings
- Prioritize agents appropriately
- Disable conflicting agents temporarily

For more detailed troubleshooting, see [TROUBLESHOOTING.md](TROUBLESHOOTING.md).

## Additional Resources

- [Custom Agents Guide](CUSTOM_AGENTS.md)
- [GitHub App Setup](GITHUB_APP_SETUP.md)
- [Quick Start Guide](QUICK_START.md)
- [Contributing Guidelines](../CONTRIBUTING.md)

## Support

For help with AI automation:

1. Check [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
2. Review GitHub Actions logs
3. Open an issue with the `ai-automation` label
4. Contact project maintainers

---

*This automation system helps maintain quality and consistency while respecting human creativity and decision-making. AI is a tool to assist, not replace, human developers.*
