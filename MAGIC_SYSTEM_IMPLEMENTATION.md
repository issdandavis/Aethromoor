# MAGIC SCHOOL SYSTEM - Implementation Plan
## Detailed Design for Spell Learning & Progression

---

## OVERVIEW

Transform current stat-only magic into a rich spell learning system with 7 schools, 49 learnable spells, and progression mechanics inspired by **Life of a Wizard** and **The Last Wizard**.

**Core Philosophy:**
- Choices raise related magic school stats (like Life of a Wizard)
- Specific spells must be learned through study, practice, or discovery
- Some spells have stat requirements before they can be learned
- Different schools synergize in interesting ways
- No "wrong" build - specialist and generalist both viable

---

## VARIABLES TO ADD TO startup.txt

```choicescript
*comment ================================================
*comment MAGIC SCHOOL SYSTEM
*comment ================================================

*comment School Mastery Levels (0-100)
*create dimensional_magic 0
*create boundary_magic 0
*create living_magic 0
*create collaborative_magic 10
*create written_magic 0
*create truth_magic 0
*create memory_magic 0

*comment Spell Unlock Flags (true/false)
*comment Format: spell_[school]_[spellname]

*comment Dimensional Magic Spells
*create spell_dimensional_sight false
*create spell_minor_portal false
*create spell_pocket_space false
*create spell_stabilized_portal false
*create spell_pocket_dimension false
*create spell_dimensional_anchor false
*create spell_reality_shift false

*comment Boundary Magic Spells
*create spell_simple_ward false
*create spell_elemental_barrier false
*create spell_selective_permeability false
*create spell_dimensional_seal false
*create spell_prison_field false
*create spell_reality_lock false
*create spell_absolute_defense false

*comment Living Magic Spells
*create spell_life_sense false
*create spell_accelerated_growth false
*create spell_minor_healing false
*create spell_life_channel false
*create spell_major_healing false
*create spell_transmutation false
*create spell_spark_of_life false

*comment Collaborative Magic Spells
*create spell_resonance_link true
*create spell_circle_casting false
*create spell_perfect_harmony false
*create spell_mass_coordination false
*create spell_network_anchor false
*create spell_gestalt_consciousness false
*create spell_legacy_binding false

*comment Written Magic Spells
*create spell_rune_reading false
*create spell_temporary_inscription false
*create spell_lasting_inscription false
*create spell_living_runes false
*create spell_artifact_forging false
*create spell_spell_storage false
*create spell_inheritance_script false

*comment Truth Magic Spells
*create spell_truth_sense false
*create spell_compel_honesty false
*create spell_oath_binding false
*create spell_contract_magic false
*create spell_truth_aura false
*create spell_reality_enforcement false
*create spell_universal_oath false

*comment Memory Magic Spells (Advanced/Secret)
*create spell_perfect_recall false
*create spell_memory_palace false
*create spell_memory_share false
*create spell_thought_preservation false
*create spell_memory_modification false
*create spell_dream_walking false
*create spell_living_archive false

*comment Spell Learning Tracking
*create total_spells_known 1
*create spells_mastered 0
*create favorite_school "none"
```

---

## LEARNING MECHANICS

### Method 1: Teacher Instruction (Most Common)

**Format:**
- Teacher explains spell theory
- Player practices spell
- Stat check OR choice determines success
- On success: spell flag = true, school stat increases

**Example - Learning Minor Portal from Izack:**

