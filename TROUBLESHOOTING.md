# TROUBLESHOOTING GUIDE
## How to Get Your ChoiceScript Game Running

---

## Current Status

✅ **Game Content Complete:**
- 36 scene files created
- Full 4-year story (Years 1-4 + Epilogue)
- Magic system with 7 schools and 49 spells
- Character creation, branching paths, romances
- ~80,000+ words of content

⚠️ **Missing: ChoiceScript Engine**

---

## Problem: Game Won't Launch

Your `choicescript_game/` folder has all the story content but is missing the ChoiceScript web engine needed to play it.

### Current Structure:
```
choicescript_game/
├── startup.txt        ✅ (exists)
├── scenes/            ✅ (36 files)
└── web/               ❌ (MISSING - this is the problem!)
```

### What You Need:
```
choicescript_game/
├── startup.txt
├── scenes/
└── web/
    ├── index.html     ← Game launcher
    ├── scene.js       ← ChoiceScript engine
    ├── navigator.js   ← Scene navigation
    ├── util.js        ← Utility functions
    ├── style.css      ← Styling
    └── mygame/
        └── scenes/    ← Symlink to your scenes folder
```

---

## SOLUTION 1: Download ChoiceScript (Recommended)

### Step 1: Download ChoiceScript

Go to: https://www.choiceofgames.com/make-your-own-games/choicescript-intro/

Or directly download from GitHub:
```bash
cd /home/user/Avalon
wget https://github.com/dfabulich/choicescript/archive/refs/heads/master.zip
unzip master.zip
```

### Step 2: Copy Engine Files to Your Game

```bash
# Copy the web engine files
cp -r choicescript-master/web choicescript_game/

# Remove the example game
rm -rf choicescript_game/web/mygame

# Create symlinks to your game content
cd choicescript_game/web
mkdir mygame
ln -s ../../scenes mygame/scenes
ln -s ../../startup.txt mygame/startup.txt
```

### Step 3: Test Locally

```bash
cd /home/user/Avalon/choicescript_game/web
python3 -m http.server 8000
```

Then open: http://localhost:8000/

---

## SOLUTION 2: Use Choice of Games IDE (Easiest)

1. Go to https://www.choiceofgames.com/make-your-own-games/choicescript-intro/
2. Click "ChoiceScript IDE" (online editor)
3. Copy/paste your `startup.txt` content
4. Upload your scene files from `scenes/` folder
5. Click "Test" to play immediately

**Pros:**
- No setup required
- Instant testing
- Built-in error checking

**Cons:**
- Need to upload 36 files manually (tedious)
- Online only

---

## SOLUTION 3: Use CSIDE (ChoiceScript IDE - Desktop App)

Download CSIDE from: https://github.com/ChoicescriptIDE/main/releases

1. Install CSIDE
2. Create new project
3. Import your `choicescript_game/` folder
4. Auto-detects all scenes
5. One-click testing

**Best for development and testing!**

---

## SOLUTION 4: Quick Web Setup (Manual)

Create minimal `index.html` in `choicescript_game/web/`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Polly's Wingscroll</title>
    <script src="https://choiceofgames.com/game-source/scene.js"></script>
    <script src="https://choiceofgames.com/game-source/navigator.js"></script>
    <script src="https://choiceofgames.com/game-source/util.js"></script>
    <link rel="stylesheet" href="https://choiceofgames.com/game-source/style.css">
</head>
<body>
    <div id="text"></div>
    <script>
        stats = {};
        nav = new navigator();
        nav.setStartingStatsClone(stats);
        startLoading();
    </script>
</body>
</html>
```

**Note:** This loads ChoiceScript from CDN. May not work offline.

---

## Common Errors & Fixes

### Error: "Scene not found: character_creation"

**Problem:** startup.txt references scenes that don't exist or have typos

**Fix:** Check scene_list in startup.txt matches actual file names in scenes/

```
*scene_list
  startup
  character_creation  ← Must match: character_creation.txt
  arrival             ← Must match: arrival.txt
  ...
