# 🚀 WORKFLOW IMPROVEMENTS FOR AVALON PROJECT

**@ @issdandavis - READ THIS FOR IMPORTANT WORKFLOW SUGGESTIONS**

## **BOLD SUGGESTION #1: STORY CONTENT PIPELINE**

### **CURRENT PROCESS NEEDS IMPROVEMENT:**
Story content is scattered across multiple directories with inconsistent naming and no clear pipeline from lore → game scenes.

### **RECOMMENDED WORKFLOW:**

1. **LORE VAULT (Single Source of Truth)**
   - **@ @issdandavis**: Move ALL canonical lore files to `/lore/` directory
   - Create subdirectories: `/lore/characters/`, `/lore/locations/`, `/lore/magic-system/`, `/lore/history/`
   - **ACTION REQUIRED**: Consolidate duplicate files like "The Spiral of Avalon.txt" (appears in 3 locations)

2. **STORY STAGING AREA**
   - Use `/writing_drafts/` ONLY for work-in-progress narrative content
   - **@ @issdandavis**: Create `/writing_drafts/ready-for-game/` for scenes approved for implementation
   - Create `/writing_drafts/brainstorming/` for experimental ideas

3. **GAME IMPLEMENTATION**
   - Maintain clear separation between `/game/scenes/` (main game) and `/choicescript_game/scenes/` (ChoiceScript version)
   - **@ @issdandavis**: Add a `SCENE_TEMPLATE.txt` file to guide consistent scene structure

---

## **BOLD SUGGESTION #2: AUTOMATION WITH sync_scenes.sh**

### **CURRENT STATE:**
The `sync_scenes.sh` script exists but its purpose and usage aren't documented.

### **RECOMMENDED IMPROVEMENTS:**

**@ @issdandavis - IMMEDIATE ACTION NEEDED:**

```bash
# Document sync_scenes.sh in README.md
# Add usage instructions
# Consider expanding it to:
#   1. Validate scene syntax
#   2. Check for lore consistency
#   3. Auto-generate scene graph/flowchart
#   4. Sync between game formats
```

**NEW SCRIPT SUGGESTION**: Create `validate_lore.sh` to:
- Check for contradictions between lore files
- Identify orphaned references in game scenes
- Generate lore index for easy reference

---

## **BOLD SUGGESTION #3: GITHUB ORGANIZATION**

### **@ @issdandavis - CRITICAL CLEANUP NEEDED:**

**FILES TO ARCHIVE/ORGANIZE:**
- `87357.docx`, `Document.docx` - Move to `/archive/` or rename descriptively
- `DAO Ultimate Addins Updater.log`, `DAOriginsConfigReport2022-10-22.xml` - Move to `/archive/game-dev-tools/`
- `typaxosakiecollab.flp`, `Osakie X TyPa Productions.flp` - Music files? Move to `/assets/music/`
- `next court date.txt`, `not ures.txt`, `notes.txt`, `notes2.txt`, `numbers.txt` - DELETE or move to personal directory (not repo)
- `Shortcut to Documents (OneDrive - Personal).lnk` - DELETE (not needed in repo)
- Various `.url` files - Consolidate into `/docs/USEFUL_LINKS.md`

**@ @issdandavis**: **RECOMMENDED DIRECTORY STRUCTURE:**

```
Avalon/
├── lore/                    # Single source of truth for canon
│   ├── characters/
│   ├── locations/
│   ├── magic-system/
│   └── history/
├── game/                    # Main game implementation
│   ├── scenes/
│   ├── assets/
│   └── README.md
├── choicescript_game/       # ChoiceScript version
├── writing_drafts/          # Work-in-progress only
│   ├── ready-for-game/
│   └── brainstorming/
├── docs/                    # Project documentation
├── assets/                  # Images, music, etc.
│   ├── music/
│   ├── images/
│   └── fonts/
├── archive/                 # Historical/deprecated files
├── .github/                 # GitHub automation
│   ├── workflows/
│   └── ISSUE_TEMPLATE.md
└── README.md
```

---

## **BOLD SUGGESTION #4: AI COLLABORATION STRUCTURE**

### **@ @issdandavis - ESTABLISH CLEAR ROLES:**

**Recommended AI Agent Roles:**

1. **@claude** → **Narrative Content Creator**
   - Focus: Writing story content, dialogue, descriptions
   - Access: Full lore vault read access
   - Output: Polished scenes in `/writing_drafts/ready-for-game/`

2. **@copilot** → **Technical Implementation & GitHub Organization**
   - Focus: Code structure, automation, organization, PR management
   - Access: Repository-wide
   - Output: Working game features, organized structure

3. **@issdandavis** → **Creative Director & Canon Keeper**
   - Focus: Final approval, vision alignment, lore consistency
   - Creates: Lore foundations, high-level direction