```choicescript
*label learn_minor_portal

Izack draws a glowing circle in the air.

[b]"Dimensional magic at its core is about creating connections between two points in space. The Minor Portal is your first true dimensional spell."[/b]

*page_break

[b]"Feel the space around you. Now, feel a location you've been before - somewhere familiar. The stronger your connection to that place, the easier this will be."[/b]

*choice
  #Visualize your dorm room - you know every detail of that space.
    *set dimensional_magic +10
    *goto portal_practice_room

  #Visualize the academy courtyard - a place of power and leylines.
    *set dimensional_magic +15
    *set collaboration +5
    *goto portal_practice_courtyard

  #Visualize home - wherever you came from before Avalon.
    *set dimensional_magic +5
    *set empathy +10
    *goto portal_practice_home

*label portal_practice_room

You close your eyes and think of your room. The cushions, the window, the familiar scent of your space.

*line_break

*if dimensional_magic >= 20
  The portal snaps into existence—small, shimmering, and perfect.

  Through it, you can see your room as if looking through a window.

  Izack grins. [b]"Excellent! Now reach through."[/b]

  *page_break

  Your hand passes through the portal. On the other side, your fingers touch your desk.

  [b]"You've done it. The Minor Portal is yours."[/b]

  *set spell_minor_portal true
  *set dimensional_magic +10
  *set total_spells_known +1
  *achievement spell_learner visible 5 First True Spell
    You learned your first dimensional spell.

  *goto spell_learned_celebration

*if dimensional_magic < 20
  You strain, reaching for the connection, but...

  Nothing happens.

  *page_break

  Izack places a reassuring hand on your shoulder.

  [b]"Don't worry. Dimensional magic takes time. Keep practicing your awareness exercises, and we'll try again soon."[/b]

  *set dimensional_magic +5

  *page_break

  You'll need to practice more before you can learn this spell.

  (Requires: Dimensional Magic 20+)

  *goto academy_life
```

---

### Method 2: Discovery Through Exploration

**Format:**
- Player encounters magical phenomenon
- Can attempt to understand/replicate it
- Success requires stat threshold OR specific previous knowledge

**Example - Discovering Life Sense in Verdant Tithe:**

```choicescript
*label verdant_discovery

You place your hand on the ancient Heartwood Tree.

The moment your skin touches bark, you feel... everything.

*page_break

Every root. Every leaf. Every insect crawling on branches miles away.

You're not just touching the tree—you're [i]in[/i] the tree. You ARE the tree.

*line_break

[i]No,[/i] something whispers. [i]You're feeling life force. The energy that connects all living things.[/i]

*page_break

*choice
  #Try to hold onto this sensation - learn to replicate it.
    *if living_magic >= 15
      *goto life_sense_learned
    *else
      *goto life_sense_failed

  #Let go - this is overwhelming and frightening.
    *set empathy -5
    *goto verdant_continue

*label life_sense_learned

You focus, memorizing the sensation. The pattern. The frequency.

*page_break

When you pull your hand away from the tree, you consciously reach out with that same sense.

There—you feel Zara, 50 meters away, her hybrid life force bright and warm.

You feel birds in the canopy. Insects in the soil. Everything living.

*page_break

The Heartwood Tree pulses with approval.

[i]You have learned to see life. Carry this gift wisely.[/i]

*set spell_life_sense true
*set living_magic +15
*set total_spells_known +1
*achievement nature_speaker visible 10 Nature's Gift
  The Heartwood Tree taught you to sense life itself.

*goto verdant_continue
```

---

### Method 3: Crisis Learning

**Format:**
- Desperate situation requires magic you don't know
- Can attempt spell beyond current skill if stakes are high enough
- Success grants spell permanently but may have consequences

**Example - Learning Dimensional Seal in a Crisis:**

```choicescript
*label dimensional_tear_crisis

The tear in reality widens. Through it, you see the void between dimensions.

Something is trying to come through.

*page_break

Aria shouts: [b]"We need a Dimensional Seal! Someone who knows boundary magic!"[/b]

*if spell_dimensional_seal = true
  *goto seal_the_tear

*if spell_dimensional_seal = false
  You don't know that spell.

  But you've watched Aria work. You've studied the theory.

  *line_break

  Maybe you can try.

  *page_break

  *choice
    #Attempt the Dimensional Seal even though you haven't learned it.
      *goto crisis_seal_attempt

    #Let Aria handle it - you're not ready for this.
      *set collaboration +10
      *goto aria_seals_tear

*label crisis_seal_attempt

You step forward, hands raised.

[b]"I'll try."[/b]

*page_break

Aria's eyes widen. [b]"${name}, you don't—"[/b]

[b]"I've studied the theory. I can do this."[/b]

*line_break

*if (boundary_magic >= 30) or (knowledge >= 70)
  *goto crisis_seal_success

*if (boundary_magic < 30) and (knowledge < 70)
  *goto crisis_seal_failure

*label crisis_seal_success

You reach for the tear, not with force, but with understanding.

A boundary is a threshold. A transition. You're not trying to destroy the tear—you're trying to [i]heal[/i] it.

*page_break

Your magic flows into the wound in reality.

Thread by thread, you weave it closed.

*line_break

The seal holds.

*page_break

Aria stares at you.

[b]"You... you just learned Dimensional Seal. Under pressure. In a crisis. That's..."[/b]

She actually looks impressed.

[b]"That's extraordinary."[/b]

*set spell_dimensional_seal true
*set boundary_magic +20
*set aria_relationship +25
*set total_spells_known +1
*set reckless_actions +1
*achievement crisis_mage visible 15 Forged in Fire
  You learned a spell through sheer desperation and will.

*page_break

[i]*Polly lands on your shoulder.*[/i]

[i]"Well. That was either incredibly brave or incredibly stupid. Possibly both. Good work though."[/i]

*goto tear_sealed

*label crisis_seal_failure

You reach for the tear, trying to remember Aria's technique.

But your understanding isn't deep enough. Your power falters.

*page_break

The seal you create is weak, unstable.

It shatters.

*line_break

The tear widens.

*set failures +1

*page_break

Aria has to intervene, combining her magic with Izack's to force it shut.

They succeed, but everyone is magically exhausted.

*line_break

Aria turns to you, disappointed.

[b]"I appreciate your courage, ${name}. But attempting magic beyond your skill in a crisis can get people killed."[/b]

*set aria_relationship -10
*set collaboration -5

*goto tear_sealed_aria
```

