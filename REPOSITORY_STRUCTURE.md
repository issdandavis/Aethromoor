# 📁 Avalon Repository Structure

## Complete Directory Organization

This document provides a complete map of the Avalon Academy project repository after consolidation and organization.

---

## 🎯 Quick Navigation

**To Play the Game:** `game/index.html` or `game/PLAY_HERE.html`  
**To Read the Docs:** Start with `START_HERE.md` or `README.md`  
**To Find Files:** Check `FILE_LOCATIONS.txt`

---

## 📂 Root Directory

```
Avalon/
├── 📄 START_HERE.md                    ← Start here! Simplest instructions
├── 📄 README.md                        ← Complete project overview  
├── 📄 REPOSITORY_STRUCTURE.md          ← This file - full directory map
├── 📄 FILE_LOCATIONS.txt               ← Quick reference guide
├── 📄 QUICK_START.md                   ← Detailed how-to-play guide
├── 📄 PLAY_THE_GAME.md                 ← Game instructions
├── 📄 CONTRIBUTING.md                  ← How to contribute
├── 📄 ORGANIZATION_SUMMARY.md          ← Organization notes
├── 📄 .gitignore                       ← Git ignore rules
│
├── 🎮 game/                            ← HTML Game (Complete)
├── 🎮 choicescript_game/              ← Professional Version (In Progress)  
├── 📚 lore/                            ← Worldbuilding & Lore
├── 📝 writing_drafts/                  ← Novel Manuscripts & Chapters
├── 📋 docs/                            ← Project Documentation
├── 📦 archive/                         ← Historical Files & Backups
└── ⚙️  config/                         ← Configuration Files
```

---

## 🎮 Game Directory

### `game/` - HTML Interactive Game

The complete, playable browser-based game.

```
game/
├── index.html                          ← MAIN GAME FILE - Open this to play!
├── PLAY_HERE.html                      ← Alternative entry point with styling
├── README.md                           ← Game-specific documentation
├── styles/                             ← Game styling
├── scripts/                            ← Game logic
└── assets/                             ← Images, sounds, etc.
```

**Status:** ✅ Complete (30+ scenes, 14 endings, 40,000+ words)

---

## 🎮 ChoiceScript Game Directory

### `choicescript_game/` - Professional Mobile Game

The professional version for app store publication.

```
choicescript_game/
├── startup.txt                         ← Game initialization & character creation
├── choicescript_stats.txt              ← Stats screen configuration
├── scenes/
│   ├── opening.txt                     ← Polly's introduction
│   ├── arrival_academy.txt             ← Three arrival paths
│   ├── first_lesson.txt                ← Complete first lesson
│   ├── expedition_choice.txt           ← Choose your expedition
│   ├── singing_dunes.txt               ← Desert expedition (In Progress)
│   ├── verdant_tithe.txt               ← Forest expedition (Planned)
│   ├── rune_glacier.txt                ← Ice expedition (Planned)
│   └── endings/                        ← 14 unique endings
└── README.md                           ← ChoiceScript game documentation
```

**Status:** ⏳ In Progress (Phase 2 - completing expeditions)

---

## 📚 Lore Directory

### `lore/` - Worldbuilding & Universe Lore

All canonical worldbuilding documents for the Spiral of Pollyoneth universe.

```
lore/
├── README.md                                           ← Lore directory guide
├── IZACK_MASTER_CHRONICLE_UPDATED.txt.txt             ← Complete Izack timeline
├── Izack_Master_Lore_Archive23.txt                    ← Izack lore archive
├── Lore_Codex.txt                                     ← Master lore reference
├── Tower_Layout_Reference.txt                         ← Avalon Tower structure
├── Fae_Song_Appendix.txt                              ← Fae magic system
├── AETHERMOOR_CHRONICLES.md                           ← Aethermoor realm lore
├── Pollys_Wingscrolls_Worldbuilding.markdown          ← Polly's character lore
├── Unified Worldbuilding Master Framew.txt            ← Master worldbuilding framework
├── __Geography and Natural Lore of the Spiral of Pollyoneth__.pdf  ← Geography PDF
└── # IZACK'S MAGICAL UNIVERSE - COMPLE.txt            ← Magic system complete
```

**Key Characters:** Izack Thorne, Polly, Aria Ravencrest, Alexander Thorne  
**Key Locations:** Avalon Academy, The Spiral, Aethermoor, Mortal Realm  
**Magic System:** Collaborative casting, dimensional theory, boundary magic

