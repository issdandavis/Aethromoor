# HTML Browser Game - AI Agent Instructions

## 🎮 Purpose
This directory contains the **complete HTML browser version** of "Polly's Wingscroll: The First Thread" - a 40,000+ word choice-based interactive game playable directly in any web browser.

## 📁 Directory Structure

```
game/
├── index.html              → Main game file (ALL CONTENT - 40,000+ words)
├── game.js                 → Game engine and state management
├── style.css               → Visual styling
├── tracing.js              → Analytics and debugging
├── scenes/                 → Scene organization (if separated)
├── bootstrap_choicescript.sh → Utility for ChoiceScript conversion
├── sync_scenes.sh          → Scene synchronization utility
└── README.md               → Game overview and play instructions
```

## 🎯 Current Status

**Status**: ✅ COMPLETE - Production-ready
**Word Count**: 40,000+ words
**Scenes**: 30+ complete scenes
**Endings**: 14 unique endings
**Purpose**: Reference implementation for ChoiceScript conversion

## 🎮 Playing the Game

**To Test Your Changes:**
1. Open `index.html` in a web browser (double-click or drag to browser)
2. Play through affected scenes
3. Verify stat tracking in browser console
4. Test all choice branches
5. Confirm endings are reachable

**Browser Console Commands** (for testing):
```javascript
// View current game state
console.log(gameState);

// Check specific stats
console.log("Collaboration:", gameState.collaboration);
console.log("Aria:", gameState.aria_relationship);

// Jump to specific scene (for testing)
loadScene('scene_name');

// Reset game state
localStorage.clear();
location.reload();
```

## ✏️ Editing Guidelines

### ⚠️ CRITICAL: This is the Master Version

**IMPORTANT**: The HTML version is the **canonical source of truth** for story content. All ChoiceScript conversions should match this version exactly.

**When making changes:**
- ✅ HTML version changes should be deliberate and well-considered
- ✅ Always update corresponding ChoiceScript version to match
- ✅ Document changes in SCENE_PARITY_CHECKLIST.md
- ✅ Test thoroughly in browser before committing
- ⚠️ Coordinate with Conversion Engineer if changing story structure

### File Structure

**All content in `index.html`:**
```html
<!-- Scene: scene_name -->
<div class="scene" id="scene_name" style="display: none;">
    <h2>Scene Title</h2>
    
    <p>Scene description and dialogue...</p>
    
    <!-- Polly's commentary -->
    <div class="polly-commentary">
        <em>"Polly's witty observation..."</em>
    </div>
    
    <!-- Choices -->
    <div class="choices">
        <button class="choice-button" onclick="makeChoice('choice_id', {stat: 'collaboration', change: 5})">
            Choice text with clear consequence
        </button>
        <button class="choice-button" onclick="makeChoice('other_choice', {stat: 'collaboration', change: -3})">
            Alternative choice text
        </button>
    </div>
</div>
```

### JavaScript Game Engine (`game.js`)

**Core Functions:**
```javascript
// Load and display scene
function loadScene(sceneId)

// Process player choice
function makeChoice(choiceId, statChanges)

// Update game statistics
function updateStat(stat, value)

// Check stat thresholds
function checkCollaboration()

// Determine ending
function determineEnding()

// Save/load game state
function saveGame()
function loadGame()
```

## 🎨 HTML/CSS Styling Standards

### Visual Design Principles
- Clean, readable typography
- Clear visual hierarchy
- Mobile-responsive layout
- Accessible color contrast
- Consistent button styling
- Polly's commentary styled distinctly

### CSS Class Conventions
```css
.scene              /* Scene container */
.polly-commentary   /* Polly's dialogue */
.choice-button      /* Player choice buttons */
.stat-display       /* Stats visibility */
.ending-text        /* Ending sequence */
```

## 📊 Stat Tracking Implementation