---

### Method 4: Research & Study

**Format:**
- Spend time in library or with texts
- Make knowledge checks or choices
- Gradual accumulation leads to spell unlock

**Example - Learning Rune Reading Through Study:**

```choicescript
*label library_research

The restricted section contains texts on Written Magic—ancient grimoires covered in glowing runes.

You can feel the magic radiating from the pages.

*page_break

*choice
  #Study the basics - start with simple rune theory.
    *set written_magic +5
    *set knowledge +5
    *goto rune_basics

  #Jump to advanced texts - you learn faster under challenge.
    *if knowledge >= 60
      *goto advanced_runes
    *else
      *goto advanced_runes_failure

  #Find a teacher instead - books alone won't be enough.
    *set collaboration +5
    *goto seek_rune_teacher

*label rune_basics

You spend hours studying the foundational principles.

Runes are magical language made physical. Each symbol carries meaning, power, intention.

*page_break

Unlike spoken spells, which disperse after casting, written magic endures.

*line_break

Over the next week, you practice reading simple protective runes, storage runes, lighting runes.

*set written_magic +10
*set knowledge +10

*page_break

*if written_magic >= 15
  One evening, you realize you can [i]read[/i] the ancient texts.

  Not translate—[i]read[/i]. The runes speak directly to your understanding.

  *set spell_rune_reading true
  *set total_spells_known +1

  [b]You have learned Rune Reading.[/b]

  *goto library_conclusion

*if written_magic < 15
  You're making progress, but mastery will take more time.

  *goto library_conclusion
```

---

## SPELL USAGE SYSTEM

### Passive Spells (Always Active Once Learned)

These provide permanent benefits:

```choicescript
*if spell_truth_sense = true
  You sense the lie immediately. His words don't match reality.

*if spell_life_sense = true
  You feel the hidden creature before you see it.

*if spell_dimensional_sight = true
  The hidden portal shimmers into visibility.
```

---

### Active Spells (Player Chooses to Cast)

These appear as choice options:

```choicescript
*choice
  #Use Minor Portal to teleport past the obstacle.
    *if spell_minor_portal = true
      *goto portal_solution
    *if spell_minor_portal = false
      *goto portal_fail

  #Use Elemental Barrier to protect against the flames.
    *if spell_elemental_barrier = true
      *goto barrier_solution
    *if spell_elemental_barrier = false
      *goto barrier_fail

  #Try to fight through without magic.
    *goto combat_solution
```

---

### Collaborative Spells (Combine with Others)

These require partners:

```choicescript
*if (spell_circle_casting = true) and (collaboration >= 60)
  *choice
    #Suggest a collaborative casting circle.
      [b]"If we work together, we can amplify this spell tenfold."[/b]

      *goto circle_casting_scene

    #Work individually - faster and simpler.
      *goto individual_casting
```

---

## PROGRESSION EXAMPLES

### Beginner Dimensional Mage (Year 1)
```
dimensional_magic: 35
Spells Known:
- Dimensional Sight (passive awareness)
- Minor Portal (short-range teleportation)
- Pocket Space (small storage dimension)

Can: Access hidden areas, teleport short distances, store items
Can't: Create stable pocket dimensions, prevent others' teleportation
```

