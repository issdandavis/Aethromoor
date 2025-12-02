# 🎯 CUSTOM AGENT RECOMMENDATIONS FOR AVALON PROJECT
## Strategic Analysis for Specialized AI Agents

**Prepared by:** Avalon Lore Steward  
**Date:** December 2, 2025  
**Purpose:** Identify critical gaps in current AI workforce and recommend specialized custom agents

---

## 📊 CURRENT STATE ANALYSIS

### Existing AI Infrastructure
**Custom Agents (2):**
- `my-agent` (Avalon Lore Steward) - File organization and lore maintenance
- `agent-manager` - Coordinates 5 AI workers

**AI Workflow Workers (5):**
1. Scene Writer - Writes story content
2. Content Polisher - Adds sensory details
3. Stat Balancer - Balances game difficulty
4. Game Tester - Finds bugs
5. Autonomous Worker - Handles misc tasks

**Automation Tools (8 Python scripts):**
- `scene_writer_agent.py` - Scene generation
- `content_polisher.py` - Sensory detail enhancement
- `stat_analyzer.py` - Statistical analysis
- `validate_choicescript.py` - Syntax validation
- `find_dead_ends.py` - Path analysis
- `ai_autonomous_worker.py` - Task queue processor
- `agent_manager_cli.py` - Management interface
- `agent_orchestrator.py` - Coordination system

### Current Task Queue Analysis
**Priority 1 (Critical):** 36 expedition scenes to write (Singing Dunes, Verdant Tithe, Rune Glacier)
**Priority 2 (Important):** 14 endings + romance system enhancement
**Priority 3 (Polish):** Sensory details, Polly's voice consistency, character dialogue
**Priority 4 (QA):** QuickTest, RandomTest, stat balance verification
**Priority 5 (Docs):** Player guide, stat mechanics, style guide

### Identified Gaps
1. **No HTML→ChoiceScript conversion specialist** - Manual, tedious, error-prone
2. **No lore consistency validator** - Risk of canon violations
3. **No character voice specialist** - Polly's voice needs dedicated attention
4. **No ChoiceScript syntax expert** - Technical validation is basic
5. **No romance/relationship specialist** - Complex polyamory system needs expertise
6. **No ending orchestrator** - 14 endings with complex stat requirements

---

## 🎯 RECOMMENDED CUSTOM AGENTS

### 1. **ChoiceScript Conversion Specialist** 
**Priority:** CRITICAL ⚡

#### Domain Expertise
- HTML game structure analysis
- ChoiceScript syntax mastery
- Stat system preservation across formats
- Choice tree reconstruction
- Narrative parity validation

#### Tasks from Queue (Direct Impact)
- **Priority 1:** All 36 expedition scenes (Singing Dunes: 15 scenes, Verdant Tithe: 12 scenes, Rune Glacier: 12 scenes)
- Converts HTML scenes in `game/scenes/` to ChoiceScript in `choicescript_game/scenes/`
- Ensures stat tracking consistency (`collaboration`, relationship variables)
- Preserves branching paths and choice consequences

#### Why Needed
**Current Gap:** The project has a complete 40,000+ word HTML game that needs conversion to professional ChoiceScript format. This is the largest bottleneck (36 scenes × 2 hours = 72 hours of work). The existing Scene Writer creates new content but doesn't specialize in format conversion.

**Unique Value:**
- Understands both HTML game.js architecture AND ChoiceScript syntax
- Can map HTML choice structures to `*choice`/`*if` statements accurately
- Preserves existing narrative quality while adapting technical format
- Validates that converted scenes maintain same story outcomes

**Success Metrics:**
- HTML and ChoiceScript versions have identical story paths
- All stat modifications preserved accurately
- No loss of player choices or narrative branches
- Conversion time: 45 mins per scene (vs 2 hours manual)

#### Technical Capabilities Required
```
INPUT: /game/scenes/prologue.txt (HTML format)
PROCESS: 
  1. Extract narrative text and choices
  2. Map stat changes to *set commands
  3. Convert branching to ChoiceScript *if/*choice
  4. Preserve Polly's commentary formatting
  5. Validate syntax with validation tools
OUTPUT: /choicescript_game/scenes/prologue.txt (ChoiceScript)
```

---

### 2. **Lore Consistency Guardian**
**Priority:** HIGH 🛡️

#### Domain Expertise
- Deep knowledge of Spiral of Pollyoneth universe
- Character chronology across 4 generations (150+ years)
- Magic system rules (collaborative casting, dimensional theory)
- Geography and realm-specific attributes
- Character relationship web validation