### gameState Object Structure
```javascript
gameState = {
    // Core stats
    collaboration: 50,           // 0-100
    aria_relationship: 0,        // -10 to +10
    zara_relationship: 0,        // -10 to +10
    polly_relationship: 0,       // -10 to +10
    
    // Expedition completion
    completed_first_lesson: false,
    completed_singing_dunes: false,
    completed_verdant_tithe: false,
    completed_rune_glacier: false,
    
    // Path tracking
    chosen_expedition: null,     // "dunes" / "forest" / "glacier"
    dunes_path: null,            // "truth" / "control" / "rejection"
    forest_path: null,           // "dreamwillow" / "thoughtvine" / "heartwood"
    glacier_path: null,          // "control" / "harmony" / "mystery"
    
    // Scene progression
    current_scene: "polly_intro",
    scenes_visited: []
};
```

### Stat Change Patterns
```javascript
// Major positive choice (collaboration approach)
makeChoice('collaborate', {stat: 'collaboration', change: 5});

// Major negative choice (control approach)
makeChoice('dominate', {stat: 'collaboration', change: -5});

// Relationship impact
makeChoice('praise_aria', {stat: 'aria_relationship', change: 2});

// Multiple stat changes
makeChoice('humble_approach', {
    stats: [
        {stat: 'collaboration', change: 3},
        {stat: 'polly_relationship', change: 1}
    ]
});
```

## 🎭 Scene Writing Standards

### Scene Structure Template
```html
<div class="scene" id="scene_name" style="display: none;">
    <!-- 1. Scene Header -->
    <h2>Scene Title</h2>
    
    <!-- 2. Setting Description -->
    <p>Vivid description of location, atmosphere, sensory details...</p>
    
    <!-- 3. NPC Introduction (if applicable) -->
    <p>Character appearance, personality indicators, initial dialogue...</p>
    
    <!-- 4. Challenge/Conflict -->
    <p>Present the magical or narrative problem...</p>
    
    <!-- 5. Polly's Commentary -->
    <div class="polly-commentary">
        <em>"Polly's witty or wise observation about the situation..."</em>
    </div>
    
    <!-- 6. Player Choice -->
    <div class="choices">
        <button class="choice-button" onclick="handleChoiceA()">
            Collaborative approach with clear indication
        </button>
        <button class="choice-button" onclick="handleChoiceB()">
            Control approach with clear indication
        </button>
        <button class="choice-button" onclick="handleChoiceC()">
            Alternative creative solution
        </button>
    </div>
</div>
```

### Dialogue Formatting
```html
<!-- Standard dialogue -->
<p>"Spoken words," character said.</p>

<!-- Polly's special commentary -->
<div class="polly-commentary">
    <em>"Polly always gets italics and special styling."</em>
</div>

<!-- Internal thoughts (player character) -->
<p><em>Internal monologue in italics...</em></p>

<!-- Action beats -->
<p>Character performed an action, revealing emotion or intent.</p>
```

## 🎯 Expedition Scenes (Reference for ChoiceScript)

### Singing Dunes Structure
1. **Introduction**: Desert arrival, Kael introduction
2. **Truth Test 1**: Initial oath-magic challenge
3. **Polly Commentary**: On truth-telling and magic
4. **Truth Test 2**: Deeper truth requirement
5. **Critical Choice**: Truth vs. Control vs. Rejection
6. **Consequence**: Immediate magical response
7. **Final Challenge**: Desert's ultimate test
8. **Resolution**: Based on accumulated choices
9. **Return**: Debrief with Izack
10. **Ending Route**: Set flags for ending determination

### Verdant Tithe Structure
1. **Introduction**: Forest entry, sentient plant awareness
2. **Plant Encounter**: Thoughtvine, Dreamwillow, or Heartwood
3. **Emotional Resonance**: Forest reading player's intent
4. **Polly Commentary**: On nature and consciousness
5. **Partnership Test**: Forest offers collaboration
6. **Critical Choice**: Which plant ally to pursue
7. **Consequence**: Plant-specific magical outcome
8. **Deepening Bond**: Relationship with chosen plant entity
9. **Resolution**: Forest acceptance or rejection
10. **Return**: Integration of forest wisdom
11. **Ending Route**: Set flags for ending determination

