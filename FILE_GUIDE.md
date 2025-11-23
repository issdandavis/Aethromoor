# 📂 FILE GUIDE - What to Touch, What to Skip

**Quick visual guide for humans working on Avalon**

---

## 🎮 GAME FILES (YOU EDIT THESE IN CSIDE)

### Main Game Folder
```
choicescript_game/              ← 🎮 DRAG THIS TO CSIDE
├── startup.txt                 ← 🎮 YOUR FILE
├── README.md                   ← 📖 Read only
└── scenes/                     ← 🎮 YOUR GAME SCENES
    ├── arrival.txt             ← 🎮 YOUR FILE
    ├── first_lesson.txt        ← 🎮 YOUR FILE
    ├── dorm_room.txt           ← 🎮 YOUR FILE
    ├── academy_life.txt        ← 🎮 YOUR FILE
    ├── expedition_prep.txt     ← 🎮 YOUR FILE
    ├── singing_dunes.txt       ← 🎮 YOUR FILE (AI creates, you polish)
    ├── verdant_tithe.txt       ← 🎮 YOUR FILE (AI creates, you polish)
    ├── rune_glacier.txt        ← 🎮 YOUR FILE (AI creates, you polish)
    ├── character_bonds.txt     ← 🎮 YOUR FILE
    ├── final_trial.txt         ← 🎮 YOUR FILE
    ├── endings.txt             ← 🎮 YOUR FILE (AI creates, you polish)
    └── choicescript_stats.txt  ← 🎮 YOUR FILE
```

**All `.txt` files = YOUR GAME FILES for CSIDE!**

---

## 🤖 AI COORDINATION FILES (AIs UPDATE THESE)

```
STATUS_CONTEXT.md               ← 🤖 AI updates (you read to see progress)
AI_TASK_QUEUE.md               ← 🤖 AI claims tasks (you assign tasks)
SCENE_PARITY_CHECKLIST.md      ← 🤖 AI tracks conversion
STATS_MATRIX.md                ← 🤖 AI tracks game balance
```

**You can READ these anytime, but AIs maintain them**

---

## 📖 DOCUMENTATION (REFERENCE ONLY)

```
docs/
├── AUTO_COMMIT_GUIDE.md        ← 📖 How to use auto-commit
├── AI_PLATFORM_INTEGRATION.md  ← 📖 Multi-AI setup guide
├── AUTOMATION_GUIDE.md         ← 📖 Zapier workflows
├── PROJECT_ROADMAP.md          ← 📖 Development plan
├── NEXT_TASKS.md               ← 📖 What needs doing
└── AI_SESSION_HANDOFF.md       ← 📖 AI instructions
```

**Read these when you need help or want to understand something**

---

## 🌐 HTML VERSION (SEPARATE GAME)

```
game/
├── index.html                  ← 🌐 Play in browser
├── game.js                     ← 🌐 Source for AI conversions
└── style.css                   ← 🌐 Browser styling
```

**This is the complete HTML version. AIs read `game.js` to convert scenes to ChoiceScript.**

---

## 📚 LORE REFERENCE (FOR AIS TO READ)

```
lore/
├── characters.md               ← 📚 Character bios
├── geography.md                ← 📚 World locations
├── magic_systems.md            ← 📚 How magic works
└── timeline.md                 ← 📚 Historical events
```

**AIs use these to keep game content consistent with your world**

---

## 🔧 AUTOMATION SCRIPTS (RUN WHEN NEEDED)

```
scripts/
├── auto-commit.sh              ← 🔧 Run: ./scripts/auto-commit.sh
├── watch-and-commit.sh         ← 🔧 Run: ./scripts/watch-and-commit.sh
├── auto-commit-config.example.sh ← 🔧 Copy to customize
└── README.md                   ← 📖 Script documentation
```

**Run these to save your work automatically**

---

## 📋 QUICK REFERENCE GUIDES

```
ROOT FOLDER:
├── HUMAN_GUIDE_CSIDE_FILES.md  ← 📋 THIS IS FOR YOU! Read this!
├── AUTO_COMMIT_QUICK_START.md  ← 📋 Quick auto-commit guide
├── START_HERE.md               ← 📋 Project overview
├── QUICK_START.md              ← 📋 How to play
└── FILE_GUIDE.md               ← 📋 This file
```

---

## 🎯 WHAT YOU ACTUALLY TOUCH

### Most of the time:
```
choicescript_game/scenes/*.txt  ← Edit these in CSIDE
```

### Sometimes:
```
./scripts/auto-commit.sh        ← Run this to save work
STATUS_CONTEXT.md               ← Read to see AI progress
AI_TASK_QUEUE.md                ← Assign tasks to AIs
```

### Rarely:
```
docs/*.md                       ← Read for reference
lore/*.md                       ← Update story background
game/index.html                 ← Play HTML version
```

### Never:
```
.git/                           ← Git internals (automated)
.github/workflows/              ← Automated scripts
node_modules/                   ← Dependencies (if any)
```

---

## 🚦 COLOR CODE SYSTEM

Throughout this repository, you'll see these markers:

### 🎮 = GAME FILES (Your editing zone)
- All ChoiceScript `.txt` files
- Your actual game content
- Edit in CSIDE or text editor

### 🤖 = AI FILES (AIs maintain these)
- Coordination files
- Task tracking
- Status updates

### 📖 = DOCS (Read for help)
- Guides and tutorials
- Reference material
- How-to instructions

### 🔧 = SCRIPTS (Run when needed)
- Automation tools
- Helper scripts
- One-command shortcuts

### 📚 = LORE (Creative reference)
- Worldbuilding
- Characters
- Story background

### 🌐 = HTML VERSION (Separate game)
- Browser-based version
- Reference for conversions
- Playable demo

---

## ⚡ SUPER QUICK VERSION

**What to edit:** Everything in `choicescript_game/` folder  
**What to run:** `./scripts/auto-commit.sh` when you make changes  
**What to read:** `HUMAN_GUIDE_CSIDE_FILES.md` for detailed help  
**What to assign:** Tasks in `AI_TASK_QUEUE.md` to your AI team  

**That's it!**

---

## 🆘 WHEN IN DOUBT

**If it's a `.txt` file in `choicescript_game/`** → You can edit it!  
**If it has 🤖 AI in the name** → Let AIs handle it  
**If you're not sure** → Read `HUMAN_GUIDE_CSIDE_FILES.md`  

---

*Keep this guide handy for quick reference!* 🎮✨
