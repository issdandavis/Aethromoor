# 🤖 AI-Assisted CSIDE Upload Instructions

**For:** Codex AI or other AI assistants  
**Purpose:** Automate the process of preparing and uploading game files to CSIDE

---

## 🎯 WHAT THIS DOES

This guide helps an AI assistant:
1. Find all your game files
2. Prepare them for CSIDE upload
3. Create a ready-to-use package
4. Provide upload instructions

**Note:** The actual upload to CSIDE still requires human action (drag-and-drop in browser), but AI can prepare everything!

---

## 🤖 FOR AI ASSISTANTS (CODEX, CLAUDE, ETC.)

### Task: Prepare Game Files for CSIDE Upload

**Instructions for AI:**

```markdown
You are helping prepare ChoiceScript game files for upload to CSIDE.

### Step 1: Run the Preparation Script
Execute this command:
```bash
cd /home/runner/work/Avalon/Avalon
./scripts/prepare-for-cside.sh
```

This creates a `cside-ready/` folder with all game files organized.

### Step 2: Verify Files
Check that the output folder contains:
- startup.txt (1 file)
- scenes/ folder with 16 .txt files
- UPLOAD_INSTRUCTIONS.txt
- FILE_LIST.txt

### Step 3: Inform User
Tell the user:
"✅ Game files prepared! All files are in the 'cside-ready/' folder.
Next: Open https://choicescriptide.github.io/ and drag the files from 'cside-ready/' to CSIDE."

### Step 4: Provide Upload Steps
Share these steps with the user:

1. Open browser to: https://choicescriptide.github.io/
2. Click "New Project" → name it "Pollys-Wingscroll"
3. Navigate to the cside-ready/ folder on your computer
4. Drag startup.txt into CSIDE first
5. Drag all files from scenes/ folder into CSIDE
6. Click "Run" to test the game

### Step 5: Troubleshooting Support
If user reports issues:
- Check that all 17 files were uploaded
- Verify startup.txt is present
- Verify all scene files are in CSIDE
- Check CSIDE "Issues" tab for specific errors
```

---

## 📋 AUTOMATION SCRIPT USAGE

### For AI to Run:

```bash
# Navigate to repository
cd /home/runner/work/Avalon/Avalon

# Run preparation script
./scripts/prepare-for-cside.sh

# Output will show:
# - Number of files packaged
# - Location of package (cside-ready/)
# - Next steps for user

# Verify output
ls -la cside-ready/
ls -la cside-ready/scenes/
```

### Expected Output:
```
cside-ready/
├── startup.txt                 (Main game file)
├── scenes/                     (All scene files)
│   ├── arrival.txt
│   ├── familiar_selection.txt
│   ├── dorm_room.txt
│   ├── first_lesson.txt
│   ├── academy_life.txt
│   ├── golem_workshop.txt
│   ├── expedition_prep.txt
│   ├── singing_dunes.txt
│   ├── verdant_tithe.txt
│   ├── rune_glacier.txt
│   ├── character_bonds.txt
│   ├── romance_scenes.txt
│   ├── secret_paths.txt
│   ├── final_trial.txt
│   ├── endings.txt
│   └── choicescript_stats.txt
├── UPLOAD_INSTRUCTIONS.txt     (Human-readable guide)
└── FILE_LIST.txt               (Complete file inventory)
```

---

## 🔄 WORKFLOW FOR AI ASSISTANT

### Scenario: User asks to prepare files for CSIDE

```
User: "Help me upload my game to CSIDE"

AI Response:
1. Run: ./scripts/prepare-for-cside.sh
2. Confirm: "✅ Files prepared in cside-ready/ folder"
3. Provide: Step-by-step upload instructions
4. Guide: Point to UPLOAD_INSTRUCTIONS.txt for details
```

### Sample AI Response Template:

```
I've prepared all your game files for CSIDE! Here's what I did:

✅ Packaged Files:
  • startup.txt (main game file)
  • 16 scene files in scenes/ folder
  • Instructions and file list included

📁 Location: /home/runner/work/Avalon/Avalon/cside-ready/

🎯 Next Steps:
1. Open: https://choicescriptide.github.io/
2. Create new project named "Pollys-Wingscroll"
3. From your computer, navigate to the cside-ready/ folder
4. Drag startup.txt into CSIDE
5. Drag all files from scenes/ folder into CSIDE
6. Click "Run" to test your game!

📖 Detailed instructions are in: cside-ready/UPLOAD_INSTRUCTIONS.txt

Need help with any step? Let me know!
```

