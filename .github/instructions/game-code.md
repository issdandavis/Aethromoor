---
applyTo: 
  - "game/**/*.js"
  - "choicescript_game/**/*.txt"
  - "choicescript_game/startup.txt"
---

# Game Code Instructions

## ChoiceScript Files

ChoiceScript files use a specific syntax for interactive fiction. When working with `.txt` files in `choicescript_game/`:

### Key Syntax Rules
- Use `*choice` for choice menus
- Use `*if`, `*else`, `*elseif` for conditionals
- Use `*set` to modify variables
- Use `*goto` and `*goto_scene` for navigation
- Use `*stat_chart` for displaying statistics
- Use `*achievement` for unlocking achievements

### Variable Naming
- Use lowercase with underscores: `collaboration_score`, `has_truth_sand`
- Boolean variables should be named clearly: `visited_glacier`, `achieved_partnership`
- Character relationship variables: `izack_relationship`, `aria_relationship`, `zara_relationship`

### Story Flow
- Each scene file should have a clear narrative arc
- Maintain the existing collaboration score system
- Preserve character relationship tracking
- Ensure all choices have meaningful consequences

### Testing ChoiceScript Changes
- Use ChoiceScript IDE or local server for testing
- Test all choice branches to ensure they work
- Verify `*goto` targets exist
- Check that variable references are correct

## HTML/JavaScript Game

The `game/game.js` file contains the story as a JavaScript object structure.

### Story Node Structure
```javascript
nodeName: {
    text: `HTML content with story text`,
    choices: [
        {
            text: "Choice text",
            next: 'nextNodeName',
            effects: { collaboration: +1, izack: +1 }
        }
    ]
}
```

### Important Conventions
- **Polly's comments**: Use `<span class="polly-comment">` for Polly's narrative voice
- **Node naming**: Use descriptive snake_case names: `first_lesson_start`, `glacier_discovery`
- **Choice effects**: Include `collaboration` score changes and character relationship impacts
- **Navigation**: Ensure `next` values reference existing nodes

### Game State Management
- The `gameState` object tracks:
  - `currentNode`: Current story position
  - `collaborationScore`: Main game metric
  - `relationships`: Character relationship scores
  - `choices`: Player choice history

### Testing HTML/JS Changes
1. Open `game/index.html` in browser
2. Open browser developer console
3. Test each choice path
4. Verify score calculations work
5. Check for JavaScript errors in console

## Narrative Consistency

### Character Voices
- **Polly**: Sarcastic, witty, meta-aware, but ultimately caring. Breaks the fourth wall occasionally
- **Izack Thorne**: Wise, patient, emphasizes listening over controlling magic
- **Aria Windcaller**: Precise, theory-focused, values understanding before action
- **Zara Thornheart**: Intuitive, connected to living magic, warm and encouraging

### Collaborative Magic Theme
- Choices should often present collaborative vs solo approaches
- Higher collaboration scores should feel rewarding narratively
- Magic works better when mages work together
- Respect for magical entities and realms is important

### Endings
The game has 14 endings tiered by achievement:
- Legendary tier (best outcomes)
- High achievement
- Success tier
- Standard tier
- Challenging tier

Maintain this structure when adding or modifying ending conditions.

## Common Pitfalls

❌ **Don't:**
- Break narrative continuity with established lore
- Add choices without considering collaboration score impact
- Create dead-end story paths without proper endings
- Forget to update both HTML and ChoiceScript versions when relevant
- Use ES6+ features in HTML version (stick to ES5 or widely supported ES6 for broad compatibility)

✅ **Do:**
- Maintain Polly's unique narrative voice
- Test all choice branches thoroughly
- Keep score changes meaningful and balanced
- Reference `lore/` for worldbuilding accuracy
- Use descriptive variable and node names

## Achievement System

When adding achievements (ChoiceScript version only):
```choicescript
*achievement breakthrough_collaboration visible 60 Breakthrough Collaboration
```

Achievement IDs should be:
- `breakthrough_collaboration`
- `truthbound_mage`
- `heartwood_guardian`
- `glacier_partner`
- `collaborative_master`

## Accessibility

- Ensure text is readable and well-structured
- Provide meaningful choice text (not just "Option A", "Option B")
- Maintain logical story flow for screen readers
- Use semantic HTML in the HTML version

## Version Parity

Major story content should exist in both versions:
- Core story beats and scenes
- Character interactions
- Key choices and their consequences
- Endings

Minor differences are acceptable:
- Technical implementation details
- Achievement display (ChoiceScript has built-in system)
- UI/UX presentation
