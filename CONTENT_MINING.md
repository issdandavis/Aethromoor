# 📚 CONTENT MINING GUIDE
## Automated Lore, Game, and Novel Content Extraction

**Purpose:** Consolidate all scattered lore, game content, and novel materials into organized, mineable sources for game development.

---

## 🎯 MINING OBJECTIVES

### Primary Goals:
1. **Catalog all existing content** across repository and external file shares
2. **Extract usable game content** from lore and novel drafts
3. **Identify duplication** and consolidate sources of truth
4. **Create searchable indexes** for quick reference
5. **Feed ChoiceScript game development** with narrative material

---

## 📁 CONTENT SOURCES

### Repository Locations

#### 1. Lore Directory (`lore/`)
**Files:**
- `IZACK'S MAGICAL UNIVERSE - COMPLE.txt` - Complete universe lore
- `Pollys_Wingscrolls_Worldbuilding.markdown` - Worldbuilding details
- `__Geography and Natural Lore of the Spiral of Pollyoneth__.pdf` - Geography reference
- `Unified Worldbuilding Master Framew.txt` - Framework document
- `README.md` - Lore directory index

**Mining Priority:** HIGH  
**Status:** ⏳ Not yet mined  
**Contains:** Character backgrounds, magic systems, geography, dimensional theory

#### 2. Writing Drafts (`writing_drafts/`)
**Expected Content:** Novel manuscripts, chapter drafts, prose versions

**Mining Priority:** HIGH  
**Status:** ⏳ Not yet inventoried  
**Action Needed:** Catalog all files and extract dialogue, scene descriptions, character moments

#### 3. Root Directory Lore Files
**Files to Process:**
- `#DarkSetting, Happy Ending The Spiral of Avalon, A complete chronical of an Dimensional architect.txt`
- `The Avalon Codex A Multi-Generation.txt`
- `The Spiral of Avalon.txt`
- `Izack_Master_Lore_Archive23.txt`
- `SpiralOfPollyoneth_Book1_FinishedChapters_Prose.markdown`
- `# Revised Chapters with Ancient Tra.txt`
- `# The Complete Writing Guide The Sp.txt`
- `## Detailed Outline The Spiral of P.txt`

**Mining Priority:** MEDIUM  
**Status:** ⏳ Not yet processed  
**Action:** Extract content, identify best version of each piece, move/consolidate

#### 4. Game Content (`game/` and `choicescript_game/`)
**Current State:**
- HTML version: Complete (30+ scenes, 14 endings)
- ChoiceScript version: Partial (foundation + first lesson complete)

**Mining Priority:** HIGH (for conversion work)  
**Status:** ✅ Well-organized, ready to mine  
**Use:** Reference for ChoiceScript conversion

#### 5. Documentation (`docs/`)
**Files:**
- `PROJECT_ROADMAP.md` - Development phases and timeline
- `AUTOMATION_GUIDE.md` - Workflow automation
- `TRACING.md` - Content tracing
- `avalon_materials/` and `reference/` subdirectories

**Mining Priority:** LOW (reference only)  
**Status:** ✅ Organized

---

## 🔍 MINING PROCESS

### Step 1: Discovery Phase
**Objective:** Catalog everything

**Actions:**
1. List all files in each content source
2. Identify file formats (TXT, MD, PDF, DOCX)
3. Note file sizes and modification dates
4. Create master inventory in this file

**Tools:**
- `find` command for file discovery
- `wc -w` for word counts
- `file` command for type detection

**Example Commands:**
```bash
# Find all text files
find . -name "*.txt" -o -name "*.md" -o -name "*.markdown"

# Count words in a file
wc -w filename.txt

# Check file type
file filename.docx
```

### Step 2: Extraction Phase
**Objective:** Pull out structured data

**For Each File Type:**

#### Text Files (.txt, .md, .markdown)
- Read directly
- Extract character names, locations, magic system rules
- Identify dialogue that could be used in game
- Note timeline references

#### PDF Files (.pdf)
- Use `pdftotext` if available, or manual review
- Extract key sections
- Note page references for citations

#### DOCX Files (.docx)
- Convert to text or read in editor
- Extract formatted content
- Preserve headings and structure

#### Binary Files (.flp, .zip, .lnk)
- Ignore music production files (.flp)
- Extract and inventory .zip archives
- Skip .lnk shortcuts

### Step 3: Consolidation Phase
**Objective:** Eliminate duplication, establish sources of truth

**Actions:**
1. Compare similar files (e.g., multiple Izack chronicles)
2. Identify the most complete/recent version
3. Mark deprecated versions for archival
4. Create unified documents where appropriate
5. Update `lore/README.md` with canonical references

### Step 4: Indexing Phase
**Objective:** Make content searchable and accessible

