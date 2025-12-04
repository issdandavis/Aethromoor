# GitHub Copilot Custom Agents Setup Guide

## Overview
This guide helps you enable and configure GitHub Copilot custom agents for the Avalon project. Custom agents allow you to create specialized AI assistants tailored to your repository's specific needs.

## Problem: "Custom models have been disabled by your enterprise policy administrators"

If you're seeing this error message, it means custom agents are currently disabled at the enterprise or organization level. Even if you're a repository administrator, you need enterprise-level permissions to enable this feature.

## Prerequisites

### Required Permissions
To enable custom agents, you need:
- **Enterprise Owner** access (for enterprise-level settings)
- **Organization Owner** access (if no enterprise policy is blocking it)
- **Repository Admin** access (minimum for creating agent files, but not for enabling the feature)

### GitHub Copilot Subscription
- Your organization/enterprise must have an active GitHub Copilot Business or Enterprise subscription
- Individual Copilot plans do not support custom agents

## Step 1: Enable Custom Agents at Enterprise Level

### For Enterprise Administrators

1. **Navigate to Enterprise Settings**
   - Click your profile picture (top-right)
   - Select **Enterprise** → Choose your enterprise
   - Go to **Policies** → **Copilot**

2. **Enable Custom Agents**
   - Under **AI Controls** section, find **Custom agents**
   - Select one of the following options:
     - **Enabled everywhere** - Forces custom agents on for all organizations
     - **Allow organizations to decide** - Lets each org set their own policy
     - **Disabled** - Blocks custom agents everywhere (current setting causing the error)
   
3. **Recommended Setting**
   - Choose **"Allow organizations to decide"** for flexibility
   - Or **"Enabled everywhere"** if you want all orgs to have access

4. **Save Changes**
   - Click **Save** to apply the policy changes

### Enterprise Settings Path
```
GitHub → Enterprise → Policies → Copilot → AI Controls → Custom agents
```

## Step 2: Enable Custom Agents at Organization Level

### For Organization Owners

