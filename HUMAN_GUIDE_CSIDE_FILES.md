# 🎮 HUMAN GUIDE - CSIDE Game Files

**PURPOSE:** These are the ACTUAL GAME FILES you drag and drop into CSIDE to play/test the game!

**LAST UPDATED:** 2025-11-23

---

## 📁 WHERE ARE THE GAME FILES?

### Main Folder: `choicescript_game/`

This entire folder contains YOUR GAME that you'll use in CSIDE.

```
choicescript_game/          ← DRAG THIS WHOLE FOLDER TO CSIDE
├── startup.txt             ← 🎮 HUMAN: Main game file (loads first)
├── choicescript_stats.txt  ← 🎮 HUMAN: Stats screen
├── scenes/                 ← 🎮 HUMAN: All your game scenes
│   ├── arrival.txt         ← 🎮 HUMAN: Arrival scene
│   ├── dorm_room.txt       ← 🎮 HUMAN: Dorm customization
│   ├── first_lesson.txt    ← 🎮 HUMAN: First lesson scene
│   ├── academy_life.txt    ← 🎮 HUMAN: Academy life scene
│   ├── expedition_prep.txt ← 🎮 HUMAN: Expedition prep
│   ├── singing_dunes.txt   ← 🎮 HUMAN: Singing Dunes (AI will create)
│   ├── verdant_tithe.txt   ← 🎮 HUMAN: Verdant Tithe (AI will create)
│   ├── rune_glacier.txt    ← 🎮 HUMAN: Rune Glacier (AI will create)
│   ├── character_bonds.txt ← 🎮 HUMAN: Character relationships
│   ├── final_trial.txt     ← 🎮 HUMAN: Final trial
│   └── endings.txt         ← 🎮 HUMAN: All 14 endings (AI will create)
└── web/                    ← DON'T TOUCH: CSIDE generates this
```

---

## 🎯 HOW TO USE WITH CSIDE

### Step 1: Open CSIDE
Go to: https://choicescriptide.github.io/

### Step 2: Create New Project
Click "New Project" or "Import Project"

### Step 3: Drag and Drop
**Drag the ENTIRE `choicescript_game` folder** into CSIDE

OR

**Manually add files:**
1. Upload `startup.txt` first
2. Upload `choicescript_stats.txt`
3. Upload all files from `scenes/` folder

### Step 4: Test Your Game!
Click "Run" or "Test" in CSIDE to play

---

## 🎮 GAME FILES YOU'LL TOUCH

### Core Files (Always Need These)

**`startup.txt`** - 🎮 HUMAN EDITABLE
- First file that runs
- Sets up character stats
- Has the introduction
- **When to edit:** Change starting stats, intro text, character creation

**`choicescript_stats.txt`** - 🎮 HUMAN EDITABLE  
- Shows player stats screen
- Displays relationships and collaboration score
- **When to edit:** Add new stats or change how stats display

### Scene Files (These Are Your Story)

All files in `scenes/` folder:

**`arrival.txt`** - 🎮 HUMAN EDITABLE
- How player arrives at academy
- **When to edit:** Change arrival dialogue or choices

**`dorm_room.txt`** - 🎮 HUMAN EDITABLE
- Dorm room customization
- **When to edit:** Add more room options or descriptions

**`first_lesson.txt`** - 🎮 HUMAN EDITABLE
- First magic lesson
- **When to edit:** Adjust difficulty or add dialogue

**`academy_life.txt`** - 🎮 HUMAN EDITABLE
- Daily life at academy
- **When to edit:** Add more academy activities

**`expedition_prep.txt`** - 🎮 HUMAN EDITABLE
- Choosing expedition
- **When to edit:** Change expedition descriptions

**`singing_dunes.txt`** - 🎮 HUMAN EDITABLE (AI will create)
- Desert expedition
- **When to edit:** After AI creates it, add polish

