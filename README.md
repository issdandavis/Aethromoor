# Avalon Repository Overview

This repository contains narrative source material and chat logs related to the Avalon/Spiral of Eternity world, plus a small ChoiceScript scaffold to help you spin up a runnable prototype locally.

## Project layout
- `docs/avalon_materials/` — all reference documents, drafts, and PDFs that were previously in `AvalonBook STUFF`.
- `docs/reference/` — miscellaneous reference files that were loose in the repo (chat logs, PDFs, and links).
- `config/.env.example` — template for API keys and other sensitive values. Copy to `.env` and fill in your own credentials.
- `game/` — ChoiceScript helper scripts, sample scenes, and README for running the demo.

## Getting ready to add game files
1. Install Node.js (LTS) and Git.
2. From the repo root, run `./game/bootstrap_choicescript.sh` to clone the official ChoiceScript engine locally under `game/choicescript/`.
3. Run `./game/sync_scenes.sh` to copy the demo scenes into `game/choicescript/web/mygame/`.
4. Start the ChoiceScript server from inside `game/choicescript/` (`run-server.bat` on Windows, `serve.command` on macOS, `bash serve.sh` on Linux/WSL), then open the browser at `http://localhost:4200/` if it does not open automatically.
5. Edit scenes in `game/scenes/` and re-run `./game/sync_scenes.sh` to refresh the playable build.

## Security
Previous commits contained plaintext API keys. They have been removed from the tracked files. Make sure to rotate any keys that may have been exposed and only store live credentials in your local `.env` file.