---

## 📝 Writing Drafts Directory

### `writing_drafts/` - Novel Manuscripts & Chapters

All novel drafts, chapters, and writing materials for the book series.

```
writing_drafts/
├── README.md                                           ← Writing directory guide
├── spiral-of-pollyoneth-novel.md                      ← Main novel draft
│
├── 📖 Manuscripts (Complete & Drafts)
│   ├── The_Spiral_of_Pollyoneth_FULL_Manuscript_CLEAN.pdf
│   ├── The_Spiral_of_Pollyoneth_Final_Manuscript.docx
│   ├── The_Spiral_of_Pollyoneth_Final_Manuscript.pdf
│   ├── Spiral Of Eternity.pdf
│   ├── Spiral_Non_Canon_And_Meta.docx
│   ├── The Spiral of Avalon.VERY GOOD.1st draft.txt
│   ├── # The Spiral of Avalon A Complete N.txt
│   └── # The Spiral of Avalon.txt
│
├── 📋 Outlines & Guides
│   ├── __The Spiral of Pollyoneth__ – Book 1 Masterplan Outline.pdf
│   ├── __The Spiral of Pollyoneth__ – Book 1 Masterplan Outline.20.pdf
│   ├── # The Complete Writing Guide The Sp.txt
│   ├── ## Detailed Outline The Spiral of P.txt
│   └── # Positioning The Avalon Codex for.txt
│
├── 📚 Story Materials
│   ├── The Avalon Codex A Multi-Generation.txt
│   ├── The Spiral of Avalon.txt
│   ├── The Spiral of Etenrity.txt
│   ├── #DarkSetting, Happy Ending.txt
│   ├── #DarkSetting, Happy Ending The Spiral of Avalon, A complete chronical of an Dimensional architect.txt
│   ├── Title_Dedication_Epigraph.txt
│   ├── Chapter_Change_Map.txt
│   ├── # Revised Chapters with Ancient Tra.txt
│   ├── SpiralOfPollyoneth_Book1_FinishedChapters_Prose.markdown
│   ├── Spiralverse_Language_Summary.markdown
│   ├── 87357.docx
│   └── Document.docx
│
└── 📂 book_chapters/                                   ← Individual chapters
    ├── # Chapter 1 The Cave and the Contra.txt
    ├── # Chapter 2 The World Tree Opens.txt
    ├── # Chapter 3 Of Gardens and Gateways.txt
    ├── # Chapter 4 The Day the World Didn'.txt
    ├── # Chapter 5 A Place Called Avalon.txt
    ├── # Chapter 6 The Entrance of Alexand.txt
    ├── Avalon story.txt
    └── [many more PDFs and documents...]
```

**Total Word Count:** 100,000+ words across all drafts

---

## 📋 Docs Directory

### `docs/` - Project Documentation

All project planning, guides, and development documentation.

```
docs/
├── README.md                                  ← Docs directory guide
├── PROJECT_ROADMAP.md                         ← Development roadmap & phases
├── AUTOMATION_GUIDE.md                        ← Zapier workflow documentation
├── NEXT_TASKS.md                              ← Immediate next steps
├── AI_SESSION_HANDOFF.md                      ← AI collaboration guide
├── TRACING.md                                 ← Development tracing
├── COMPLETE_MATERIALS_SUMMARY.md              ← Materials inventory
├── FEATURES_COMPLETE.md                       ← Completed features list
├── FINAL_GAME_DEV_CHECKLIST.md                ← Game development checklist
├── GAME_DEVELOPMENT_MASTER_REFERENCE.md       ← Game dev master guide
├── SUBMISSION_GUIDE.md                        ← Publishing submission guide
│
├── 📂 avalon_materials/                       ← Additional materials
└── 📂 reference/                              ← Reference documents
```

**Key Documents:**
- `PROJECT_ROADMAP.md` - Current development phase and timeline
- `AUTOMATION_GUIDE.md` - How to use Zapier workflows
- `SUBMISSION_GUIDE.md` - How to submit to Hosted Games

---

## 📦 Archive Directory

### `archive/` - Historical Files & Backups

Old versions, chat logs, and historical materials.

