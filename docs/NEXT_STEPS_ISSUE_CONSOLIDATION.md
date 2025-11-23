# Next Steps for Issue Consolidation

This document provides a clear action plan for consolidating and organizing the repository's open issues.

## Quick Summary

**Current State:** 8 open issues, mix of valuable content and placeholders
**Goal:** Organized issue tracker with actionable tasks, lore in proper files
**Timeline:** Can be completed in 1-2 hours

## Immediate Actions Required

### Step 1: Migrate Lore Content (Issues #3, #4, #5)

The custom agent "my-agent" can help with this migration task. Here's the plan:

**Issue #4 Content → Create these files:**
- `lore/MAGICAL_SYSTEMS.md` - The complete magical system overview
- `lore/COMPLETE_WORLD_OVERVIEW.md` - Characters, realms, timeline

**Issue #3 Content → Create this file:**
- `lore/FACTIONS_AND_POLITICS.md` - Faction histories, strategic doctrines, political systems

**Issue #5 Content → Create this file:**
- `writing_drafts/NOVEL_PLANNING.md` - Story planning and novel adaptation outline

**Commands to execute:**
```bash
# Let the lore curator agent handle this
# It will organize content properly into the lore structure
```

### Step 2: Enhance Issue #26 (Game Development Task)

This is the only legitimate active task that should remain open.

**Current title:** "Need more scenes"
**New title:** "Add remaining expedition scenes to ChoiceScript game"

**Updated description should include:**
```markdown
## Scenes Needed (from PROJECT_ROADMAP.md Phase 2)

According to the project roadmap, the following scenes need to be converted from HTML to ChoiceScript:

- [ ] `singing_dunes.txt` - Singing Dunes expedition
- [ ] `verdant_tithe.txt` - Verdant Tithe expedition  
- [ ] `rune_glacier.txt` - Rune Glacier expedition

## Context
These are the remaining expedition scenes from the HTML game that need to be ported to the ChoiceScript version for professional publication.

## Requirements
- Maintain narrative consistency with HTML version
- Implement proper stat tracking (Collaboration stat)
- Include Polly's commentary
- Test all choice paths and endings
- Verify stat progression balance

## Related Files
- Source: `game/game.js` (HTML version)
- Target: `choicescript_game/scenes/`
- Reference: `docs/PROJECT_ROADMAP.md` (Phase 2 section)

## Labels
enhancement, game-content, choicescript, good first issue
```

### Step 3: Close Placeholder Issues

These issues should be closed with explanatory comments:

**Issue #60: "everweave-export.pdf"**
Closing comment:
```
This issue contained only an external link to a PDF export. External content should be archived in the repository or documented in markdown files. If the PDF content is valuable, please:
1. Download and add to repository
2. Create a lore file with the content
3. Open a new issue with proper description
```

**Issue #53: "Try and connect"**
**Issue #45: "Livlve"**
Closing comment:
```
This issue contained only a link to a ChatGPT conversation. ChatGPT conversations are temporary and should not be tracked as issues. If the conversation content is valuable:
1. Copy relevant content into a markdown file in the repository
2. Create a proper issue with description and context
3. Use GitHub Discussions for brainstorming conversations
```

**Issue #47: "work"**
Closing comment:
```
Closing as this issue has no actionable content. Future issues should:
1. Have descriptive titles
2. Include clear descriptions of the task or problem
3. Provide necessary context and requirements
4. Use the issue templates in .github/ISSUE_TEMPLATE/
```

## Implementation Timeline

### Phase 1: Documentation Migration (30-45 minutes)
1. Create lore files from issues #3, #4, #5
2. Verify all content migrated correctly
3. Update lore/README.md with links to new files
4. Close issues with migration notes

### Phase 2: Issue Cleanup (15-20 minutes)
1. Update issue #26 with detailed description
2. Add labels and milestone to #26
3. Close placeholder issues #45, #47, #53, #60
4. Verify issue tracker is clean

