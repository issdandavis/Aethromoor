# How to Sort and Consolidate Open Issues - START HERE

If you're asking "how do I sort and consolidate my open issues?", you're in the right place!

## The Situation

Your Avalon repository has **8 open issues** that need organization:
- 3 contain valuable lore content (but shouldn't be in issues)
- 1 is a legitimate game development task (needs enhancement)
- 4 are placeholder/test issues (should be closed)

## The Solution (3 Easy Steps)

### Step 1: Let the Custom Agent Migrate Lore (30 minutes)

Your repository has a custom agent perfect for this task. Run it with:

```
@my-agent Please migrate lore content from GitHub issues to organized markdown files:

From issue #4 "Magical overview" create:
- lore/MAGICAL_SYSTEMS.md (the magic system details)
- lore/COMPLETE_WORLD_OVERVIEW.md (characters, realms, timeline)

From issue #3 "Expanded faction organization" create:
- lore/FACTIONS_AND_POLITICS.md (faction details and politics)

From issue #5 "Sytll" create:
- writing_drafts/NOVEL_PLANNING.md (story planning content)

Organize with tables of contents and ensure consistency with existing lore.
```

After the agent completes, close issues #3, #4, #5 with:
> "Content migrated to [filename]. Future lore should be added via pull requests to lore files."

### Step 2: Enhance the Real Task (10 minutes)

Issue #26 is your only legitimate active task. Update it:

**Change title to:** "Add remaining expedition scenes to ChoiceScript game"

**Add this description:**
```markdown
## Scenes Needed (from PROJECT_ROADMAP.md Phase 2)
- [ ] singing_dunes.txt - Singing Dunes expedition
- [ ] verdant_tithe.txt - Verdant Tithe expedition  
- [ ] rune_glacier.txt - Rune Glacier expedition

## Context
Convert these HTML game scenes to ChoiceScript for professional publication.

## Related Files
- Source: game/game.js
- Target: choicescript_game/scenes/
- Reference: docs/PROJECT_ROADMAP.md
```

**Add labels:** enhancement, game-content, choicescript

### Step 3: Close Placeholder Issues (5 minutes)

Close these 4 issues with quick notes:

**#60** (PDF link): "Closing - external links should be archived in-repo."
**#53, #45** (ChatGPT links): "Closing - ChatGPT conversations should be documented in markdown files."
**#47** (just emoji): "Closing - no actionable content. Use issue templates for future issues."

## Done! 

**Result:**
- ✅ Clean issue tracker (1 well-defined task)
- ✅ Lore properly organized in files
- ✅ Templates ready for future issues
- ✅ Total time: ~45 minutes

## Helpful Documents

This PR includes everything you need:

1. **Quick Start** (you are here!): `docs/HOW_TO_CONSOLIDATE_ISSUES.md`
2. **Quick Reference**: `docs/QUICK_REFERENCE_ISSUE_CONSOLIDATION.md`
3. **Detailed Guide**: `docs/ISSUE_ORGANIZATION_GUIDE.md`
4. **Step-by-Step**: `docs/NEXT_STEPS_ISSUE_CONSOLIDATION.md`
5. **Checklist**: `docs/CONSOLIDATION_CHECKLIST.md`
6. **Flowchart**: `docs/ISSUE_MANAGEMENT_FLOWCHART.md`

Pick the one that matches your style - they all lead to the same organized result!

## Future Issues

Going forward, use the templates in `.github/ISSUE_TEMPLATE/`:
- **Game Scene Request** - For new game content
- **Bug Report** - For problems
- **Feature Request** - For ideas
- **Lore Addition** - For worldbuilding (then submit as PR)

See `CONTRIBUTING.md` for full guidelines.

## Questions?

- Not sure which file to use? → See Quick Reference
- Want step-by-step? → See Next Steps guide  
- Need a checklist? → See Consolidation Checklist
- Want the full story? → See Issue Organization Guide
- Need a flowchart? → See Issue Management Flowchart

---

**Ready?** Start with Step 1 above and you'll have organized issues in under an hour!
