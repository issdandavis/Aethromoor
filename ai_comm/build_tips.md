# AI Communication Channel: Build & Run Tips

This log documents technical tips, build commands, testing procedures, and debugging shortcuts.

## Format
Each entry should follow: `- YYYY-MM-DDTHH:MM:SSZ — [Tool/Command/Tip]. Context: [When to use]. Details: [How to use]`

---

## Entries

- 2025-11-23T08:49:01Z — Testing HTML version. Context: Quick playthrough to verify game flow and endings. Details: Open `game/index.html` directly in browser (no build step required). All 30+ scenes and 14 endings are functional.

- 2025-11-23T08:49:01Z — ChoiceScript testing. Context: Validating ChoiceScript scene syntax and logic. Details: Scenes in `choicescript_game/scenes/` require ChoiceScript IDE or CSIDE (https://choicescriptide.github.io/). See `QUICK_START.md` for setup instructions. Alternatively, use ChoiceScript compiler for syntax validation.

- 2025-11-23T08:49:01Z — Fast searching. Context: Finding specific text across large codebase. Details: Use `rg` (ripgrep) instead of `grep -r` for faster searches. Example: `rg "collaboration" choicescript_game/` to find stat references.

- 2025-11-23T08:49:01Z — Linting ChoiceScript. Context: Before committing scene changes. Details: Check for stray tabs (ChoiceScript requires spaces), verify all `*goto` labels exist, ensure stat names match `startup.txt` definitions.
