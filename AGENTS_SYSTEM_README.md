# 🤖 AI Agent Communication System

## Overview

This repository uses **AGENTS.md files** to enable effective collaboration between different AI coding assistants (ChatGPT, Claude, GitHub Copilot, Cody, etc.) working on the Avalon Codex project.

## What Are AGENTS.md Files?

AGENTS.md files are directory-specific instruction documents that AI agents automatically read when working in those directories. They provide:

- **Context**: What this directory contains and its role in the project
- **Standards**: Coding conventions, writing style, and quality requirements
- **Workflows**: How to collaborate with other AI agents
- **Guidelines**: Dos and don'ts specific to this area of the codebase
- **References**: Links to related documentation and resources

## File Locations

```
Avalon/
├── AGENTS.md                          → Global project instructions
├── choicescript_game/AGENTS.md        → ChoiceScript development guidance
├── game/AGENTS.md                     → HTML game maintenance
├── lore/AGENTS.md                     → Worldbuilding and canon consistency
├── writing_drafts/AGENTS.md           → Novel manuscript guidelines
└── docs/AGENTS.md                     → Documentation standards
```

## How It Works

### Scope and Inheritance
- Each AGENTS.md applies to **its directory and all subdirectories**
- Deeper AGENTS.md files **override** higher-level ones for specific guidance
- All agents should read the **root AGENTS.md** first for global context

### Reading Priority
When an AI agent works in a directory:
1. Read `/AGENTS.md` (global project context)
2. Read `/[directory]/AGENTS.md` (specific area guidance)
3. Follow both sets of instructions, with directory-specific taking priority

## Multi-AI Collaboration Roles

The AGENTS.md system defines specialized roles for different AI assistants:

### **Lore Curator** 
- **Best for**: Claude, GPT-4 (creative focus)
- **Responsibilities**: Validate narrative against canon, flag inconsistencies
- **Works in**: `lore/`, reviews content from other directories

### **Conversion Engineer**
- **Best for**: GitHub Copilot, Continue
- **Responsibilities**: Translate HTML game → ChoiceScript format
- **Works in**: `choicescript_game/`, references `game/`

### **Structural Reviewer**
- **Best for**: Cody, Codeium
- **Responsibilities**: Verify scene parity, validate implementations
- **Works in**: All directories, cross-references between `game/` and `choicescript_game/`

### **Quality Balancer**
- **Best for**: Any AI agent
- **Responsibilities**: Ensure gameplay balance, stat progression consistency
- **Works in**: `game/` and `choicescript_game/`

### **Automation Planner**
- **Best for**: Any AI agent
- **Responsibilities**: Document workflows, maintain automation guides
- **Works in**: `docs/`, `config/`

## Shared Context Artifacts

To enable coordination, AI agents maintain these tracking documents:

### **STATUS_CONTEXT.md** (in `/docs/`)
Weekly snapshot of current work, blockers, and pending tasks.

### **SCENE_PARITY_CHECKLIST.md** (in `/docs/`)
Tracks HTML vs ChoiceScript conversion status for each scene.

### **STATS_MATRIX.md** (in `/docs/`)
Documents all stat-affecting choices and ending thresholds.

## Hand-off Conventions

### Comment Prefixes (in draft code)
```
// TODO:[LORE]: Check character consistency
// TODO:[CONVERT]: Needs ChoiceScript translation
// TODO:[STRUCT]: Verify scene parity
// TODO:[BALANCE]: Stat threshold may be too easy
// TODO:[AUTO]: Add to automation workflow
```

### Commit Message Prefixes
```
Lore: Updated character timeline
Convert: Translated Singing Dunes to ChoiceScript
Struct: Fixed branching mismatch
Balance: Adjusted Collaboration thresholds
Auto: Added Zapier trigger
```

## For Human Contributors

### Setting Up Communication with AI Agents

1. **Read the relevant AGENTS.md** for the area you're working on
2. **Follow the established conventions** (file naming, commit prefixes, etc.)
3. **Update tracking documents** when making significant changes
4. **Use TODO comments** to flag items for specific AI roles
5. **Check AGENTS.md files** before asking AI agents for help

### Creating New AGENTS.md Files

If you create a new major directory:

1. **Create `[directory]/AGENTS.md`** with these sections:
   - **Purpose**: What this directory contains
   - **Structure**: File organization
   - **Standards**: Conventions and requirements
   - **Guidelines**: Dos and don'ts
   - **Integration Points**: How this relates to other directories
   - **Quality Checklist**: How to verify good work

