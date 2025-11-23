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
  echo "Target directory $TARGET_DIR does not exist. Creating it to hold synced scenes..." >&2
  mkdir -p "$TARGET_DIR"
fi

echo "WARNING: This script uses 'rsync --delete' which will remove files in the target"
echo "directory that don't exist in the source. Any custom scenes you created directly"
echo "in $TARGET_DIR will be permanently deleted."
echo ""
read -p "Continue? (y/N) " -n 1 -r
echo ""
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
  echo "Sync cancelled."
  exit 0
fi

echo "Copying scenes from $SOURCE_DIR to $TARGET_DIR..."
rsync -av --delete "$SOURCE_DIR/" "$TARGET_DIR/"
echo "Done. Launch the ChoiceScript server from $SCRIPT_DIR/choicescript to play."
