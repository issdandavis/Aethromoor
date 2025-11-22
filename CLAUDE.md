# CLAUDE.md - AI Assistant Guide for Avalon Repository

This document provides guidance for AI assistants working with the Avalon/Spiral of Pollyoneth codebase.

## Project Overview

**Avalon** is a creative writing and interactive fiction project containing:
- A **choice-based narrative game** ("Polly's Wingscroll: The First Thread") set in Avalon Academy
- **Lore and worldbuilding materials** for the Spiral of Pollyoneth fantasy universe
- **Writing drafts** for a planned novel series

The game exists in two implementations:
1. **HTML/JavaScript version** (`game/`) - Instant play in browser
2. **ChoiceScript version** (`choicescript_game/`) - Professional format for publishing via Hosted Games

## Repository Structure

```
Avalon/
├── game/                       # HTML game version (instant play)
│   ├── index.html              # Main game file - open in browser to play
│   ├── game.js                 # Game logic, story nodes, state management
│   ├── style.css               # Game styling
│   ├── scenes/                 # ChoiceScript-format scene files
│   ├── bootstrap_choicescript.sh  # Clone official ChoiceScript engine
│   └── sync_scenes.sh          # Sync scenes to ChoiceScript engine
│
├── choicescript_game/          # ChoiceScript version (for publishing)
│   ├── startup.txt             # Game config, stats, character creation
│   └── scenes/                 # All game scenes (.txt files)
│       ├── arrival.txt         # Opening scene
│       ├── first_lesson.txt    # Magic lesson
│       ├── singing_dunes.txt   # Desert expedition
│       ├── verdant_tithe.txt   # Forest expedition
│       ├── rune_glacier.txt    # Glacier expedition
│       ├── endings.txt         # 14 unique endings
│       └── ...                 # Other scene files
│
├── lore/                       # Worldbuilding documents
│   ├── Pollys_Wingscrolls_Worldbuilding.markdown
│   └── *.txt, *.pdf            # Geography, magic systems, character lore
│
├── writing_drafts/             # Novel manuscript drafts
│   └── spiral-of-pollyoneth-novel.md
│
├── docs/                       # Project documentation
│   ├── AUTOMATION_GUIDE.md     # Zapier/integration workflows
│   ├── PROJECT_ROADMAP.md      # Development phases and milestones
│   ├── avalon_materials/       # Reference documents and PDFs
│   └── reference/              # Additional reference files
│
├── archive/                    # Historical/backup files
├── config/                     # Configuration templates
│   └── .env.example            # API key template
│
├── .github/
│   ├── workflows/jekyll-docker.yml  # CI for Jekyll site builds
│   └── agents/my-agent.agent.md     # GitHub Copilot agent config
│
├── README.md                   # Main project README
├── PLAY_THE_GAME.md           # Quick start for playing
├── SUBMISSION_GUIDE.md        # Publishing/submission info
└── QUICK_START.md             # Getting started guide
```

## Key Technologies

### Game Engines
- **ChoiceScript**: Text-based interactive fiction framework by Choice of Games
  - Uses `.txt` files with custom markup
  - Commands: `*choice`, `*goto`, `*set`, `*if`, `*create`, etc.
  - Documentation: https://www.choiceofgames.com/make-your-own-games/choicescript-intro/

- **HTML/JavaScript**: Custom implementation in `game/game.js`
  - Story nodes as JavaScript objects
  - State management for collaboration score and relationships

### Build Tools
- **Node.js**: Required for running ChoiceScript server
- **Bash scripts**: For setup and syncing (`bootstrap_choicescript.sh`, `sync_scenes.sh`)

## Development Workflows

### Playing the HTML Version
```bash
# Simply open in browser - no build required
open game/index.html
```

### Setting Up ChoiceScript Development
```bash
# 1. Clone official ChoiceScript engine
./game/bootstrap_choicescript.sh

# 2. Sync demo scenes
./game/sync_scenes.sh

# 3. Start server (from game/choicescript/)
cd game/choicescript
# Windows: run-server.bat
# macOS: ./serve.command
# Linux: bash serve.sh

# 4. Open http://localhost:4200/
```

### Editing Game Content
- **HTML version**: Edit `game/game.js` - modify `storyNodes` object
- **ChoiceScript version**: Edit files in `choicescript_game/scenes/`
- After editing ChoiceScript scenes: Run `./game/sync_scenes.sh` to refresh

## ChoiceScript Conventions

### File Structure
```
*comment Header comment
*title Game Title
*author Author Name

*scene_list
  startup
  scene1
  scene2

*create variable_name default_value

*label section_name
Text content here...

*choice
  #Option 1
    *set variable +10
    *goto next_section
  #Option 2
    *goto other_section
```

### Key Variables (from startup.txt)
- **Stats**: `collaboration`, `power`, `knowledge`, `empathy` (0-100)
- **Relationships**: `izack_relationship`, `aria_relationship`, `zara_relationship`, `polly_relationship`
- **Character**: `name`, `gender`, `he_she`, `him_her`, `his_her`
- **Paths**: `chosen_path`, `expedition_choice`, `artifact_earned`
- **Romance**: `izack_romance`, `aria_romance`, `zara_romance` (boolean)