Once enterprise policy allows it (or if you're not under enterprise management):

1. **Navigate to Organization Settings**
   - Go to your organization page
   - Click **Settings** tab
   - Select **Copilot** in the left sidebar

2. **Configure Custom Agents**
   - Find **Custom agents** section
   - Enable custom agents for your organization
   - Choose which repositories can use custom agents:
     - **All repositories**
     - **Selected repositories** (recommended for testing)

3. **Save Configuration**

### Organization Settings Path
```
GitHub → Organization → Settings → Copilot → Custom agents
```

## Step 3: Configure Custom Agent Repository

### Repository-Level Setup (After enabling at org/enterprise level)

The Avalon repository already has a custom agent configured. The file is located at:
```
.github/agents/my-agent.agent.md
```

This file defines the "Avalon Lore Steward" agent.

### Verifying Agent Configuration

1. **Check the Agent File**
   - Navigate to `.github/agents/` in your repository
   - Verify `my-agent.agent.md` exists
   - Ensure it has proper YAML frontmatter with required fields:
     - `name` - Agent's display name
     - `description` - Brief description of agent's purpose (REQUIRED)
     - `target` - Platform (github-copilot)
     - `tools` - List of tools the agent can use

2. **Merge to Default Branch**
   - Custom agents are only active when the `.agent.md` file is in the default branch (usually `main`)
   - Create a PR to merge your agent configuration if it's not already in main

3. **Wait for Activation**
   - After merging, wait 5-10 minutes for GitHub to process the new agent
   - Agents are automatically discovered and made available

## Step 4: Using Your Custom Agent

### In GitHub Copilot Chat

1. **Open Copilot Chat**
   - In VS Code: Click the Copilot icon or use `Ctrl+Shift+I` (Windows/Linux) or `Cmd+Shift+I` (Mac)
   - In GitHub.com: Click the Copilot icon in the interface

2. **Reference Your Agent**
   - Type `@avalon-lore-steward` (or whatever name you gave your agent)
   - Ask questions specific to Avalon lore and organization
   - Example: `@avalon-lore-steward Help me verify this character's timeline consistency`

3. **Agent Scope**
   - Repository agents are available in that repository
   - Organization agents (in `.github-private` repo) are available across all org repos

## Advanced Configuration

### Creating Organization-Wide Agents

For agents available across all repositories in your organization:

1. **Create `.github-private` Repository**
   ```
   Repository name: .github-private
   Visibility: Private
   ```

2. **Add Agent Files**
   ```
   .github-private/
   └── agents/
       ├── lore-curator.agent.md
       ├── code-reviewer.agent.md
       └── compliance-checker.agent.md
   ```

3. **Merge to Default Branch**
   - All org members with Copilot access can use these agents

### Agent File Template

```yaml
---
name: your-agent-name
description: Brief description of what this agent does (REQUIRED)
target: github-copilot
tools:
  - read
  - edit
  - view
metadata:
  version: 1.0.0
  expertise: your-domain
---

# Agent Name

Detailed instructions for the agent...

## Commands
- List of common commands
- Tools the agent should use

## Boundaries
- What the agent should never do
- Security and compliance rules

## Code Style Examples
Show specific examples of desired output format.
```

## Troubleshooting

### "Custom agents are disabled"
**Solution**: Check enterprise and organization policies as described in Steps 1-2 above.

### "I can't access enterprise settings"
**Solution**: You're not an enterprise owner. Contact your enterprise administrator to request custom agents be enabled.

### "Organization settings are grayed out"
**Solution**: Your organization is under enterprise management with a restricting policy. Contact your enterprise owner.

### "Agent doesn't appear after merging"
**Solutions**:
- Wait 5-10 minutes for GitHub to process the change
- Verify the file is in `.github/agents/` directory
- Check that `description` field is present in YAML frontmatter
- Ensure the file is merged to the default branch
- Verify your Copilot subscription includes custom agents

### "Agent gives unexpected responses"
**Solutions**:
- Review the agent's instructions in the `.agent.md` file
- Be more specific in your prompts
- Check that the agent has appropriate tools listed
- Verify boundaries and examples are clear

## Security and Compliance

### Best Practices
- Never include secrets or API keys in agent configurations
- Use `metadata` fields to tag agents with compliance requirements
- Document forbidden actions in the "Boundaries" section
- Regularly review and update agent instructions
- Use organization-wide agents for security/compliance checks

### Metadata for Compliance
```yaml
metadata:
  compliance: GDPR-compliant
  security-level: high
  approved-by: security-team
  last-review: 2025-11-01
```

## Additional Resources

### Official Documentation
- [GitHub Copilot Custom Agents Configuration](https://docs.github.com/en/copilot/reference/custom-agents-configuration)
- [Creating Custom Agents](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents)
- [Preparing for Custom Agents in Enterprise](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-agents/prepare-for-custom-agents)
- [Configuring AI Model Access](https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/use-ai-models/configure-access-to-ai-models)

### Community Resources
- [GitHub Blog: Custom Agents Announcement](https://github.blog/changelog/2025-10-28-custom-agents-for-github-copilot/)
- [How to Write a Great agents.md](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/)
- [Custom Agents Template Repository](https://github.com/docs/custom-agents-template)

### Testing Your Agent
- Use the Copilot CLI for local testing: [gh.io/customagents/cli](https://gh.io/customagents/cli)
- Test in a non-production repository first
- Start with simple prompts and gradually increase complexity

## Quick Reference

### Permission Hierarchy
```
Enterprise Owner (can enable for all orgs)
    ↓
Organization Owner (can enable for org, if allowed by enterprise)
    ↓
Repository Admin (can create agent files only)
```

### File Locations
- **Repository agents**: `.github/agents/*.agent.md`
- **Organization agents**: `{org}/.github-private/agents/*.agent.md`
- **User agents**: `~/.copilot/agents/*.agent.md` (local testing)

### Priority Order
1. Repository agents (highest priority)
2. Organization agents
3. User agents (lowest priority)

## Need Help?

If you're still experiencing issues:
1. Verify you have the correct permissions level
2. Check the GitHub Status page for any service disruptions
3. Contact GitHub Support with your enterprise/org details
4. Review the official documentation links above

---

**Last Updated**: November 2025  
**Version**: 1.0.0  
**Maintainer**: Avalon Project Team
