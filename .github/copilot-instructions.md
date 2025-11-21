# Copilot Instructions for Avalon Repository

## Project Overview

This repository contains **Polly's Wingscroll: The First Thread**, an interactive fiction game set in the Avalon Academy universe (part of The Spiral of Pollyoneth lore). The game exists in two versions:

1. **ChoiceScript Version** (`choicescript_game/`) - Professional version for publication to Choice of Games/Hosted Games
2. **HTML/JavaScript Version** (`game/`) - Standalone web version for instant play

## Repository Structure

```
Avalon/
├── choicescript_game/          # ChoiceScript version (main development focus)
│   ├── startup.txt            # Game configuration, achievements, variables
│   ├── scenes/                # All game scenes (.txt files)
│   └── README.md
├── game/                      # HTML/JS standalone version
│   ├── index.html
│   ├── game.js               # Game logic and story nodes
│   └── style.css
├── lore/                     # Worldbuilding documents
├── writing_drafts/           # Novel manuscripts
└── docs/                     # Additional documentation
```

## Core Conventions

### ChoiceScript Files (.txt)

- **Language**: ChoiceScript markup (not traditional programming)
- **File Extension**: `.txt` (required by ChoiceScript)
- **Comments**: Use `*comment` directive
- **Line Breaks**: Use `*line_break` or `*page_break`
- **Variables**: Set with `*set variable_name value` or `*set variable_name +10`
- **Choices**: Use `*choice` blocks with `#Option text` syntax
- **Labels**: Use `*label label_name` for navigation
- **Goto**: Use `*goto label_name` to jump between sections
- **Conditionals**: Use `*if`, `*elseif`, `*else` with proper indentation

#### Important ChoiceScript Syntax Rules:
- All commands start with `*`
- Indentation matters for conditionals and choices
- Use `${variable_name}` for variable interpolation
- Use `[i]text[/i]` for italics, `[b]text[/b]` for bold
- Scene files must be listed in `startup.txt` under `*scene_list`

### JavaScript/HTML Version

- **Style**: Modern ES6+ JavaScript
- **Structure**: Object-based story nodes with choices
- **State Management**: Single `gameState` object
- **Naming**: camelCase for variables and functions

## Key Variables and Stats

### Primary Stats (tracked in both versions):
- `collaboration` - Core theme stat (collaborative vs domination magic)
- `power` - Raw magical strength
- `knowledge` - Understanding of magical theory
- `empathy` - Connection to others and living magic

### Relationship Stats:
- `izack_relationship` - Bond with Izack Thorne (legendary mage)
- `aria_relationship` - Bond with Aria Ravencrest (scholar)
- `zara_relationship` - Bond with Zara (dragon-kin nature mage)
- `polly_relationship` - Bond with Polly (ancient raven familiar)

### Morality Axes (opposed pairs, 0-100):
- `communication_vs_domination` - How you approach magic (50 = balanced)
- `honesty_vs_deception` - Relationship with truth
- `tradition_vs_innovation` - Learning approach
- `individual_vs_collective` - Solo power vs collaboration

## Lore and Worldbuilding

### Core Concepts:
- **Avalon Academy**: Living pocket dimension where legendary mages teach collaborative magic
- **Dimensional Magic**: Magic based on communication with reality, not domination
- **The Spiral of Pollyoneth**: Larger universe this game is set in
- **Polly (Polymnia Aetheris)**: Ancient raven familiar, dimensional anchor, narrator with sarcastic personality

