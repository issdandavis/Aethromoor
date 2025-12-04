# ChoiceScript Game Development - AI Agent Instructions

## 🎮 Purpose
This directory contains the **professional ChoiceScript version** of "Polly's Wingscroll: The First Thread" for mobile app publication via Hosted Games platform.

## 📁 Directory Structure

```
choicescript_game/
├── startup.txt              → Game initialization, stats, character creation
├── scenes/
│   ├── character_creation.txt
│   ├── polly_intro.txt
│   ├── arrival_*.txt        → Three arrival paths (teleport/walk/fly)
│   ├── first_lesson.txt     → Complete tutorial expedition
│   ├── expedition_choice.txt
│   ├── singing_dunes.txt    → Desert expedition (IN PROGRESS)
│   ├── verdant_tithe.txt    → Forest expedition (PLANNED)
│   ├── rune_glacier.txt     → Ice expedition (PLANNED)
│   └── ending_*.txt         → 14 unique endings
└── README.md
```

## 🎯 Current Development Status

**Phase**: Scene conversion from HTML to ChoiceScript
**Priority**: Complete the three expeditions
- ✅ First Lesson (tutorial) - COMPLETE
- ⏳ Singing Dunes - IN PROGRESS
- ⏳ Verdant Tithe - PLANNED
- ⏳ Rune Glacier - PLANNED

## 🔧 ChoiceScript Technical Standards

### File Naming Conventions
- All scene files: lowercase with underscores (`first_lesson.txt`)
- Ending files: `ending_<descriptor>.txt` (e.g., `ending_collaborative_master.txt`)
- Branch variants: `<scene>_<variant>.txt` (e.g., `arrival_teleport.txt`)

### Required ChoiceScript Commands

**Every scene file must include:**
```choicescript
*comment Scene: [descriptive name]
*comment Source: [HTML scene reference if applicable]
*comment Stat impacts: [list stat changes]

[scene content]

*finish [next_scene_name]
```

**For choices affecting stats:**
```choicescript
*choice
    #[Choice text with clear consequence indication]
        *set collaboration %+5
        *set aria_relationship %+1
        [consequence text]
        *goto next_section
```

### Stat Variable Conventions

**Core Stats (in startup.txt):**
- `collaboration` - Main gameplay stat (0-100)
- `aria_relationship` - Aria Ravencrest relationship (-10 to +10)
- `zara_relationship` - Zara Frostborn relationship (-10 to +10)
- `polly_relationship` - Polly relationship (-10 to +10)

**Expedition Flags:**
- `completed_first_lesson` - Boolean
- `completed_singing_dunes` - Boolean
- `completed_verdant_tithe` - Boolean
- `completed_rune_glacier` - Boolean
- `chosen_expedition` - String ("dunes" / "forest" / "glacier")

**Path Tracking:**
- `dunes_path` - String ("truth" / "control" / "rejection")
- `forest_path` - String ("dreamwillow" / "thoughtvine" / "heartwood")
- `glacier_path` - String ("control" / "harmony" / "mystery")

### Scene Flow Pattern

All expeditions should follow this structure:
1. **Introduction** - Setting description, NPC introduction
2. **Challenge Setup** - Present magical problem
3. **Choice Point 1** - Collaboration vs. Control approach (major stat impact)
4. **Consequence** - Immediate feedback on choice
5. **Challenge Deepens** - Problem escalates or reveals complexity
6. **Choice Point 2** - Path-defining decision (sets expedition_path variable)
7. **Resolution** - Outcome based on accumulated choices
8. **Return** - Debrief with Izack, final stat adjustments
9. **Finish** - Route to next expedition or ending

## 🎨 Conversion Guidelines

### When Converting from HTML to ChoiceScript

**DO:**
- ✅ Maintain exact story beats and choice structures
- ✅ Preserve all dialogue and descriptions
- ✅ Keep the same number of choices per decision point
- ✅ Match stat impacts between versions
- ✅ Maintain Polly's personality and commentary style
- ✅ Use ChoiceScript's `*page_break` for pacing
- ✅ Add `*comment` headers documenting source material