**@ @issdandavis - CREATE THESE FILES:**
- `.github/AI_COLLABORATION_GUIDE.md` - Define each agent's role clearly
- `lore/CANON_CHECKLIST.md` - Quick reference for what's canonical
- `CONTRIBUTING.md` - Guide for how AI agents should contribute

---

## **BOLD SUGGESTION #5: VERSION CONTROL BEST PRACTICES**

### **@ @issdandavis - BRANCHING STRATEGY:**

```
main (protected)
  ├── dev (integration branch)
  │     ├── feature/new-scene-name
  │     ├── lore/character-development
  │     └── docs/organization-update
  └── release/v1.0
```

**RECOMMENDED COMMIT STRUCTURE:**
- `feat: Add new convergence scene with enhanced lore`
- `lore: Update Izack Thorne backstory`
- `docs: Reorganize lore directory structure`
- `fix: Correct timeline inconsistency in prologue`
- `chore: Archive deprecated files`

**@ @issdandavis - USE PR TEMPLATES:**
Create `.github/PULL_REQUEST_TEMPLATE.md` with:
- [ ] Lore consistency checked
- [ ] No contradictions with existing canon
- [ ] Scenes tested in game engine
- [ ] Documentation updated

---

## **BOLD SUGGESTION #6: DOCUMENTATION STANDARDS**

### **@ @issdandavis - EVERY MAJOR FILE NEEDS:**

1. **Header comment explaining:**
   - What this file contains
   - How it relates to other files
   - Last updated date
   - Canon status (official/draft/experimental)

2. **README in every directory:**
   - `/lore/README.md` - Lore organization guide
   - `/game/scenes/README.md` - Scene structure guide
   - `/writing_drafts/README.md` - Draft staging process

**EXAMPLE HEADER:**
```
# [OFFICIAL CANON] Izack Thorne Character Sheet
# Last Updated: 2025-11-22
# Related Files: lore/characters/aria-ravencrest.txt, game/scenes/prologue.txt
# 
# This file contains the canonical character details for Izack Thorne,
# dimensional architect and founder of Avalon Academy.
```

---

## **BOLD SUGGESTION #7: AUTOMATION OPPORTUNITIES**

### **@ @issdandavis - SCRIPTS TO CREATE:**

1. **`scripts/lint_scenes.sh`**
   - Validate ChoiceScript syntax
   - Check for broken scene references
   - Ensure all variables are defined

2. **`scripts/generate_scene_map.sh`**
   - Auto-generate visual flowchart of scene connections
   - Export to `/docs/scene-map.svg`

3. **`scripts/sync_game_versions.sh`**
   - Keep `/game/` and `/choicescript_game/` content aligned
   - Flag scenes that exist in one but not the other

4. **`scripts/lore_index.sh`**
   - Generate searchable index of all lore files
   - Create cross-reference guide

**@ @issdandavis - GitHub Actions Workflow:**
Create `.github/workflows/validate-content.yml`:
```yaml
name: Validate Content
on: [pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Check lore consistency
        run: ./scripts/lint_scenes.sh
      - name: Validate scene syntax
        run: npm test # or appropriate test command
```

---

## **QUICK WINS - IMPLEMENT THESE FIRST:**

**@ @issdandavis - PRIORITY ACTIONS (DO THESE NOW):**

1. ✅ **IMMEDIATE:** Delete personal files (`next court date.txt`, shortcuts, etc.)
2. ✅ **TODAY:** Create `/lore/README.md` explaining organization
3. ✅ **THIS WEEK:** Consolidate duplicate lore files
4. ✅ **THIS WEEK:** Add PR template for content contributions
5. ✅ **THIS MONTH:** Implement automated scene validation

---

## **QUESTIONS FOR @issdandavis:**

**@ @issdandavis - PLEASE CLARIFY:**

1. **ChoiceScript vs. Custom Game:** Are you maintaining both versions? If so, what's the sync strategy?
2. **Canon Authority:** Who has final say on lore additions - you, or collaborative consensus?
3. **Game Engine:** What engine is `/game/game.js` built for? This affects automation possibilities.
4. **Release Timeline:** When do you want a playable demo? This affects prioritization.
5. **Music Integration:** Are the `.flp` files intended for game music? Should they be in the repo?

---

## **SUMMARY**

**@ @issdandavis - KEY TAKEAWAYS:**

✅ **Story content has been significantly enriched** (17 files enhanced with lore-based narrative)  
✅ **Workflow improvements suggested above** will prevent future organizational issues  
✅ **Clear AI agent roles** will improve collaboration efficiency  
✅ **Automation opportunities** will reduce manual work and errors  
✅ **GitHub organization** needs immediate attention to maintain project clarity  

**NEXT STEPS:**
1. Review this document
2. Implement "Quick Wins" section
3. Answer clarifying questions
4. Choose which bold suggestions to prioritize
5. Create issues for each improvement to track progress

---

**Document Created:** 2025-11-22  
**Created By:** @copilot (GitHub Copilot Workspace Agent)  
**Purpose:** Workflow optimization for Avalon project collaborative development  
