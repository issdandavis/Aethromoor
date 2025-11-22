# INSTRUCTIONS FOR GITHUB COPILOT AND AI ASSISTANTS

**Project:** Polly's Wingscroll: The First Thread
**Goal:** Expand ChoiceScript game from placeholders to 100+ fully-written scenes
**Priority:** HIGH - This is the main development focus

---

## WHAT THIS PROJECT IS

A choice-based interactive fiction game built in **ChoiceScript** (the engine used by Choice of Games/Hosted Games). The game follows a new student at Avalon Academy, guided by Polly - a sarcastic immortal raven.

**Current State:** Foundation complete, but expedition scenes are PLACEHOLDERS
**Target State:** Professional-quality game with 100+ scenes, each with meaningful depth

---

## YOUR TASK (FOR ANY AI WORKING ON THIS)

### Primary Goal
Expand the ChoiceScript files in `choicescript_game/scenes/` to match the quality of published Choice of Games titles.

### Files That Need Expansion

| File | Current State | Target |
|------|---------------|--------|
| `singing_dunes.txt` | ~12 lines placeholder | 500+ lines, 15-20 scenes |
| `verdant_tithe.txt` | ~12 lines placeholder | 500+ lines, 15-20 scenes |
| `rune_glacier.txt` | ~12 lines placeholder | 500+ lines, 15-20 scenes |
| `endings.txt` | ~12 lines placeholder | 300+ lines, 14 endings |

### Reference Material
- `game/game.js` - Contains ALL the story content to convert (use this as source)
- `choicescript_game/scenes/first_lesson.txt` - Example of proper ChoiceScript formatting

---

## CHOICESCRIPT SYNTAX GUIDE

### Basic Structure
```choicescript
*comment Scene header
*label scene_name

Narrative text here. Use [i]italics[/i] for emphasis.
Use [b]bold[/b] for important terms.

*line_break

More text after a visual break.

*choice
    #First choice option
        Result of choosing this.
        *set collaboration +5
        *goto next_scene
    #Second choice option
        Different result.
        *set some_stat -3
        *goto other_scene

*label next_scene
Continue the story here...
```

### Stat Modifications
```choicescript
*set collaboration +10
*set izack_relationship +5
*set aria_relationship -3
```

### Conditionals
```choicescript
*if collaboration > 60
    High collaboration text.
*elseif collaboration > 30
    Medium collaboration text.
*else
    Low collaboration text.
```

### Polly's Commentary
Always use italics for Polly's sarcastic narrator voice:
```choicescript
[i]"And here we go again. Another student about to learn the hard way."[/i]
```

### Scene Transitions
```choicescript
*goto_scene singing_dunes
*goto label_name
*finish
```

---

## SCENE EXPANSION TEMPLATE

Each major location should have this structure:

```
1. ARRIVAL (1-2 scenes)
   - Initial description of the location
   - First impressions
   - Polly's commentary
   - Introduction to local guide/character

2. EXPLORATION (3-5 scenes)
   - Multiple paths to explore
   - Environmental storytelling
   - Learning about the location's magic
   - Character interactions
   - Stat-based variations

3. CHALLENGE (3-5 scenes)
   - Central test or conflict
   - Multiple approaches (collaboration vs solo)
   - Consequences of choices
   - Character development moments

4. RESOLUTION (2-3 scenes)
   - Outcomes based on earlier choices
   - Lessons learned
   - Rewards/artifacts earned
   - Lead-in to endings

5. BRANCHES (varies)
   - Alternative paths
   - Hidden discoveries
   - Relationship-specific scenes
```

---

## SINGING DUNES EXPANSION GUIDE

### Setting
- Truth-testing desert where sand judges honesty
- Oath-bound sand spirits
- Ironwood oases
- Guide: Kael (desert sage)