### Advanced Dimensional Mage (Year 3)
```
dimensional_magic: 75
Spells Known:
- Dimensional Sight
- Minor Portal
- Pocket Space
- Stabilized Portal
- Pocket Dimension
- Dimensional Anchor

Can: Everything above PLUS create lasting portals, inhabitable spaces, prevent unwanted teleportation
Can't: Reality manipulation (requires mastery)
```

### Master Dimensional Mage (Year 4)
```
dimensional_magic: 95
Spells Known:
- All 7 Dimensional spells

Can: Create pocket dimensions like Avalon (small scale), manipulate local reality, anchor or unlock dimensions at will
Unlocks: "Dimensional Archmage" ending path
```

---

## SYNERGIES BETWEEN SCHOOLS

**Example 1: Dimensional + Boundary**
```choicescript
*if (spell_pocket_dimension = true) and (spell_reality_lock = true)
  You can create a pocket dimension that is [i]locked[/i]—accessible only by those you permit.

  This combination unlocks unique content:
    - Personal sanctum nobody can access
    - Secure research space for dangerous experiments
    - Hidden meeting place for secret societies
```

**Example 2: Living + Truth**
```choicescript
*if (spell_life_sense = true) and (spell_truth_sense = true)
  You can feel both the life force [i]and[/i] emotional state of living beings.

  You know not just that someone is lying, but WHY they're lying—fear, greed, protection.

  This combination unlocks:
    - Deep empathy paths
    - Advanced diplomacy options
    - Unique romance scenes (understanding true feelings)
```

**Example 3: Collaborative + Written**
```choicescript
*if (spell_legacy_binding = true) and (spell_inheritance_script = true)
  You can create collaborative enchantments that last forever and pass between generations.

  This unlocks:
    - Founding your own magical tradition
    - Creating academy-like institutions
    - "Legacy Builder" ending path
```

---

## SPELL CHECK GATES (Examples)

### Research Path (Year 2+)

```choicescript
*if spell_rune_reading = false
  The ancient texts are illegible to you.

  You'll need to learn Rune Reading before you can continue this research path.

  *goto alternative_path

*if spell_rune_reading = true
  You read the ancient text with ease.

  It describes a lost dimensional technique—exactly what you need.

  *goto research_breakthrough
```

### Secret Path Access

```choicescript
*if (spell_dimensional_sight = true) and (spell_truth_sense = true)
  You see both the hidden portal AND sense that it's safe to enter.

  This is a secret that most students never find.

  *goto hidden_chamber

*if (spell_dimensional_sight = false) or (spell_truth_sense = false)
  Something feels... off about this wall. But you can't quite place it.

  *goto miss_secret
```

### Combat/Crisis Scenario

```choicescript
*if spell_prison_field = true
  #Use Prison Field to trap the hostile entity.
    You raise your hands and weave boundary magic into a cage.

    The creature slams against the barriers but cannot escape.

    Crisis averted.

    *goto crisis_resolved

*if spell_prison_field = false
  You don't know how to contain it. You'll need a different approach.

  *goto alternative_solution
```

---

## MASTERY THRESHOLDS

```choicescript
*comment Check mastery levels periodically
*label check_magical_mastery

*if dimensional_magic >= 80
  *if dimensional_mastery_acknowledged = false
    Izack calls you aside after class.

    [b]"${name}, you've achieved what few students ever do. You've mastered Dimensional Magic."[/b]

    *set dimensional_mastery_acknowledged true
    *set izack_relationship +20
    *achievement dimensional_master visible 25 Master of Dimensions
      You have mastered Izack's specialty.

*if (dimensional_magic + boundary_magic + living_magic + collaborative_magic + written_magic + truth_magic + memory_magic) / 7 >= 60
  *if generalist_acknowledged = false
    Aria, Izack, and Zara gather you for a meeting.

    [b]"We've been tracking your progress,"[/b] Aria says. [b]"You're not specializing—you're mastering [i]everything[/i]."[/b]

    Izack nods. [b]"A true generalist mage. It's rare and valuable."[/b]

    *set generalist_acknowledged true
    *achievement universal_mage visible 30 Universal Mage
      You have achieved broad mastery across all schools.

*if (dimensional_magic >= 100) and (boundary_magic >= 100) and (living_magic >= 100) and (collaborative_magic >= 100) and (written_magic >= 100) and (truth_magic >= 100) and (memory_magic >= 100)
  *achievement perfect_mage visible 50 The Perfect Mage
    You have achieved 100% mastery in all seven schools of magic.
    You are one of the greatest mages in history.
```