### Rune Glacier Structure
1. **Introduction**: Ice realm entry, living ice explanation
2. **Memory Crystal**: Discovering frozen spell library
3. **Aria's Teaching**: Precision vs. Partnership
4. **Polly Commentary**: On ice and memory
5. **Ice Awakening**: Glacier consciousness emerges
6. **Critical Choice**: Control vs. Harmony vs. Mystery
7. **Consequence**: Ice responds to approach
8. **Rune Challenge**: Testing magical understanding
9. **Resolution**: Glacier's judgment
10. **Return**: Carrying ice wisdom
11. **Ending Route**: Set flags for ending determination

## ✅ HTML Version Maintenance Checklist

When modifying the HTML version:

- [ ] Change maintains canon consistency (check `../lore/`)
- [ ] Character dialogue matches established personality
- [ ] Stat impacts are balanced with other scenes
- [ ] All choice branches are tested in browser
- [ ] Polly's commentary maintains her voice
- [ ] Scene flow is natural and well-paced
- [ ] Stat changes are logged in STATS_MATRIX.md
- [ ] Corresponding ChoiceScript scene needs updating
- [ ] SCENE_PARITY_CHECKLIST.md updated
- [ ] Game is playable from start to affected scene
- [ ] Changes don't break existing save states (if possible)

## 🔍 Testing Workflow

### Browser Testing Steps:
1. **Clear Cache**: Ctrl+Shift+R (or Cmd+Shift+R on Mac)
2. **Open Console**: F12 or right-click → Inspect → Console
3. **Start Fresh**: Clear localStorage, reload page
4. **Play Through**: Test from beginning or use scene jump
5. **Check Stats**: Verify stat changes in console
6. **Test Branches**: Try all major choice variations
7. **Verify Endings**: Confirm ending logic still works
8. **Cross-browser**: Test in Chrome, Firefox, Safari (if available)

### Common Testing Commands:
```javascript
// View current scene
console.log(gameState.current_scene);

// Check if ending is reachable
if (gameState.collaboration >= 80 && gameState.completed_glacier) {
    console.log("Collaborative Master ending reachable");
}

// Test stat threshold
gameState.collaboration = 85; // Temporarily set for testing
determineEnding(); // See which ending this triggers
```

## 🚨 Common HTML Pitfalls

**Avoid These Mistakes:**
- ❌ Breaking existing stat logic when adding choices
- ❌ Creating scenes without `display: none;` (they'll all show at once)
- ❌ Forgetting to update `scenes_visited` tracking
- ❌ Using unclear choice button text (be explicit about consequences)
- ❌ Changing Polly's established personality
- ❌ Adding content that breaks mobile responsiveness
- ❌ Modifying core game.js without thorough testing
- ❌ Creating orphan scenes (unreachable from game flow)

## 🔗 Integration Points

### ChoiceScript Conversion Reference
- HTML scenes are the **source material** for ChoiceScript conversion
- Conversion Engineer should match HTML logic exactly
- Any HTML changes require ChoiceScript updates
- Consult `../choicescript_game/AGENTS.md` for conversion patterns

### Lore Consistency
- All narrative content must match `../lore/` canon
- Character dialogue references `../lore/IZACK_MASTER_CHRONICLE_UPDATED.txt`
- Magic system follows established dimensional theory
- Timeline events consistent across all documents

## 📚 Reference Materials

**Within This Repository:**
- Character canon: `../lore/IZACK_MASTER_CHRONICLE_UPDATED.txt`
- Worldbuilding: `../lore/` directory
- Project roadmap: `../docs/PROJECT_ROADMAP.md`
- ChoiceScript version: `../choicescript_game/`

**External Resources:**
- HTML5 Semantic Elements reference
- JavaScript ES6 standards
- CSS Grid/Flexbox for responsive design
- Web Accessibility Guidelines (WCAG)

## 🎊 Quality Standards

Your HTML changes meet quality standards if:
- ✅ Game is fully playable in major browsers
- ✅ All choices have clear consequences
- ✅ Stat tracking is accurate and logged
- ✅ Story maintains canon consistency
- ✅ Character voices are authentic
- ✅ Mobile-responsive and accessible
- ✅ No broken links or orphan scenes
- ✅ ChoiceScript parity is maintained
- ✅ Code is clean and commented
- ✅ Tested from start to affected endings

---

*This is the master version. Treat it with respect, test thoroughly, and maintain its integrity as the canonical source of truth.*
