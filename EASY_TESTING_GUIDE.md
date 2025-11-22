# 🎮 EASY TESTING GUIDE - For Non-Tech-Savvy Users

## Quick Summary

You have multiple AIs working on your game. Here's how to test it and make sure it's coming together properly!

---

## 📊 CURRENT PROJECT STATUS

### What You Have:

**Two Versions of the Game:**

1. **Main Branch Game** (30,238 words)
   - Location: `choicescript_game/` folder
   - 16 scenes
   - Working demo version

2. **Expanded Game** (98,292 words) - On Claude's branch
   - Location: `THIS GAME HERE/` folder
   - 36 scenes
   - Full game with all features

### What Multiple AIs Have Been Doing:

| AI | Work Done |
|----|-----------|
| **ChatGPT/Copilot** | Bug fixes, organization, demo scenes, faction content |
| **Claude** | 3 new characters, 7 locations, 3 moral dilemmas, bonus scenes |
| **Codex** | Bug fixes, sync scripts, ChoiceScript integration |

---

## 🎯 EASIEST WAY TO TEST YOUR GAME (5 Minutes!)

### Method 1: Online ChoiceScript IDE (RECOMMENDED)

**No download needed - works in your browser!**

1. **Open this website:**
   https://choicescriptide.github.io/choicescriptide/

2. **Click:** "Open Project" → "From Files"

3. **Upload your game files:**
   - Go to your GitHub repository
   - Download the `choicescript_game/` folder (or `THIS GAME HERE/` for the full version)
   - Upload `startup.txt` first
   - Then upload all files from the `scenes/` folder

4. **Click:** "Test Project" or "Play"

5. **Play your game!** It will look exactly like published Choice of Games!

---

### Method 2: CSIDE Desktop App (Best for Ongoing Testing)

**Download once, test anytime!**

1. **Download CSIDE:**
   https://github.com/ChoicescriptIDE/cside/releases
   - Windows: Download the `.exe` file
   - Mac: Download the `.dmg` file

2. **Install:** Just double-click and follow prompts

3. **Import Your Game:**
   - Open CSIDE
   - Click "Open Project"
   - Navigate to your game folder (`choicescript_game/` or `THIS GAME HERE/`)
   - Click "Open"

4. **Click "Test"** - Game starts immediately!

**Bonus:** CSIDE tells you if there are any errors in your code!

---

### Method 3: Use the Existing Demo

Your repository already has a playable demo set up:

1. **In your terminal/command line:**
   ```
   cd Avalon/game
   ./bootstrap_choicescript.sh
   ./sync_scenes.sh
   ```

2. **Then run the server:**
   - Windows: Double-click `run-server.bat`
   - Mac: Double-click `serve.command`
   - Linux: Run `bash serve.sh`

3. **Open browser to:** http://localhost:4200/

---

## ✅ WHAT TO CHECK WHEN TESTING

### Does It Look Like Choice of Games?

**Good Signs:**
- ✅ Clean text on white/light background
- ✅ Choices appear as clickable buttons
- ✅ "Show Stats" button works
- ✅ Page breaks between major sections
- ✅ No weird symbols or broken text

