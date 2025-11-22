# 🎮 QUICK START GUIDE
## Polly's Wingscroll: The First Thread

**The bundled ChoiceScript web build is ready to play.** You can launch it locally or use an external IDE if you prefer.

---

## 🌟 OPTION 1: Play the Bundled ChoiceScript Build (Recommended)

### **Play immediately**

**Step 1: Open the packaged index:**
- On your computer, go to: `Avalon/choicescript_game/web/`
- Open `index.html` (it auto-redirects to the game)

**Step 2: If your browser blocks local files:**
- Run a quick local server from the same folder:
```
cd Avalon/choicescript_game/web
python3 -m http.server 8000
```
- Then open http://localhost:8000/ in your browser.

**Step 3: Smoke-check (1 minute):**
- Confirm the ChoiceScript UI renders (title, menu buttons, first page of text)
- If you see missing-script errors, refresh, then check `TROUBLESHOOTING.md`

**Features in this build:**
✅ Professional save/load system
✅ Stats screen (click "Show Stats")
✅ Achievements that pop up
✅ Multiple paths and endings
✅ Same feel as published games

### **Current Content:**
- Full game with 30+ scenes
- 14 unique endings
- 3 realm explorations
- 50+ meaningful choices

---

## 🌐 OPTION 2: Use an External IDE (CSIDE or Online ChoiceScript IDE)

If you prefer an IDE workflow or run into local security restrictions, use CSIDE or the official online IDE (see `TROUBLESHOOTING.md`).

### **CSIDE (Desktop) quick steps:**
- Install CSIDE from https://github.com/ChoicescriptIDE/main/releases
- Open `Avalon/choicescript_game/` as a project
- Press **Play Test**

### **Online ChoiceScript IDE quick steps:**
- Open https://www.choiceofgames.com/make-your-own-games/choicescript-intro/
- Launch **ChoiceScript IDE**
- Upload `startup.txt` and the `scenes/` folder from `Avalon/choicescript_game/`
- Click **Test** to run

---

## 📊 COMPARISON

| Feature | Bundled ChoiceScript | CSIDE/Online IDE |
|---------|----------------------|------------------|
| **Setup** | Open `choicescript_game/web/index.html` | Import project/files |
| **Feel** | Professional game | IDE preview |
| **Save/Load** | Built-in | Built-in |
| **Stats Screen** | Professional | Professional |
| **Publishing** | Suitable base | IDE-only |
| **Content** | Full game | Full game |

---

## 🎯 WHICH SHOULD YOU PLAY?

**Choose ChoiceScript if:**
- You want the "real game" experience
- You're interested in publishing to app stores
- You don't mind a small setup process
- You want professional features

**Choose HTML if:**
- You want to play RIGHT NOW
- You want the full content
- You don't want to download anything
- You just want a quick test

---

## 🎮 GAMEPLAY TIPS

**Your choices matter!**
- **Collaboration Score** determines which paths you can take
- **Relationships** with characters unlock special scenes
- **Different approaches** lead to completely different realms

**Multiple playthroughs recommended:**
- Try all 3 arrival approaches
- Explore each of the 3 biomes
- Aim for different endings

**Endings to discover:**
- Collaborative Master
- Truthbound Mage
- Forestbound Guardian
- Heartwood Guardian
- Runeweaver
- Glacier Partner
- And more!

---

## 🐛 TROUBLESHOOTING

### **ChoiceScript Build:**

**"The game won't load!"**
- Open the bundled launcher: `choicescript_game/web/index.html`
- If the browser blocks file access, run `python3 -m http.server 8000` in that folder and retry at http://localhost:8000/
- Refresh once if you saw a missing-script warning; the bundled `version.js` is included.

**"I see errors about missing scenes!"**
- Double-check the `*scene_list` in `startup.txt` matches the files in `choicescript_game/web/mygame/scenes/`
- Re-copy the `web/` folder from the repository if anything was modified locally.

**"Stats aren't showing!"**
- Click the "Show Stats" button in the game (upper right)
- If you edited stats, rerun the game after saving changes

### **Need CSIDE/IDE alternatives?**
- Jump to `TROUBLESHOOTING.md` for CSIDE/online IDE instructions and rebuild steps.

---

## 💾 SAVING YOUR PROGRESS

**ChoiceScript:**
- Automatic save system built-in
- Your progress persists between sessions
- Just reload and continue!

**HTML:**
- No built-in saves
- Play through in one session
- Or screenshot your choices to remember

---

## 🆘 NEED HELP?

**Check these files:**
- `TROUBLESHOOTING.md` - Alternative launch methods (CSIDE/IDE) and rebuild steps
- `choicescript_game/README.md` - ChoiceScript-specific notes
- `docs/AUTOMATION_GUIDE.md` - Advanced setup

**Resources:**
- ChoiceScript forums: https://forum.choiceofgames.com/
- Official tutorial: https://www.choiceofgames.com/make-your-own-games/

---

## 🚀 NEXT STEPS

**After playing:**
1. Try different paths to see all the content
2. Check out the lore documents in the repository
3. If you enjoyed it, consider:
   - Providing feedback
   - Beta testing new content
   - Contributing to development

---

## 📝 WHAT'S IN EACH VERSION

### **ChoiceScript (Professional Demo):**
```
✅ Title screen
✅ Character creation
✅ Polly's introduction
✅ 3 arrival paths (polite/curious/confident)
✅ Meeting Izack, Aria, or Zara
✅ First dimensional magic lesson
✅ Breakthrough/crisis scenarios
✅ Expedition selection
🚧 Singing Dunes (coming soon)
🚧 Verdant Tithe (coming soon)
🚧 Rune Glacier (coming soon)
🚧 14 endings (coming soon)
```

### **HTML (Full Game):**
```
✅ Everything above, PLUS:
✅ Complete Singing Dunes expedition
✅ Complete Verdant Tithe exploration
✅ Complete Rune Glacier journey
✅ All 14 unique endings
✅ Truthbound Mage path
✅ Forestbound Guardian path
✅ Heartwood Guardian path
✅ Runeweaver path
✅ Glacier Partner path
✅ And more!
```

---

## 🎊 READY TO PLAY!

Pick your version and dive into Avalon Academy!

**The spiral awaits...**

*"In a land where even flowers hum with magic, tread wisely – the ivy has ears and the crows have tales to tell."*

---

*For more information about The Spiral of Pollyoneth universe, explore the lore documents in this repository.*
