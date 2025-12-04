---
name: Scene Conversion
description: Template for AI-assisted scene conversion from HTML to ChoiceScript
labels: ["game-development", "ai-task", "conversion"]
---

## Scene to Convert

**Scene Name:** <!-- e.g., singing_dunes, verdant_tithe -->

**Source Location:** `game/game.js` (search for: <!-- scene identifier -->)

**Target Location:** `choicescript_game/scenes/<!-- scene_name -->.txt`

## Conversion Requirements

### Content Elements
- [ ] Environmental descriptions (vivid, sensory)
- [ ] Character interactions
- [ ] Polly's sarcastic commentary
- [ ] Choice-based branching
- [ ] Stat modifications (Collaboration, relationships)
- [ ] Proper scene transitions

### Technical Requirements
- [ ] All `*goto` statements have matching `*label` targets
- [ ] Stat syntax is correct (`*set stat_name +/-value`)
- [ ] Scene connects to appropriate endings
- [ ] No dead ends in narrative flow

## AI Assistance Plan

**Suggested AI Role:** <!-- Conversion Engineer, Lore Curator, etc. -->

**Reference Files:**
- Source: `game/game.js`
- Format guide: `.github/COPILOT_INSTRUCTIONS.md`
- Example: `choicescript_game/scenes/first_lesson.txt`
- Lore check: `lore/IZACK_MASTER_CHRONICLE_UPDATED.txt`

**Automated Validation:**
- [ ] Content validation workflow will run on PR
- [ ] ChoiceScript syntax check will verify gotos and stats
- [ ] Scene parity check will compare with HTML version

## Quality Checklist

### Narrative Quality
- [ ] 500+ lines for expedition scenes
- [ ] Multiple branching paths (3+ major choices)
- [ ] Polly commentary appears at least 3-5 times
- [ ] Environmental details are vivid and specific
- [ ] Character voices are consistent

### Technical Quality
- [ ] All gotos resolve to valid labels or scenes
- [ ] Stats are modified appropriately
- [ ] Conditionals use correct syntax
- [ ] Scene connects to ending paths

## Expected Outcome

**Word Count Target:** <!-- 500+ for expeditions, 300+ for endings -->

**Branching Paths:** <!-- Number of major choice points -->

**Connected Endings:** <!-- Which endings this scene leads to -->

---

## AI Loop Coordination

<!-- If using multiple AI assistants, specify roles: -->

1. **Lore Curator**: Validate narrative consistency
2. **Conversion Engineer**: Translate HTML to ChoiceScript
3. **Structural Reviewer**: Verify branching and stats
4. **Quality Balancer**: Adjust stat thresholds

---

*Use `/create-checklist` command in comments to generate a detailed task checklist*
