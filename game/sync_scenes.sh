#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SOURCE_DIR="$SCRIPT_DIR/scenes"
TARGET_DIR="$SCRIPT_DIR/choicescript/web/mygame/scenes"

if [ ! -d "$SCRIPT_DIR/choicescript" ]; then
  echo "ChoiceScript not found in $SCRIPT_DIR/choicescript. Run ./game/bootstrap_choicescript.sh first." >&2
  exit 1
fi

if [ ! -d "$TARGET_DIR" ]; then
  mkdir -p "$TARGET_DIR"
fi

echo "Copying scenes from $SOURCE_DIR to $TARGET_DIR..."
rsync -av --delete "$SOURCE_DIR/" "$TARGET_DIR/"

# Generate mygame.js
echo "Generating mygame.js..."
cd "$SCRIPT_DIR/choicescript"
node mygamegenerator.js mygame > web/mygame/mygame.js

echo "Done. Launch the ChoiceScript server from $SCRIPT_DIR/choicescript to play."
