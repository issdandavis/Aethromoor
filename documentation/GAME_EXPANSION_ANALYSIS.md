# GAME EXPANSION ANALYSIS & RECOMMENDATIONS
## Comparison with Professional Choice of Games Titles

---

## Current Game Status

**Polly's Wingscroll: The First Thread**
- **Word Count:** 30,238 words (ChoiceScript files only)
- **Timespan:** 3 months (single semester at academy)
- **Structure:** Mostly linear with variations
- **Scenes:** 15 total
- **Magic System:** Stat-based (power, knowledge, empathy, collaboration)
- **Companion Systems:** Familiars (6 options) + Golems (60 combinations)

---

## Comparison with Researched Games

### 1. Choice of the Vampire
**Stats:**
- **Word Count:** 850,000 words (4 volumes)
- **Timespan:** 85+ years (1815-1900s)
- **Structure:** Massive branching with hidden content

**Key Features We Should Adopt:**
- **Life-spanning narrative** - Story follows character across decades
- **Heavy stat system** - Agility, Charm, Intelligence, Strength, Willpower, PLUS skills like Creation, Fighting, Lore, Perception, Shapeshifting, Stealth, Status, Streetwise, Technology
- **Hidden relationship tracking** - NPC approval ratings affect dialogue and branches
- **Historical time progression** - Each chapter/volume covers different era
- **Secrets and replay value** - "Find something new every playthrough"

**What This Means for Our Game:**
- Expand from 3 months to multi-year story (Years 1-4 at Avalon, then post-graduation)
- Add more skill categories beyond just 4 stats
- Implement hidden relationship modifiers that affect available scenes
- Create time-skip mechanics between years

---

### 2. Choice of Robots
**Stats:**
- **Word Count:** 300,000 words
- **Structure:** Linear at start, 3 MAJOR exclusive branches

**Key Features We Should Adopt:**
- **Exclusive branching points** - Choices that create completely different paths
- **Deep stat tracking** - 10 relationships, 4 robot stats, personal/political stats
- **Character divergence** - "Two playthroughs can have relatively little overlap"
- **Companion building** - Creating your robot (similar to our golem system, but deeper)

**What This Means for Our Game:**
- Create at least 2-3 major branch points where story splits significantly
  - Example: After Year 1 - Join research team vs become combat mage vs diplomatic corps
  - Example: Mid-game crisis - Side with Izack's methods vs Aria's methods vs forge your own path
- Ensure different expedition/focus choices lead to genuinely different content
- Expand companion creation impact on story

---

### 3. Lords of Aswick
**Stats:**
- **Word Count:** 250,000 words
- **Timespan:** Entire lifetime (childhood to death)
- **Hidden Stats:** Wealth hidden, Nobility/Valour/Courtesy visible

**Key Features We Should Adopt:**
- **Life stages** - Childhood through death
- **Hidden influential stats** - Some stats affect outcomes but aren't shown to player
- **Political intrigue** - War, succession, marriage, alliances
- **Management elements** - Territory management alongside personal story

**What This Means for Our Game:**
- Add "reputation" and "influence" as hidden stats
- Create academy politics sub-system
- Add territory/project management (research projects, teaching responsibilities)
- Extend story beyond graduation (adult life as practicing mage)

---

### 4. Life of a Wizard
**Stats:**
- **Word Count:** 130,000 words
- **Timespan:** 80 years across 4 life stages
- **Magic Schools:** Divination, Enchantment, Conjuration, Transmutation, Illusion, Necromancy

**Key Features We Should Adopt:**
- **Multiple magic schools** - Players develop different magical specialties
- **Stat-raising through choices** - "Any choice raises the stat it's related to" (Arcana +15, etc.)
- **Life stage progression** - Childhood → University → Adventuring → Royal Advisor
- **100% achievable mastery** - With planning, can master ALL schools

**What This Means for Our Game:**
- **CRITICAL:** Add magic school system with learnable spells
- Create clear progression: Student → Journeyman → Master → Archmage
- Make each life stage feel distinct with different challenges
- Allow players to specialize OR generalize

