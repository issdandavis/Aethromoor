# Avalon Repository Overview

This repository contains narrative source material and chat logs related to the Avalon/Spiral of Eternity world, plus a small ChoiceScript scaffold to help you spin up a runnable prototype locally.

## 📚 Quick Start Documentation

**@ @issdandavis - IMPORTANT ORGANIZATIONAL GUIDES:**

- **[WORKFLOW_IMPROVEMENTS.md](WORKFLOW_IMPROVEMENTS.md)** - Comprehensive workflow optimization guide with bold suggestions
- **[.github/AI_COLLABORATION_GUIDE.md](.github/AI_COLLABORATION_GUIDE.md)** - AI agent roles and collaboration protocols
- **[lore/CANON_CHECKLIST.md](lore/CANON_CHECKLIST.md)** - Quick reference for canonical lore elements
- **[.github/ISSUE_TEMPLATE/](.github/ISSUE_TEMPLATE/)** - Templates for story, technical, and lore issues
- **[.github/PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md)** - PR submission checklist

## Project layout
- `lore/` — Canonical lore and worldbuilding (single source of truth)
- `game/scenes/` — Main game scene files
- `choicescript_game/scenes/` — ChoiceScript implementation scenes
- `writing_drafts/` — Work-in-progress narrative content
- `docs/` — Project documentation and reference materials
- `config/.env.example` — template for API keys and other sensitive values. Copy to `.env` and fill in your own credentials.
- `game/` — ChoiceScript helper scripts, sample scenes, and README for running the demo (with stats screen and branching scenes).

## Getting ready to add game files
1. Install Node.js (LTS) and Git.
2. From the repo root, run `./game/bootstrap_choicescript.sh` to clone the official ChoiceScript engine locally under `game/choicescript/`.
3. Run `./game/sync_scenes.sh` to copy the demo scenes into `game/choicescript/web/mygame/`.
4. Start the ChoiceScript server from inside `game/choicescript/` (`run-server.bat` on Windows, `serve.command` on macOS, `bash serve.sh` on Linux/WSL), then open the browser at `http://localhost:4200/` if it does not open automatically.
5. Edit scenes in `game/scenes/` and re-run `./game/sync_scenes.sh` to refresh the playable build.

## Security
Previous commits contained plaintext API keys. They have been removed from the tracked files. Make sure to rotate any keys that may have been exposed and only store live credentials in your local `.env` file.
