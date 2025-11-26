# The Avalon Codex

> **A multi-generational fantasy narrative project featuring Polly's Wingscroll: The First Thread**  
> *Play an interactive game, explore rich lore, or contribute to autonomous AI-powered development*

[![Play Now](https://img.shields.io/badge/▶️_Play-Now-brightgreen?style=for-the-badge)](game/index.html)
[![Version](https://img.shields.io/badge/version-1.0-blue)](https://github.com/issdandavis/Avalon)
[![Word Count](https://img.shields.io/badge/words-40000%2B-green)](choicescript_game/)
[![Endings](https://img.shields.io/badge/endings-14-purple)](choicescript_game/scenes/)

---

## 🎯 What Is This?

The Avalon Codex is a fantasy worldbuilding and interactive fiction project centered around the **Spiral of Pollyoneth** universe. This repository contains:

- 🎮 **A Complete Choice-Based Game** - Play as a student at Avalon Academy
- 📚 **Rich Lore & Worldbuilding** - Characters, magic systems, multi-generational history
- ✍️ **Novel Manuscripts** - Fantasy fiction set in the same universe
- 🤖 **AI Development System** - Autonomous game development workflows
- 🔧 **Professional Game Framework** - ChoiceScript implementation for mobile publishing

---

## 🚀 Quick Start - Choose Your Path

### 🎮 I Want to Play the Game
**Instant Play (HTML Version):**
1. Open `game/index.html` in your browser
2. Play immediately - no setup required!

**Professional Version (ChoiceScript):**
- See **[PLAY_THE_GAME.md](PLAY_THE_GAME.md)** for detailed instructions

### 👨‍💻 I Want to Develop/Contribute
**For Contributors:**
- Read **[CONTRIBUTING.md](CONTRIBUTING.md)** for contribution guidelines
- Check **[docs/PROJECT_ROADMAP.md](docs/PROJECT_ROADMAP.md)** for current development status

**For ISDanDavis (Repository Owner):**
- **Start Here:** [README_FOR_ISSDANDAVIS.md](README_FOR_ISSDANDAVIS.md)
- **Quick Reference:** [ISSDANDAVIS_QUICKSTART.md](ISSDANDAVIS_QUICKSTART.md)
- **Agent Management:** [AGENT_START_HERE.md](AGENT_START_HERE.md)

### 📖 I Want to Explore the Lore
Navigate to:
- `lore/` - Complete worldbuilding documentation
- `writing_drafts/` - Novel manuscripts and chronicles
- `docs/AETHERMOOR_CHRONICLES.md` - Complete world history

### 🤖 I Want to Use the AI System
- **Activation Guide:** [AI_SYSTEM_ACTIVATION_GUIDE.md](AI_SYSTEM_ACTIVATION_GUIDE.md)
- **System Index:** [AI_SYSTEM_INDEX.md](AI_SYSTEM_INDEX.md)
- **Management:** [AGENT_MANAGEMENT_README.md](AGENT_MANAGEMENT_README.md)

---

## 📁 Repository Structure

```
Avalon/
├── 🎮 game/                     # HTML game (complete & playable)
│   ├── index.html              # ← Double-click to play!
│   ├── game.js                 # Game logic
│   └── style.css               # Styling
│
├── 🎯 choicescript_game/       # Professional ChoiceScript version
│   ├── startup.txt             # Game configuration
│   ├── scenes/                 # All game scenes (11 complete)
│   └── web/                    # Web player files
│
├── 📚 lore/                    # Fantasy worldbuilding
│   ├── Character chronicles
│   ├── Magic system documentation
│   └── Geographical lore
│
├── ✍️ writing_drafts/          # Novel manuscripts
│   ├── Complete chronicles
│   └── Chapter drafts
│
├── 📖 docs/                    # Project documentation
│   ├── PROJECT_ROADMAP.md      # Development plan
│   ├── AUTOMATION_GUIDE.md     # AI workflows
│   └── Reference materials
│
└── 🤖 .github/                 # AI autonomous system
    ├── workflows/              # GitHub Actions (automated development)
    └── scripts/                # AI agent coordination
```

**Quick File Finder:** [FILE_LOCATIONS.txt](FILE_LOCATIONS.txt)

---

## 🎮 About Polly's Wingscroll: The First Thread

### The Game
A choice-based interactive narrative where you play as a new student at **Avalon Academy**, a living pocket dimension where legendary mages teach collaborative dimensional magic. Guided by **Polly**—a sarcastic, ancient raven familiar—you'll navigate relationships, explore magical realms, and shape your destiny through meaningful choices.

### Key Features
- **40,000+ words** of interactive narrative
- **11 complete scenes** with branching storylines
- **14 unique endings** from legendary master to expelled student
- **5 achievements** to unlock
- **Deep character relationships** that affect your story
- **Multiple expedition paths**: Singing Dunes, Verdant Tithe, or Rune Glacier
- **Customizable dorm room** with magical features
- **Collaboration stat system** - choices shape your magical approach

### Game Stats
- **Playtime:** 45-90 minutes per playthrough
- **Total Scenes:** 11
- **Unique Choices:** 100+
- **Relationship Tracking:** 5 major characters
- **High Replay Value:** Multiple paths and endings

---

## 🤖 AI Autonomous Development System

This repository features a **complete AI workflow system** that autonomously develops the game:

### What It Does
- ✨ **Scene Writer** - Adds new ChoiceScript content (every 3 hours)
- ✨ **Content Polisher** - Enhances atmosphere and details (every 4 hours)
- ✨ **Stat Balancer** - Adjusts game difficulty (daily)
- ✨ **Game Tester** - Validates code and finds bugs (daily)
- ✨ **Agent Manager** - Coordinates all AI workers and reports health

### Quick Commands
```bash
# Check system health (60 seconds)
python .github/scripts/agent_manager_cli.py health

# See recommendations
python .github/scripts/agent_manager_cli.py recommend

# View visual dashboard
open agent-dashboard.html
```

### AI System Guides
- **Beginner Guide:** [AGENT_MANAGEMENT_README.md](AGENT_MANAGEMENT_README.md)
- **Activation:** [AI_SYSTEM_ACTIVATION_GUIDE.md](AI_SYSTEM_ACTIVATION_GUIDE.md)
- **Tutorial:** [AGENT_TUTORIAL.md](AGENT_TUTORIAL.md)
- **Quick Reference:** [AGENT_QUICK_REFERENCE.md](AGENT_QUICK_REFERENCE.md)

---

## 🏢 Automation & Enterprise Features

### Inbox Management
- ✅ Auto-replies to GitHub notifications (30 seconds)
- ✅ Smart categorization of issues, PRs, discussions
- ✅ Multi-platform support (GitHub, GitLab, Bitbucket)
- ✅ 5 AI agents managing communications 24/7

### Enterprise Monitoring
- ✅ Automated validation every 4 hours
- ✅ Health reports with analysis and recommendations
- ✅ Security validation and integration status
- ✅ Multi-platform monitoring

### Automation Resources
- **[ACCOUNTS_README.md](ACCOUNTS_README.md)** - Account automation setup
- **[docs/AUTOMATION_GUIDE.md](docs/AUTOMATION_GUIDE.md)** - Integration workflows
- **Configuration:** `config/automation-settings.json`

All automation runs in **silent mode** by default (no notifications for routine updates).

---

## 🔐 Security

⚠️ **Important:** Previous commits contained plaintext API keys (now removed).
- Rotate any exposed credentials
- Store credentials only in local `.env` file
- All automation credentials use GitHub Secrets

See `config/.env.example` for template.

---
## 🌟 The Spiral of Pollyoneth Universe

### Core Narrative
A four-generation epic spanning 150+ years, centered around:
- **Izack Thorne** - Mage-turned-king who founded Avalon Academy
- **Polly** - "Polydimensional Manifestation of Accumulated Wisdom and Occasional Sarcasm"
- **Collaborative Magic** - A revolutionary approach to dimensional magic vs. hierarchical control

### The World
- **Avalon Academy** - A living pocket dimension dedicated to teaching collaborative magic
- **The Spiral** - Multi-dimensional reality with interconnected realms
- **Dimensional Theory** - A complete magical system built on collaborative casting
- **150+ Years of History** - Detailed chronicles across multiple generations

---

## 🎭 Game Content Overview

### Scene Flow
1. **Arrival** → Make your first impression
2. **Dorm Room** → Customize your living space
3. **First Lesson** → Learn collaborative magic principles  
4. **Academy Life** → Choose your training focus
5. **Expedition Prep** → Prepare for your journey
6. **Expedition** → Explore Singing Dunes, Verdant Tithe, or Rune Glacier
7. **Character Bonds** → Deepen relationships with mentors
8. **Final Trial** → Face the ultimate test of collaboration
9. **Endings** → Discover your fate (14 unique possibilities)

### Major Choice Points
- **Dorm Customization:** Sanctuary, Study, Workshop, or Zen Garden style
- **Magical Features:** Multi-realm window, time clock, living garden, or memory crystal
- **Training Focus:** Theory (Aria), Practical (Izack), or Living Magic (Zara)
- **Expedition Path:** Which realm to explore and master
- **Relationship Priorities:** Which mentors to bond with
- **Trial Approach:** Leadership, collaboration, or support role

---

## 🏆 Endings Guide

### 🥇 Legendary Tier (Best Outcomes)
1. **Collaborative Master** - True partnership + 80+ collaboration score
2. **Glacier Partner** - Achieved mastery through unity
3. **Heartwood Guardian** - Bonded with the ancient consciousness

### 🥈 High Achievement Tier
4. **Truthbound Mage** - Mastered the desert's truth + high collaboration
5. **Runeweaver** - Achieved fluency in the First Tongue
6. **Forestbound Guardian** - Deep connection with the Verdant Tithe

### 🥉 Success Tier
7. **Collaborative Scholar** - 75+ collaboration, solid foundation
8. **Balanced Mage** - Found harmony across disciplines
9. **Humble Seeker** - Chose the path of mystery and growth

### 📋 Standard Tier
10. **Boundary Specialist** - Competent professional mage
11. **Second Chance** - Redemption through persistent effort

### ⚠️ Challenging Tier
12. **Humbled Student** - Struggled but ultimately graduated
13. **Expelled** - Failed to uphold collaborative principles
14. **Standard Path** - Average graduation without distinction

---

## 💻 Technical Information

### Dual Implementation
The game exists in two versions:

**HTML Version** (`game/`)
- **Language:** JavaScript + HTML5 + CSS3
- **Size:** ~100KB total
- **Platform:** All modern browsers
- **Status:** Complete and fully playable offline

**ChoiceScript Version** (`choicescript_game/`)
- **Language:** ChoiceScript
- **Scenes:** 11 complete .txt files
- **Lines:** 5,000+ lines of code
- **Achievements:** 5 defined achievements
- **Variables:** 20+ stats and flags tracked
- **Status:** Ready for professional publication

### Development Workflow
1. **Content Creation** → Prototype in HTML or write directly in ChoiceScript
2. **AI Enhancement** → Autonomous polishing and expansion
3. **Testing** → Automated validation and manual playtesting
4. **Publishing** → Submission to Hosted Games platform

---

## 📤 Publishing Status

### ✅ Ready for Submission
- ✅ Exceeds 30,000 word minimum (40,000+ words)
- ✅ Complete narrative with all endings implemented
- ✅ Title under 30 characters
- ✅ Professional ChoiceScript formatting
- ✅ Multiple meaningful branching choices
- ✅ All content is original (human-written with AI polishing)

### Publication Process
1. **Beta Testing** - Submit to Choice of Games forum (2-4 weeks)
2. **Community Feedback** - Gather player input and refine
3. **Submission** - Submit to Hosted Games via email
4. **Review Period** - Wait for editorial review (2-6 weeks)
5. **Publication** - If approved, game goes live (4-6 months total)

**Complete details:** [SUBMISSION_GUIDE.md](SUBMISSION_GUIDE.md)

---

## 🛠️ Development & Contribution

### For New Contributors
1. Read **[CONTRIBUTING.md](CONTRIBUTING.md)** for guidelines
2. Check **[docs/PROJECT_ROADMAP.md](docs/PROJECT_ROADMAP.md)** for current priorities
3. Review **[FILE_LOCATIONS.txt](FILE_LOCATIONS.txt)** to navigate the repository
4. Test the game by opening `game/index.html`

### For Repository Owner (issdandavis)
- **Your Personal Guide:** [README_FOR_ISSDANDAVIS.md](README_FOR_ISSDANDAVIS.md)
- **Quick Commands:** [ISSDANDAVIS_QUICKSTART.md](ISSDANDAVIS_QUICKSTART.md)
- **Managing AI Agents:** [AGENT_START_HERE.md](AGENT_START_HERE.md)
- **System Verification:** [CLOSED_SESSIONS_VERIFICATION.md](CLOSED_SESSIONS_VERIFICATION.md)

### Development Tools
- **Node.js** (LTS) for local ChoiceScript testing
- **Git** for version control
- **Python 3.8+** for AI automation scripts
- Modern web browser for HTML version

### Build & Test
```bash
# For ChoiceScript version (detailed setup)
cd game
./bootstrap_choicescript.sh  # Clone ChoiceScript engine
./sync_scenes.sh             # Copy scenes to engine
cd choicescript
# Run server for your OS:
# - Windows: run-server.bat
# - macOS: serve.command  
# - Linux/WSL: bash serve.sh

# For HTML version
# Simply open game/index.html in browser

# For AI system health check
python .github/scripts/agent_manager_cli.py health
```

---

## 🎨 What's New in Version 1.0

### Recent Additions (November 2025)
- ✨ **Dorm Room Customization** - 16 unique combinations
- 📚 **Academy Life Scene** - Training path selection
- 🗺️ **Expedition Preparation** - Meaningful pre-quest choices
- 💕 **Character Bonds** - Deep relationship development scenes
- ⚔️ **Final Trial** - Collaborative crisis management climax
- 📝 **40,000+ Words** - More than doubled original content
- 🎯 **Achievement System** - Proper ChoiceScript achievements
- 🤖 **AI Development** - Autonomous content creation and polishing
- 🔧 **Professional Polish** - Submission-ready quality

---

## 📚 Documentation Index

### Getting Started
- **[START_HERE.md](START_HERE.md)** - Simplest possible start guide
- **[QUICK_START.md](QUICK_START.md)** - Detailed play instructions
- **[PLAY_THE_GAME.md](PLAY_THE_GAME.md)** - Complete game playing guide

### For Users
- **[PLAY_HERE.html](PLAY_HERE.html)** - Alternative game launcher
- **[FILE_LOCATIONS.txt](FILE_LOCATIONS.txt)** - Quick reference for all files

### For Developers
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - How to contribute
- **[docs/PROJECT_ROADMAP.md](docs/PROJECT_ROADMAP.md)** - Development plan
- **[docs/GAME_DEVELOPMENT_MASTER_REFERENCE.md](docs/GAME_DEVELOPMENT_MASTER_REFERENCE.md)** - Complete dev guide
- **[docs/AUTOMATION_GUIDE.md](docs/AUTOMATION_GUIDE.md)** - Workflow automation

### For AI System Management
- **[AGENT_START_HERE.md](AGENT_START_HERE.md)** - Begin here for AI system
- **[AGENT_MANAGEMENT_README.md](AGENT_MANAGEMENT_README.md)** - 3-minute guide
- **[AI_SYSTEM_ACTIVATION_GUIDE.md](AI_SYSTEM_ACTIVATION_GUIDE.md)** - Setup instructions
- **[AGENT_TUTORIAL.md](AGENT_TUTORIAL.md)** - Step-by-step practice
- **[AI_SYSTEM_INDEX.md](AI_SYSTEM_INDEX.md)** - Find any AI documentation

### For Repository Owner
- **[README_FOR_ISSDANDAVIS.md](README_FOR_ISSDANDAVIS.md)** - Personalized summary
- **[ISSDANDAVIS_QUICKSTART.md](ISSDANDAVIS_QUICKSTART.md)** - Quick reference
- **[ACCOUNTS_README.md](ACCOUNTS_README.md)** - Account automation setup

### Reference Materials
- **[docs/AETHERMOOR_CHRONICLES.md](docs/AETHERMOOR_CHRONICLES.md)** - Complete world history
- **[CHANGELOG.md](CHANGELOG.md)** - Version history
- **[SUBMISSION_GUIDE.md](SUBMISSION_GUIDE.md)** - Publishing information

---

## 🎊 Credits & Attribution

### Game Design & Writing
- All narrative content and worldbuilding
- Character creation and development
- Game mechanics and choice architecture
- Lore development across 150+ years of fictional history

### Tools & Frameworks
- **[ChoiceScript](https://www.choiceofgames.com/make-your-own-games/choicescript-intro/)** by Choice of Games LLC
- **HTML5/CSS3/JavaScript** for web version
- **GitHub Actions** for automation
- **Anthropic Claude** (via API) for AI development assistance

### Open Source Components
- ChoiceScript engine (used under Choice of Games license)
- Various JavaScript libraries (see `game/` for details)

---

## 📞 Support & Contact

### Getting Help
- **Issues:** Create a [GitHub Issue](https://github.com/issdandavis/Avalon/issues)
- **Discussions:** Use [GitHub Discussions](https://github.com/issdandavis/Avalon/discussions)
- **Documentation:** Check the extensive docs in this repository

### Reporting Bugs
1. Check if the issue already exists
2. Provide steps to reproduce
3. Include browser/system information (for HTML version)
4. Specify which version (HTML or ChoiceScript)

### Contributing
We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📜 License & Usage

This project contains original creative work. Please respect the intellectual property:
- **Game content** - All rights reserved
- **Code** - Available for reference and learning
- **Lore & Worldbuilding** - All rights reserved

For licensing inquiries, please create an issue.

---

## 🎮 Ready to Begin?

### Play the Game
**👉 Open [game/index.html](game/index.html) or see [PLAY_THE_GAME.md](PLAY_THE_GAME.md)**

### Explore the World
**👉 Browse `lore/` directory or read [docs/AETHERMOOR_CHRONICLES.md](docs/AETHERMOOR_CHRONICLES.md)**

### Start Developing
**👉 Read [CONTRIBUTING.md](CONTRIBUTING.md) and [docs/PROJECT_ROADMAP.md](docs/PROJECT_ROADMAP.md)**

### Manage AI Workers
**👉 See [AGENT_START_HERE.md](AGENT_START_HERE.md)**

---

*"I've watched Avalon Academy for three hundred years. Your story is about to begin."*  
— **Polly (Polymnia Aetheris)**

---

**Repository maintained by issdandavis** | **Last updated: November 2025**