---

## NEW SCENE: magic_training.txt

Create dedicated spell practice scene:

```choicescript
*comment ================================================
*comment MAGIC TRAINING
*comment Daily/weekly spell practice and learning
*comment ================================================

*label start

[b]== MAGIC TRAINING ==[/b]

*line_break

You have free time to practice magic.

*page_break

*if favorite_school = "none"
  You haven't yet chosen a magical focus.

*if favorite_school != "none"
  You've been focusing on ${favorite_school}, but you can study other schools too.

*page_break

What would you like to work on today?

*choice
  #Practice Dimensional Magic with Izack
    *set dimensional_magic +5
    *goto dimensional_practice

  #Study Boundary Magic with Aria
    *set boundary_magic +5
    *goto boundary_practice

  #Learn Living Magic with Zara
    *set living_magic +5
    *goto living_magic_practice

  #Work on Collaborative Magic with study partners
    *set collaborative_magic +5
    *goto collaborative_practice

  #Research Written Magic in the library
    *set written_magic +5
    *goto written_practice

  #Explore Truth Magic (if Singing Dunes visited)
    *if expedition_choice = "Singing Dunes"
      *set truth_magic +5
      *goto truth_practice
    *if expedition_choice != "Singing Dunes"
      *goto unavailable_truth

  #Investigate Memory Magic (secret path)
    *if hidden_lore_discovered >= 3
      *set memory_magic +5
      *goto memory_practice
    *if hidden_lore_discovered < 3
      *goto unavailable_memory

  #Review and choose spell to focus on
    *goto spell_selection_menu

*comment Continue with specific practice scenes for each school...
```

---

## IMPLEMENTATION STEPS

### Step 1: Update startup.txt
- Add all 49 spell variables
- Add 7 magic school stats
- Add tracking variables (total_spells_known, etc.)

### Step 2: Create magic_training.txt
- Practice scenes for each school
- Spell learning opportunities
- Teacher interactions

### Step 3: Modify Existing Scenes
- **first_lesson.txt** - Add spell learning (Resonance Link)
- **academy_life.txt** - Add training option → magic_training
- **expedition scenes** - Each teaches school-specific spells
- **character_bonds.txt** - Teachers offer advanced spell training

### Step 4: Add Spell Checks Throughout
- Gate certain paths behind spell requirements
- Provide alternate solutions if player lacks specific spell
- Reward creative spell combinations

### Step 5: Create Stat Chart Integration
```choicescript
*stat_chart
  text name
  text gender_full

  percent collaboration Collaboration
  percent power Power
  percent knowledge Knowledge
  percent empathy Empathy

  opposed_pair communication_vs_domination
    Communication
    Domination

  opposed_pair honesty_vs_deception
    Honesty
    Deception

  opposed_pair tradition_vs_innovation
    Tradition
    Innovation

  opposed_pair individual_vs_collective
    Individual
    Collective

  percent dimensional_magic Dimensional Magic
  percent boundary_magic Boundary Magic
  percent living_magic Living Magic
  percent collaborative_magic Collaborative Magic
  percent written_magic Written Magic
  percent truth_magic Truth Magic
  percent memory_magic Memory Magic (Secret)

  text total_spells_known Spells Learned

  percent izack_relationship Izack Relationship
  percent aria_relationship Aria Relationship
  percent zara_relationship Zara Relationship
  percent polly_relationship Polly Relationship
```

---

## ESTIMATED WORD COUNT ADDITION

**Magic Training Scenes:** 15,000 words
- 7 schools × 2,000 words each = 14,000
- General training framework = 1,000

**Spell Learning Scenes:** 10,000 words
- 49 spells × ~200 words each = ~10,000

**Spell Check Gates & Usage:** 8,000 words
- Scattered throughout existing and new scenes

**Total:** ~33,000 additional words

---

*This system transforms the game from stat-based magic into a rich spell-learning experience that rewards exploration, study, and strategic choice.*
