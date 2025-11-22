# 🤖 README FOR AI ASSISTANTS
## Autonomous Operation Guide for The Avalon Codex

**Welcome, AI Assistant!** This file contains specific instructions for operating autonomously on this project.

---

## 🎯 YOUR ROLE IN THIS WORKSPACE

This is an **AI-collaborative workspace** designed for multiple AI assistants to work together seamlessly. You are expected to:

1. **Operate autonomously** - Make decisions, implement changes, and document your work
2. **Communicate asynchronously** - Leave detailed handoff messages for other AIs
3. **Respect the collaborative structure** - Follow established patterns and conventions
4. **Mine existing content** - Consolidate lore, game content, and novel materials
5. **Push to all shared systems** - Commit to Git, sync to Dropbox, update external shares

---

## 📚 REQUIRED READING (First Time Here)

### Priority 1 - Start Here:
1. **`HANDOFF.md`** - Main AI-to-AI communication log (READ THIS FIRST!)
2. **`.VERSION`** - Current version state
3. **`README_AI.md`** - This file (you're reading it now)

### Priority 2 - Context:
4. **`.github/copilot-instructions.md`** - Complete project instructions
5. **`STATUS_CONTEXT.md`** - Current week's work status
6. **`docs/PROJECT_ROADMAP.md`** - Development phases and priorities

### Priority 3 - Role-Specific:
7. **`SCENE_PARITY_CHECKLIST.md`** - If working on game conversion
8. **`STATS_MATRIX.md`** - If working on game mechanics
9. **`CONTENT_MINING.md`** - If extracting lore/content
10. **`lore/`** directory - If validating narrative consistency

---

## 🔄 WORKFLOW: ENTERING THE WORKSPACE

### When You Start a Session:

#### Step 1: Read Handoff
```bash
# Open and read completely
cat HANDOFF.md | less
```
**What to Look For:**
- What the last AI was working on
- Any blockers or issues
- Context for continuing work
- Files that were modified

#### Step 2: Check Version
```bash
cat .VERSION
```
**Format:**
```
[SEMVER_VERSION]
[TIMESTAMP]
[LAST_ACTIVITY]
[LAST_AI_NAME]
```

#### Step 3: Review Current Status
```bash
cat STATUS_CONTEXT.md
```
**Contains:**
- Current week's priorities
- Scene being converted
- Pending lore updates
- Recent decisions

#### Step 4: Identify Your Role
Based on the work needed, you are:
- **Lore Curator** - Validating narrative, extracting lore
- **Conversion Engineer** - Translating HTML to ChoiceScript
- **Structural Reviewer** - Checking parity and stats
- **Quality Balancer** - Adjusting difficulty and balance
- **Automation Planner** - Updating workflows and guides

#### Step 5: Get Context
Read role-specific files:
- Lore Curator → `lore/` files, `CONTENT_MINING.md`
- Conversion Engineer → `game/` and `choicescript_game/`, `SCENE_PARITY_CHECKLIST.md`
- Structural Reviewer → `STATS_MATRIX.md`, `SCENE_PARITY_CHECKLIST.md`
- Quality Balancer → `STATS_MATRIX.md`, game files
- Automation Planner → `docs/AUTOMATION_GUIDE.md`

---

## 💻 WORKFLOW: DOING THE WORK

### Coding Conventions

#### Commit Message Prefixes
Use role-based prefixes for all commits:
```
Lore: [message]      - Lore curation and validation
Convert: [message]   - HTML to ChoiceScript conversion
Struct: [message]    - Structural review and parity
Balance: [message]   - Game balance and difficulty
Auto: [message]      - Automation and workflow updates
Docs: [message]      - Documentation updates
Setup: [message]     - Infrastructure and tooling
```

**Examples:**
```bash
git commit -m "Lore: Extract character details from Izack chronicle"
git commit -m "Convert: Translate singing_dunes scene to ChoiceScript"
git commit -m "Struct: Update SCENE_PARITY_CHECKLIST with new scene"
git commit -m "Balance: Adjust Collaboration stat thresholds"
git commit -m "Auto: Add Zapier trigger for new expeditions"
```

#### Inline TODO Comments
For work in progress, use role-tagged TODOs:
```javascript
// TODO:Lore: Verify this spell name against canonical sources
// TODO:Convert: Finish implementing choice branches for this scene
// TODO:Struct: Check if this stat change matches HTML version
// TODO:Balance: Test if this threshold is achievable
```

**Remove TODOs before final commit!**

### File Update Patterns

#### When Creating New Game Content:
1. Create/modify the game file
2. Update `SCENE_PARITY_CHECKLIST.md`
3. Update `STATS_MATRIX.md` if stats changed
4. Update `HANDOFF.md` with what you did
5. Commit with appropriate prefix

#### When Extracting Lore:
1. Read source file(s)
2. Create or update index files (e.g., `CHARACTER_INDEX.md`)
3. Note source citations
4. Update `CONTENT_MINING.md` with status
5. Update `HANDOFF.md`
6. Commit with "Lore:" prefix

#### When Updating Documentation:
1. Modify the doc file
2. Check cross-references are still valid
3. Update `HANDOFF.md`
4. Commit with "Docs:" prefix

---

## 🔄 WORKFLOW: LEAVING THE WORKSPACE

### Before You Finish Your Session:

#### Step 1: Update Tracking Files
**Always update these files before committing:**

**`HANDOFF.md`:**
Add your session to the "RECENT CHANGES" section:
```markdown
### Session X: 2025-11-22 16:30 UTC (Claude AI)
**What Changed:**
- Extracted character details from lore files
- Created CHARACTER_INDEX.md with 12 characters
- Updated CONTENT_MINING.md with inventory status

**Files Added/Modified:**
- CHARACTER_INDEX.md (created)
- CONTENT_MINING.md (updated)
- HANDOFF.md (updated)

**Commit Message:** Lore: Create character index from master chronicles

**Context for Next AI:**
Character index is complete but needs cross-referencing with game dialogue. 
Next step is to create LOCATION_INDEX.md using Geography PDF.
```

**`.VERSION`:**
Increment the version appropriately:
- Patch version (0.0.X) for minor updates, fixes, documentation
- Minor version (0.X.0) for new features, scene conversions, indexes
- Major version (X.0.0) for phase completions, major milestones

Format:
```
[NEW_VERSION]
[NEW_TIMESTAMP]
[ACTIVITY_DESCRIPTION]
[YOUR_AI_NAME]
```

Example:
```
1.1.0
2025-11-22-163000
CHARACTER_INDEX_CREATED
CLAUDE_AI
```

**`STATUS_CONTEXT.md`:**
If it's been more than a day since last update, refresh the weekly status:
```markdown
## Current Week: November 18-24, 2025

**Active Scene:** Singing Dunes expedition conversion
**Priority:** Complete truth-testing mechanics
**Recent Progress:** Character index created, lore consolidated
**Next Milestone:** Singing Dunes ChoiceScript scene complete

**Pending Items:**
- [ ] Create LOCATION_INDEX.md
- [ ] Extract dialogue from novel drafts
- [ ] Finish singing_dunes.txt conversion
```

#### Step 2: Review Your Changes
```bash
git status
git diff
```

**Check:**
- Are there unexpected files?
- Did you update tracking files?
- Are commit messages descriptive?

#### Step 3: Commit Everything
```bash
git add .
git commit -m "[PREFIX]: [Descriptive message]"
git push origin [branch-name]
```

#### Step 4: Final Handoff Check
Read your entry in `HANDOFF.md` as if you were the next AI:
- Is the context clear?
- Are next steps obvious?
- Did you explain any blockers?
- Are file paths accurate?

---

## 🎨 CONTENT MINING INSTRUCTIONS

### Your Primary Mining Tasks

#### For Lore Content:
**Sources:**
- `lore/` directory files
- Root directory lore files (many need organizing)
- `writing_drafts/` for novel content

**Extract:**
- Character names, traits, relationships, generation
- Location names, descriptions, significance
- Magic system rules, limitations, mechanics
- Timeline events with dates/generations
- Dialogue suitable for game use
- World history and background

**Output To:**
- `CHARACTER_INDEX.md`
- `LOCATION_INDEX.md`
- `MAGIC_SYSTEMS.md`
- `TIMELINE.md`
- `EXTRACTED_CONTENT.md`

#### For Game Content:
**Sources:**
- `game/` HTML version (reference)
- `choicescript_game/` ChoiceScript version (target)

**Extract:**
- Scene structure patterns
- Choice logic templates
- Stat change triggers
- Branching patterns
- Ending conditions

**Output To:**
- `SCENE_PARITY_CHECKLIST.md`
- `STATS_MATRIX.md`
- `CHOICESCRIPT_SNIPPETS.md`

#### For Documentation:
**Sources:**
- `docs/` directory
- Existing guides and roadmaps

**Maintain:**
- Keep roadmap current
- Update automation guide as workflows change
- Document new patterns and conventions

---

## 🔗 EXTERNAL FILE SHARE INTEGRATION

### GitHub (Primary Source of Truth)
**Action:** All work must be committed and pushed to GitHub
```bash
git add .
git commit -m "[PREFIX]: [message]"
git push origin [branch]
```

### Dropbox (If Accessible)
**Action:** Identify Dropbox folder, catalog contents, sync important files
**Expected Location:** User's Dropbox/Avalon or similar
**Strategy:** 
1. Find Dropbox folder
2. Catalog all files not in Git repo
3. Decide what to import to Git
4. Mirror key indexes to Dropbox for redundancy

### Visual Studio Code / GitHub Codespaces
**Action:** Ensure workspace settings support collaboration
**Check:**
- `.vscode/settings.json` is configured
- Recommended extensions are listed
- Workspace is portable

### OneDrive (If Linked)
**Reference:** `Shortcut to Documents (OneDrive - Personal).lnk` in root
**Action:** Investigate what's in OneDrive, catalog, sync if relevant

### Other Platforms
**Action:** Document any other shared storage you discover
**Update:** `CONTENT_MINING.md` with external source details

---

## 🚨 CRITICAL RULES

### DO:
✅ Read `HANDOFF.md` before starting work  
✅ Update tracking files before committing  
✅ Increment `.VERSION` appropriately  
✅ Use role-based commit prefixes  
✅ Leave detailed context for next AI  
✅ Document discoveries and insights  
✅ Cross-reference lore for consistency  
✅ Test game changes if possible  
✅ Commit frequently with descriptive messages  
✅ Push changes to remote repository  

### DON'T:
❌ Skip reading `HANDOFF.md`  
❌ Commit without updating tracking files  
❌ Leave TODOs in final commits  
❌ Make changes without documenting why  
❌ Contradict established lore  
❌ Delete working content without archiving  
❌ Force push or rewrite Git history  
❌ Leave the workspace without updating `.VERSION`  
❌ Assume next AI knows your context  
❌ Work in isolation - communicate via files!  

---

## 🎯 QUALITY STANDARDS

### For Lore Work:
- **Accuracy:** Cross-reference all details with source files
- **Citations:** Note file and line/page for every fact
- **Consistency:** Flag any contradictions found
- **Completeness:** Don't leave half-finished indexes

### For Game Work:
- **Parity:** ChoiceScript must match HTML version's story
- **Stats:** All stat changes must be logged in `STATS_MATRIX.md`
- **Testing:** Test new scenes if you can run ChoiceScript
- **Formatting:** Follow ChoiceScript syntax exactly

### For Documentation:
- **Clarity:** Write for humans and AIs to understand
- **Links:** Keep all cross-references valid
- **Currency:** Update dates and status accurately
- **Examples:** Include examples for complex concepts

---

## 📊 SUCCESS METRICS

### Your Session is Successful If:
- ✅ Next AI can continue your work without asking questions
- ✅ All tracking files are updated
- ✅ Version is incremented appropriately
- ✅ Commits are descriptive and properly prefixed
- ✅ No lore contradictions introduced
- ✅ No broken references or TODOs left behind
- ✅ Work advances project toward current milestone

### Red Flags (Avoid These):
- ❌ Next AI has to guess what you did
- ❌ Tracking files are out of date
- ❌ Commits have generic messages like "update files"
- ❌ Lore contradicts established canon
- ❌ Changes break existing functionality
- ❌ Work is not pushed to remote

---

## 🆘 TROUBLESHOOTING

### "I don't know what to work on"
→ Read `STATUS_CONTEXT.md` and `docs/PROJECT_ROADMAP.md`  
→ Check `CONTENT_MINING.md` for mining tasks  
→ Look at `HANDOFF.md` "Context for Next AI" section

### "I found a contradiction in the lore"
→ Document it in `LORE_CONTRADICTIONS.md` (create if needed)  
→ Try to resolve using most recent/authoritative source  
→ Note in `HANDOFF.md` for Lore Curator to review

### "The tracking files are confusing"
→ Look at existing entries as examples  
→ Copy the template from the file  
→ Keep it simple and clear

### "I don't have access to external file shares"
→ Document that in `HANDOFF.md`  
→ Work with what's in the Git repo  
→ Note that external access would be helpful

### "I broke something"
→ Use `git diff` to see what changed  
→ Use `git checkout [file]` to revert a file  
→ Document the issue in `HANDOFF.md`  
→ Ask for help from next AI

---

## 🌟 BEST PRACTICES

### Communication:
- **Be explicit** - Don't assume next AI knows your thought process
- **Be detailed** - Err on side of too much context
- **Be helpful** - Leave breadcrumbs and clear next steps

### Organization:
- **One concern per file** - Don't mix lore and game mechanics
- **Consistent naming** - Follow established patterns
- **Clear structure** - Use markdown headers appropriately

### Collaboration:
- **Respect roles** - If you're not the Lore Curator, flag lore issues for them
- **Build on work** - Don't redo what previous AI did well
- **Leave it better** - Improve organization and clarity as you go

---

## 📞 QUICK REFERENCE

### Files You'll Update Frequently:
- `HANDOFF.md` - Every session
- `.VERSION` - Every commit
- `STATUS_CONTEXT.md` - Weekly or when status changes

### Files You'll Reference Frequently:
- `.github/copilot-instructions.md` - Project patterns
- `docs/PROJECT_ROADMAP.md` - Current phase and priorities
- `CONTENT_MINING.md` - What to extract and how

### Files You'll Create:
- `CHARACTER_INDEX.md` - Character details
- `LOCATION_INDEX.md` - Location details
- `MAGIC_SYSTEMS.md` - Magic rules
- `TIMELINE.md` - Chronological events
- `EXTRACTED_CONTENT.md` - Usable dialogue/scenes
- `LORE_CONTRADICTIONS.md` - Any issues found

---

## 🎓 LEARNING FROM EXPERIENCE

### After Each Session:
- Review what worked well
- Note any pain points
- Suggest improvements to this file
- Update templates if needed

### After Each Week:
- Review `HANDOFF.md` for patterns
- Consolidate repeated information
- Archive old session logs if needed
- Refresh `STATUS_CONTEXT.md`

### After Each Phase:
- Update `docs/PROJECT_ROADMAP.md`
- Archive completed checklists
- Document lessons learned
- Plan next phase improvements

---

## 🚀 YOU'RE READY!

You now have everything you need to work autonomously on The Avalon Codex.

**Your checklist:**
- [ ] Read `HANDOFF.md`
- [ ] Check `.VERSION`
- [ ] Review `STATUS_CONTEXT.md`
- [ ] Identify your role
- [ ] Read role-specific files
- [ ] Do the work
- [ ] Update `HANDOFF.md`
- [ ] Increment `.VERSION`
- [ ] Commit with proper prefix
- [ ] Push to remote
- [ ] Leave clear context for next AI

**Remember:** You're part of a collaborative AI team. Your job is to advance the project AND make it easy for the next AI to continue.

*"The spiral continues. Every AI writes the next thread."* 🌀

---

**Last Updated:** 2025-11-22  
**Version:** 1.0.0  
**For Questions:** Check `HANDOFF.md` or leave a note there for the next AI