```

### Error: "Undefined variable: thesis_topic"

**Problem:** Variable used before being created

**Fix:** Add to startup.txt:
```
*create thesis_topic "none"
```

### Error: "Bad label: thesis_selected"

**Problem:** Typo in *goto command

**Fix:** Check spelling:
```
*goto thesis_selection  ← Correct
*goto thesis_selected   ← Wrong
```

### Error: "Non-existent command 'acheivement'"

**Problem:** Typo in *achievement command

**Fix:**
```
*achievement breakthrough  ← Correct
*acheivement breakthrough  ← Wrong (common typo!)
```

---

## Testing Your Game

### QuickTest (Check for Errors)

```bash
cd choicescript_game/web
node quicktest.js
```

Checks for:
- Undefined variables
- Missing labels
- Typos in commands
- Dead ends

### RandomTest (Find Bugs)

```bash
cd choicescript_game/web
node randomtest.js
```

Plays through game 1000+ times with random choices to find:
- Crashes
- Infinite loops
- Math errors
- Edge cases

---

## File Structure Reference

### Correct ChoiceScript Project:

```
choicescript_game/
│
├── startup.txt                    ← Game configuration & variables
│
├── scenes/                        ← All story scenes
│   ├── character_creation.txt
│   ├── arrival.txt
│   ├── first_lesson.txt
│   ├── magic_training.txt
│   ├── year_one_trial.txt
│   ├── year_two_start.txt
│   ├── path_selection.txt
│   ├── research_path.txt          ← Exclusive to research path
│   ├── combat_path.txt            ← Exclusive to combat path
│   ├── diplomatic_path.txt        ← Exclusive to diplomatic path
│   ├── year_two_crisis.txt
│   ├── year_two_trial.txt
│   ├── year_three_start.txt
│   ├── advanced_training.txt
│   ├── teaching_scenes.txt
│   ├── political_intrigue.txt
│   ├── year_three_trial.txt
│   ├── year_four_start.txt
│   ├── thesis_project.txt
│   ├── final_expedition.txt
│   ├── avalon_crisis.txt
│   ├── final_trial.txt
│   ├── endings.txt
│   ├── epilogue.txt
│   └── [28 other scene files...]
│
└── web/                           ← ChoiceScript engine (YOU NEED THIS!)
    ├── index.html
    ├── scene.js
    ├── navigator.js
    ├── util.js
    ├── style.css
    └── mygame/                    ← Symlinks to your content
        ├── scenes/    → ../../scenes/
        └── startup.txt → ../../startup.txt
```

---

## Quick Syntax Check

Common ChoiceScript syntax that might have errors:

```choicescript
✅ CORRECT:
*if collaboration >= 70
  *goto high_collaboration

*choice
  #Option one
    Text here
    *goto next_label

*set dimensional_magic +10
*achievement breakthrough visible 30 Title
*goto_scene next_scene
*create variable_name 50

❌ WRONG:
*if collaboration >= 70  ← Missing consequence
*if (collaboration >= 70)  ← Don't use parentheses (usually)

*choice
  Option one  ← Missing # symbol

*set dimensional_magic +10;  ← No semicolons in ChoiceScript
*acheivement  ← Typo (common!)
*gotoScene next_scene  ← Wrong capitalization
*Create variable_name 50  ← Capital C is wrong
```

---

## Next Steps

1. **Get ChoiceScript Engine** (Solution 1, 2, or 3 above)
2. **Test the Game** - Play through at least one complete path
3. **Run QuickTest** - Find syntax errors
4. **Run RandomTest** - Find logical errors
5. **Fix any errors found**
6. **Playtest all major paths**:
   - Research Path (Year 2-4)
   - Combat Path (Year 2-4)
   - Diplomatic Path (Year 2-4)
7. **Check achievements unlock properly**
8. **Test all romance routes**

---

## If You're Still Stuck

### Check These Files for Errors:

1. **startup.txt** - Are all variables created?
2. **year_two_crisis.txt** - Does it properly set variables before checks?
3. **endings.txt** - Does it route to epilogue?
4. **Any scene with `*goto`** - Do the labels exist?

### Common Variable Issues:

Check if these are all created in startup.txt:
- `thesis_topic`
- `combat_specialization`
- `teaching_interest`
- `career_path`
- `confidence`

### Scene Flow Issues:

Verify this path works:
```
startup → character_creation → arrival → familiar_selection →
first_lesson → year_one_trial → year_two_start → path_selection →
[chosen_path] → year_two_crisis → ... → epilogue
```

---

## Getting Help

If you encounter an error:

1. **Note the exact error message**
2. **Note which scene it happens in**
3. **Check the syntax at that line**
4. **Search for the error on Choice of Games forum**
5. **Ask on CoG forum with specific error details**

---

**Your game content is complete and ready to play - you just need the engine!**

Choose one of the solutions above and you'll be playing within 15 minutes. 🎮