**`verdant_tithe.txt`** - 🎮 HUMAN EDITABLE (AI will create)
- Forest expedition  
- **When to edit:** After AI creates it, add polish

**`rune_glacier.txt`** - 🎮 HUMAN EDITABLE (AI will create)
- Glacier expedition
- **When to edit:** After AI creates it, add polish

**`character_bonds.txt`** - 🎮 HUMAN EDITABLE
- Build relationships
- **When to edit:** Add more character interactions

**`final_trial.txt`** - 🎮 HUMAN EDITABLE
- Final challenge
- **When to edit:** Adjust difficulty

**`endings.txt`** - 🎮 HUMAN EDITABLE (AI will create)
- All 14 endings
- **When to edit:** Polish ending text after AI creates them

---

## ❌ FILES YOU DON'T TOUCH

### Documentation Files (For Reference Only)

These live in the main repository, NOT in CSIDE:

**`STATUS_CONTEXT.md`** - 🤖 AI ONLY
- AI communication file
- **You:** Just read to see what AIs are doing

**`AI_TASK_QUEUE.md`** - 🤖 AI ONLY (You assign tasks)
- AI task list
- **You:** Assign tasks to AIs, then let them update it

**`SCENE_PARITY_CHECKLIST.md`** - 🤖 AI ONLY
- Tracks AI progress
- **You:** Read to see completion status

**`STATS_MATRIX.md`** - 🤖 AI ONLY
- Technical stat tracking
- **You:** Read if curious about game balance

**`docs/` folder** - 📖 REFERENCE ONLY
- All guides and documentation
- **You:** Read these for help, don't edit

**`lore/` folder** - 📖 REFERENCE FOR AIs
- Story background
- **You:** AIs read these, you can too

**`game/` folder** - 🌐 HTML VERSION
- The browser-based game
- **You:** Can play this, but CSIDE uses `choicescript_game/`

**`scripts/` folder** - 🔧 AUTOMATION
- Auto-commit scripts
- **You:** Run these, don't edit unless you know coding

---

## 📝 QUICK REFERENCE TABLE

| File/Folder | Touch It? | Use in CSIDE? | Purpose |
|-------------|-----------|---------------|---------|
| `choicescript_game/startup.txt` | ✅ YES | ✅ YES | Main game file |
| `choicescript_game/choicescript_stats.txt` | ✅ YES | ✅ YES | Stats display |
| `choicescript_game/scenes/*.txt` | ✅ YES | ✅ YES | All game scenes |
| `STATUS_CONTEXT.md` | 👀 READ ONLY | ❌ NO | AI communication |
| `AI_TASK_QUEUE.md` | 👀 READ ONLY | ❌ NO | Task tracking |
| `docs/` | 👀 READ ONLY | ❌ NO | Documentation |
| `lore/` | 👀 READ ONLY | ❌ NO | Story reference |
| `game/` (HTML version) | 🎮 PLAY ONLY | ❌ NO | Browser game |
| `scripts/` | 🔧 RUN ONLY | ❌ NO | Automation |

---

## 🎯 TYPICAL WORKFLOW

### When AI Finishes a Scene:

1. **AI commits** their work (e.g., `singing_dunes.txt`)
2. **You pull** latest from GitHub:
   ```bash
   cd /path/to/Avalon
   git pull
   ```
3. **You open** CSIDE
4. **You drag** the updated file into your CSIDE project
5. **You test** the scene in CSIDE
6. **You polish** if needed (fix typos, adjust dialogue)
7. **You save** in CSIDE
8. **You commit** your polish:
   ```bash
   ./scripts/auto-commit.sh -m "Human: Polished Singing Dunes dialogue"
   ```

### When You Want to Edit Something:

1. **Open file** in CSIDE (or any text editor)
2. **Make changes** to the `.txt` file
3. **Test** in CSIDE to make sure it works
4. **Save** the file
5. **Commit** your changes:
   ```bash
   ./scripts/auto-commit.sh -m "Human: Updated dorm room options"
   ```