2. **Link to parent AGENTS.md** for context inheritance

3. **Document in root AGENTS.md** if it's a major new area

### When to Update AGENTS.md Files

Update when:
- ✅ Conventions change (new standards adopted)
- ✅ New workflow established (collaboration pattern)
- ✅ Common mistakes identified (add to "avoid" list)
- ✅ New tools/integrations added (document usage)
- ✅ Quality standards evolve (update checklists)

Don't update for:
- ❌ Temporary project state (use STATUS_CONTEXT.md instead)
- ❌ Personal preferences (keep instructions general)
- ❌ One-off tasks (not worth documenting permanently)

## Benefits of This System

### For AI Agents
- **Context-aware**: Understand project structure and goals immediately
- **Coordinated**: Work together without stepping on each other
- **Consistent**: Follow established patterns and conventions
- **Efficient**: Don't repeat mistakes or duplicate work

### For Humans
- **Onboarding**: New contributors learn project structure quickly
- **Quality**: AI agents produce consistent, high-quality work
- **Coordination**: Multiple AI agents can work in parallel
- **Documentation**: Living documentation that stays current

## Examples of Usage

### Example 1: Converting a Game Scene
```
1. Lore Curator reads lore/AGENTS.md
2. Reviews HTML scene against lore canon
3. Approves or flags inconsistencies
4. Conversion Engineer reads choicescript_game/AGENTS.md
5. Translates approved HTML → ChoiceScript
6. Structural Reviewer reads game/AGENTS.md and choicescript_game/AGENTS.md
7. Verifies parity between versions
8. Updates SCENE_PARITY_CHECKLIST.md
```

### Example 2: Updating Documentation
```
1. Automation Planner reads docs/AGENTS.md
2. Documents new Zapier workflow in AUTOMATION_GUIDE.md
3. Follows documentation standards from AGENTS.md
4. Commits with "Auto:" prefix per hand-off conventions
```

### Example 3: Writing Novel Content
```
1. Writer (human or AI) reads writing_drafts/AGENTS.md
2. Checks lore/AGENTS.md for character voice guidelines
3. Writes new chapter following established standards
4. Lore Curator validates against canon
5. Commits with descriptive message
```

## Quick Reference

### For ChatGPT Users (Avalon Codex Creator)
Your AI agents will **automatically read** relevant AGENTS.md files when you ask them to work on the repository. You can:
- Reference specific AGENTS.md sections in your prompts
- Ask agents to validate against AGENTS.md guidelines
- Remind agents about role assignments (Lore Curator, etc.)

### For AI Agents Reading This
1. **Always read** the root `/AGENTS.md` first
2. **Read directory-specific** AGENTS.md for your current task
3. **Follow established roles** if one is assigned to you
4. **Update tracking documents** when making changes
5. **Use hand-off conventions** for clear communication
6. **Ask questions** if AGENTS.md guidance is unclear

## Troubleshooting

### "AI agent isn't following the guidelines"
- Ensure the agent has read the relevant AGENTS.md file
- Reference specific sections: "Please review the [section] in [directory]/AGENTS.md"
- Check if there are conflicting instructions between AGENTS.md files

### "Multiple AI agents created conflicting changes"
- Review the role assignments in root AGENTS.md
- Ensure each agent is working in their specialized area
- Use STATUS_CONTEXT.md to coordinate current work
- Update AGENTS.md if role boundaries are unclear

### "AGENTS.md is too long/complex"
- That's okay! Comprehensive is better than incomplete
- AI agents can handle long documents better than humans
- Use clear headings and formatting for easy navigation
- Link to other docs rather than duplicating information

## Future Enhancements

Potential improvements to this system:
- **Template AGENTS.md** for new directories
- **Validation script** to check AGENTS.md completeness
- **Cross-reference checker** to ensure consistency
- **Version history** tracking for AGENTS.md changes

---

## Getting Started

**For AI Agents**: Read `/AGENTS.md` now, then read the AGENTS.md file for the directory you're working in.

**For Humans**: Review the AGENTS.md file for the area you're working on before starting. It contains all the context and conventions you need to know.

**For New Contributors**: Start with `/AGENTS.md` for the big picture, then dive into specific AGENTS.md files as you explore different parts of the codebase.

---

*This system enables AI agents to work together like a well-coordinated team, each bringing their specialized expertise while maintaining consistency across the entire project.*