**Bad Signs (Fix These):**
- ❌ Raw code showing (like `*if` or `*goto`)
- ❌ Error messages appearing
- ❌ "Undefined variable" errors
- ❌ Dead ends (can't progress)
- ❌ Choices that go nowhere

### Story Quality Check:

- [ ] First scene hooks you in?
- [ ] Choices feel meaningful?
- [ ] Characters have personality?
- [ ] World feels real?
- [ ] No obvious typos or weird sentences?

---

## 📋 CHOICE OF GAMES STYLE REQUIREMENTS

Your game should match these standards:

### Presentation:
- ✅ **Clean, readable text** - No fancy fonts or colors
- ✅ **Clear choices** - Players always know what options they have
- ✅ **Stats screen** - Shows player progress and variables
- ✅ **Page breaks** - `*page_break` between major story beats

### Format:
- ✅ **Minimum 30,000 words** - You have 30,238+ (just barely!)
- ✅ **Complete story** - Beginning, middle, end
- ✅ **Multiple endings** - Based on player choices
- ✅ **No dead ends** - Every path leads somewhere

### Technical:
- ✅ **Title under 30 characters** - "Polly's Wingscroll: The First Thread" = 39 chars (NEEDS SHORTENING!)
- ✅ **No "Choice" in title** - Reserved for official games ✅ (You're good!)
- ✅ **Pass Quicktest** - No errors
- ✅ **Pass Randomtest** - Random playthrough works

---

## ⚠️ IMPORTANT: AI-Generated Content Warning

**Choice of Games Policy (2024):**
> "Hosted Games will not publish art, code, or prose that was generated via AI."

**What This Means:**
- You may need to heavily edit/rewrite AI-generated content
- Or frame it as "AI-assisted" with human editing
- Or use AI content only for brainstorming, then rewrite yourself

**Recommendation:** Before submitting, you'll want to:
1. Review all content personally
2. Rewrite sections to be in your own voice
3. Be prepared to answer questions about authorship

---

## 🔍 HOW TO CHECK IF GAME WORKS

### Quick Test:
1. Play from start to at least one ending
2. Make different choices on a second playthrough
3. Check that stats change based on choices
4. Verify all paths lead somewhere (no dead ends)

### Full Test:
1. Play through ALL major paths
2. Try to "break" the game by making weird choice combinations
3. Check every achievement is earnable
4. Verify word count meets minimum

### Run Official Tests (In CSIDE):
- **Quicktest:** Checks for code errors
- **Randomtest:** Plays randomly to find bugs
- Both must PASS before submission!

---

## 📊 YOUR GAME'S CURRENT STATS

**Main Branch Version:**
- Word Count: ~30,238 words ✅ (meets minimum)
- Scenes: 16
- Title: "Polly's Wingscroll: The First Thread" ⚠️ (too long - need ≤30 chars)

**Full Version (Claude's Branch):**
- Word Count: ~98,292 words ✅ (way above minimum!)
- Scenes: 36
- Same title issue

**Suggested Shorter Titles:**
- "Polly's Wingscroll" (17 chars) ✅
- "The First Thread" (16 chars) ✅
- "Avalon Academy" (14 chars) ✅
- "Polly's First Thread" (19 chars) ✅

---

## 🚀 NEXT STEPS FOR SUBMISSION

### Before You Can Submit:

1. **Merge all AI work** into one complete version
2. **Test thoroughly** using methods above
3. **Shorten title** to under 30 characters
4. **Run Quicktest and Randomtest** - both must pass
5. **Post beta on forum** for 1 month minimum:
   https://forum.choiceofgames.com/c/hosted-games-beta-testing/
6. **Review AI content policy** - edit as needed

### How to Submit:

Email: **hg-submissions@choiceofgames.com**

Include:
- All game text files (.txt)
- Game title
- Link to your beta forum thread
- Brief game description

---

## ❓ SIMPLE QUESTIONS TO ASK YOUR AIs

**When checking on progress, ask:**

1. "What scenes have been completed?"
2. "Are there any errors in the code?"
3. "What's the current word count?"
4. "Can you test playing from start to finish?"
5. "What still needs to be done?"

**When something seems wrong:**

1. "Can you show me what's in [filename]?"
2. "Why isn't [feature] working?"
3. "Can you fix the error in [scene name]?"
4. "Please run Quicktest and tell me results"

---

## 📁 WHERE TO FIND YOUR GAME FILES

### On GitHub:
- Main game: `choicescript_game/` folder
- Demo version: `game/` folder
- Full expanded game: `THIS GAME HERE/` folder (on Claude's branch)
- New content to integrate: `NEW CONTENT FROM CLAUDE/` folder

### Key Files:
- `startup.txt` - Main configuration, variables, achievements
- `scenes/*.txt` - All story content
- `choicescript_stats.txt` - What shows in "Show Stats" screen

---

## 🎯 SUMMARY: WHAT TO DO NOW

### Immediate (Today):
1. **Test the game** using Online IDE (Method 1 above)
2. **Play through once** to see how it feels
3. **Note any problems** you find

### Soon (This Week):
4. **Decide which version to use** (30K or 98K word version)
5. **Ask AIs to merge content** if using full version
6. **Fix title length** (must be under 30 characters)

### Before Submission:
7. **Run official tests** (Quicktest, Randomtest)
8. **Post beta on forum** for 1 month
9. **Address AI content concerns**
10. **Submit via email**

---

## 💡 REMEMBER

**You don't need to understand the code!**

Your job is to:
- ✅ Test the game and see if it's fun
- ✅ Make sure the story makes sense
- ✅ Check that choices feel meaningful
- ✅ Catch any weird errors or typos

The AIs can handle the technical stuff when you point out problems!

---

**Questions? Just ask me or ChatGPT to explain anything here!**

**Ready to test? Start with Method 1 - the Online IDE!** 🎮