### Required Scenes
1. `dunes_arrival` - Portal arrival, first impression of golden sand
2. `dunes_preparation` - Meeting Kael, learning desert rules and preparing for the journey
3. `dunes_first_truth` - Initial truth test with multiple response options
4. `dunes_honest_path` - Reward for vulnerability and openness
5. `dunes_safe_path` - Result of playing it safe with truthful but guarded answers
6. `dunes_rejected_path` - Consequence of evasion or dishonesty
7. `dunes_deep_truth_path` - Path for those who share profound personal truths
8. `dunes_oasis_journey` - Traveling to the Ironwood oasis
9. `dunes_spirit_story` - Kael shares the history of oath-bound spirits
10. `dunes_spirit_contact` - First encounter with the sand spirits
11. `dunes_spirit_recognition` - Spirits acknowledge your worthiness
12. `dunes_night_song` - Twilight vision and song sequence with the desert
13. `dunes_humbled_journey` - Path for those learning humility
14. `dunes_blessed_journey` - Path for those already aligned with desert wisdom
15. `dunes_morning` - Dawn breaking over the desert
16. `dunes_oath_teaching` - Learning to bind promises with oath-magic
17. `dunes_keeper_oath` - Making your oath to the desert
18. `dunes_final` - Final choices and departure with desert's blessing

### Key Mechanics
- Truth level tracking (honest choices accumulate)
- Sand's response changes based on truthfulness
- Relationship with Kael affects what you learn
- Multiple ending paths based on honesty

---

## VERDANT TITHE EXPANSION GUIDE

### Setting
- Sentient forest that reads thoughts
- Thoughtvines share consciousness
- Dreamwillows show possible futures
- Heartwood Tree is the forest's heart
- Guide: Izack leads this expedition

### Required Scenes
1. `forest_arrival` - Stepping into the living forest, sensing its awareness
2. `forest_first_steps` - Initial reactions from the Thoughtvines
3. `forest_path_split` - Three paths diverge into the forest depths
4. `forest_guided_path` - Following the forest's subtle guidance
5. `dreamwillow_grove` - Discovering the silver Dreamwillow tree
6. `dreamwillow_visions` - Experiencing visions of possible futures
7. `dreamwillow_conclusion` - Processing and responding to the visions
8. `thoughtvine_deep` - Choosing to merge deeply with the forest mind
9. `dreamwillow_path` - Following the Dreamwillow's vision path
10. `thoughtvine_path` - Choosing the Thoughtvine connection path
11. `thoughtvine_merge` - Fully merging consciousness with the vines
12. `thoughtvine_careful` - Cautious approach to the vine connection
13. `thoughtvine_retreat` - Pulling back from deep merge
14. `thoughtvine_question` - The forest asks for a promise or commitment
15. `heartwood_approach` - Nearing the ancient Heartwood Tree
16. `heartwood_communion` - Ritual of communion with the Heartwood
17. `forest_bond_accepted` - The forest accepts your bond
18. `heartwood_path` - Choosing the Heartwood Guardian path
19. `heartwood_acceptance` - Accepting the role of Heartwood Guardian
20. `heartwood_decline` - Declining the Heartwood's offer
21. `heartwood_question` - The Heartwood poses a pivotal question
22. `forest_return` - Returning from the forest expedition
23. `heartwood_transformation` - Undergoing transformation by the Heartwood
24. `heartwood_declined` - The Heartwood's offer is declined and consequences unfold
25. `forest_conclusion` - Final reflections and consequences of the forest journey

### Key Mechanics
- Thoughts are visible to the forest
- Quieting your mind affects outcomes
- Memory sharing with ancient consciousness
- Different paths lead to different endings

---

## RUNE GLACIER EXPANSION GUIDE

### Setting
- Living ice inscribed with adaptive runes
- Frozen spell library
- Ice responds to magical intention
- Guide: Aria teaches boundary magic here

