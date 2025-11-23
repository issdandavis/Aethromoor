# GitHub Configuration Directory

This directory contains configuration files for GitHub Copilot and other GitHub features.

## Structure

### `copilot-instructions.md`
**Main Copilot configuration file** - Contains project overview, architecture patterns, development guidelines, and best practices for AI assistants working on this repository.

**Purpose**: Helps GitHub Copilot understand the Avalon Codex project structure, coding patterns, and narrative consistency requirements.

### `agents/`
Custom agent configurations for specialized tasks:
- **`my-agent.agent.md`** - Avalon Lore Steward agent for managing narrative canon, organizing files, and maintaining lore consistency

### `workflows/`
GitHub Actions workflow definitions:
- **`jekyll-docker.yml`** - Automated deployment workflow

### `instructions/`
Legacy organization notes and general AI collaboration guidelines.

## For AI Assistants

When working on this repository:
1. **Start with**: `.github/copilot-instructions.md` for project overview
2. **Use custom agents**: Tag `@my-agent` for lore and file organization tasks
3. **Consult detailed guides**: See `docs/GAME_EXPANSION_GUIDE.md` for specific game development tasks
4. **Follow patterns**: Maintain consistency with established architecture and narrative canon

## Best Practices

This configuration follows GitHub's recommended structure for Copilot instructions:
- Single source of truth: `copilot-instructions.md` (lowercase)
- Custom agents for specialized domains
- Clear separation between general guidelines and task-specific documentation
- References to detailed documentation in `docs/` directory

## Maintenance

- Update `copilot-instructions.md` when project architecture changes
- Keep custom agent definitions focused and actionable
- Version control all configuration changes
- Document significant updates in commit messages