### Phase 3: Process Improvements (10-15 minutes)
1. Update CONTRIBUTING.md with issue guidelines
2. Verify issue templates are in place
3. Document labeling strategy
4. Create GitHub labels if needed

## Files Created in This PR

The following files have been created to support issue organization:

1. `docs/ISSUE_ORGANIZATION_GUIDE.md` - Comprehensive guide for issue organization
2. `.github/ISSUE_TEMPLATE/game-scene-request.md` - Template for game content requests
3. `.github/ISSUE_TEMPLATE/lore-addition.md` - Template for lore additions
4. `.github/ISSUE_TEMPLATE/bug-report.md` - Template for bug reports
5. `.github/ISSUE_TEMPLATE/feature-request.md` - Template for feature requests
6. `docs/NEXT_STEPS_ISSUE_CONSOLIDATION.md` - This file

## Manual Steps for Repository Owner

After this PR is merged, you'll need to:

1. **Create the lore files** (or delegate to custom agent):
   - Copy content from issues #3, #4, #5 into new markdown files
   - Organize content logically
   - Add navigation/table of contents

2. **Update issue #26**:
   - Edit the issue with new title and description
   - Add labels: `enhancement`, `game-content`, `choicescript`
   - Create and assign "Phase 2 Development" milestone

3. **Close placeholder issues** (#45, #47, #53, #60):
   - Add closing comments as specified above
   - Close each issue

4. **Create GitHub labels** (if they don't exist):
   - `game-content` - Game scene/content additions
   - `lore` - Worldbuilding and lore
   - `choicescript` - ChoiceScript-specific
   - `html-game` - HTML game-specific
   - `documentation` - Documentation improvements

## Using the Custom Agent

The repository has a custom agent "my-agent" described as:
> "Curates, organizes, and safeguards the Avalon narrative canon while assisting with coding and file management tasks."

This agent would be perfect for:
1. Migrating lore content from issues to properly organized files
2. Ensuring consistency across lore documents
3. Validating that content fits the established narrative
4. Organizing content by theme and chronology

**Suggested prompt for the agent:**
```
Please help migrate lore content from GitHub issues to proper markdown files:

1. From issue #4 "Magical overview" - create:
   - lore/MAGICAL_SYSTEMS.md (magic system details)
   - lore/COMPLETE_WORLD_OVERVIEW.md (characters, realms, timeline)

2. From issue #3 "Expanded faction organization" - create:
   - lore/FACTIONS_AND_POLITICS.md

3. From issue #5 "Sytll" - create:
   - writing_drafts/NOVEL_PLANNING.md

Organize the content logically, add table of contents to each file, and ensure consistency with existing lore. After migration, I'll close these issues with references to the new files.
```

## Success Criteria

You'll know this consolidation is successful when:

✅ Issue tracker has only actionable, well-defined tasks
✅ Lore content is in markdown files, not GitHub issues  
✅ Issue #26 has clear requirements and labels
✅ Placeholder issues are closed with helpful guidance
✅ Issue templates guide future contributors
✅ Documentation clearly explains the issue process

## Questions or Problems?

If you encounter issues during this consolidation:

1. **For lore migration questions**: Refer to existing files in `lore/` for format examples
2. **For issue structure questions**: See `CONTRIBUTING.md` for guidelines
3. **For technical problems**: Create a new issue using the bug report template
4. **For process questions**: Refer to `docs/ISSUE_ORGANIZATION_GUIDE.md`

## Future Recommendations

After completing this consolidation:

1. **Regular cleanup**: Review open issues monthly
2. **Use milestones**: Track progress with GitHub milestones
3. **Use projects**: Consider GitHub Projects for game development tracking
4. **Documentation first**: Add lore to files, not issues
5. **Templates work**: Encourage use of issue templates
6. **Label consistently**: Apply labels to all issues for filtering

---

**Ready to proceed?** Start with Phase 1 (documentation migration) and work through each phase systematically. The custom agent can handle the heavy lifting of content migration.
