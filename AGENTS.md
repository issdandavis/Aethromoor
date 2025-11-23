# The Avalon Codex - AI Agent Instructions

## 🎯 Project Mission
Create "Polly's Wingscroll: The First Thread" - a publishable choice-based interactive game set in the Spiral of Pollyoneth universe, featuring a dual-format release (HTML browser version + ChoiceScript mobile app).

## 📁 Repository Structure

```
Avalon/
├── game/                  → HTML browser game (COMPLETE - 40,000+ words)
├── choicescript_game/     → Professional ChoiceScript version (IN PROGRESS)
├── lore/                  → Worldbuilding canon and character chronicles
├── writing_drafts/        → Novel manuscripts and narrative content
├── docs/                  → Roadmaps, guides, and project documentation
└── config/                → Automation and workflow configurations
```

## 🎭 Multi-AI Collaboration Roles

When multiple AI assistants work on this project, use these specialized roles:

### **Lore Curator** (Best: Claude, GPT-4 with creative focus)
- Validates narrative consistency against established canon
- Cross-references `lore/IZACK_MASTER_CHRONICLE_UPDATED.txt` and worldbuilding docs
- Flags timeline conflicts or magic system contradictions
- Ensures character behavior matches established personality traits

### **Conversion Engineer** (Best: GitHub Copilot, Continue)
- Translates HTML game content → ChoiceScript format
- Preserves choice logic and branching structure
- Implements stat tracking accurately
- Maintains scene parity between versions

### **Structural Reviewer** (Best: Cody, Codeium)
- Verifies scene parity (same endings, same branching count)
- Validates stat progression consistency
- Checks technical implementation quality
- Ensures proper file organization

### **Quality Balancer** (Any AI)
- Equalizes Collaboration stat difficulty across expeditions
- Validates choice consequences are meaningful
- Ensures all paths are equally rewarding
- Balances gameplay difficulty curves

### **Automation Planner** (Any AI)
- Updates Zapier workflow documentation
- Maintains automation guides
- Documents new triggers or integrations
- Tracks analytics requirements

## 📋 Shared Context Artifacts

All AI agents should maintain these tracking documents:

### **STATUS_CONTEXT.md**
Weekly snapshot of current work:
- Scene currently being converted
- Pending lore updates
- Known issues or blockers

### **SCENE_PARITY_CHECKLIST.md**
HTML vs ChoiceScript scene tracking:
- List each scene with status: Missing / Draft / Verified
- Track word count parity
- Note ending references

### **STATS_MATRIX.md**
Choice impact tracking:
- Source file + choice description
- Stat deltas (Collaboration +5, Aria relationship +1, etc.)
- Required thresholds for branches

## 🔄 Collaboration Workflow

1. **Lore Curator** approves scene's canon integrity (HTML source)
2. **Conversion Engineer** drafts ChoiceScript scene (no stat tuning)
3. **Structural Reviewer** verifies branching & ending alignment
4. **Quality Balancer** adjusts stat thresholds & gameplay balance
5. **Automation Planner** notes new analytics triggers

## 🎨 Hand-off Conventions

### Comment Prefixes (for draft files only):
```
// TODO:[LORE]: Check if Aria's dialogue matches her established personality
// TODO:[CONVERT]: Add stat tracking for this choice branch
// TODO:[STRUCT]: Verify this matches HTML scene ending count
// TODO:[BALANCE]: This choice seems too easy to trigger
// TODO:[AUTO]: Track this choice for analytics dashboard
```

### Commit Message Prefixes:
```
Lore: Updated character timeline for consistency
Convert: Translated Singing Dunes to ChoiceScript
Struct: Fixed branching mismatch in first_lesson.txt
Balance: Adjusted Collaboration thresholds in glacier expedition
Auto: Added Zapier trigger for new expedition completion
```

## 🎮 Core Lore Rules (NEVER VIOLATE)

### The Spiral of Pollyoneth Universe
- **Central Character**: Izack Thorne (founder of Avalon Academy)
- **Key Companion**: Polly (dimensional entity, sarcastic mentor)
- **Magic Philosophy**: Collaboration > Domination
- **Timeline**: Four-generation epic spanning 150+ years

### Character Personalities (IMMUTABLE)
- **Izack**: Humble, collaborative, innovative, values partnerships
- **Aria Ravencrest**: Precision-focused, boundary magic expert, patient teacher
- **Zara Frostborn**: Experimental, ice magic specialist, encouraging
- **Polly**: Sarcastic, wise, playful, fourth-wall-aware

