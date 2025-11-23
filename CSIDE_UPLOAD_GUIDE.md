# 🎮 CSIDE Upload Guide - Complete Instructions

**Last Updated:** 2025-11-23  
**Purpose:** Step-by-step guide to upload your game files to CSIDE and test them

---

## 📍 FINDING YOUR GAME FILES

### All Your Game Files Are Here:
```
/home/runner/work/Avalon/Avalon/choicescript_game/
├── startup.txt                    ← Main game file (REQUIRED)
└── scenes/                        ← All scene files (REQUIRED)
    ├── arrival.txt
    ├── familiar_selection.txt
    ├── dorm_room.txt
    ├── first_lesson.txt
    ├── academy_life.txt
    ├── golem_workshop.txt
    ├── expedition_prep.txt
    ├── singing_dunes.txt
    ├── verdant_tithe.txt
    ├── rune_glacier.txt
    ├── character_bonds.txt
    ├── romance_scenes.txt
    ├── secret_paths.txt
    ├── final_trial.txt
    ├── endings.txt
    └── choicescript_stats.txt     ← Stats screen
```

**Total Files:** 17 (1 main + 16 scenes)

---

## 🚀 METHOD 1: CSIDE Web Editor (Easiest!)

### Step 1: Open CSIDE
Go to: **https://choicescriptide.github.io/**

### Step 2: Create New Project
1. Click **"New Project"** or **"Projects"** tab
2. Enter project name: `Pollys-Wingscroll`
3. Click **"Create"**

### Step 3: Upload Files

**Option A: Drag and Drop (Recommended)**
1. Open your file explorer to: `/home/runner/work/Avalon/Avalon/choicescript_game/`
2. Select `startup.txt`
3. Drag it into CSIDE's file panel
4. Open the `scenes/` folder
5. Select ALL 16 files in the scenes folder
6. Drag them all into CSIDE at once

**Option B: Manual Upload**
1. In CSIDE, click **"Add File"** or **"+"** button
2. Upload `startup.txt` first (IMPORTANT: must be first!)
3. Click **"Add File"** again
4. Upload each scene file from the `scenes/` folder one by one

### Step 4: Verify Files Loaded
Check that CSIDE shows all these files:
- ✅ startup.txt
- ✅ arrival.txt
- ✅ familiar_selection.txt
- ✅ dorm_room.txt
- ✅ first_lesson.txt
- ✅ academy_life.txt
- ✅ golem_workshop.txt
- ✅ expedition_prep.txt
- ✅ singing_dunes.txt
- ✅ verdant_tithe.txt
- ✅ rune_glacier.txt
- ✅ character_bonds.txt
- ✅ romance_scenes.txt
- ✅ secret_paths.txt
- ✅ final_trial.txt
- ✅ endings.txt
- ✅ choicescript_stats.txt

### Step 5: Test Your Game!
1. Click **"Run"** or **"Test"** button
2. Your game should start!
3. Try creating a character and playing through

**If you see errors:** Check the "Issues" tab in CSIDE - it will tell you what's wrong

---

## 🖥️ METHOD 2: Downloaded ChoiceScript (Advanced)