### Naming Conventions
- Scene files: lowercase with underscores (e.g., `first_lesson.txt`)
- Variables: lowercase with underscores (e.g., `collaboration_score`)
- Labels: lowercase with underscores (e.g., `*label polite_approach`)

## Game Design Principles

### Core Themes
1. **Collaborative magic** - Success comes from working together
2. **Honesty and vulnerability** - The game rewards authentic choices
3. **Relationships matter** - Character bonds affect outcomes

### Stat Philosophy
- High collaboration score = better endings
- Relationship building unlocks special scenes
- Multiple valid paths through the game

### Endings (14 total)
- **Legendary Tier**: Collaborative Master, Glacier Partner, Heartwood Guardian
- **High Achievement**: Truthbound Mage, Runeweaver, Forestbound Guardian
- **Success Tier**: Collaborative Scholar, Balanced Mage, Humble Seeker
- **Standard Tier**: Boundary Specialist, Second Chance
- **Challenge Tier**: Humbled Student, Expelled, Standard Path

## Lore Reference

### Key Characters
- **Izack Thorne**: Dimensional mage, co-founder of Avalon Academy
- **Aria Ravencrest**: Boundary specialist, Izack's wife
- **Zara**: Hybrid student, first student at Avalon
- **Polly (Polymnia Aetheris)**: Ancient raven familiar, narrator

### Key Locations
- **Avalon Academy**: Living pocket dimension, main setting
- **Spiral Spire**: Central tower, convergence of leylines
- **Singing Dunes**: Desert biome, truth-testing sand
- **Verdant Tithe**: Sentient forest, Thoughtvines and Heartwood Tree
- **Rune Glacier**: Living ice inscribed with shifting runes

### Magic System
- **Third Thread**: Collaborative magic that transcends individual limits
- **Dimensional boundaries**: Membranes between realms
- **Leylines**: Magical energy currents

## Common Tasks

### Adding a New Scene
1. Create `.txt` file in `choicescript_game/scenes/`
2. Add scene name to `*scene_list` in `startup.txt`
3. Add `*goto_scene scene_name` from connecting scenes
4. Run `./game/sync_scenes.sh` if using ChoiceScript engine

### Adding a New Ending
1. Create ending label in `endings.txt` or relevant scene
2. Add ending type to `ending_type` variable
3. Include stat summary and narrative conclusion
4. Ensure `*ending` command at conclusion

### Adding a New Character Stat
1. Add `*create stat_name default` in `startup.txt`
2. Add to `choicescript_stats.txt` for display
3. Update relevant scenes to modify stat

### Modifying HTML Game
1. Edit `storyNodes` object in `game/game.js`
2. Add new node with `text`, `choices` array
3. Each choice needs `text`, `next`, and optional `effects`
4. Refresh browser to test

## Security Considerations

- **Never commit `.env` files** - Use `.env.example` as template
- **API keys**: Store only in local `.env`, never in tracked files
- Previous commits contained exposed keys - they have been removed
- If contributing: Rotate any keys that may have been exposed

## Testing

### Manual Testing
1. Play through all paths in HTML version
2. Verify stat changes work correctly
3. Test all 14 endings are reachable
4. Check for broken `*goto` references in ChoiceScript

### ChoiceScript Validation
- ChoiceScript engine reports syntax errors on load
- Check browser console for JavaScript errors
- Verify all scenes are listed in `*scene_list`

## CI/CD

- **GitHub Actions**: Jekyll site build on push to main (`.github/workflows/jekyll-docker.yml`)
- Future: Add ChoiceScript validation workflow

## Publishing Workflow

Target: **Hosted Games** (Choice of Games platform)
1. Complete all 14 endings
2. Beta test with community (2-4 weeks)
3. Submit via Hosted Games email
4. Wait for review (2-6 weeks)
5. Publication (4-6 months total timeline)

Requirements:
- 30,000+ word minimum (current: 40,000+)
- Complete game with all endings working
- Professional ChoiceScript formatting
- No AI-generated content in final submission

## Quick Reference

### Play the Game
```bash
# HTML version (instant)
open game/index.html

# ChoiceScript version
./game/bootstrap_choicescript.sh  # First time only
./game/sync_scenes.sh
cd game/choicescript && bash serve.sh
# Open http://localhost:4200/
```

### Key Files to Edit
- Game logic: `game/game.js` (HTML) or `choicescript_game/scenes/*.txt`
- Stats/config: `choicescript_game/startup.txt`
- Styling: `game/style.css`
- Lore: `lore/` directory

### Project Status
- **Phase**: Phase 2 - Complete ChoiceScript Game
- **Next Milestone**: Complete expedition scenes
- **Target**: Hosted Games publication

## Additional Resources

- [ChoiceScript Documentation](https://www.choiceofgames.com/make-your-own-games/choicescript-intro/)
- [Choice of Games Forum](https://forum.choiceofgames.com/)
- [Hosted Games Submission Guidelines](https://www.choiceofgames.com/looking-for-writers/)
- Project roadmap: `docs/PROJECT_ROADMAP.md`
- Automation guide: `docs/AUTOMATION_GUIDE.md`