**Proposed Magic Schools for Avalon:**
1. **Dimensional Magic** (Izack's specialty) - Portals, pocket dimensions, reality manipulation
2. **Boundary Magic** (Aria's specialty) - Wards, barriers, sealing, dimensional anchoring
3. **Living Magic** (Zara's specialty) - Nature magic, alchemy, life force manipulation
4. **Collaborative Magic** (Avalon's core) - Group casting, resonance, shared power
5. **Written Magic** (Rune Glacier) - Spell inscription, permanent enchantments, artifact creation
6. **Truth Magic** (Singing Dunes) - Oaths, honesty detection, binding contracts
7. **Memory Magic** (Optional advanced) - Mind palaces, thought preservation, dream walking

---

### 5. The Last Wizard
**Stats:**
- **Multiple learnable spells** - Golem building, dragon riding, necromancy, healing, fire, flight, invisibility, lightning, enchantment
- **Skill checks** - Specific abilities needed to pass events
- **Artifact collection** - Acquiring powerful magical items

**What This Means for Our Game:**
- Add specific spell acquisition scenes
- Create skill check gates (need X spell or Y stat to access path)
- Expand artifact system beyond just 3 expedition rewards
- Make spells learnable through: study, practice, discovery, teaching

---

### 6. Life of a Space Force Captain
**Stats:**
- **Word Count:** 350,000 words
- **7 Traits:** Strength, Agility, Endurance, Perception, Willpower, Charm, Intelligence
- **9 Skills:** Combat, Computers, Ranged Weapons, Leadership, Mechanics, Medicine, Pilot, Science, Streetwise
- **Faction relationships** - Learning from alien species requires relationship checks

**What This Means for Our Game:**
- Add faction system (different magical traditions at Avalon)
- Learning advanced magic from certain teachers requires relationship thresholds
- Expand skill system beyond just 4 stats

---

## MAJOR GAPS IN CURRENT GAME

### 1. **Limited Timespan**
- **Current:** 3 months (one semester)
- **Should Be:** Multi-year story (4+ years at academy, then post-graduation)
- **Fix:** Add Year 2, Year 3, Year 4 chapters + epilogue

### 2. **No Spell Learning System**
- **Current:** Only stat-based magic
- **Should Be:** Learnable spells in multiple schools
- **Fix:** Create 7 magic schools with 5-10 spells each

### 3. **Too Linear**
- **Current:** Mostly single path with variations
- **Should Be:** Multiple exclusive branches that weave in/out
- **Fix:** Add 3 major branching points with exclusive content

### 4. **Insufficient Mid-Game Content**
- **Current:** academy_life is one short scene
- **Should Be:** Rich daily life with many choices
- **Fix:** Expand academy life to recurring event system

### 5. **No Open Start**
- **Current:** Game starts at arrival
- **Should Be:** Choose your origin/background
- **Fix:** Add character creation intro with background selection

### 6. **Limited Word Count Per Playthrough**
- **Current:** ~30k total, player sees most of it
- **Should Be:** 150k+ total, player sees 40-60k per playthrough
- **Fix:** Add exclusive content that requires multiple playthroughs

---

## RECOMMENDED EXPANSION PLAN

### PHASE 1: Magic School System (HIGH PRIORITY)

**Add 7 Magic Schools with Progression:**

```choicescript
*comment Magic School Mastery Levels
*create dimensional_magic 0
*create boundary_magic 0
*create living_magic 0
*create collaborative_magic 0
*create written_magic 0
*create truth_magic 0
*create memory_magic 0

*comment Unlocked Spells (tracked individually)
*create spell_portal false
*create spell_pocket_dimension false
*create spell_ward false
*create spell_growth false
*create spell_healing false
*create spell_resonance false
*create spell_inscription false
*create spell_oath false
```

**Spell Learning Mechanics:**
- Study with teachers (Izack, Aria, Zara) → raises school stat
- Practice specific spells → unlocks spell_[name] variable
- Discover spells through exploration/secrets
- Master level requires reaching 80+ in school

**Implementation:**
- Create `magic_training.txt` scene for spell practice
- Add spell learning to existing scenes (expeditions can teach spells)
- Create spell check gates (need specific spell to access certain paths)

---

### PHASE 2: Multi-Year Timeline (HIGH PRIORITY)

**Expand from 3 months to 4 years + epilogue:**

**Current Structure:**
- Arrival → First Lesson → Academy Life → Expedition → Final Trial → Endings

**New Structure:**
```
Character Creation (Origin Selection)
↓
YEAR 1: Foundations
- Arrival → Familiar → First Lesson → Academy Life (recurring) → Expedition 1 → Year 1 Trial
↓
YEAR 2: Specialization
- Choose Focus Path → Advanced Training → Expedition 2 → Major Crisis Event → Year 2 Trial
↓
YEAR 3: Mastery
- Independent Research → Teaching Underclassmen → Expedition 3 → Political Intrigue → Year 3 Trial
↓
YEAR 4: Ascension
- Thesis Project → Final Expedition → Avalon Crisis → Graduation Trial → Endings
↓
EPILOGUE: 10 Years Later
- See consequences of choices, relationship outcomes, your legacy
```

**Word Count Target:** 150,000-200,000 words total

---

### PHASE 3: Open-Start Character Creation (MEDIUM PRIORITY)

**Add Origin Selection Scene:**

Player chooses background that affects starting stats and available dialogue/paths:

1. **Noble Heritage** - Start with high Status but lower practical skills
2. **Self-Taught Prodigy** - High Power but low Collaboration
3. **Magical Lineage** - Family tradition, high Knowledge but pressure to succeed
4. **Late Bloomer** - Discovered magic late, high Empathy but low Power
5. **Dimensional Refugee** - From another realm, unique perspective, high Innovation
6. **Commoner Scholar** - Earned admission through merit, balanced stats, chip on shoulder

**Implementation:**
- Create `character_creation.txt` scene before arrival
- Add origin-specific dialogue throughout game
- Some paths/NPCs only available to certain origins
- Affects starting relationship with teachers

---

### PHASE 4: Exclusive Branching Points (HIGH PRIORITY)

**Add 3 Major Branch Points:**

**Branch Point 1: End of Year 1**
```
Choice: How do you want to advance at Avalon?

A) RESEARCH PATH
   - Work with Aria on dimensional theory
   - Unlock advanced boundary magic
   - Academic challenges, publishing papers
   - Leads to "Scholar" ending track

B) COMBAT PATH
   - Train with battle mages
   - Learn defensive and offensive casting
   - Dungeon delving, artifact hunting
   - Leads to "Protector" ending track

C) DIPLOMATIC PATH
   - Work with dimensional diplomats
   - Mediate between magical factions
   - Political intrigue, negotiation
   - Leads to "Ambassador" ending track
```

**Each path has 15,000-20,000 words of exclusive content**

**Branch Point 2: Mid-Year 2**
```
Crisis: Avalon is threatened by dimensional instability

Choice: How do you respond?

A) SIDE WITH IZACK
   - Trusts collaborative magic to solve it
   - Risky but aligned with academy values
   - Can fail if collaboration too low

B) SIDE WITH ARIA
   - Use boundary magic to seal problem
   - Safer but abandons some principles
   - Can create future consequences

C) FORGE YOUR OWN PATH
   - Combine both approaches uniquely
   - Requires high Knowledge + Empathy
   - Best outcome but difficult to achieve
```

**Branch Point 3: Year 4 Thesis**
```
Choice: What is your thesis project?

A) CREATE NEW POCKET DIMENSION
   - Follow in Izack's footsteps
   - Builds on Avalon's legacy

B) BRIDGE TO OTHER REALM
   - Diplomatic/exploratory focus
   - Opens new story possibilities

C) SOLVE ANCIENT MAGICAL MYSTERY
   - Research-focused
   - Connects to lore (Third Thread, etc.)

D) REVOLUTIONIZE TEACHING METHOD
   - Educational reform
   - Political implications
```

---

### PHASE 5: Recurring Academy Life Events (MEDIUM PRIORITY)

**Expand academy_life into EVENT SYSTEM:**

Instead of one academy_life scene, create recurring daily life:

```choicescript
*label academy_week

*choice
  #Attend advanced lecture
    *goto lecture_event

  #Practice spells in training grounds
    *goto practice_event

  #Study in library
    *goto study_event

  #Socialize with students
    *goto social_event

  #Explore Avalon grounds
    *goto exploration_event

  #Work on independent project
    *goto project_event
```

**Each event type has 5-10 variations that appear randomly or based on stats/flags**

**Example - Practice Event Variations:**
- Duel with another student (tests combat skills)
- Collaborative casting exercise (raises collaboration)
- Experiment goes wrong (crisis to solve)
- Breakthrough moment (learn new spell)
- Teaching moment (help struggling student)

**This creates emergent gameplay and replay value**

---

### PHASE 6: Hidden Content & Secrets Expansion (MEDIUM PRIORITY)

**Add More Secret Scenarios:**

Current: 4 secret paths

Target: 15+ secret scenarios including:

**Secret Romance Paths:**
- Hidden poly option (romance multiple with their consent)
- Secret forbidden romance (consequences if discovered)
- Time-delayed romance (starts hostile, becomes romantic)

**Secret Magic Discoveries:**
- Forbidden spell grimoire in restricted library
- Ancient mage spirit in hidden chamber
- Dimensional anomaly leading to parallel Avalon
- Polly's true nature revelation (she's more than she seems)

**Secret Factions:**
- Underground student rebellion against academy rules
- Secret society of dimensional explorers
- Traditionalist mages opposing Izack's methods
- Cult trying to access Varn'ka'zul demon realm

**Secret Achievements:**
- Perfect all magic schools (100% in all 7)
- Never fail a single check (flawless playthrough)
- Unlock every secret path in one run
- Discover Polly's full history

---

## WORD COUNT BREAKDOWN (Target)

```
Character Creation: 5,000 words
Year 1: 35,000 words
  - Arrival: 3,000
  - Familiar Selection: 4,000
  - First Lesson: 5,000
  - Academy Life (recurring): 10,000
  - Expedition 1: 8,000
  - Year 1 Trial: 5,000

Year 2: 45,000 words
  - Path Selection: 5,000
  - Path-Specific Content: 20,000 (exclusive branches)
  - Academy Life Year 2: 10,000
  - Expedition 2: 5,000
  - Crisis Event: 5,000

Year 3: 40,000 words
  - Advanced Content: 15,000
  - Teaching Scenes: 8,000
  - Expedition 3: 7,000
  - Political Intrigue: 10,000

Year 4: 45,000 words
  - Thesis Project: 15,000 (varies by choice)
  - Final Expedition: 10,000
  - Avalon Crisis: 10,000
  - Graduation: 10,000

Romance Content: 15,000 words (optional scenes)
Secret Paths: 15,000 words (hidden content)
Epilogue & Endings: 20,000 words

TOTAL: ~220,000 words
Per Playthrough: 60,000-80,000 words (player sees ~35%)
```

---

## MAGIC SYSTEM DETAILED DESIGN

### School: DIMENSIONAL MAGIC (Izack's Specialty)

**Core Concept:** Manipulating space and reality itself

**Progression:**
- **Novice (0-20):** Sense dimensional boundaries
- **Apprentice (21-40):** Create temporary portals
- **Journeyman (41-60):** Stabilize pocket dimensions
- **Adept (61-80):** Create lasting pocket dimensions
- **Master (81-100):** Reality manipulation, dimensional anchoring

**Learnable Spells:**
1. **Dimensional Sight** (Novice) - See boundaries and leylines
2. **Minor Portal** (Apprentice) - Short-range teleportation
3. **Pocket Space** (Journeyman) - Small storage dimension
4. **Stabilized Portal** (Adept) - Long-lasting teleportation gates
5. **Pocket Dimension** (Adept) - Create small inhabitable space
6. **Dimensional Anchor** (Master) - Prevent unwanted teleportation
7. **Reality Shift** (Master) - Temporarily alter local physics

**How to Learn:**
- Study with Izack (primary teacher)
- Practice in Dimensional Lab
- Successful expedition to Dimensional Fringe
- Research ancient texts in library
- Breakthrough moments during crises

**Spell Checks in Story:**
- Need Minor Portal to access hidden areas
- Need Dimensional Sight to detect certain secrets
- Need Pocket Dimension for certain endings
- Need Dimensional Anchor to prevent demon incursions

---

### School: BOUNDARY MAGIC (Aria's Specialty)

**Core Concept:** Creating barriers and controlling thresholds

**Progression:**
- **Novice:** Simple wards against intrusion
- **Apprentice:** Elemental barriers
- **Journeyman:** Selective permeability (let some through, block others)
- **Adept:** Dimensional sealing
- **Master:** Absolute barriers, reality locks

**Learnable Spells:**
1. **Simple Ward** (Novice) - Keep out mundane intruders
2. **Elemental Barrier** (Apprentice) - Block fire, ice, etc.
3. **Selective Permeability** (Journeyman) - Choose what passes through
4. **Dimensional Seal** (Adept) - Close tears in reality
5. **Prison Field** (Adept) - Trap entities
6. **Reality Lock** (Master) - Prevent dimensional manipulation in area
7. **Absolute Defense** (Master) - Temporary invulnerability

**How to Learn:**
- Study with Aria (primary teacher)
- Practice defensive scenarios
- Rune Glacier expedition (boundary magic in written form)
- Crisis events (learn under pressure)

**Spell Checks:**
- Need Dimensional Seal to fix tears (required for some endings)
- Need Prison Field for certain combat scenarios
- Need Selective Permeability for secret path access

---

### School: LIVING MAGIC (Zara's Specialty)

**Core Concept:** Working with life force and natural energies

**Progression:**
- **Novice:** Sense life energy
- **Apprentice:** Accelerate growth
- **Journeyman:** Healing magic
- **Adept:** Life force manipulation
- **Master:** Creation of life, transmutation

**Learnable Spells:**
1. **Life Sense** (Novice) - Feel living things around you
2. **Accelerated Growth** (Apprentice) - Plants grow faster
3. **Minor Healing** (Journeyman) - Heal wounds
4. **Life Channel** (Adept) - Share life force
5. **Major Healing** (Adept) - Cure diseases, regenerate
6. **Transmutation** (Master) - Transform living things
7. **Spark of Life** (Master) - Awaken consciousness (golems, etc.)

**How to Learn:**
- Study with Zara (primary teacher)
- Work in magical gardens
- Verdant Tithe expedition
- Golem workshop (Spark of Life)

**Spell Checks:**
- Need Healing for certain character saves
- Need Life Sense to find hidden creatures
- Need Transmutation for shape-shifting path
- Need Spark of Life for advanced golem creation

---

### School: COLLABORATIVE MAGIC (Avalon's Core)

**Core Concept:** Amplifying magic through partnership

**Progression:**
- **Novice:** Basic resonance with one partner
- **Apprentice:** Group casting (3-5 mages)
- **Journeyman:** Perfect synchronization
- **Adept:** Large-scale collaboration (10+ mages)
- **Master:** Network casting (entire academy)

**Learnable Spells:**
1. **Resonance Link** (Novice) - Connect with one partner
2. **Circle Casting** (Apprentice) - Cast with small group
3. **Perfect Harmony** (Journeyman) - No energy loss in collaboration
4. **Mass Coordination** (Adept) - Lead large group efforts
5. **Network Anchor** (Master) - Become central node for collaborative spells
6. **Gestalt Consciousness** (Master) - Temporary hive mind with consent
7. **Legacy Binding** (Master) - Create permanent collaborative enchantments

**How to Learn:**
- Practice with study partners
- Successful collaborative crisis resolution
- Teaching others (raises your own skill)
- Special Izack mentorship scenes

**Spell Checks:**
- Need Circle Casting for group expedition success
- Need Mass Coordination for academy defense
- Need Network Anchor for certain epic endings
- High collaborative magic unlocks special graduation ceremony

---

### School: WRITTEN MAGIC (Rune Glacier Tradition)

**Core Concept:** Permanent enchantments through inscription

**Progression:**
- **Novice:** Read simple magical runes
- **Apprentice:** Write temporary enchantments
- **Journeyman:** Create lasting inscriptions
- **Adept:** Living runes (self-modifying)
- **Master:** Artifact creation

**Learnable Spells:**
1. **Rune Reading** (Novice) - Understand magical writing
2. **Temporary Inscription** (Apprentice) - Enchantments that last hours
3. **Lasting Inscription** (Journeyman) - Permanent enchantments
4. **Living Runes** (Adept) - Runes that adapt to circumstances
5. **Artifact Forging** (Adept) - Create magical items
6. **Spell Storage** (Master) - Store spells in objects for later
7. **Inheritance Script** (Master) - Enchantments that pass to chosen heirs

**How to Learn:**
- Rune Glacier expedition (primary source)
- Study ancient texts
- Aria teaches theory
- Practical experimentation

**Spell Checks:**
- Need Rune Reading to access ancient lore
- Need Artifact Forging for equipment paths
- Need Spell Storage for certain strategies
- Need Living Runes for adaptive defenses

---

### School: TRUTH MAGIC (Singing Dunes Tradition)

**Core Concept:** Binding oaths and revealing honesty

**Progression:**
- **Novice:** Detect lies
- **Apprentice:** Compel truth
- **Journeyman:** Binding oaths
- **Adept:** Contract magic
- **Master:** Absolute truth, reality enforcement

**Learnable Spells:**
1. **Truth Sense** (Novice) - Feel when someone lies
2. **Compel Honesty** (Apprentice) - Make it hard to lie
3. **Oath Binding** (Journeyman) - Create magical promises
4. **Contract Magic** (Adept) - Enforceable magical agreements
5. **Truth Aura** (Adept) - Area where lies are impossible
6. **Reality Enforcement** (Master) - Make statements become true
7. **Universal Oath** (Master) - Binding that affects entire dimensions

**How to Learn:**
- Singing Dunes expedition (primary source)
- Study with oath-keepers
- Political intrigue path (practical use)
- Diplomatic corps training

**Spell Checks:**
- Need Truth Sense for investigation scenes
- Need Oath Binding for certain alliances
- Need Contract Magic for diplomatic endings
- Need Truth Aura for courtroom scenarios

---

### School: MEMORY MAGIC (Advanced/Optional)

**Core Concept:** Preserving and manipulating thoughts and memories

**Progression:**
- **Novice:** Perfect recall
- **Apprentice:** Memory palaces
- **Journeyman:** Share memories
- **Adept:** Memory modification
- **Master:** Collective consciousness, living archives

**Learnable Spells:**
1. **Perfect Recall** (Novice) - Remember everything you've learned
2. **Memory Palace** (Apprentice) - Mental storage system
3. **Memory Share** (Journeyman) - Show memories to others
4. **Thought Preservation** (Adept) - Store memories in crystals
5. **Memory Modification** (Adept) - Carefully edit memories (ethical concerns)
6. **Dream Walking** (Master) - Enter others' dreams
7. **Living Archive** (Master) - Become repository of knowledge

**How to Learn:**
- Secret path only (hidden teacher)
- High Knowledge stat required (70+)
- Complete library research quest chain
- Discover memory crystal artifacts

**Spell Checks:**
- Need Perfect Recall for perfect exam scores
- Need Memory Share for certain romance scenes
- Need Dream Walking for secret paths
- Need Living Archive for scholar ending

---

## IMPLEMENTATION PRIORITY

### IMMEDIATE (Do This First)
1. **Magic School System** - Adds core gameplay loop
2. **Year 2 Content** - Extends game meaningfully
3. **Spell Learning Scenes** - Makes magic feel real

### SHORT-TERM (Next Phase)
4. **Branch Point 1** (End of Year 1 path selection)
5. **Recurring Academy Events** - Adds replay value
6. **Character Creation/Origin** - Improves opening

### MEDIUM-TERM (After Core Content)
7. **Year 3 & Year 4** - Complete academy experience
8. **Branch Points 2 & 3** - Major story divergence
9. **Secret Content Expansion** - Rewards exploration

### LONG-TERM (Polish & Completion)
10. **Epilogue System** - See long-term consequences
11. **Advanced Endings** - 30+ unique endings
12. **Achievement System** - Full completion tracking

---

## ESTIMATED FINAL SCOPE

**Total Word Count:** 220,000+ words
**Minimum Playthrough:** 60,000 words
**Maximum Playthrough:** 85,000 words
**Percentage Seen Per Run:** ~35%
**Recommended Playthroughs:** 8-12 to see all major content
**Completionist Playthroughs:** 20+ to see everything

**Comparison to Published Games:**
- Exceeds Hosted Games minimum (30k) by 7x
- Approaching Choice of Robots (300k)
- Competitive with Lords of Aswick (250k)
- Still smaller than Choice of the Vampire (850k) but more focused

**Publishing Readiness:**
- ✅ Hosted Games (30k minimum)
- ✅ Hosted Games Premium tier (100k+)
- ⚠️ Steam (150k minimum) - Would need slight expansion OR count this as "Episode 1"

---

## NEXT STEPS

1. **Review this document** - Confirm priorities
2. **Start with Magic Schools** - Create 7 school stat variables + spell flags
3. **Design spell learning scenes** - How does player acquire each spell?
4. **Expand academy_life** - Create recurring event system
5. **Draft Year 2 outline** - Major branch point + exclusive content
6. **Test branching** - Ensure different paths feel meaningfully different

**Questions to Answer:**
- Do you want full 4-year academy experience or shorter?
- Should some magic schools be harder to access than others?
- How important is combat vs social vs research gameplay?
- Should there be "fail states" or always paths to graduation?
- Do you want player to choose specialization or allow full generalist?

---

*This expansion would transform the game from a solid 30k intro into a comprehensive 220k+ interactive epic comparable to the best Choice of Games titles.*
