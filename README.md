# Avalon Repository Overview

This repository currently contains narrative source material and chat logs related to the Avalon/Spiral of Eternity world. There is not yet runnable game code, so this commit organizes the project to make it easier to add game files and safely manage configuration.

## Project layout
- `docs/avalon_materials/` — all reference documents, drafts, and PDFs that were previously in `AvalonBook STUFF`.
- `docs/reference/` — miscellaneous reference files that were loose in the repo (chat logs, PDFs, and links).
- `config/.env.example` — template for API keys and other sensitive values. Copy to `.env` and fill in your own credentials.

## Getting ready to add game files
1. Create a virtual environment or game project directory under a new folder (for example, `game/` or `src/`).
2. Copy `config/.env.example` to `.env` and populate the required keys. Keep `.env` out of version control.
3. Add your game code and assets alongside the docs, using the `docs/` folder strictly for reference material.

## Security
Previous commits contained plaintext API keys. They have been removed from the tracked files. Make sure to rotate any keys that may have been exposed and only store live credentials in your local `.env` file.