### Required Scenes
1. `glacier_arrival` - Stepping onto the living ice, feeling its awareness
2. `glacier_introduction` - First contact with the glacier's rune-consciousness
3. `glacier_path_choice` - Choosing approach: Control, Harmony, or Mystery
4. `glacier_greeting` - The glacier's response to your chosen approach
5. `glacier_conversation_path` - Path of dialogue and understanding with the ice
6. `glacier_communion` - Deep communion with the glacier's ancient mind
7. `glacier_control_path` - Attempting to master and control the ice
8. `control_test_one` - First test of dominance over the runes
9. `control_test_two` - Second test pushing boundaries of control
10. `control_conclusion` - Outcome of the control-focused approach
11. `glacier_harmony_path` - Partnering with the ice as equals
12. `harmony_test_one` - First collaborative working with the glacier
13. `harmony_test_two` - Deeper partnership and trust building
14. `harmony_conclusion` - Outcome of the harmony-focused approach
15. `harmony_consequence` - Long-term consequences of partnership choice
16. `harmony_transformation` - Transformation resulting from deep harmony with the glacier
17. `glacier_mystery_path` - Exploring the glacier's ancient mysteries
18. `mystery_creation` - Discovering how the runes were created
19. `mystery_conversation` - Dialogue about the glacier's origins
20. `mystery_test` - Facing a test of faith or understanding in the mystery path
21. `mystery_revelation` - Revelation of the glacier's deepest secret
22. `mystery_faith` - Leap of faith in trusting the glacier's wisdom
23. `glacier_final` - Final choices and departure from the glacier
24. `path_mystery` - Additional mystery path exploration
25. `glacier_conclusion` - Final reflections and consequences of the glacier journey

### Key Mechanics
- Control vs Harmony stat tracking
- Ice responds differently to each approach
- Aria's approval affects what you learn
- Hidden paths for high-collaboration players

---

## ENDINGS EXPANSION GUIDE

### All 14 Endings Required

Each ending needs:
- 30-50 lines of text
- Personalized based on journey
- Polly's final commentary
- Achievement unlock
- `*ending` command

### Ending List
1. `ending_collaborative_master` - Highest collaboration
2. `ending_truthbound_mage` - Desert blessing
3. `ending_forestbound_guardian` - Forest connection
4. `ending_heartwood_guardian` - Deepest forest bond (rare)
5. `ending_runeweaver` - Glacier control master
6. `ending_glacier_partner` - Ice partnership
7. `ending_balanced_mage` - Middle path
8. `ending_boundary_specialist` - Aria's protege
9. `ending_collaborative_scholar` - Teaching focus
10. `ending_humble_seeker` - Wisdom through humility
11. `ending_second_chance` - Recovery from failure
12. `ending_humbled_student` - Learned through rejection
13. `ending_expelled` - Failed completely (dramatic)
14. `ending_standard_path` - Neutral completion

---

## QUALITY STANDARDS

### Every Scene Must Have:
- [ ] Vivid environmental description (2-3 sentences minimum)
- [ ] Polly commentary (at least once per scene)
- [ ] Meaningful choice with consequences
- [ ] Stat modifications that matter
- [ ] Connection to overall narrative

### Polly's Voice Guidelines
- Sarcastic but caring
- 3000+ years old, seen everything
- Fourth-wall aware
- Actually wants students to succeed
- Never cruel, but brutally honest

Example:
```
[i]"Oh good, you're about to do the thing. You know, the thing where you think you're smarter than the ancient magical desert. This always ends well."[/i]
```

### Prose Quality
- Literary but accessible
- Show don't tell
- Sensory details (sight, sound, smell, feel)
- Emotional resonance
- Consistent tone throughout

---

## CONVERSION PROCESS

When converting from `game/game.js` to ChoiceScript:

1. **Find the scene** in game.js (search for the node name)
2. **Extract the narrative** from the `text` property
3. **Remove HTML tags** and convert to ChoiceScript formatting
4. **Expand the content** - add 2-3x more detail
5. **Add Polly commentary** if missing
6. **Convert choices** to `*choice` blocks
7. **Add stat effects** with `*set` commands
8. **Add conditionals** for stat-based variations
9. **Test the flow** with `*goto` statements

---

## EXAMPLE CONVERSION

