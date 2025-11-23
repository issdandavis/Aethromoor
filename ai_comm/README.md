# AI Communication Channels

This directory contains communication logs for AI agents working across different sessions on the Avalon Codex project.

## Purpose

These logs enable:
- **Cross-session continuity**: Future AI agents can pick up where previous sessions left off
- **Knowledge sharing**: Important discoveries, patterns, and decisions are preserved
- **Priority tracking**: Current and upcoming work is clearly documented
- **Context preservation**: Narrative and technical context remains accessible

## Channel Files

| File | Purpose | What to Log |
|------|---------|-------------|
| `priorities.md` | Development priorities and next actions | Current phase status, blocking issues, upcoming milestones |
| `scene_ideas.md` | Narrative concepts and story enhancements | New scene concepts, character moments, plot branches |
| `build_tips.md` | Technical tips and commands | Build/test commands, debugging shortcuts, tool usage |
| `lore_index.md` | Canonical lore references | Key document locations, consistency notes, magic system rules |

## Usage Guidelines

### For AI Agents

1. **Read First**: Check all channels at session start to understand current state
2. **Log Discoveries**: Add entries when you find important patterns or make key decisions
3. **Update Status**: When completing work, update the relevant channel with results
4. **Use ISO Timestamps**: Format entries as `YYYY-MM-DDTHH:MM:SSZ` for sortability

### Entry Format

Each channel has its own format (see individual files), but all follow this pattern:
```
- [ISO Timestamp] — [Summary]. [Context Field]: [Details]. [Action Field]: [Next steps]
```

### When to Add Entries

- Starting a new work phase
- Discovering important lore consistency rules
- Finding useful tools or commands
- Identifying future work items
- Completing major milestones

## Maintenance

- Keep entries concise but informative
- Remove obsolete entries when work is completed
- Link to relevant files/docs when possible
- Avoid duplicating information already in `docs/` - reference those files instead

---

*"The spiral continues. Every session writes the next chapter."*
