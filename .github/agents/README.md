# Custom GitHub Agents for Avalon

This directory contains configurations for custom GitHub Copilot agents designed to assist with the Avalon game development project.

## Available Agents

### 1. Avalon Lore Steward (`my-agent.agent.md`)
**Purpose:** Curates, organizes, and safeguards the Avalon narrative canon while assisting with coding and file management tasks.

**Use Cases:**
- Validating lore consistency across game scenes
- Organizing narrative materials
- Maintaining character and world information
- Ensuring story continuity across multiple game paths

### 2. Code Review Agent (`code_review_agent.yml`)
**Purpose:** Automated code review for game scripts, ChoiceScript files, and JavaScript code.

**Use Cases:**
- Reviewing ChoiceScript scene files for syntax errors
- Checking game logic and branching consistency
- Validating stat tracking and variable usage
- Ensuring code quality standards

### 3. Documentation Agent (`documentation_agent.yml`)
**Purpose:** Maintains and improves project documentation.

**Use Cases:**
- Updating README files
- Creating tutorial content
- Ensuring documentation stays current with code changes
- Generating API documentation

## Agent Configuration

Agents are configured using YAML files that define:
- Agent name and description
- Trigger conditions
- Required permissions
- Actions to perform

See `config.yml` for global agent settings.

## Using Custom Agents

### For GitHub Copilot Users
Custom agents appear automatically in your IDE when working in this repository. Simply mention the agent's name in comments or prompts.

### For CLI Users
```bash
# Test an agent locally
gh copilot agent test my-agent

# Run an agent on specific files
gh copilot agent run code_review_agent --files "choicescript_game/scenes/*.txt"
```

### For CI/CD
Agents can be triggered automatically via GitHub Actions workflows. See `.github/workflows/` for examples.

## Creating New Agents

1. Create a new `.yml` file in this directory
2. Define the agent configuration (see existing files for examples)
3. Add agent documentation to this README
4. Test the agent locally before committing
5. Update `config.yml` to include the new agent

## Best Practices

- **Specificity:** Design agents for specific, well-defined tasks
- **Testing:** Always test agents locally before deploying
- **Documentation:** Keep this README updated with agent capabilities
- **Permissions:** Grant minimum necessary permissions
- **Versioning:** Track agent configuration changes in git

## Related Documentation

- [Custom Agents Guide](../../docs/CUSTOM_AGENTS.md) - Detailed agent development guide
- [AI Automation](../../docs/AI_AUTOMATION.md) - Overall AI automation strategy
- [GitHub App Setup](../../docs/GITHUB_APP_SETUP.md) - Setting up GitHub Apps for agents

## Troubleshooting

### Agent Not Appearing
- Ensure the `.yml` file is properly formatted
- Check that the agent is listed in `config.yml`
- Verify you're on the default branch or have merged the agent config

### Agent Not Working as Expected
- Review agent logs in GitHub Actions
- Test locally with `gh copilot agent test`
- Check permission settings in the agent config

### Performance Issues
- Consider reducing agent scope
- Optimize trigger conditions
- Review agent action complexity

For more troubleshooting help, see [docs/TROUBLESHOOTING.md](../../docs/TROUBLESHOOTING.md).
