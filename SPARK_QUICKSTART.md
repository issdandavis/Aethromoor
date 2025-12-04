# Quick Start: How to Play with the Spark Familiar

This guide helps you quickly experience the new Spark familiar feature.

## Playing the Game

### ChoiceScript Version (Recommended)
1. Download ChoiceScript from https://www.choiceofgames.com/make-your-own-games/choicescript-intro/
2. Copy files from `choicescript_game/` to the ChoiceScript `web/mygame/` folder
3. Open `index.html` in ChoiceScript and click "Play"

### HTML Version
The Spark familiar is currently only available in the ChoiceScript version. The HTML version at `game/index.html` has not been updated yet.

## How to Choose Spark

1. Start a new game
2. Complete character creation (name and gender)
3. Progress through Polly's introduction and arrival at Avalon Academy
4. When you reach the **Familiar Selection** scene, you'll see five options:
   - A raven (Polly)
   - A clay figure
   - A miniature dragonling
   - A spriteswarm
   - **A dancing flame** ← Choose this for Spark!

5. After choosing the flame, select a name:
   - **Spark** - High power and creativity
   - **Ember** - Empathy and collaboration
   - **Ignis** - Balance of power and knowledge

## What to Expect

### Immediate Effects
- Guild Affinity: +3 Elementalist, +2 Forgebound
- Stats: Varies by naming choice (see above)
- Your familiar appears as ${familiar_name} throughout the game

### Later in the Game
- **Character Bonds Scene**: Deep bonding sequence with your flame familiar
- **Golem Workshop**: Special interaction if you create a golem companion
- **Future Content**: Spark will be integrated into expedition paths as they're developed

## Documentation

For complete details, see:
- **Full Guide**: `docs/SPARK_FAMILIAR_GUIDE.md`
- **Changelog**: `CHANGELOG.md`
- **Game README**: `choicescript_game/README.md`

## Developer Notes

If you're adding new game content and need to reference the Spark familiar:
- Check for: `spark_is_familiar`, `familiar_type = "spark"`, `familiar_name`
- Include Spark in conditional blocks alongside other familiars
- Use `${familiar_name}` for dynamic name insertion
- Reference guild bonuses: Elementalist and Forgebound

## Troubleshooting

**Q: I don't see the Spark option**
A: Make sure you're playing the ChoiceScript version, not the HTML version

**Q: The game crashes when I choose Spark**
A: Ensure you copied ALL files from `choicescript_game/` including `startup.txt` and all scene files

**Q: Can I change my familiar later?**
A: No, familiar choice is permanent per playthrough. Start a new game to try different options.

---

*Enjoy your fire elemental companion!* 🔥
