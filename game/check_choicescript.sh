#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
GAME_DIR="$ROOT_DIR/game"
ENGINE_DIR="$GAME_DIR/choicescript"
SCENES_DIR="$GAME_DIR/scenes"
TARGET_SCENES_DIR="$ENGINE_DIR/web/mygame/scenes"

echo "Bootstrapping ChoiceScript engine..."
"$GAME_DIR/bootstrap_choicescript.sh"

if [[ ! -d "$ENGINE_DIR" ]]; then
  echo "ChoiceScript engine missing at $ENGINE_DIR after bootstrap. Aborting." >&2
  exit 1
fi

echo "Syncing scenes into the ChoiceScript engine..."
"$GAME_DIR/sync_scenes.sh"

echo "Verifying synced scenes are current..."
if rsync -ain --delete "$SCENES_DIR/" "$TARGET_SCENES_DIR/" | grep -q .; then
  echo "ChoiceScript scene copies are stale. Run ./game/sync_scenes.sh locally before committing." >&2
  exit 1
fi

declare -a QUICKTEST_COMMAND=(node quicktest.js mygame)

if command -v node >/dev/null 2>&1 && [[ -f "$ENGINE_DIR/quicktest.js" ]]; then
  echo "Running ChoiceScript quicktest..."
  (cd "$ENGINE_DIR" && "${QUICKTEST_COMMAND[@]}")
  echo "Quicktest completed."
else
  echo "Node.js or quicktest.js missing; skipping quicktest." >&2
fi