### Important Lore Elements:
- Collaborative magic is the core philosophy (Izack's approach)
- Magic responds to intention and connection, not just power
- The World Tree connects dimensions
- Leylines are magical currents that can be listened to
- Grey and Clayborn: golem creation is based on emotion and partnership
- Third Thread Mystery: Hidden lore about Zara, Alexander, and the Demon Child
- Varn'ka'zul: Demon realm (inverted reality from main lore)

## Testing and Validation

### ChoiceScript Version:
**NO automated build or test system exists.** Manual testing only:

1. Download ChoiceScript from https://www.choiceofgames.com/make-your-own-games/choicescript-intro/
2. Copy files from `choicescript_game/` to ChoiceScript's `web/mygame/` folder
3. Open ChoiceScript's `index.html` in a browser
4. Click through game to test changes
5. Check browser console for ChoiceScript errors

**Common ChoiceScript Errors to Avoid:**
- Missing scenes from `*scene_list` in `startup.txt`
- Incorrect indentation in `*choice` blocks
- Undefined variables (must be declared with `*create` in `startup.txt`)
- Missing `*goto` targets
- Syntax errors in conditionals (`*if` statements)

### HTML/JavaScript Version:
1. Open `game/index.html` directly in a browser
2. Check browser console for JavaScript errors
3. Click through game paths to verify changes
4. Test on multiple browsers if making significant changes

**No linters, build tools, or test frameworks are configured.**

## Publishing Requirements

### For Hosted Games Submission:
- ✅ Minimum 30,000 words (currently 30,238 in ChoiceScript)
- ✅ Must use ChoiceScript format
- ✅ Complete game with multiple endings (currently 14)
- ✅ Gender/pronoun selection included
- ✅ No AI-generated content
- ✅ Professional formatting

## Style Guidelines

### Writing Style:
- Polly's voice: Sarcastic, honest, occasionally meta, but caring underneath
- Izack's voice: Warm, wise, gentle, speaks with "dimensional resonance"
- Aria's voice: Precise, scholarly, passionate about knowledge
- Zara's voice: Warm, nature-connected, dragon-kin wisdom

### Code Comments:
- Use `*comment` in ChoiceScript files for section headers and explanations
- Use `// Comment` in JavaScript for explanations
- Comment major sections and scene transitions
- Explain complex stat calculations

### Formatting:
- ChoiceScript: Use `*line_break` between paragraphs for readability
- ChoiceScript: Use `*page_break` for major scene transitions
- JavaScript: Use consistent indentation (2 spaces)
- Keep choice text concise but descriptive

## Making Changes

### When adding new scenes:
1. Create new `.txt` file in `choicescript_game/scenes/`
2. Add scene name to `*scene_list` in `startup.txt` (alphabetical order)
3. Use `*finish` at the end to transition to next scene
4. Test thoroughly by playing through

### When adding new variables:
1. Declare in `startup.txt` with `*create variable_name value`
2. Document purpose in comments
3. Use consistent naming (lowercase with underscores for ChoiceScript)

### When modifying stats:
1. Consider impact on endings (many require specific stat thresholds)
2. Test different paths to ensure balance
3. Update stat descriptions if changing meaning

### When adding achievements:
1. Define in `startup.txt` with `*achievement` directive
2. Include pre_stat and post_stat text
3. Set visibility and point value
4. Grant with `*achieve achievement_name` when earned

## Common Workflows

### Adding a new character relationship:
1. Add `*create character_relationship 0` to `startup.txt`
2. Add stat to stats screen in `choicescript_stats.txt`
3. Increment/decrement in relevant choice blocks
4. Use in conditionals for character-specific content

### Creating a new ending:
1. Add ending scene in `endings.txt`
2. Use conditionals to check requirements
3. Consider: stats, relationships, choices made, items collected
4. Include achievement if appropriate
5. Test all paths that lead to this ending

### Balancing collaborative magic theme:
- Choices that involve listening/partnering should increase `collaboration`
- Choices that involve dominating/controlling should decrease `collaboration`
- High collaboration unlocks better endings
- Low collaboration doesn't mean failure, but different narrative

## Important Considerations

### Maintaining Lore Consistency:
- Polly is ancient (300+ years old) but not all-knowing
- Izack Thorne is legendary but humble about it
- Magic is about communication, not domination (core theme)
- The Academy is a living dimension, not just a building
- Reference existing lore documents when needed

### Preserving Game Balance:
- Don't make any ending too easy or too hard to achieve
- Ensure multiple viable paths to success
- Romance is optional, not required for best endings
- Failure should be narratively interesting, not punishment

### File Organization:
- Keep ChoiceScript scenes focused on one narrative section each
- Don't create files outside proper directories
- Update relevant README files when adding major features
- Don't modify lore documents without explicit instruction

## Security and Best Practices

- This is a creative writing project, not a web application
- No user data is collected or stored
- No backend services or APIs
- No dependencies to update (ChoiceScript is vendored)
- No build artifacts to commit
- Files are human-readable text

## When in Doubt

1. Manually test changes by playing the game
2. Check ChoiceScript syntax in browser console
3. Reference existing scenes for patterns
4. Maintain the core theme: collaborative magic and meaningful choices
5. Keep Polly's sarcastic-but-caring voice consistent
