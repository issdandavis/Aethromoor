# AI Agent State Directory

This directory contains runtime state for AI agents.

## Purpose

Agents use this directory to:
- Track generation progress
- Maintain history of actions
- Share state between runs
- Cache results for efficiency

## Files

### content_organizer_state.json
```json
{
  "last_run": "2024-01-15T02:00:00Z",
  "files_organized": 42,
  "pending_reviews": [],
  "organization_score": 0.95
}
```

### lore_curator_state.json
```json
{
  "last_canon_check": "2024-01-15T02:00:00Z",
  "identified_gaps": [
    "Midnight Council history",
    "Elara's childhood"
  ],
  "validation_queue": []
}
```

### content_generator_state.json
```json
{
  "last_generation": "2024-01-15T02:00:00Z",
  "scenes_generated": 15,
  "current_priority": "singing_dunes",
  "generation_queue": [
    "scene:verdant_tithe_expansion",
    "lore:midnight_council"
  ]
}
```

## Persistence

State files are:
- Updated after each agent run
- Versioned with timestamps
- Backed up before modifications
- Validated on load

## Cleanup

State files are automatically cleaned:
- Old versions archived weekly
- Stale cache entries removed
- Temporary files deleted

## Manual Management

You generally don't need to edit these files, but if you do:

```bash
# View current state
cat .github/agents/state/content_generator_state.json | jq

# Reset agent state (forces fresh start)
rm .github/agents/state/*.json

# Backup state
cp -r .github/agents/state .github/agents/state_backup_$(date +%Y%m%d)
```

## Troubleshooting

### Agent seems stuck
Reset its state:
```bash
rm .github/agents/state/[agent_name]_state.json
```

### Corrupted state file
Delete it; agent will recreate:
```bash
rm .github/agents/state/[agent_name]_state.json
```

### Want to see history
Check state file history in git:
```bash
git log -- .github/agents/state/
```

---

*State files are managed automatically by the AI Agent system*