**DON'T:**
- ❌ Add new story branches not in HTML version
- ❌ Change character personalities or dialogue tone
- ❌ Modify the number of endings
- ❌ Alter stat progression difficulty
- ❌ Remove Polly's fourth-wall-breaking moments
- ❌ Change magic system logic
- ❌ Skip validation testing

### HTML → ChoiceScript Translation Patterns

**HTML Choice Structure:**
```html
<div class="choice">
    <button onclick="choice('collaborate')">Work together with the land</button>
    <button onclick="choice('control')">Take command of the magic</button>
</div>
```

**ChoiceScript Equivalent:**
```choicescript
*choice
    #Work together with the land
        *set collaboration %+5
        *comment Collaborative approach chosen
        *goto collaborate_path
    
    #Take command of the magic
        *set collaboration %-3
        *comment Control approach chosen
        *goto control_path
```

**HTML Stat Check:**
```javascript
if (gameState.collaboration >= 60) {
    // Success path
}
```

**ChoiceScript Equivalent:**
```choicescript
*if (collaboration >= 60)
    *comment Player has high collaboration
    *goto success_path
*else
    *goto struggle_path
```

## 🎭 Character Voice Guidelines

### Polly's Commentary
Polly should comment on player choices with:
- Sarcastic wit ("Oh, how delightfully predictable.")
- Gentle guidance ("You might want to consider...")
- Fourth-wall awareness ("I see you're the 'try everything' type of player.")
- Occasional wisdom ("Collaboration isn't weakness, little mage.")

**Pattern:**
```choicescript
*comment Polly's commentary
"${polly_commentary}"
*line_break

*if (collaboration > 50)
    *set polly_commentary "Nicely done. You're getting the hang of this."
*else
    *set polly_commentary "Well, that could have gone better. But we learn from mistakes, don't we?"
```

### Izack's Teaching Style
Izack should be:
- Encouraging without being condescending
- Patient with mistakes
- Emphasizing collaboration over power
- Humble about his own journey

### Aria Ravencrest
- Precise and formal in speech
- Values accuracy and control
- Boundary magic expertise
- Patient but exacting teacher

### Zara Frostborn
- Experimental and enthusiastic
- Encouraging of creativity
- Ice magic specialist
- Warm personality (ironic for ice mage)

## 📊 Stat Balancing Requirements

### Collaboration Stat Thresholds
Each expedition should use consistent thresholds:

- **Low Collaboration** (0-30): Struggle path, learns humility
- **Medium Collaboration** (31-60): Mixed results, steady learning
- **High Collaboration** (61-85): Success path, positive outcomes
- **Master Collaboration** (86-100): Exceptional results, unique options

### Relationship Stat Impacts
- **Major positive choice**: +2 to relevant NPC relationship
- **Minor positive choice**: +1 to relevant NPC relationship
- **Neutral/mixed choice**: +0 to relationships
- **Minor negative choice**: -1 to relevant NPC relationship
- **Major negative choice**: -2 to relevant NPC relationship

### Stat Progression Balance
Each expedition should offer:
- 3-5 major collaboration choices (±5 to ±10)
- 5-8 minor collaboration choices (±2 to ±4)
- 2-4 relationship choices per NPC featured
- At least one "redemption" opportunity for low-collaboration players

## 🎯 Scene-Specific Requirements

### Singing Dunes Expedition
**Core Mechanics:**
- Truth-testing desert magic (oath-binding)
- Kael as desert guide NPC
- Truth-sworn sand artifacts
- Three paths: Truth / Control / Rejection

**Required Stat Variables:**
```choicescript
*create kael_relationship 0
*create truth_sworn false
*create desert_artifact_obtained false
```

**Ending Connections:**
- Truth path → `ending_truthbound_mage.txt`
- Balanced approach → `ending_balanced_mage.txt`
- Rejection path → `ending_humbled_student.txt`

### Verdant Tithe Expedition
**Core Mechanics:**
- Sentient forest consciousness
- Plant-based magic (Thoughtvine, Dreamwillow, Heartwood)
- Emotional resonance with nature
- Three paths: Dreamwillow / Thoughtvine / Heartwood

