# Avalon Custom Agents Overview

## What Are Custom Agents?

Custom agents are specialized AI assistants for GitHub Copilot that are tailored to specific repository needs. They have domain-specific knowledge and follow defined rules and boundaries.

## Available Agents in This Repository

### 1. Avalon Lore Steward
**Location**: `.github/agents/my-agent.agent.md`

**Purpose**: Curates, organizes, and safeguards the Avalon narrative canon

**Use Cases**:
- Validating new narrative content against existing lore
- Cross-referencing character details and timelines
- Ensuring magic system consistency
- Organizing lore files and documents
- Managing character relationship continuity

**How to Use**:
```
@avalon-lore-steward Please verify this character's timeline against the master chronicle
@avalon-lore-steward Help me organize these new lore files
@avalon-lore-steward Check if this magical concept fits the established system
```

---

### 2. ChoiceScript Converter
**Location**: `.github/agents/choicescript-converter.agent.md`

**Purpose**: Converts HTML game content to professional ChoiceScript format

**Use Cases**:
- Converting HTML scenes to ChoiceScript `.txt` files
- Implementing proper stat tracking
- Maintaining scene parity between versions
- Ensuring correct ChoiceScript syntax
- Documenting stat changes and branching logic

**How to Use**:
```
@choicescript-converter Convert the singing_dunes scene from HTML to ChoiceScript
@choicescript-converter Implement stat tracking for this expedition scene
@choicescript-converter Verify the branching structure matches the HTML original
```

---

## How to Enable Custom Agents

If you're seeing an error about custom models being disabled:

### Quick Solution
See [QUICK_START_CUSTOM_AGENTS.md](./QUICK_START_CUSTOM_AGENTS.md) for a 5-minute fix.

### Complete Guide
See [CUSTOM_AGENTS_SETUP.md](./CUSTOM_AGENTS_SETUP.md) for detailed setup instructions.

### Summary
1. **Enterprise Owner**: Enable in Enterprise → Policies → Copilot → Custom agents
2. **Organization Owner**: Enable in Organization → Settings → Copilot → Custom agents
3. **Repository Admin**: Merge `.agent.md` files to main branch
4. **Wait**: 5-10 minutes for activation
5. **Use**: Reference agents with `@agent-name` in Copilot Chat

---

## Agent Architecture

### File Structure
```
.github/
└── agents/
    ├── my-agent.agent.md              # Avalon Lore Steward
    ├── choicescript-converter.agent.md # ChoiceScript Converter
    └── [future-agent].agent.md        # Additional agents
```

### Agent File Format
Each agent file contains:
1. **YAML Frontmatter** - Configuration (name, description, tools, metadata)
2. **Instructions** - Detailed role and responsibilities
3. **Commands** - Common commands and operations
4. **Boundaries** - What the agent should/shouldn't do
5. **Examples** - Code style and output format examples

### Basic Template
```yaml
---
name: agent-name
description: Brief description (REQUIRED)
target: github-copilot
tools:
  - read
  - edit
  - view
metadata:
  version: 1.0.0
---

# Agent Name

Detailed instructions for the agent...
```

---

## Multi-Agent Workflow

The Avalon project uses multiple specialized agents that work together:

### Workflow Example: Converting a Scene

1. **Lore Curator** (@avalon-lore-steward)
   - Validates scene's narrative consistency
   - Checks character details against chronicles
   - Approves lore integrity

2. **Conversion Engineer** (@choicescript-converter)
   - Converts HTML to ChoiceScript
   - Implements stat tracking
   - Creates scene file

3. **Structural Reviewer** (Human or future agent)
   - Verifies branching structure
   - Checks scene parity
   - Updates tracking documents

4. **Quality Balancer** (Human or future agent)
   - Adjusts stat thresholds
   - Ensures balanced gameplay
   - Updates stats matrix

### Shared Documents
Agents coordinate through shared tracking files:
- `STATUS_CONTEXT.md` - Current work snapshot
- `SCENE_PARITY_CHECKLIST.md` - Conversion status
- `STATS_MATRIX.md` - Stat changes tracking

---

## Best Practices

### When to Use Custom Agents

**Use Lore Steward for**:
- ✅ Validating narrative consistency
- ✅ Character timeline verification
- ✅ Magic system compliance
- ✅ File organization
- ✅ Lore documentation updates

**Use ChoiceScript Converter for**:
- ✅ HTML to ChoiceScript conversion
- ✅ Stat tracking implementation
- ✅ Syntax verification
- ✅ Scene parity checking
- ✅ Documentation updates

### When to Use General Copilot

**Use regular @workspace or direct Copilot for**:
- General coding questions
- Repository-wide searches
- Non-Avalon specific tasks
- Quick file edits
- Generic programming help

### Agent Communication

