#!/usr/bin/env bash
# CSIDE Preparation Script
# Prepares all game files for easy upload to CSIDE

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
SOURCE_DIR="$REPO_ROOT/choicescript_game"
OUTPUT_DIR="$REPO_ROOT/cside-ready"

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}================================================${NC}"
echo -e "${BLUE}   CSIDE Game Files Preparation${NC}"
echo -e "${BLUE}================================================${NC}"
echo ""

# Check if source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo -e "${YELLOW}Error: Source directory not found at $SOURCE_DIR${NC}"
    exit 1
fi

# Create output directory
echo -e "${GREEN}Creating CSIDE-ready package...${NC}"
rm -rf "$OUTPUT_DIR"
mkdir -p "$OUTPUT_DIR/scenes"

# Copy startup file
echo "Copying startup.txt..."
cp "$SOURCE_DIR/startup.txt" "$OUTPUT_DIR/"

# Copy all scene files
echo "Copying scene files..."
cp "$SOURCE_DIR/scenes/"*.txt "$OUTPUT_DIR/scenes/"

# Count files
SCENE_COUNT=$(ls -1 "$OUTPUT_DIR/scenes/"*.txt 2>/dev/null | wc -l)
TOTAL_COUNT=$((SCENE_COUNT + 1))

echo ""
echo -e "${GREEN}✅ Package created successfully!${NC}"
echo ""
echo -e "${BLUE}Files packaged:${NC}"
echo "  • startup.txt (1 file)"
echo "  • scenes/*.txt ($SCENE_COUNT files)"
echo "  • Total: $TOTAL_COUNT files"
echo ""

# Create instructions file
cat > "$OUTPUT_DIR/UPLOAD_INSTRUCTIONS.txt" << 'EOF'
╔════════════════════════════════════════════════════════════════╗
║                 CSIDE UPLOAD INSTRUCTIONS                      ║
╚════════════════════════════════════════════════════════════════╝

📁 THIS FOLDER CONTAINS ALL YOUR GAME FILES FOR CSIDE

Files Ready:
  ✅ startup.txt (main game file)
  ✅ scenes/ folder (all scene files)

═══════════════════════════════════════════════════════════════

🚀 QUICK UPLOAD TO CSIDE WEB EDITOR

Step 1: Open CSIDE
  Go to: https://choicescriptide.github.io/

Step 2: Create New Project
  • Click "New Project"
  • Name it: Pollys-Wingscroll
  • Click "Create"

Step 3: Upload Files
  
  METHOD A: Drag and Drop (Easiest!)
  • Drag startup.txt into CSIDE
  • Open the scenes/ folder
  • Select ALL files in scenes/
  • Drag them all into CSIDE

  METHOD B: Manual Upload
  • Click "Add File" in CSIDE
  • Upload startup.txt FIRST
  • Then upload each file from scenes/

Step 4: Test Your Game
  • Click "Run" or "Test"
  • Game should start!
  • Create a character and play

═══════════════════════════════════════════════════════════════

📊 FILE CHECKLIST

After uploading, verify you have:
  ☐ startup.txt
  ☐ scenes/arrival.txt
  ☐ scenes/familiar_selection.txt
  ☐ scenes/dorm_room.txt
  ☐ scenes/first_lesson.txt
  ☐ scenes/academy_life.txt
  ☐ scenes/golem_workshop.txt
  ☐ scenes/expedition_prep.txt
  ☐ scenes/singing_dunes.txt
  ☐ scenes/verdant_tithe.txt
  ☐ scenes/rune_glacier.txt
  ☐ scenes/character_bonds.txt
  ☐ scenes/romance_scenes.txt
  ☐ scenes/secret_paths.txt
  ☐ scenes/final_trial.txt
  ☐ scenes/endings.txt
  ☐ scenes/choicescript_stats.txt

═══════════════════════════════════════════════════════════════

🔧 TROUBLESHOOTING

Problem: "Scene not found" error
  → Check all scene files uploaded
  → File names must match exactly

Problem: Game won't run
  → Make sure startup.txt uploaded first
  → Check CSIDE "Issues" tab for errors

Problem: Stats screen missing
  → Verify choicescript_stats.txt is in scenes/

═══════════════════════════════════════════════════════════════

📖 FULL GUIDE

For complete instructions, see:
  CSIDE_UPLOAD_GUIDE.md (in repository root)

═══════════════════════════════════════════════════════════════

✨ Your game files are ready! Just upload to CSIDE and play! ✨

EOF

# Create a file list
echo "Creating file list..."
cat > "$OUTPUT_DIR/FILE_LIST.txt" << EOF
CSIDE GAME FILES - Complete List
Generated: $(date)

MAIN FILE:
  startup.txt

SCENE FILES (in scenes/ folder):
EOF

ls -1 "$OUTPUT_DIR/scenes/" >> "$OUTPUT_DIR/FILE_LIST.txt"

echo ""
echo -e "${BLUE}📦 Package Location:${NC}"
echo "  $OUTPUT_DIR"
echo ""
echo -e "${GREEN}📄 Included:${NC}"
echo "  • All game files (.txt)"
echo "  • UPLOAD_INSTRUCTIONS.txt (step-by-step guide)"
echo "  • FILE_LIST.txt (complete file list)"
echo ""
echo -e "${BLUE}🎯 Next Steps:${NC}"
echo "  1. Open: $OUTPUT_DIR"
echo "  2. Read: UPLOAD_INSTRUCTIONS.txt"
echo "  3. Go to: https://choicescriptide.github.io/"
echo "  4. Drag files to CSIDE"
echo "  5. Click 'Run' to test!"
echo ""
echo -e "${GREEN}✨ Ready to upload to CSIDE!${NC}"
echo ""