### Step 1: Download ChoiceScript
1. Go to: https://www.choiceofgames.com/make-your-own-games/choicescript-intro/
2. Click **"Download ChoiceScript"** (it's free!)
3. Unzip the downloaded file

### Step 2: Copy Your Game Files
1. Navigate to the unzipped ChoiceScript folder
2. Open: `ChoiceScript/web/mygame/`
3. **DELETE** everything in that folder
4. **COPY** all files from `/home/runner/work/Avalon/Avalon/choicescript_game/` 
5. **PASTE** them into `web/mygame/`

**Your `web/mygame/` folder should now have:**
```
web/mygame/
├── startup.txt
├── scenes/
│   ├── arrival.txt
│   ├── (all other scene files)
│   └── choicescript_stats.txt
```

### Step 3: Play Your Game
1. Open `ChoiceScript/web/index.html` in your browser
2. Your game should load automatically!
3. If not, make sure all files copied correctly

---

## 🤖 METHOD 3: Automated Script (For Codex AI)

I've created an automated script that packages your files for CSIDE!

### Quick Use:
```bash
cd /home/runner/work/Avalon/Avalon
./scripts/prepare-for-cside.sh
```

This creates a `cside-ready/` folder with:
- All game files organized
- A checklist of what to upload
- Instructions included

**Then:** Just drag the entire `cside-ready/` folder to CSIDE!

---

## ✅ VERIFICATION CHECKLIST

After uploading to CSIDE, verify:

### Files Check:
- [ ] `startup.txt` is present and opens
- [ ] All 16 scene files are present
- [ ] `choicescript_stats.txt` is in the scenes folder
- [ ] No files missing from the scene list

### Game Check:
- [ ] Click "Run" - game loads without errors
- [ ] Can create a character
- [ ] Can see Polly's introduction
- [ ] Can make choices
- [ ] Stats screen shows up (press "Show Stats")
- [ ] Can reach at least one scene

### Common Issues:
❌ **"Scene not found" error**
- Fix: Make sure the scene file exists in CSIDE
- Check: File name matches exactly (case-sensitive!)

❌ **"Startup file not found"**
- Fix: Upload `startup.txt` first
- Make sure it's named exactly `startup.txt`

❌ **Game won't run**
- Fix: Check the "Issues" tab in CSIDE
- Look for syntax errors or missing files

---

## 🎯 WHAT EACH FILE DOES

### `startup.txt` - The Boss File
- Loads first, always
- Sets up your stats (Collaboration, relationships)
- Defines achievements
- Lists all scene files
- **Must be present or nothing works!**

### Scene Files - Your Story
- `arrival.txt` - How you arrive at the academy (3 paths)
- `familiar_selection.txt` - Choose your familiar
- `dorm_room.txt` - Customize your room
- `first_lesson.txt` - First magic lesson
- `academy_life.txt` - Daily life scenes
- `golem_workshop.txt` - Golem crafting
- `expedition_prep.txt` - Choose your expedition
- `singing_dunes.txt` - Desert expedition
- `verdant_tithe.txt` - Forest expedition
- `rune_glacier.txt` - Glacier expedition
- `character_bonds.txt` - Build relationships
- `romance_scenes.txt` - Romance options
- `secret_paths.txt` - Hidden content
- `final_trial.txt` - Climactic challenge
- `endings.txt` - Your 14 different endings

### `choicescript_stats.txt` - Stats Display
- Shows your Collaboration score
- Shows all your relationships
- Displays achievements
- **Must be in scenes/ folder**

---

## 🔧 TROUBLESHOOTING

### Problem: "Files won't upload to CSIDE"
**Solution:**
1. Make sure you're using Chrome, Firefox, or Edge (not Safari)
2. Try uploading one file at a time
3. Clear browser cache and try again
4. Use the downloaded ChoiceScript method instead

### Problem: "Game starts but crashes on first choice"
**Solution:**
1. Check that ALL scene files uploaded
2. Verify `choicescript_stats.txt` is in scenes folder
3. Look at CSIDE "Issues" tab for specific error

### Problem: "Can't find the files on my computer"
**Solution:**
They're at: `/home/runner/work/Avalon/Avalon/choicescript_game/`

On Windows: Use File Explorer, paste that path
On Mac: Use Finder → Go → Go to Folder
On Linux: Use your file manager

### Problem: "Stats screen doesn't show"
**Solution:**
1. Make sure `choicescript_stats.txt` uploaded
2. It must be in the scenes folder, not root
3. Check for typos in the filename

---

## 📱 TESTING YOUR GAME

### Quick Test (5 minutes):
1. Start game
2. Create a character
3. Choose one arrival path
4. Complete first lesson
5. Choose an expedition
6. Reach one ending

### Full Test (30 minutes):
1. Try all 3 arrival paths
2. Test all expedition choices
3. Try different Collaboration choices
4. Check stats screen works
5. Reach multiple endings
6. Verify achievements unlock

### What to Look For:
✅ Choices make sense
✅ Stats change correctly
✅ Story flows naturally
✅ No broken links
✅ Polly's commentary appears
✅ Endings are reachable

---

## 🎮 READY TO PUBLISH?

Once your game works in CSIDE:

### Beta Testing:
1. Use CSIDE's share feature
2. Send link to friends
3. Collect feedback
4. Fix any issues

### Publishing to Hosted Games:
1. Join forum: https://forum.choiceofgames.com/
2. Post in "Hosted Games" section
3. Get community feedback
4. Submit to Hosted Games
5. If approved → **Real mobile app!**

---

## 🆘 NEED HELP?

### Resources:
- **ChoiceScript Tutorial:** https://www.choiceofgames.com/make-your-own-games/choicescript-intro/
- **CSIDE Help:** Click "?" button in CSIDE
- **Forum:** https://forum.choiceofgames.com/
- **Wiki:** https://choicescriptdev.fandom.com/

### Quick Help:
- Check `HUMAN_GUIDE_CSIDE_FILES.md` for file organization
- Check `FILE_GUIDE.md` for quick reference
- Check `SETUP_COMPLETE.md` for overall setup

---

## 📋 QUICK REFERENCE

### Files Location:
```
/home/runner/work/Avalon/Avalon/choicescript_game/
```

### CSIDE Web Editor:
```
https://choicescriptide.github.io/
```

### Upload Order:
```
1. startup.txt (FIRST!)
2. All scene files (any order)
```

### To Test:
```
Click "Run" in CSIDE
```

---

**That's it! Your game files are ready. Just upload and play!** 🎮✨

*Last updated by: Copilot Agent*
