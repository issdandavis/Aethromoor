# ChoiceScript integration guide

This repository now includes a small ChoiceScript-friendly scaffolding to help you get a runnable prototype working quickly. The actual ChoiceScript engine is **not** vendored here; use the helper script below to download it locally and sync the included sample scenes.

## Prerequisites
- Node.js (recommended LTS version)
- Git (for cloning the ChoiceScript engine)

## Bootstrap the ChoiceScript engine locally
1. From the repository root, run `./game/bootstrap_choicescript.sh`.
   - This clones the official ChoiceScript repository into `game/choicescript/`.
   - If the folder already exists, the script will skip the clone.
2. (Optional) To update later, run `cd game/choicescript && git pull`.

## Load the sample Avalon demo scenes
1. Ensure `game/choicescript/` exists (see bootstrap step above).
2. Run `./game/sync_scenes.sh` to copy the sample scenes from `game/scenes/` into `game/choicescript/web/mygame/`.
3. Launch the ChoiceScript local server from inside `game/choicescript/`:
   - Windows: double-click `run-server.bat` (may show as `run-server`).
   - macOS: double-click `serve.command` (you may need to allow it under System Settings > Gatekeeper the first time).
   - Linux/WSL: run `bash serve.sh`.
4. Your browser should open to the demo. If it doesn’t, open `http://localhost:4200/` manually while the server is running.
5. Use the in-game **Show Stats** button to track honor, attunement, resolve, mentor, and renown as you test branches.

## Editing and extending scenes
- The sample scenes live in `game/scenes/`. Edit them directly there.
- Run `./game/sync_scenes.sh` after changes to push updates into the engine’s `web/mygame/` folder.
- Scene order and available files are controlled by `*scene_list` at the top of `startup.txt`.
- The included demo highlights multiple ChoiceScript features you can reuse:
  - `startup.txt` seeds player stats and points to subsequent scenes.
  - `council.txt` shows nested choices and `*goto_scene` routing.
  - `crossroads.txt` demonstrates an inline stat check before branching.
  - `mission.txt` contains multi-level `*if`, `*elseif`, and `*else` checks.
  - `epilogue.txt` uses stat-driven endings.
  - `choicescript_stats.txt` defines the stats screen for the **Show Stats** button.

## Linking to existing narrative materials
- Reference lore and narrative drafts live under `docs/avalon_materials/` and `docs/reference/`.
- You can paste text from those sources into ChoiceScript scenes. Be mindful of indentation and convert smart quotes to straight quotes when necessary to avoid syntax errors.

## Next steps
- Expand the `*scene_list` in `startup.txt` with new chapters.
- Use ChoiceScript stats to track player choices (see the inline comments in the sample scenes for examples).
- When ready to distribute, follow ChoiceScript’s packaging guidelines from the official repository.