### Magic System Principles
- **Collaborative Casting**: Multiple mages working in harmony
- **Dimensional Theory**: Magic draws from parallel dimensions
- **Realm Variety**: Each location has unique magical properties
- **Truth Magic**: Oath-binding desert magic (Singing Dunes)
- **Living Forests**: Sentient plant consciousness (Verdant Tithe)
- **Memory Ice**: Crystallized spell libraries (Rune Glacier)

## 📊 Quality Standards

### Technical Requirements
- **Word Count**: 40,000+ words total across all content
- **Endings**: 14 unique endings with meaningful variations
- **Stat Tracking**: Accurate Collaboration + relationship tracking
- **Scene Parity**: HTML and ChoiceScript tell identical stories

### Writing Standards
- **Tone**: Accessible YA fantasy with depth for adults
- **Polly's Voice**: Witty, conversational, occasionally breaks fourth wall
- **Choice Quality**: Every choice should feel meaningful
- **Consequence Clarity**: Players should understand choice impacts

## 🚀 Current Development Phase

**Phase 2: Complete ChoiceScript Game**
- Priority: Converting expeditions (Singing Dunes → Verdant Tithe → Rune Glacier)
- Status: See `docs/PROJECT_ROADMAP.md` for detailed progress
- Next Milestone: Singing Dunes expedition complete

## 🔍 Before Making Changes

### Always Check:
1. **Current Phase**: Review `docs/PROJECT_ROADMAP.md`
2. **File Locations**: Consult `FILE_LOCATIONS.txt`
3. **Lore Canon**: Cross-reference `lore/` directory
4. **Existing Work**: Check both `game/` and `choicescript_game/` versions
5. **Shared Artifacts**: Update STATUS_CONTEXT.md, SCENE_PARITY_CHECKLIST.md, STATS_MATRIX.md

### Quick Validation Tests:
- Does this change maintain story parity between HTML & ChoiceScript?
- Are character personalities consistent with established canon?
- Do stat changes follow existing patterns?
- Is the magic system logic consistent?
- Would this confuse players familiar with the HTML version?

## 📝 Quick Reference Links

- **Play the Game**: `game/index.html` (double-click to test)
- **Project Overview**: `START_HERE.md`
- **Development Status**: `docs/PROJECT_ROADMAP.md`
- **Automation Guide**: `docs/AUTOMATION_GUIDE.md`
- **Character Canon**: `lore/IZACK_MASTER_CHRONICLE_UPDATED.txt`
- **ChoiceScript Docs**: See `choicescript_game/README.md`

## 🎯 Success Criteria for AI Contributions

Your work is successful if:
- ✅ Story canon remains consistent with established lore
- ✅ HTML and ChoiceScript versions maintain parity
- ✅ Character personalities match their established traits
- ✅ Stat tracking is accurate and meaningful
- ✅ All 14 endings remain accessible through proper choices
- ✅ Documentation is updated to reflect changes
- ✅ Code follows existing naming and structural conventions
- ✅ Changes are tested in context (play the affected scenes)

## 🤝 Communication Protocol

When passing work between AI agents:
1. Update relevant tracking document (STATUS_CONTEXT, SCENE_PARITY, or STATS_MATRIX)
2. Use appropriate commit message prefix (Lore:, Convert:, Struct:, Balance:, Auto:)
3. Document any assumptions or uncertainties in TODO comments
4. Flag blocking issues clearly for next agent
5. Reference source files explicitly (path + line numbers when relevant)

## ⚠️ Common Pitfalls to Avoid

- ❌ Creating character traits that contradict established chronicles
- ❌ Adding magic system rules inconsistent with dimensional theory
- ❌ Breaking parity between HTML and ChoiceScript versions
- ❌ Making Collaboration stat too easy/hard compared to other expeditions
- ❌ Changing Polly's personality or tone
- ❌ Adding endings beyond the established 14
- ❌ Modifying timeline events without checking character ages/relationships
- ❌ Creating choices without meaningful stat consequences

## 🎊 When You're Unsure

If you're uncertain about:
- **Lore details**: Check `lore/` directory, especially character chronicles
- **Game structure**: Play `game/index.html` to see it in action
- **Development phase**: Review `docs/PROJECT_ROADMAP.md`
- **File locations**: Consult `FILE_LOCATIONS.txt`
- **Technical patterns**: Look at existing similar files in same directory

**When in doubt, ask rather than guess!**

---

*"The spiral continues. Every choice writes your story."*
— Polly's signature phrase