---

## 🛠️ WHAT AI CAN DO

### ✅ AI Can Automate:
- Running the preparation script
- Creating the package folder
- Copying all game files
- Generating instructions
- Creating file lists
- Verifying file count
- Checking file integrity

### ❌ AI Cannot Do (Human Required):
- Opening web browser to CSIDE
- Dragging files into CSIDE interface
- Clicking "Run" button in CSIDE
- Testing the game manually
- Debugging gameplay issues

---

## 🔧 ADVANCED: AI-Generated Upload Package

### For AI Creating Custom Packages:

```python
# Example: AI script to prepare files
import os
import shutil

source_dir = "/home/runner/work/Avalon/Avalon/choicescript_game"
output_dir = "/home/runner/work/Avalon/Avalon/cside-ready"

# Create output directory
os.makedirs(f"{output_dir}/scenes", exist_ok=True)

# Copy startup file
shutil.copy(f"{source_dir}/startup.txt", output_dir)

# Copy all scene files
for file in os.listdir(f"{source_dir}/scenes"):
    if file.endswith('.txt'):
        shutil.copy(
            f"{source_dir}/scenes/{file}",
            f"{output_dir}/scenes/{file}"
        )

print("✅ Files prepared for CSIDE upload!")
print(f"📁 Location: {output_dir}")
```

---

## 📊 VERIFICATION CHECKLIST (FOR AI)

After running preparation, AI should verify:

```bash
# Check main file exists
[ -f cside-ready/startup.txt ] && echo "✅ startup.txt" || echo "❌ Missing startup.txt"

# Count scene files (should be 16)
SCENE_COUNT=$(ls -1 cside-ready/scenes/*.txt | wc -l)
echo "Scene files: $SCENE_COUNT (should be 16)"

# Verify instructions created
[ -f cside-ready/UPLOAD_INSTRUCTIONS.txt ] && echo "✅ Instructions created"

# Show file sizes
du -sh cside-ready/
```

---

## 🎯 COMMON AI ASSISTANCE SCENARIOS

### Scenario 1: "Prepare my game for CSIDE"
```bash
./scripts/prepare-for-cside.sh
# Then provide upload instructions
```

### Scenario 2: "How do I upload to CSIDE?"
```markdown
Point to: CSIDE_UPLOAD_GUIDE.md
Highlight: Method 1 (CSIDE Web Editor) sections
```

### Scenario 3: "Which files do I need?"
```markdown
All files in: cside-ready/ folder
  • startup.txt (required)
  • Everything in scenes/ (required)
```

### Scenario 4: "Is my game ready?"
```bash
# Verify all files present
ls -R cside-ready/
# Should show 17 .txt files total
```

---

## 📖 REFERENCE FOR AI

### File Locations:
```
Source: /home/runner/work/Avalon/Avalon/choicescript_game/
Output: /home/runner/work/Avalon/Avalon/cside-ready/
Script: /home/runner/work/Avalon/Avalon/scripts/prepare-for-cside.sh
Guide:  /home/runner/work/Avalon/Avalon/CSIDE_UPLOAD_GUIDE.md
```

### Key Commands:
```bash
# Prepare files
./scripts/prepare-for-cside.sh

# Verify preparation
ls -la cside-ready/

# Count files
find cside-ready -name "*.txt" | wc -l
# Should output: 17

# Show instructions
cat cside-ready/UPLOAD_INSTRUCTIONS.txt
```

### CSIDE URL:
```
https://choicescriptide.github.io/
```

---

## ✨ SUMMARY FOR AI

**What You Can Do:**
1. Run preparation script
2. Verify files packaged
3. Create instructions
4. Guide user through process
5. Troubleshoot file issues

**What User Must Do:**
1. Open CSIDE in browser
2. Drag files to CSIDE
3. Test the game
4. Fix any gameplay issues

**Your Role:**
- Prepare everything perfectly
- Provide clear instructions
- Support troubleshooting
- Make it as easy as possible for user

---

*This guide enables AI assistants to automate the file preparation process while providing clear handoff instructions for the manual steps.*
