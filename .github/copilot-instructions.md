# Copilot Instructions for Avalon Repository

## Repository Overview

This is the **Avalon** repository - a narrative game and creative writing project featuring "Polly's Wingscroll: The First Thread," a choice-based narrative game set in Avalon Academy.

## Project Structure

```
Avalon/
├── game/                   # HTML/CSS/JS version (instant play)
│   ├── index.html         # Main game file
│   ├── game.js            # Game logic
│   └── style.css          # Styling
│
├── choicescript_game/     # Professional ChoiceScript version
│   ├── startup.txt        # Game configuration
│   └── scenes/            # Game scenes (.txt files)
│
├── lore/                  # Worldbuilding documents
├── writing_drafts/        # Novel manuscripts
├── docs/                  # Project documentation
├── archive/               # Historical files
└── .github/               # GitHub configuration
```

## Content Type

This repository contains:
- **Game files**: HTML/JavaScript game and ChoiceScript game implementation
- **Creative content**: Lore documents, worldbuilding, novel drafts
- **Documentation**: README files, guides, and project planning documents
- **No traditional source code**: No compilation, build system, or automated tests

## Key Conventions

### File Organization
- Game-related files go in `game/` (HTML version) or `choicescript_game/` (ChoiceScript version)
- All worldbuilding and lore documents belong in `lore/`
- Novel and story drafts belong in `writing_drafts/`
- Project planning and guides belong in `docs/`
- Historical or deprecated files go in `archive/`

### Documentation Style
- Use clear, accessible language - this project is for creative writers, not just developers
- Maintain existing markdown formatting style (.md files)
- Keep README files friendly and welcoming
- Include emojis in headers for visual appeal (existing style)
- Provide step-by-step instructions for non-technical users

### ChoiceScript Conventions
- Scene files are plain text with .txt extension
- Use ChoiceScript syntax (not regular programming languages)
- Maintain narrative consistency with existing lore
- Follow ChoiceScript best practices for variable naming and flow control
- Preserve the collaborative magic theme throughout the game

### HTML/JavaScript Game
- Keep `game/index.html` simple and self-contained
- Maintain vanilla JavaScript (no frameworks)
- Ensure offline playability
- Keep styling in `game/style.css`

## Lore and Worldbuilding

### Core Themes
- **Magic as communication**: Not domination, but partnership
- **Collaborative dimensional magic**: Working together across realities
- **Character-driven narrative**: Relationships matter
- **Polly (Polymnia Aetheris)**: Ancient sarcastic raven familiar - a key character

### Important Lore Elements
- Avalon Academy is a living pocket dimension
- Magic system based on communication and consent
- Characters include Izack Thorne, Aria Ravencrest, Zara, Grey
- The "Third Thread" mystery connects to deeper lore
- Dimensional architecture and boundary magic are central concepts

## Working with This Repository

### Making Changes
- **Game content changes**: Test by opening `game/index.html` in a browser
- **Documentation changes**: No testing required, just review for clarity
- **ChoiceScript changes**: Requires ChoiceScript IDE or web player for testing
- **Lore additions**: Ensure consistency with existing worldbuilding

### No Build/Test Infrastructure
- This repository has no npm, package.json, Makefile, or test suite
- No linting or automated testing configured
- Validation is manual: open HTML files in browser, read documentation for clarity
- Jekyll CI workflow exists but is for GitHub Pages deployment only

### Git Workflow
- Keep commits focused and descriptive
- Don't commit temporary files, build artifacts, or system files
- Preserve existing file organization
- Respect the archive/ directory - don't modify old files there

## Important Files

### Entry Points
- `START_HERE.md`: Simplest starting point for users
- `README.md`: Complete project overview
- `PLAY_THE_GAME.md`: How to play the game
- `game/index.html`: The actual game (double-click to play)

### Documentation
- `FEATURES_COMPLETE.md`: Complete feature list for the game
- `SUBMISSION_GUIDE.md`: Publishing information
- `ORGANIZATION_SUMMARY.md`: Repository organization notes
- `docs/PROJECT_ROADMAP.md`: Project planning
- `docs/AUTOMATION_GUIDE.md`: Automation notes

### Configuration
- `.github/workflows/jekyll-docker.yml`: Jekyll CI for GitHub Pages
- No other build configuration files exist

## Best Practices for Contributing

1. **Preserve the creative vision**: This is an artistic project with established lore and tone
2. **Maintain accessibility**: Keep language clear for non-technical users
3. **Test changes manually**: Open files to verify they work as expected
4. **Respect file organization**: Files are carefully organized into folders
5. **Keep it simple**: No need for complex tooling or frameworks
6. **Document thoroughly**: Other users may not be developers
7. **Maintain consistency**: Follow existing patterns in code, documentation, and lore

## Common Tasks

### Adding New Game Content
- For HTML version: Edit `game/game.js`
- For ChoiceScript: Add/modify files in `choicescript_game/scenes/`
- Ensure consistency with existing narrative and lore
- Test by playing through the relevant sections

### Updating Documentation
- Keep markdown formatting consistent
- Use clear headers and sections
- Include examples where helpful
- Maintain the friendly, accessible tone

### Adding Lore
- Add files to `lore/` directory
- Ensure consistency with existing worldbuilding
- Reference existing lore documents when relevant
- Update README files if adding significant content

## What NOT to Do

- ❌ Don't add build tools, package managers, or test frameworks unless explicitly requested
- ❌ Don't modify files in `archive/` - they're historical
- ❌ Don't change the core theme of "magic as collaboration"
- ❌ Don't make the documentation overly technical
- ❌ Don't commit large binary files or media assets without discussion
- ❌ Don't delete or dramatically reorganize existing content without explicit instruction

## Target Audience

The primary users of this repository are:
- The repository owner (creative writer and game designer)
- Potential beta testers and players
- Choice of Games community members
- Creative collaborators

Most are **not professional software developers** - keep this in mind for all changes.

## Questions or Uncertainties?

If you're unsure about:
- Whether a change fits the lore
- How to organize new content
- Whether to modify existing files

Ask the user for clarification rather than making assumptions. The creative vision and existing lore should be preserved.