---

## 💡 TIPS FOR HUMANS

### Editing ChoiceScript Files

**Safe Edits:**
- ✅ Changing dialogue text
- ✅ Adding new choices
- ✅ Adjusting stat amounts
- ✅ Fixing typos
- ✅ Adding Polly's sarcastic comments

**Be Careful With:**
- ⚠️ Changing `*goto` destinations (can break game flow)
- ⚠️ Modifying stat names (must match everywhere)
- ⚠️ Deleting entire sections (might break later scenes)

**Learn ChoiceScript:**
- Tutorial: https://www.choiceofgames.com/make-your-own-games/choicescript-intro/
- Quick reference: https://choicescriptdev.fandom.com/wiki/ChoiceScript_Wiki

### Testing Your Changes

**Always test in CSIDE after editing:**
1. Click "Run" in CSIDE
2. Play through your changes
3. Make sure choices work
4. Check stats update correctly
5. Verify no error messages

### When to Ask AI for Help

**Ask AI to:**
- Create entire new scenes
- Convert HTML to ChoiceScript
- Balance stat thresholds
- Write complex branching logic

**Do yourself:**
- Quick text edits
- Typo fixes
- Minor dialogue tweaks
- Adding flavor text

---

## 🆘 TROUBLESHOOTING

### "CSIDE shows error when I test"

**Check:**
1. Did you close all `*if` statements with matching structure?
2. Are all `*goto` labels spelled correctly?
3. Did you save the file?
4. Is the file in the right folder?

**Fix:** Read the error message - it usually tells you the line number

### "Changes don't show up in game"

**Solutions:**
1. Save the file in CSIDE
2. Refresh the test window
3. Try "Quick Test" to check for errors

### "I broke something!"

**Don't panic:**
1. Check `git log` to see your recent changes
2. Use `git diff` to see what changed
3. Revert if needed: `git checkout -- filename.txt`
4. Or ask an AI to fix it

---

## 📱 MOBILE EDITING (OPTIONAL)

If you want to edit on your phone:

**iOS:**
- Working Copy app (git client)
- Textastic (text editor with ChoiceScript syntax)

**Android:**  
- MGit (git client)
- QuickEdit (text editor)

Then sync back to GitHub, AIs can see your changes!

---

## 🎮 FILE NAMING CONVENTION

### For Humans (You):
- Game scene files: `scene_name.txt` (all lowercase, underscores)
- Example: `singing_dunes.txt`, `character_bonds.txt`

### For AIs:
- Status files: `ALL_CAPS_WITH_UNDERSCORES.md`
- Example: `STATUS_CONTEXT.md`, `AI_TASK_QUEUE.md`

**This way you can instantly tell** which files are for the game (you) vs coordination (AIs)!

---

## ✨ SUMMARY

### Files YOU Touch (Game Files):
```
choicescript_game/
├── startup.txt              🎮 HUMAN
├── choicescript_stats.txt   🎮 HUMAN
└── scenes/
    └── *.txt                🎮 HUMAN (all scene files)
```

### Files AIs Touch (Coordination Files):
```
STATUS_CONTEXT.md            🤖 AI
AI_TASK_QUEUE.md            🤖 AI
SCENE_PARITY_CHECKLIST.md   🤖 AI
STATS_MATRIX.md             🤖 AI
```

### Files Nobody Touches (Generated/Reference):
```
docs/           📖 Read only
lore/           📖 Read only  
game/           🌐 HTML version (separate)
scripts/        🔧 Run only
```

---

**REMEMBER:** 
- 🎮 = You edit these in CSIDE
- 🤖 = AIs update these automatically
- 📖 = Just read these for reference
- 🔧 = Run these scripts when needed

**EASIEST WAY:** Just work with files in the `choicescript_game/` folder. Everything else is automated!

---

*Now you know exactly which files to drag into CSIDE!* 🎮✨