**Create Indexes For:**
- **Characters:** Name, role, generation, key traits, relationships
- **Locations:** Realm, description, significance, scenes set there
- **Magic Systems:** Type, rules, limitations, game mechanics
- **Timeline Events:** Generation, year, event, characters involved
- **Dialogue Snippets:** Context, character, potential game use
- **Scene Ideas:** Setting, characters, conflict, resolution

**Index Format:** Simple markdown tables or YAML for easy parsing

### Step 5: Integration Phase
**Objective:** Feed game development

**Actions:**
1. Cross-reference extracted content with `SCENE_PARITY_CHECKLIST.md`
2. Identify lore that supports planned expeditions
3. Extract dialogue for character interactions
4. Note magic system rules that affect game mechanics
5. Update `STATS_MATRIX.md` with lore-supported stat changes

---

## 📊 CONTENT INVENTORY

### Character Content
**Source Files:**
- `Izack_Master_Lore_Archive23.txt`
- `lore/IZACK'S MAGICAL UNIVERSE - COMPLE.txt`
- `lore/Pollys_Wingscrolls_Worldbuilding.markdown`

**Extraction Status:** ⏳ Not started  
**Characters to Index:**
- Izack Thorne (Generation 1)
- Aria Ravencrest (Generation 1)
- Alexander Thorne (Generation 2)
- Polly (Polydimensional entity)
- Zara (student character)
- Kael (desert guide)
- Other NPCs

**Next Action:** Create `CHARACTER_INDEX.md` with all character details

### Location Content
**Source Files:**
- `lore/__Geography and Natural Lore of the Spiral of Pollyoneth__.pdf`
- Geography sections in lore files

**Extraction Status:** ⏳ Not started  
**Locations to Index:**
- Avalon Academy
- Singing Dunes
- Verdant Tithe
- Rune Glacier
- Time Ocean
- Flame Deserts
- Floating Mountains
- Mortal realm boundaries

**Next Action:** Create `LOCATION_INDEX.md` with all location details

### Magic System Content
**Source Files:**
- Lore files discussing dimensional theory
- Game mechanics in `choicescript_game/startup.txt`

**Extraction Status:** ⏳ Not started  
**Systems to Document:**
- Collaborative casting
- Hierarchical magic
- Dimensional theory
- Boundary magic
- Oath magic (Singing Dunes)
- Growth magic (Verdant Tithe)
- Control/Harmony magic (Rune Glacier)

**Next Action:** Create `MAGIC_SYSTEMS.md` with complete rules

### Timeline Content
**Source Files:**
- Chronicle files
- Novel drafts

**Extraction Status:** ⏳ Not started  
**Timeline Span:** 150+ years across 4 generations

**Next Action:** Create `TIMELINE.md` with chronological events

### Dialogue & Scene Content
**Source Files:**
- Novel drafts in `writing_drafts/`
- Prose versions in root directory

**Extraction Status:** ⏳ Not started  
**Potential Use:** ChoiceScript dialogue, scene descriptions, flavor text

**Next Action:** Extract high-quality dialogue and scenes to `EXTRACTED_CONTENT.md`

---

## 🤖 AI-SPECIFIC MINING TASKS

### For Lore Curators:
**Your Mining Tasks:**
1. Read through all lore files
2. Extract and consolidate character information
3. Document magic system rules authoritatively
4. Build timeline of canonical events
5. Flag any contradictions between sources
6. Create unified lore documents

**Output Files:**
- `CHARACTER_INDEX.md`
- `LOCATION_INDEX.md`
- `MAGIC_SYSTEMS.md`
- `TIMELINE.md`
- `LORE_CONTRADICTIONS.md` (if any found)

### For Conversion Engineers:
**Your Mining Tasks:**
1. Review HTML game scenes for dialogue patterns
2. Extract reusable ChoiceScript code snippets
3. Document stat change triggers
4. Identify choice structure patterns
5. Note successful narrative techniques

**Output Files:**
- `CHOICESCRIPT_SNIPPETS.md`
- Updates to `SCENE_PARITY_CHECKLIST.md`

### For Structural Reviewers:
**Your Mining Tasks:**
1. Inventory all endings in HTML version
2. Map stat requirements for each path
3. Document branching logic
4. Identify balance issues

**Output Files:**
- Updates to `STATS_MATRIX.md`
- `BRANCHING_LOGIC.md`

### For All AIs:
**Shared Task:**
- Update this `CONTENT_MINING.md` with your discoveries
- Log sources examined in `HANDOFF.md`
- Note any external files found (Dropbox, Visual Studio, GitHub)

---

## 🔗 EXTERNAL FILE SHARES

### GitHub
**Status:** ✅ Primary source  
**Location:** https://github.com/issdandavis/Avalon  
**Action:** This is the source of truth. All content should be committed here.

### Dropbox
**Status:** ⏳ Not yet accessed  
**Expected Content:** Possibly additional drafts, backups, shared materials  
**Action Needed:** Identify Dropbox folder, catalog contents, decide what to import

