# Issue Consolidation Quick Reference

## TL;DR - What to Do

You have 8 open issues that need sorting. Here's the fastest way to consolidate them:

### ✅ 1. Use the Custom Agent for Lore Migration

Run this command/prompt with your custom agent:
```
Please migrate lore content from GitHub issues #3, #4, and #5 into organized markdown files:

From issue #4 → Create:
- lore/MAGICAL_SYSTEMS.md
- lore/COMPLETE_WORLD_OVERVIEW.md

From issue #3 → Create:
- lore/FACTIONS_AND_POLITICS.md

From issue #5 → Create:
- writing_drafts/NOVEL_PLANNING.md

After migration, add a note to each file crediting the original issue.
```

Then close issues #3, #4, #5 with:
> "Content migrated to [filename]. Future lore should be added via PRs to lore files."

### ✅ 2. Fix Issue #26 (The Only Real Task)

Edit the issue with:
- **New title:** "Add remaining expedition scenes to ChoiceScript game"
- **Add this description:**
  ```markdown
  Scenes needed from PROJECT_ROADMAP.md Phase 2:
  - [ ] singing_dunes.txt
  - [ ] verdant_tithe.txt  
  - [ ] rune_glacier.txt
  
  These scenes exist in the HTML game and need ChoiceScript conversion.
  See docs/PROJECT_ROADMAP.md for details.
  ```
- **Add labels:** enhancement, game-content, choicescript

### ✅ 3. Close Placeholder Issues

Close these issues with a quick note:

**#45, #53** (ChatGPT links):
> "Closing - ChatGPT links are temporary. Please archive valuable content in markdown files."

**#47** (just emoji):
> "Closing - no actionable content. Use issue templates for future issues."

**#60** (PDF link):
> "Closing - external links should be archived in-repo. Re-open with archived content if needed."

## Result

After these steps:
- ✅ 4 issues closed (after lore migration)
- ✅ 4 issues closed (cleanup)
- ✅ 1 issue enhanced (proper task)
- ✅ Clean, organized issue tracker

## Files Already Created

This PR includes:
1. ✅ `docs/ISSUE_ORGANIZATION_GUIDE.md` - Full guide
2. ✅ `docs/NEXT_STEPS_ISSUE_CONSOLIDATION.md` - Detailed steps
3. ✅ `.github/ISSUE_TEMPLATE/*.md` - 4 issue templates
4. ✅ Updated `CONTRIBUTING.md` - Issue guidelines
5. ✅ This quick reference card

## Time Required

- Lore migration: 30 minutes (with custom agent)
- Issue updates: 15 minutes
- **Total: ~45 minutes**

## Questions?

See the full guides:
- `docs/ISSUE_ORGANIZATION_GUIDE.md` - Complete guide
- `docs/NEXT_STEPS_ISSUE_CONSOLIDATION.md` - Step-by-step
- `CONTRIBUTING.md` - Updated with issue guidelines
