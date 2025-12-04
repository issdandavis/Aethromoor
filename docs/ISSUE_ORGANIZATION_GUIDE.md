# Issue Organization Guide

## Current Status

As of November 2025, the Avalon repository has 8 open issues that need to be sorted and consolidated.

## Issue Analysis & Categorization

### Category 1: Lore & Worldbuilding Documentation (3 issues)

**Issues #3, #4, #5** contain extensive lore content that should be migrated to proper documentation files rather than living in GitHub issues.

#### Issue #4: "Magical overview"
- **Content**: Complete magical universe overview including characters, realms, timeline, magical systems
- **Status**: Valuable worldbuilding content
- **Recommendation**: Migrate to `lore/MAGICAL_SYSTEMS.md` and `lore/COMPLETE_WORLD_OVERVIEW.md`
- **Action**: Close issue after migration

#### Issue #3: "Expanded faction organization"
- **Content**: Detailed faction histories, strategic doctrines, Avalon Academy analysis
- **Status**: Comprehensive faction and political system documentation
- **Recommendation**: Migrate to `lore/FACTIONS_AND_POLITICS.md`
- **Action**: Close issue after migration

#### Issue #5: "Sytll"
- **Content**: Story excerpts and plan to adapt into novel format
- **Status**: Writing project planning mixed with narrative content
- **Recommendation**: Migrate to `writing_drafts/NOVEL_PLANNING.md`
- **Action**: Close issue after migration

### Category 2: Active Game Development Tasks (1 issue)

**Issue #26: "Need more scenes"**
- **Content**: Request to create more game scenes for ChoiceScript game
- **Status**: Legitimate, actionable game development task
- **Recommendation**: Keep open, add proper labels and milestone
- **Suggested Labels**: `enhancement`, `game-content`, `choicescript`
- **Suggested Milestone**: Create "Phase 2 Development" milestone (per PROJECT_ROADMAP.md)
- **Action**: 
  - Update title to be more descriptive: "Add remaining expedition scenes to ChoiceScript game"
  - Link to relevant documentation in PROJECT_ROADMAP.md
  - Create checklist of specific scenes needed

### Category 3: Placeholder/Test Issues (4 issues)

These appear to be test or temporary issues with minimal useful content:

**Issue #60: "everweave-export.pdf"**
- **Content**: Link to PDF export from everweave.ai
- **Status**: External link, unclear purpose
- **Recommendation**: Close or migrate PDF content to repository if valuable
- **Action**: Ask owner if PDF should be archived, otherwise close

**Issue #53: "Try and connect"**
- **Content**: ChatGPT conversation link
- **Status**: External link, temporary
- **Recommendation**: Close issue
- **Action**: Close with note that ChatGPT conversations should be documented in markdown files if content is valuable

**Issue #47: "work"**
- **Content**: Single emoji (`:wink:`)
- **Status**: Test/placeholder issue
- **Recommendation**: Close issue
- **Action**: Close as not actionable

**Issue #45: "Livlve"**
- **Content**: ChatGPT conversation link
- **Status**: External link, temporary
- **Recommendation**: Close issue
- **Action**: Close with same reasoning as #53

## Recommended Actions

### Immediate Actions