### Original (game.js):
```javascript
singing_dunes_journey: {
    text: `
        <p>The portal opens onto endless golden sand...</p>
        <p><span class="polly-comment">"Welcome to the truth desert..."</span></p>
    `,
    choices: [
        { text: "Speak a vulnerable truth", next: 'dunes_honest_truth' },
        { text: "Share something safe", next: 'dunes_safe_truth' }
    ]
}
```

### Expanded (ChoiceScript):
```choicescript
*label dunes_arrival

The portal deposits you onto golden sand that gleams with crystalline fragments. Each grain catches the light differently, creating a landscape that seems to shimmer with hidden meaning.

The heat is immediate but not oppressive—the desert's warmth feels almost welcoming, like it's been waiting for you.

*line_break

In the distance, dunes rise like frozen waves, their crests singing in the wind. The sound is haunting—a harmony that seems to carry words just beyond understanding.

[i]"Welcome to the Sunscarred Dunes, where the sand itself passes judgment. Every lie you've ever told? The desert remembers. Every truth you've avoided? It knows. Sleep well tonight."[/i]

*line_break

Your expedition guide, a weathered man named Kael, steps forward. His robes are the color of sunset sand, and his eyes hold the patience of someone who has watched the desert for decades.

"The Singing Dunes test all who enter," he says, his voice carrying the dry rasp of wind over stone. "They seek truth—not facts, but the truth of who you are. Are you prepared to be known?"

*page_break

He produces small vials of sand, one for each student.

"These will be your witnesses. The sand will react to your words. Gold for truth, red for deception. The desert is patient, but it does not forget."

[i]"Pro tip: the desert has been doing this for about ten thousand years. It's very, very good at spotting lies. Even the ones you tell yourself."[/i]

*choice
    #"I'm ready. I have nothing to hide."
        Kael's eyes crinkle with something between amusement and respect.

        "Bold. The desert appreciates directness, even if it later proves... optimistic."

        *set collaboration +5
        *goto dunes_first_test

    #"What happens if the sand turns red?"
        "The desert's displeasure," Kael says simply. "Minor deceptions bring minor consequences—a burned hand, a night of troubled dreams. Major lies..."

        He doesn't finish, but Polly does.

        [i]"Let's just say the desert has been known to swallow people whole. Not often! But, you know. It happens."[/i]

        *goto dunes_first_test

    #"Can we just... observe? See how others do it first?"
        *set collaboration -3

        Kael shakes his head slowly.

        "The desert does not permit spectators. You enter, you are tested. There is no middle ground in the Singing Dunes."

        [i]"Translation: no hiding at the back of the class here. The desert is about to get very personal with you whether you like it or not."[/i]

        *goto dunes_first_test
```

---

## VERIFICATION CHECKLIST

Before submitting any scene expansion:

- [ ] All `*goto` targets exist
- [ ] All `*label` names are unique
- [ ] Stats are properly modified
- [ ] Polly has at least one comment per major scene
- [ ] Choices lead to meaningful different outcomes
- [ ] No dead ends (every path continues or ends properly)
- [ ] Tone matches established style
- [ ] Environmental details are vivid
- [ ] Character voices are consistent

---

## HOW TO HELP

### If you're Copilot/AI assistant:
1. Read this document fully
2. Check `game/game.js` for source content
3. Use `first_lesson.txt` as formatting reference
4. Expand one scene file at a time
5. Follow the templates above
6. Maintain quality standards
7. Test that all gotos resolve

### Priority Order:
1. `singing_dunes.txt` (most developed in game.js)
2. `verdant_tithe.txt` (complex branching)
3. `rune_glacier.txt` (needs control/harmony mechanics)
4. `endings.txt` (requires all paths to exist first)

---

## CONTACT

This project is maintained by @issdandavis on GitHub.
AI session handoff documentation: `docs/AI_SESSION_HANDOFF.md`
Task queue: `docs/NEXT_TASKS.md`

---

*"The spiral continues. Every scene you write adds another thread."*

**Last Updated:** November 22, 2025
**By:** Claude Code Session (teleport-session-recovery)