#### Tasks from Queue (Direct Impact)
- **Priority 1:** Validates all 36 expedition scenes for lore accuracy
- **Priority 3:** Ensures character dialogue consistency
- **Priority 2:** Validates ending requirements match character arcs
- **Priority 5:** Creates comprehensive stat mechanics documentation

#### Why Needed
**Current Gap:** The project has:
- 8+ lore documents (Geography PDF, Character Chronicles, Worldbuilding markdown)
- 4-generation character timeline (Izack → Alexander → Grandchildren → Zara)
- Complex magic rules (collaborative vs hierarchical casting)
- No automated system to catch contradictions

**Unique Value:**
- Prevents embarrassing lore breaks (e.g., character appearing before they're born)
- Cross-references new content against `IZACK_MASTER_CHRONICLE_UPDATED.txt`
- Validates magic usage follows collaborative philosophy
- Checks realm-specific details (Sul'dessar sand magic, Verdant Tithe thoughtvines)

**Success Metrics:**
- Zero lore contradictions in published game
- Character voice remains consistent across 15+ scenes
- Magic system rules applied uniformly
- Geographic details match canonical descriptions

#### Validation Capabilities
```
CHECK AGAINST:
- /lore/Pollys_Wingscrolls_Worldbuilding.markdown (realm details)
- /lore/# IZACK'S MAGICAL UNIVERSE - COMPLE.txt (character canon)
- /lore/Unified Worldbuilding Master Framew.txt (magic rules)
- /lore/__Geography and Natural Lore of the Spiral of Pollyoneth__.pdf

VALIDATES:
- Character ages/timeline consistency
- Magic system adherence (collaboration > control)
- Realm-specific flora/fauna accuracy
- Relationship continuity (who knows whom when)
```

---

### 3. **Polly's Voice Architect**
**Priority:** MEDIUM-HIGH 🪶

#### Domain Expertise
- Polly's unique character voice (dimensional consciousness with sass)
- Meta-commentary timing and placement
- Breaking 4th wall appropriately
- Balancing wisdom with sarcasm
- "Caw" integration naturalness

#### Tasks from Queue (Direct Impact)
- **Priority 3:** Polish Polly's voice across all scenes (estimated 3 hours)
- Enhances commentary in all 36 expedition scenes
- Adds Polly interjections to 14 endings
- Ensures Polly's presence feels consistent

#### Why Needed
**Current Gap:** Polly is a unique character - a "Polydimensional Manifestation of Accumulated Wisdom and Occasional Sarcasm" who:
- Breaks the 4th wall regularly
- Provides meta-commentary on magic
- Uses italicized dialogue format: `[i]"Commentary here"[/i]`
- Says "Caw" as punctuation
- Balances being helpful and sarcastic

Current AI workers treat Polly like a normal character, missing the nuance.

**Unique Value:**
- Specialized training on Polly's existing dialogue patterns
- Knows when Polly should comment vs. stay silent
- Understands dimensional magic context for her insights
- Can inject humor without breaking immersion

**Success Metrics:**
- Players recognize Polly's voice as consistent
- Commentary adds value (explains magic, provides hints)
- Humor lands without being annoying
- "Caw" usage feels natural, not forced

#### Example Quality Standards
```
❌ BAD: "Hello, I am Polly. I will help you learn magic."
✅ GOOD: [i]"Welcome to magical academia, where they'll teach you to bend reality 
but somehow forgot to mention the tuition is paid in existential crises. Caw."[/i]

❌ BAD: Polly explains everything in detail
✅ GOOD: Polly offers cryptic hints that make sense in retrospect

❌ BAD: Constant commentary every paragraph
✅ GOOD: Strategic interjections at key magical moments
```

---

### 4. **ChoiceScript Technical Validator**
**Priority:** MEDIUM 🔧

#### Domain Expertise
- Advanced ChoiceScript syntax (beyond basic validation)
- Stat progression balancing across paths
- Achievement trigger optimization
- Dead-end path detection
- RandomTest/QuickTest interpretation

#### Tasks from Queue (Direct Impact)
- **Priority 4:** Run QuickTest on all scenes (30 min)
- **Priority 4:** Run RandomTest 1000 iterations (1 hour)
- **Priority 4:** Check unreachable endings (1 hour)
- **Priority 3:** Balance stat adjustments (2 hours)
- **Priority 3:** Implement stat-based scene variations (3 hours)

#### Why Needed
**Current Gap:** Existing `validate_choicescript.py` does basic syntax checking but doesn't:
- Analyze stat progression curves
- Detect "impossible" stat thresholds
- Optimize achievement unlock conditions
- Find subtle dead-ends in complex branching

**Unique Value:**
- Deep ChoiceScript expertise (understands advanced features)
- Can run official ChoiceScript test suites
- Interprets RandomTest failures intelligently
- Suggests stat rebalancing based on playtesting data

**Success Metrics:**
- All paths complete QuickTest without errors
- RandomTest finds all 14 endings within 1000 iterations
- No achievement is unreachable
- Stat thresholds feel fair (50% player success rate target)

#### Technical Validation Scope
```
SYNTAX VALIDATION:
- Proper *label usage
- Correct *goto/*goto_scene references
- Valid *if/*elseif/*else structures
- Balanced *choice blocks

GAMEPLAY VALIDATION:
- All endings reachable with reasonable stat builds
- No "trap" choices that make victory impossible
- Achievement triggers fire correctly
- Romance flags don't conflict

PERFORMANCE VALIDATION:
- No infinite loops
- Scene file sizes reasonable (<10KB each)
- Stat checks appropriately distributed
```

---

### 5. **Romance System Orchestrator**
**Priority:** MEDIUM 💕

#### Domain Expertise
- Polyamory relationship modeling
- Jealousy/conflict systems
- Romance progression pacing
- Character-specific romance paths (Aria, Zara, Alex)
- Relationship stat balancing

#### Tasks from Queue (Direct Impact)
- **Priority 2:** Add romance progression scenes (3 hours)
- **Priority 2:** Implement polyamory system (2 hours)
- Enhances character bond scenes with romantic options
- Creates romance-specific endings

#### Why Needed
**Current Gap:** The game supports:
- 3 romance options (Aria Ravencrest, Zara, Alexander)
- Polyamory system (multiple simultaneous relationships)
- Relationship stats (`aria_relationship`, `zara_relationship`, etc.)
- BUT: No specialized AI understanding polyamory narrative design

**Unique Value:**
- Understands ethical polyamory representation
- Can create jealousy systems that feel fair, not punishing
- Knows how to pace romance across 30+ scenes
- Designs romance choices that respect player agency

**Success Metrics:**
- Romance feels organic, not forced
- Polyamory paths are as fulfilling as monogamy
- Jealousy mechanics create drama without feeling unfair
- Each romance partner has distinct relationship arc

#### System Design Requirements
```
RELATIONSHIP TRACKING:
- Individual relationship stats (0-100)
- Romance flags (dating_aria, dating_zara, dating_alex)
- Jealousy triggers (when appropriate)
- Exclusive vs polyamory paths

SCENE INTEGRATION:
- Romantic moments in expedition scenes
- Private conversations in academy_life.txt
- Romance-specific dialogue variations
- Romance endings (paired with main endings)

POLYAMORY HANDLING:
- Multiple partners possible
- Transparent communication mechanics
- Consent-based relationship escalation
- Non-judgmental narrative framing
```

---

## 📋 IMPLEMENTATION PRIORITY

### Phase 1: Critical Path (Create Immediately)
1. **ChoiceScript Conversion Specialist** - Unblocks 72 hours of work
2. **Lore Consistency Guardian** - Prevents costly rewrites from canon breaks

### Phase 2: Quality Assurance (Create Next)
3. **ChoiceScript Technical Validator** - Ensures professional quality
4. **Polly's Voice Architect** - Differentiates game from competitors

### Phase 3: Enhanced Features (Create Later)
5. **Romance System Orchestrator** - Adds replay value

---

## 🛠️ TECHNICAL IMPLEMENTATION NOTES

### Agent Creation Process
Each custom agent should be defined in `.github/agents/` with:
- **Agent definition file:** `{agent-name}.agent.md`
- **System prompt:** Specialized expertise description
- **Tool access:** Which repository files/scripts it can use
- **Success criteria:** How to evaluate its work

### Integration with Existing Workers
Custom agents should:
- Read from `docs/AI_TASK_QUEUE.md` like other workers
- Commit to feature branches (`ai-{specialty}-work`)
- Update progress in task queue
- Flag uncertainties in `docs/AI_QUESTIONS.md`

### Resource Requirements
- **API Costs:** ~$50-100/month for Claude Sonnet (all 5 agents)
- **Compute:** GitHub Actions (free tier sufficient)
- **Storage:** Minimal (text-only output)

---

## 📊 EXPECTED IMPACT

### Without Custom Agents (Current Trajectory)
- **Timeline:** 3-4 months to complete all tasks
- **Quality:** Inconsistent lore, manual validation needed
- **Risk:** Canon violations, voice inconsistencies, syntax errors

### With Custom Agents (Recommended)
- **Timeline:** 1-2 months (50% reduction)
- **Quality:** Professional, lore-accurate, consistent voice
- **Risk:** Minimal (automated validation at every step)

### ROI Calculation
```
MANUAL WORK SAVED:
- Conversion: 72 hours → 27 hours (45 hours saved)
- Lore checking: 20 hours → 5 hours (15 hours saved)
- Polly polish: 3 hours → 1 hour (2 hours saved)
- Technical QA: 8 hours → 2 hours (6 hours saved)
- Romance design: 5 hours → 2 hours (3 hours saved)

TOTAL TIME SAVED: 71 hours
COST: ~$100/month in API calls
HUMAN HOURLY VALUE: $50-100/hour
NET BENEFIT: $3,550-$7,100 value for $100 investment
```

---

## 🎯 NEXT STEPS

### Immediate Actions
1. **Create ChoiceScript Conversion Specialist agent**
   - Define in `.github/agents/choicescript-converter.agent.md`
   - Train on existing conversion patterns (first_lesson.txt)
   - Test on one HTML scene before full deployment

2. **Create Lore Consistency Guardian agent**
   - Define in `.github/agents/lore-guardian.agent.md`
   - Index all lore documents for quick reference
   - Test by validating existing scenes for contradictions

3. **Document agent handoff protocols**
   - Update `docs/AI_AUTONOMOUS_WORKFLOW.md`
   - Create agent coordination rules
   - Define conflict resolution process

### Validation Milestones
- **Week 1:** Converter completes Singing Dunes (15 scenes)
- **Week 2:** Lore Guardian validates + Converter does Verdant Tithe
- **Week 3:** Converter does Rune Glacier + begin endings
- **Week 4:** All custom agents working in coordination

---

## 🔍 ALTERNATIVE CONSIDERED (Not Recommended)

### Why Not Just Scale Up Generic Workers?
**Problem:** Generic AI workers lack domain expertise:
- Scene Writer doesn't understand ChoiceScript vs HTML differences
- Content Polisher can't validate lore consistency
- Stat Balancer doesn't understand romance psychology
- Autonomous Worker can't specialize in Polly's voice

**Result:** More workers = more errors requiring human review

### Why Not Use Human Writers?
**Problem:** Specialized human writers for:
- ChoiceScript conversion: $25-50/hour × 72 hours = $1,800-$3,600
- Lore consistency: Requires reading all 8 lore docs repeatedly
- Technical QA: ChoiceScript expertise is rare and expensive

**Result:** Custom AI agents provide expert-level work at 1-5% of human cost

---

## 📚 SUPPORTING EVIDENCE

### From Task Queue Analysis
- **36 conversion tasks** explicitly listed in Priority 1
- **"Autonomous work" rated HIGH** for technical tasks
- **"Needs human judgment" rated LOW** for stat balance (can be automated)

### From Existing Code
- `scene_writer_agent.py` shows pattern for specialized agents
- `validate_choicescript.py` shows validation is already valued
- `content_polisher.py` proves focused agents work better than generalists

### From Repository Structure
- **Dual codebase** (HTML + ChoiceScript) requires conversion specialist
- **8+ lore documents** require consistency specialist
- **Complex stat system** (collaboration + 3 relationships) requires expert validation

---

## 🎊 CONCLUSION

The Avalon project has reached a critical juncture where **specialized domain expertise** is more valuable than general AI assistance. The recommended custom agents address specific, high-value bottlenecks:

1. **ChoiceScript Conversion Specialist** - Eliminates 72-hour conversion bottleneck
2. **Lore Consistency Guardian** - Prevents expensive rewrites from canon violations
3. **ChoiceScript Technical Validator** - Ensures professional-grade quality
4. **Polly's Voice Architect** - Creates unique player experience
5. **Romance System Orchestrator** - Adds replay value and player engagement

**Recommended Action:** Implement Phase 1 agents (Converter + Lore Guardian) immediately. These two agents alone will accelerate development by 60+ hours while improving quality.

---

**Prepared by Avalon Lore Steward**  
*"The spiral turns. Specialized expertise emerges. The game ships faster."*  
**Caw.** 🪶