**Be specific in your prompts**:
```
❌ "Help with this scene"
✅ "@choicescript-converter Convert singing_dunes.html to ChoiceScript format with stat tracking"

❌ "Check lore"
✅ "@avalon-lore-steward Verify Izack's timeline in this chapter against IZACK_MASTER_CHRONICLE_UPDATED.txt"
```

**Include context**:
```
@avalon-lore-steward I'm adding a new character named Elara who appears in 
Chapter 3. She's a dimensional mage who studied under Aria. Please check if 
this conflicts with existing lore and verify her powers align with the 
collaborative magic system.
```

---

## Creating New Agents

### Process
1. **Identify Need**: What specialized task needs a dedicated agent?
2. **Create File**: Add new `.agent.md` file in `.github/agents/`
3. **Define Role**: Write clear instructions and boundaries
4. **Add Examples**: Show desired output format
5. **Test Locally**: Use Copilot CLI if available
6. **Merge to Main**: Agent activates 5-10 minutes after merge
7. **Document**: Update this overview with new agent info

### Example Ideas for Future Agents
- **Quality Balancer** - Adjusts stat thresholds and gameplay balance
- **Structural Reviewer** - Verifies scene parity and branching logic
- **Documentation Specialist** - Updates and maintains documentation
- **Testing Assistant** - Helps write and run tests
- **Compliance Checker** - Ensures ChoiceScript follows submission guidelines

---

## Troubleshooting

### Agent Not Appearing

**Check**:
- [ ] File is in `.github/agents/` directory
- [ ] File has `.agent.md` extension
- [ ] YAML frontmatter has `description` field
- [ ] File is merged to main/default branch
- [ ] Waited 5-10 minutes after merge
- [ ] Copilot subscription is Business or Enterprise

### Agent Gives Unexpected Responses

**Solutions**:
- Review agent's instruction file
- Be more specific in your prompt
- Include necessary context
- Check agent's defined boundaries
- Verify agent has correct tools listed

### Can't Create/Enable Agents

**See**:
- [QUICK_START_CUSTOM_AGENTS.md](./QUICK_START_CUSTOM_AGENTS.md) - Quick fix
- [CUSTOM_AGENTS_SETUP.md](./CUSTOM_AGENTS_SETUP.md) - Full guide

**Common Causes**:
- Enterprise policy blocking custom agents
- Insufficient permissions (need Enterprise/Org Owner)
- Wrong subscription type (need Business/Enterprise)

---

## Security & Compliance

### Agent Permissions
- Agents only use tools explicitly listed in their configuration
- Agents follow boundaries defined in their instruction files
- Agents don't have access to secrets unless explicitly given
- Agents are scoped to repositories where they're defined

### Best Practices
- Never include API keys or secrets in agent files
- Define clear boundaries for each agent
- Use metadata tags for compliance tracking
- Review and update agents regularly
- Document any changes to agent capabilities

### Compliance Metadata Example
```yaml
metadata:
  version: 1.0.0
  compliance: project-specific
  security-level: standard
  last-review: 2025-11-25
  approved-by: project-lead
```

---

## Resources

### Documentation
- [Custom Agents Setup Guide](./CUSTOM_AGENTS_SETUP.md)
- [Quick Start Guide](./QUICK_START_CUSTOM_AGENTS.md)
- [GitHub Official Docs](https://docs.github.com/en/copilot/reference/custom-agents-configuration)

### Project-Specific
- [Multi-AI Coordination](./../.github/AGENTS.md)
- [Copilot Instructions](./../.github/copilot-instructions.md)
- [Project Roadmap](./PROJECT_ROADMAP.md) (if exists)

### External Resources
- [GitHub Blog: Custom Agents](https://github.blog/changelog/2025-10-28-custom-agents-for-github-copilot/)
- [How to Write Great Agents](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/)
- [Custom Agents Template Repo](https://github.com/docs/custom-agents-template)
- [Copilot CLI for Testing](https://gh.io/customagents/cli)

---

## FAQ

### Q: Do I need custom agents to use this repository?
**A**: No. Custom agents are helpful but optional. You can use regular GitHub Copilot or work without AI assistance.

### Q: Can I use these agents in other repositories?
**A**: Repository agents only work in the repository where they're defined. For org-wide agents, create them in a `.github-private` repository.

### Q: Can I modify existing agents?
**A**: Yes! Edit the `.agent.md` files and merge to main. Changes activate after 5-10 minutes.

### Q: How do I disable an agent?
**A**: Delete or rename the `.agent.md` file, or move it out of the `.github/agents/` directory.

### Q: Can I have multiple agents active?
**A**: Yes! You can have as many agents as needed. Reference them individually with `@agent-name`.

### Q: Do agents cost extra?
**A**: No additional cost beyond your GitHub Copilot Business or Enterprise subscription.

---

**Last Updated**: November 2025  
**Version**: 1.0.0  
**Maintainer**: Avalon Project Team