### Visual Studio / VSCode
**Status:** ⏳ Workspace not yet configured  
**Action Needed:** Ensure workspace settings support multi-AI collaboration

### Other Platforms
**To Investigate:**
- OneDrive (referenced by `Shortcut to Documents (OneDrive - Personal).lnk`)
- Any other cloud storage or shared folders

**Action:** Catalog all external content sources in this section

---

## 📋 MINING CHECKLIST

### Phase 1: Inventory (Week 1)
- [ ] Catalog all files in `lore/`
- [ ] Catalog all files in `writing_drafts/`
- [ ] Catalog all lore files in root directory
- [ ] Identify external file shares (Dropbox, OneDrive, etc.)
- [ ] Document file formats and sizes
- [ ] Create master file inventory

### Phase 2: Extraction (Week 2-3)
- [ ] Extract character information → `CHARACTER_INDEX.md`
- [ ] Extract location information → `LOCATION_INDEX.md`
- [ ] Extract magic system rules → `MAGIC_SYSTEMS.md`
- [ ] Extract timeline events → `TIMELINE.md`
- [ ] Extract usable dialogue → `EXTRACTED_CONTENT.md`
- [ ] Note contradictions → `LORE_CONTRADICTIONS.md`

### Phase 3: Consolidation (Week 3-4)
- [ ] Compare duplicate files
- [ ] Identify canonical versions
- [ ] Archive deprecated content
- [ ] Update `lore/README.md` with sources of truth
- [ ] Organize root directory files into proper folders

### Phase 4: Integration (Week 4-5)
- [ ] Cross-reference with `SCENE_PARITY_CHECKLIST.md`
- [ ] Update `STATS_MATRIX.md` with lore-based stat logic
- [ ] Feed extracted content to ChoiceScript conversion
- [ ] Document game development decisions
- [ ] Update `docs/PROJECT_ROADMAP.md` if needed

### Phase 5: Maintenance (Ongoing)
- [ ] Update indexes as new content is created
- [ ] Keep external file shares synchronized
- [ ] Document new discoveries in `HANDOFF.md`
- [ ] Maintain clean separation between working files and archives

---

## 🎯 SUCCESS METRICS

**Inventory Phase Success:**
- Complete file list for all directories
- All external sources identified
- Baseline word count established

**Extraction Phase Success:**
- All indexes created and populated
- No major lore contradictions unresolved
- Sufficient content extracted for Phase 2 game development

**Integration Phase Success:**
- Game development references indexes regularly
- No duplication of effort due to lost content
- Clear sources of truth established

---

## 💾 BACKUP & SYNC STRATEGY

### Git Repository (Primary)
**Strategy:** All extracted content committed to repo  
**Frequency:** After each mining session  
**Files to Commit:** All .md indexes, consolidated documents

### External Shares (Secondary)
**Strategy:** Mirror important content to Dropbox/OneDrive for redundancy  
**Frequency:** Weekly syncs  
**Files to Mirror:** Master indexes, consolidated lore

### Local Backups (Tertiary)
**Strategy:** AI assistants should not rely on local storage  
**Frequency:** N/A (rely on Git and cloud)

---

## 🚨 MINING PRIORITIES

### THIS WEEK (Highest Priority):
1. Create `CHARACTER_INDEX.md` from existing lore
2. Create `MAGIC_SYSTEMS.md` with rules for expeditions
3. Review `writing_drafts/` for usable dialogue
4. Update this file with inventory findings

### THIS MONTH (High Priority):
1. Complete all indexes
2. Consolidate duplicate lore files
3. Organize root directory content
4. Identify and catalog external file shares

### THIS QUARTER (Medium Priority):
1. Extract all novel content for potential game use
2. Create comprehensive timeline
3. Resolve any lore contradictions
4. Build searchable lore database

---

## 📝 NOTES & OBSERVATIONS

### Lore Quality:
- Extensive worldbuilding exists across multiple files
- Multi-generational timeline is complex but well-thought-out
- Magic systems are detailed and consistent

### Organization Observations:
- Root directory contains many valuable lore files that should be in `lore/`
- Some file naming uses special characters (# prefix)
- Multiple versions of similar content exist (need deduplication)

### Content Richness:
- 40,000+ words already in HTML game
- Significant prose content in writing drafts
- PDF reference material is professional quality

### Challenges:
- Binary formats (PDF, DOCX) require conversion
- Large number of files to process
- Need to establish canonical versions

---

## 🔄 UPDATES LOG

**2025-11-22:** Initial creation of content mining guide  
**Next Update:** When first mining session completes

---

**Remember:** Content mining is an ongoing process. Update this guide as you discover new sources, extract new content, and refine the organization system.

*"Every thread of lore strengthens the spiral."* 🌀