**Required Stat Variables:**
```choicescript
*create forest_connection 0
*create plant_affinity "none"
*create heartwood_blessing false
```

**Ending Connections:**
- Dreamwillow path → `ending_dreamweaver.txt`
- Thoughtvine path → `ending_forestbound_guardian.txt`
- Heartwood path → `ending_heartwood_guardian.txt`

### Rune Glacier Expedition
**Core Mechanics:**
- Living ice and crystallized memories
- Frozen spell library
- Balance between control and harmony
- Three paths: Control / Harmony / Mystery

**Required Stat Variables:**
```choicescript
*create ice_mastery 0
*create glacier_partnership false
*create rune_knowledge 0
```

**Ending Connections:**
- Control path → `ending_runeweaver.txt`
- Harmony path → `ending_collaborative_master.txt`
- Mystery path → `ending_glacier_partner.txt`

## ✅ Pre-Commit Checklist

Before committing ChoiceScript scene changes:

- [ ] Scene maintains parity with HTML version (same story beats)
- [ ] All stat variables are defined in `startup.txt`
- [ ] Stat changes match HTML version's impacts
- [ ] Scene has proper `*finish` command routing to next scene
- [ ] Polly's commentary maintains her established voice
- [ ] Character dialogue matches established personalities
- [ ] Choice consequences are clear and meaningful
- [ ] Scene tested in ChoiceScript IDE (if available) or validated syntax
- [ ] `*comment` headers document source and stat impacts
- [ ] File uses correct naming convention
- [ ] SCENE_PARITY_CHECKLIST.md updated

## 🔍 Testing Your Changes

### Validation Steps:
1. **Syntax Check**: Ensure no ChoiceScript syntax errors
2. **Flow Check**: Verify all `*goto` and `*finish` commands route correctly
3. **Stat Check**: Confirm stat changes match HTML version
4. **Dialogue Check**: Read aloud - does it sound like the character?
5. **Parity Check**: Compare to HTML - same choices, same outcomes?
6. **Balance Check**: Are Collaboration opportunities consistent with other expeditions?

### Manual Playtest Focus:
- Try each major choice branch
- Verify stat thresholds trigger correct paths
- Check that all endings remain reachable
- Confirm Polly's commentary appears at appropriate moments
- Ensure pacing feels natural with `*page_break` usage

## 🚨 Common ChoiceScript Pitfalls

**Avoid These Mistakes:**
- ❌ Using `*set stat +5` instead of `*set stat %+5` (use `%+` for relative changes)
- ❌ Forgetting `*create` declarations in `startup.txt`
- ❌ Inconsistent variable naming (use underscores, not camelCase)
- ❌ Missing `*finish` at scene end (causes game to crash)
- ❌ Using `*if` without matching `*else` or branching logic
- ❌ Overusing `*page_break` (only for major pacing moments)
- ❌ Not testing stat threshold boundaries (test at exact threshold values)

## 📚 ChoiceScript Resources

**Official Documentation:**
- ChoiceScript Wiki: https://choicescriptdev.fandom.com/
- Hosted Games Forum: https://forum.choiceofgames.com/
- ChoiceScript IDE: https://www.choiceofgames.com/make-your-own-games/choicescript-intro/

**Project-Specific References:**
- HTML source: `../game/index.html` and `../game/scenes/`
- Lore canon: `../lore/`
- Character details: `../lore/IZACK_MASTER_CHRONICLE_UPDATED.txt`
- Project roadmap: `../docs/PROJECT_ROADMAP.md`

## 🎊 Success Metrics

Your ChoiceScript conversion is successful if:
- ✅ Story is identical to HTML version (same beats, same choices)
- ✅ All 14 endings are accessible through proper choice paths
- ✅ Stat tracking accurately reflects player choices
- ✅ Character voices are consistent with established lore
- ✅ Collaboration stat progression matches HTML difficulty
- ✅ Scene transitions flow naturally
- ✅ Code is clean, commented, and follows conventions

---

*Remember: ChoiceScript is player-facing code. Keep it readable, test it thoroughly, and make every choice meaningful.*
