# Issue Management Flowchart

## When Creating a New Issue

```
START: I want to contribute to Avalon
│
├─ Is it LORE/WORLDBUILDING content?
│  │
│  YES → Create a markdown file in lore/
│       └─ Submit as Pull Request
│           └─ Use lore-addition template for discussion if needed
│
├─ Is it a GAME SCENE request?
│  │
│  YES → Use "Game Scene Request" template
│       ├─ Specify: HTML game or ChoiceScript?
│       ├─ Provide context and requirements
│       └─ Add labels: game-content, enhancement
│
├─ Is it a BUG or PROBLEM?
│  │
│  YES → Use "Bug Report" template
│       ├─ Describe the issue clearly
│       ├─ Provide steps to reproduce
│       └─ Add label: bug
│
├─ Is it a FEATURE IDEA?
│  │
│  YES → Use "Feature Request" template
│       ├─ Explain the problem it solves
│       ├─ Describe proposed solution
│       └─ Add label: enhancement
│
└─ Is it a QUESTION or DISCUSSION?
   │
   YES → Use GitHub Discussions instead
       └─ Issues are for actionable tasks only
```

## When Reviewing Existing Issues

```
START: Looking at an existing issue
│
├─ Does it have a clear, actionable task?
│  │
│  NO → Ask for clarification or close with guidance
│  │
│  YES → Continue ↓
│
├─ Is it lore content in an issue?
│  │
│  YES → Migrate to markdown file
│       └─ Close issue with reference to new file
│  │
│  NO → Continue ↓
│
├─ Is it just an external link?
│  │
│  YES → Archive content in-repo or close
│       └─ Add closing comment with guidance
│  │
│  NO → Continue ↓
│
├─ Is it a legitimate task?
│  │
│  YES → Ensure it has:
│       ├─ Descriptive title
│       ├─ Clear requirements
│       ├─ Appropriate labels
│       ├─ Assigned milestone (if applicable)
│       └─ Links to relevant files
│
└─ DONE: Well-organized issue!
```

## Label Decision Tree

```
What type of issue is this?

├─ Game Content?
│  └─ Add: game-content
│      ├─ HTML specific? → html-game
│      └─ ChoiceScript specific? → choicescript
│
├─ Lore/Worldbuilding?
│  └─ Add: lore
│      └─ Usually becomes a PR instead
│
├─ Bug or Problem?
│  └─ Add: bug
│      ├─ Critical? → priority-high
│      └─ Easy fix? → good first issue
│
├─ New Feature?
│  └─ Add: enhancement
│      ├─ Documentation? → documentation
│      ├─ Automation? → automation
│      └─ Easy to implement? → good first issue
│
└─ Process/Meta?
   └─ Add: meta
       └─ Repository organization, workflows, etc.
```

## Milestone Assignment

```
What phase is this issue part of?

├─ Current Phase 2 tasks?
│  └─ Milestone: "Phase 2 Development"
│      └─ Converting HTML scenes to ChoiceScript
│
├─ Future planned work?
│  └─ Milestone: "Phase 3 Planning"
│      └─ New content beyond current roadmap
│
├─ Quick wins / easy tasks?
│  └─ Milestone: "Quick Wins"
│      └─ Small improvements, fixes
│
└─ No specific timeline?
   └─ No milestone (backlog)
```

## Priority Assessment

```
How urgent is this issue?

HIGH Priority (address immediately):
├─ Game-breaking bugs
├─ Security issues
├─ Blockers for other work
└─ Time-sensitive tasks

MEDIUM Priority (address soon):
├─ Important features
├─ Non-critical bugs
├─ Current milestone tasks
└─ Community requests

LOW Priority (backlog):
├─ Nice-to-have features
├─ Minor improvements
├─ Long-term ideas
└─ Exploration tasks
```

## Quick Reference Table

| Issue Type | Template | Labels | Milestone | Priority |
|------------|----------|--------|-----------|----------|
| New game scene | game-scene-request.md | game-content, enhancement, choicescript/html-game | Phase 2/3 | Medium |
| Lore proposal | lore-addition.md → PR | lore | N/A | Low |
| Bug report | bug-report.md | bug | Current | High/Medium |
| Feature idea | feature-request.md | enhancement | Future | Medium/Low |
| Documentation | feature-request.md | documentation | Quick Wins | Low |
| External link | N/A - Close | N/A | N/A | Close |
| Placeholder | N/A - Close | N/A | N/A | Close |

## Common Scenarios

### Scenario 1: Someone opens an issue with just a link
**Action:**
1. Check if link content is valuable
2. If yes: Ask them to archive content in markdown
3. If no: Close with guidance on proper issue creation
4. Reference: Issue templates and CONTRIBUTING.md

### Scenario 2: Large lore dump in an issue
**Action:**
1. Thank them for the content
2. Ask to submit as PR to lore/ directory
3. Use custom agent to help organize if needed
4. Close issue once migrated with reference to PR

### Scenario 3: Vague feature request
**Action:**
1. Ask for clarification using template questions
2. Request problem statement and use cases
3. Update issue description once clarified
4. Add appropriate labels and milestone

### Scenario 4: Duplicate issue
**Action:**
1. Link to original issue
2. Ask reporter to add comments to original
3. Close duplicate with reference
4. Consider if original needs updating

### Scenario 5: Issue resolved but not closed
**Action:**
1. Verify resolution
2. Add closing comment summarizing fix
3. Close issue
4. Reference PR or commit if applicable

## Best Practices Summary

✅ **DO:**
- Use templates
- Be specific in titles
- Link related issues/files
- Update issues as status changes
- Close when resolved
- Add helpful labels
- Assign to milestones

❌ **DON'T:**
- Create placeholder issues
- Use issues for documentation
- Rely only on external links
- Leave issues abandoned
- Mix multiple topics
- Skip the template
- Forget to label

## Tools to Help

1. **Custom Agent (`@my-agent`):**
   - Validate lore consistency
   - Help organize content
   - Check for conflicts

2. **Issue Templates:**
   - Guide proper issue creation
   - Ensure all info included
   - Maintain consistency

3. **GitHub Labels:**
   - Filter and sort
   - Track categories
   - Identify priorities

4. **Milestones:**
   - Group related work
   - Track progress
   - Plan releases

5. **Projects (optional):**
   - Kanban boards
   - Workflow visualization
   - Team coordination

## Maintaining a Healthy Issue Tracker

### Weekly Review
- [ ] Triage new issues
- [ ] Update stale issues
- [ ] Close resolved issues
- [ ] Update priorities

### Monthly Cleanup
- [ ] Review open issues
- [ ] Close outdated/invalid
- [ ] Update documentation
- [ ] Adjust milestones

### As Needed
- [ ] Create new labels
- [ ] Update templates
- [ ] Revise guidelines
- [ ] Improve processes

---

**Remember:** A well-organized issue tracker makes collaboration easier for everyone!