1. **Create lore documentation files** (migrate content from issues #3, #4, #5):
   ```
   lore/
   ├── MAGICAL_SYSTEMS.md         (from issue #4)
   ├── COMPLETE_WORLD_OVERVIEW.md (from issue #4)
   ├── FACTIONS_AND_POLITICS.md   (from issue #3)
   
   writing_drafts/
   └── NOVEL_PLANNING.md           (from issue #5)
   ```

2. **Enhance issue #26** with proper structure:
   - Update title: "Add remaining expedition scenes to ChoiceScript game"
   - Add description with checklist of scenes from PROJECT_ROADMAP.md Phase 2
   - Add labels: `enhancement`, `game-content`, `choicescript`, `good first issue`
   - Link to relevant files: `choicescript_game/scenes/`

3. **Close placeholder issues** (#45, #47, #53, #60):
   - Add closing comment explaining why
   - Suggest better practices for future (use discussions for temporary links, markdown files for content)

### Process Improvements

4. **Create issue templates** in `.github/ISSUE_TEMPLATE/`:
   - `game-scene-request.md` - Template for requesting new game scenes
   - `bug-report.md` - Template for reporting bugs
   - `lore-addition.md` - Template for proposing lore additions
   - `feature-request.md` - Template for feature requests

5. **Establish issue guidelines** in `CONTRIBUTING.md`:
   - Issues should be specific and actionable
   - Lore content belongs in markdown files, not issues
   - External links should be archived or documented in-repo
   - Use discussions for conversations, issues for tasks

6. **Create GitHub labels** for better organization:
   - `game-content` - Game scene/content additions
   - `lore` - Worldbuilding and lore
   - `choicescript` - ChoiceScript-specific issues
   - `html-game` - HTML game-specific issues
   - `documentation` - Documentation improvements
   - `good first issue` - Easy tasks for new contributors

## Migration Checklist

### For Lore Issues (#3, #4, #5)

- [ ] Create `lore/MAGICAL_SYSTEMS.md` with content from issue #4
- [ ] Create `lore/COMPLETE_WORLD_OVERVIEW.md` with content from issue #4
- [ ] Create `lore/FACTIONS_AND_POLITICS.md` with content from issue #3
- [ ] Create `writing_drafts/NOVEL_PLANNING.md` with content from issue #5
- [ ] Add index/navigation to main README linking to new lore files
- [ ] Close issues #3, #4, #5 with comment: "Content migrated to [filename]. Future lore additions should be submitted as pull requests to lore files."

### For Active Task (#26)

- [ ] Update issue #26 title to: "Add remaining expedition scenes to ChoiceScript game"
- [ ] Add detailed description with scene checklist
- [ ] Add labels: `enhancement`, `game-content`, `choicescript`
- [ ] Create "Phase 2 Development" milestone
- [ ] Assign milestone to issue #26

### For Placeholder Issues (#45, #47, #53, #60)

- [ ] Close issue #45 with note about proper documentation practices
- [ ] Close issue #47 as not actionable
- [ ] Close issue #53 with note about proper documentation practices
- [ ] Close issue #60 after confirming PDF disposition with owner

### For Future Prevention

- [ ] Create issue templates in `.github/ISSUE_TEMPLATE/`
- [ ] Update `CONTRIBUTING.md` with issue guidelines
- [ ] Create GitHub labels for better categorization
- [ ] Document issue workflow in this guide

## Issue Templates

### Game Scene Request Template

```markdown
---
name: Game Scene Request
about: Request a new scene for the ChoiceScript or HTML game
title: '[SCENE] '
labels: 'game-content, enhancement'
assignees: ''
---

## Scene Description
Brief description of the scene being requested.

## Game Version
- [ ] HTML game (`game/`)
- [ ] ChoiceScript game (`choicescript_game/`)
- [ ] Both

## Context
Where does this scene fit in the game? What comes before/after?

## Requirements
- [ ] Specific stat checks needed
- [ ] Character development moments
- [ ] Polly commentary
- [ ] Multiple choice outcomes

## Related Files
List any related scene files or lore documents.

## Additional Context
Any other information that would help implement this scene.
```

### Lore Addition Template

```markdown
---
name: Lore Addition
about: Propose a lore or worldbuilding addition
title: '[LORE] '
labels: 'lore'
assignees: ''
---

## Lore Category
- [ ] Character backstory
- [ ] Magic system
- [ ] Geography/locations
- [ ] History/timeline
- [ ] Faction/organization
- [ ] Other: ___________

## Proposed Addition
Detailed description of the lore being added.

## Consistency Check
How does this fit with existing lore? List relevant existing documents.

## Target File
Which lore file should this be added to?
- File path: `lore/___________`

## Additional Context
Any references or inspirations for this lore.
```

## Best Practices Going Forward

### DO:
- ✅ Create specific, actionable issues for tasks
- ✅ Use pull requests to add lore content
- ✅ Link related issues and files
- ✅ Add appropriate labels and milestones
- ✅ Keep external content archived in-repo
- ✅ Use discussions for brainstorming
- ✅ Update issues when status changes

### DON'T:
- ❌ Use issues as documentation storage
- ❌ Create vague or placeholder issues
- ❌ Rely on external links without backup
- ❌ Leave issues open indefinitely without updates
- ❌ Create duplicate issues without checking existing ones
- ❌ Mix multiple unrelated topics in one issue

## Conclusion

This reorganization will result in:
- **4 issues closed** (#3, #4, #5 after migration; #45, #47, #53, #60 as cleanup)
- **1 issue enhanced** (#26 with proper structure)
- **Better organization** through templates and labels
- **Clearer processes** for future contributions

The goal is to keep the issue tracker focused on actionable tasks while properly documenting lore and content in the repository structure.