```
archive/
├── README.md                                  ← Archive directory guide
│
├── 📂 conversations/                          ← AI chat logs
│   ├── Entire chat log.txt
│   ├── The_Spiral_of_Avalon_FULL_Conversation.txt
│   ├── The_Spiral_of_Avalon_Full_Conversation_For_ClaudeAI.txt
│   ├── Open Ai and Claudie.txt
│   ├── AI_Handoff_Prompt.txt
│   ├── Fantasy World History Expansion - Claude.html
│   ├── Here is your updated Chronological quotes.txt
│   └── Here is your updated Chronological.txt
│
├── 📂 old_versions/                           ← Old bundles & exports
│   ├── archive.zip
│   ├── Spiral_Pollyoneth_Bundle_FINAL.zip
│   ├── Spiral_of_Pollyoneth_Bundle.zip
│   └── everweave-export.pdf
│
├── 📂 personal/                               ← Personal notes & files
│   ├── notes.txt
│   ├── notes2.txt
│   ├── numbers.txt
│   ├── next court date.txt
│   ├── not ures.txt
│   ├── issac's Notebook.url
│   ├── Osakie X TyPa Productions.flp
│   ├── typaxosakiecollab.flp
│   ├── typaxosakiecollab_dub_added.flp
│   ├── DAO Ultimate Addins Updater.log
│   ├── DAOriginsConfigReport2022-10-22.xml
│   └── New Rich Text Format.rtf
│
├── Entire chat log 2 missing begining.txt
├── Entire chat log.txt
├── 700000 characters.txt
├── ChatGPT Data Export.html
├── Skip to content.txt
├── MATERIALS_FOUND.txt
└── README.mdClaudeAI thigns
```

**Purpose:** Preserve historical context without cluttering active workspace

---

## ⚙️ Config Directory

### `config/` - Configuration Files

Environment and configuration files.

```
config/
└── .env.example                        ← Example environment variables
```

---

## 🎯 File Categorization

### By Purpose

**Game Files:**
- `game/` - Playable HTML version
- `choicescript_game/` - Professional mobile version

**Creative Content:**
- `lore/` - Worldbuilding & universe canon
- `writing_drafts/` - Novels, chapters, manuscripts

**Project Management:**
- `docs/` - Planning, guides, roadmaps
- `README.md`, `START_HERE.md` - Entry points

**Historical:**
- `archive/` - Old versions, chat logs, backups

---

## 📊 Statistics

**Total Files:** 150+ files organized  
**Game Content:** 40,000+ words (HTML) + ChoiceScript in progress  
**Novel Content:** 100,000+ words across drafts  
**Documentation:** 15+ comprehensive guides  
**Lore Documents:** 10+ worldbuilding files  

---

## 🗺️ Navigation Tips

### For Players:
1. Go to `game/index.html`
2. Double-click to play in browser
3. That's it!

### For Writers/Collaborators:
1. Check `lore/` for canon worldbuilding
2. Check `writing_drafts/` for manuscripts
3. Read `docs/PROJECT_ROADMAP.md` for current status

### For Developers:
1. Check `choicescript_game/` for mobile version
2. Read `docs/GAME_DEVELOPMENT_MASTER_REFERENCE.md`
3. Review `docs/PROJECT_ROADMAP.md` for next tasks

### For New Contributors:
1. Read `START_HERE.md`
2. Read `CONTRIBUTING.md`
3. Check `docs/NEXT_TASKS.md`

---

## 🔄 Maintenance

### Keeping Repository Clean:

**DO commit:**
- ✅ Lore documents
- ✅ Writing drafts
- ✅ Game files
- ✅ Documentation

**DON'T commit:**
- ❌ Personal notes
- ❌ Temporary files
- ❌ Music production files (.flp)
- ❌ OS-specific files (.DS_Store, Thumbs.db)
- ❌ Shortcuts (.lnk, .url)

**The `.gitignore` file handles this automatically!**

---

## 📞 Questions?

- **Can't find a file?** Check `FILE_LOCATIONS.txt`
- **Don't know where to start?** Read `START_HERE.md`
- **Want to contribute?** Read `CONTRIBUTING.md`
- **Need development info?** Check `docs/`

---

**Last Updated:** November 2025  
**Repository Status:** ✅ Fully Organized & Consolidated  
**Current Development Phase:** Phase 2 - Complete ChoiceScript Game

---

*"The spiral continues. Every file has its place."*
