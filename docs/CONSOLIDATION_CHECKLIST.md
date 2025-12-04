# Issue Consolidation Checklist

Use this checklist to track your progress consolidating the 8 open issues.

## Phase 1: Lore Migration (30-45 min)

### Issue #4: "Magical overview"
- [ ] Extract magical system content
- [ ] Create `lore/MAGICAL_SYSTEMS.md`
- [ ] Extract world overview content  
- [ ] Create `lore/COMPLETE_WORLD_OVERVIEW.md`
- [ ] Add table of contents to both files
- [ ] Verify all content migrated
- [ ] Close issue with comment: "Content migrated to lore/MAGICAL_SYSTEMS.md and lore/COMPLETE_WORLD_OVERVIEW.md. Future lore additions should be submitted as pull requests to lore files."

### Issue #3: "Expanded faction organization"
- [ ] Extract faction content
- [ ] Create `lore/FACTIONS_AND_POLITICS.md`
- [ ] Add table of contents
- [ ] Verify all content migrated
- [ ] Close issue with comment: "Content migrated to lore/FACTIONS_AND_POLITICS.md. Future faction lore should be submitted as pull requests."

### Issue #5: "Sytll"
- [ ] Extract story planning content
- [ ] Create `writing_drafts/NOVEL_PLANNING.md`
- [ ] Organize by sections
- [ ] Verify all content migrated
- [ ] Close issue with comment: "Content migrated to writing_drafts/NOVEL_PLANNING.md. Future writing planning should be done in files, not issues."

### After Migration
- [ ] Update lore/README.md with links to new files (if needed)
- [ ] Commit new lore files
- [ ] Push to repository

## Phase 2: Active Task Enhancement (15-20 min)

### Issue #26: "Need more scenes"
- [ ] Edit issue title to: "Add remaining expedition scenes to ChoiceScript game"
- [ ] Update issue body with detailed description (see QUICK_REFERENCE)
- [ ] Add label: `enhancement`
- [ ] Add label: `game-content`
- [ ] Add label: `choicescript`
- [ ] Create milestone "Phase 2 Development" (if doesn't exist)
- [ ] Assign milestone to issue
- [ ] Verify issue is well-structured

## Phase 3: Placeholder Issue Cleanup (10-15 min)

### Issue #60: "everweave-export.pdf"
- [ ] Determine if PDF content is valuable
- [ ] If yes: Download and archive in repository
- [ ] If no: Proceed to close
- [ ] Add closing comment: "Closing - external links should be archived in repository. If this PDF content is valuable, please download it, add to repo, and create a new issue with proper description referencing the archived file."
- [ ] Close issue

### Issue #53: "Try and connect"
- [ ] Add closing comment: "Closing - ChatGPT conversation links are temporary and not suitable for issue tracking. If the conversation contains valuable content, please copy it into a markdown file in the repository and open a new issue with proper description and context."
- [ ] Close issue

### Issue #47: "work"  
- [ ] Add closing comment: "Closing - no actionable content. Future issues should have descriptive titles and include clear descriptions of tasks or problems. Please use the issue templates in .github/ISSUE_TEMPLATE/ for guidance."
- [ ] Close issue

### Issue #45: "Livlve"
- [ ] Add closing comment: "Closing - ChatGPT conversation links are temporary and not suitable for issue tracking. If the conversation contains valuable content, please copy it into a markdown file in the repository and open a new issue with proper description and context."
- [ ] Close issue

## Phase 4: GitHub Configuration (Optional, 10 min)

### Create Labels (if they don't exist)
- [ ] `game-content` - Game scene/content additions (color: #1d76db)
- [ ] `lore` - Worldbuilding and lore (color: #d4c5f9)
- [ ] `choicescript` - ChoiceScript-specific (color: #0e8a16)
- [ ] `html-game` - HTML game-specific (color: #fbca04)
- [ ] `documentation` - Documentation improvements (color: #0075ca)
- [ ] `enhancement` - New features (color: #a2eeef)
- [ ] `bug` - Something broken (color: #d73a4a)
- [ ] `good first issue` - Easy for newcomers (color: #7057ff)

### Create Milestone
- [ ] Create "Phase 2 Development" milestone
- [ ] Set description: "Converting remaining HTML expeditions to ChoiceScript"
- [ ] Link to PROJECT_ROADMAP.md in description

## Final Verification

### Issue Tracker
- [ ] Only issue #26 remains open
- [ ] Issue #26 has clear description
- [ ] Issue #26 has labels and milestone
- [ ] All other issues closed with helpful comments

### Documentation
- [ ] New lore files created and committed
- [ ] CONTRIBUTING.md updated with issue guidelines
- [ ] Issue templates available in .github/ISSUE_TEMPLATE/
- [ ] Documentation guides in docs/ directory

### Communication
- [ ] Consider posting update in Discussions about new issue process
- [ ] Consider pinning issue #26 as current priority
- [ ] Update project README if needed to reference new structure

## Success Metrics

After completion, you should have:
- ✅ 7 issues closed (4 lore migrated, 3 placeholders cleaned)
- ✅ 1 issue enhanced (properly structured active task)
- ✅ 3-4 new lore files in repository
- ✅ Clear issue templates for future use
- ✅ Updated contribution guidelines
- ✅ Clean, organized issue tracker

## Time Tracking

| Phase | Estimated | Actual | Notes |
|-------|-----------|--------|-------|
| Lore Migration | 30-45 min | ___ min | Use custom agent to help |
| Task Enhancement | 15-20 min | ___ min | Issue #26 update |
| Cleanup | 10-15 min | ___ min | Close placeholders |
| Configuration | 10 min | ___ min | Optional labels/milestone |
| **Total** | **65-90 min** | **___ min** | |

## Notes & Issues Encountered

Use this space to track any problems or decisions made during consolidation:

---

## Completed!

- [ ] All checklist items complete
- [ ] Issue tracker is clean and organized
- [ ] Documentation is updated
- [ ] Ready for normal operations

**Date completed:** _______________

**Next steps:** Monitor issue tracker, enforce new guidelines, use templates for new issues.
