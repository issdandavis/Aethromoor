# Repository Instructions for Copilot

This repository contains "Polly's Wingscroll: The First Thread", a choice-based narrative game set in the Avalon Academy universe, along with worldbuilding documentation and novel drafts.

## Project Overview

This is a narrative game/interactive fiction project with two implementations:
- **HTML/JavaScript version** (`game/` directory) - Standalone browser-based game
- **ChoiceScript version** (`choicescript_game/` directory) - Professional format for publishing

The repository also contains:
- **Worldbuilding documentation** (`lore/` directory)
- **Novel manuscripts** (`writing_drafts/` directory)
- **Project documentation** (`docs/` directory)

## Key Principles

1. **Preserve narrative continuity** - This is a story-driven project. All changes to game content should maintain story coherence and character consistency.

2. **Maintain dual implementations** - The HTML and ChoiceScript versions should offer equivalent story content. When updating one, consider if the other needs updates.

3. **Respect the worldbuilding** - The Avalon universe has established lore. Check `lore/` directory for canonical information before making story changes.

4. **No build process required** - This project doesn't use package managers or build tools. The HTML game runs directly in browsers, and the ChoiceScript version uses a simple Node.js server.

## File Organization

```
Avalon/
├── game/                  # HTML browser game (standalone)
│   ├── index.html        # Game entry point
│   ├── game.js           # Game logic and story nodes
│   └── style.css         # Game styling
│
├── choicescript_game/    # ChoiceScript professional version
│   ├── startup.txt       # Game configuration
│   └── scenes/           # Story scenes (*.txt files)
│
├── lore/                 # Worldbuilding documentation
├── writing_drafts/       # Novel manuscripts
├── docs/                 # Project documentation
└── archive/              # Historical files (do not modify)
```

## Testing and Validation

### Testing the HTML Game
1. Open `game/index.html` in a web browser
2. Play through key story paths to verify changes
3. Check browser console for any JavaScript errors

### Testing ChoiceScript Game
1. Requires Node.js installed
2. Navigate to `choicescript_game/` directory
3. Run `node server.js` (if server.js exists) or use ChoiceScript IDE
4. Test in browser at `http://localhost:3000`

### Documentation Changes
- Verify markdown formatting renders correctly
- Ensure internal links work properly
- Check that file paths in documentation are accurate

## Common Tasks

### Updating Game Content
- **HTML version**: Edit `game/game.js` to modify story nodes and choices
- **ChoiceScript version**: Edit appropriate `.txt` files in `choicescript_game/scenes/`
- Consider updating both versions to maintain parity

### Updating Documentation
- **Player guides**: `README.md`, `START_HERE.md`, `PLAY_THE_GAME.md`, `QUICK_START.md`
- **Worldbuilding**: Add to `lore/` directory
- **Development docs**: Update files in `docs/` directory

### Fixing Bugs
- Check browser console for JavaScript errors (HTML version)
- Review ChoiceScript syntax in `.txt` files (ChoiceScript version)
- Test game flow thoroughly after fixes

## Style Guidelines

### Code Style
- **JavaScript**: Use clear variable names, maintain existing code style
- **ChoiceScript**: Follow ChoiceScript syntax conventions (see Choice of Games documentation)
- **HTML/CSS**: Keep semantic HTML, maintain accessibility

### Documentation Style
- Use clear, conversational language for player-facing docs
- Use markdown formatting consistently
- Include examples where helpful
- Keep technical docs concise and accurate

### Narrative Style
- Maintain character voices (especially Polly's sarcastic commentary)
- Keep collaborative magic themes consistent
- Follow established worldbuilding from `lore/` directory
- Preserve the balance of dark setting with optimistic outcomes

## Important Notes

- **No external dependencies**: This project intentionally avoids npm packages, build tools, or complex dependencies
- **Browser compatibility**: HTML game should work in modern browsers without polyfills
- **Archive directory**: Do not modify files in `archive/` - they are historical records
- **Lore consistency**: Reference `lore/` files for canonical information about characters, magic systems, and world geography

## Questions or Clarifications

If you're unsure about:
- **Story/lore questions**: Check `lore/` directory and existing game content
- **Character voice**: Review existing dialogue in game files
- **Technical implementation**: Examine existing code patterns in the project
- **Project structure**: Refer to `README.md` and `ORGANIZATION_SUMMARY.md`
