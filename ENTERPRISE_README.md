# Enterprise Documentation - The Avalon Codex Project

**Repository:** [issdandavis/Avalon](https://github.com/issdandavis/Avalon)  
**Project Type:** Interactive Fiction Game Development & Publishing  
**Primary Language:** JavaScript, ChoiceScript  
**License:** Proprietary (Pre-publication)  

---

## Executive Summary

The Avalon Codex is a multi-format narrative project centered on "Polly's Wingscroll: The First Thread," a choice-based interactive game designed for commercial publication through Hosted Games (Choice of Games LLC). The repository manages:

- **40,000+ word** interactive narrative game
- Dual-platform implementation (HTML5 web, ChoiceScript mobile)
- Comprehensive worldbuilding lore and reference materials
- Novel manuscript drafts for future publication
- Automated development and publishing workflows

**Current Phase:** Development Phase 2 - Professional ChoiceScript conversion  
**Target Launch:** Q2-Q3 2026 (estimated)

---

## Repository Organization

### 1. Core Architecture

```
Avalon/
├── game/                      # Production-ready HTML5 version
│   ├── index.html             # Standalone web game (deployable)
│   ├── game.js                # Game engine & content (40,000+ words)
│   └── style.css              # UI styling
│
├── choicescript_game/         # Professional mobile version (in development)
│   ├── startup.txt            # Game initialization & variables
│   ├── scenes/                # Individual scene files (ChoiceScript)
│   │   ├── arrival.txt        # ✅ Complete
│   │   ├── first_lesson.txt   # ✅ Complete
│   │   ├── singing_dunes.txt  # ⏳ In Progress
│   │   ├── verdant_tithe.txt  # 📋 Planned
│   │   ├── rune_glacier.txt   # 📋 Planned
│   │   └── endings.txt        # 📋 Planned (14 unique endings)
│   └── web/                   # ChoiceScript engine files (gitignored)
│
├── lore/                      # Worldbuilding & canon reference
│   ├── # IZACK'S MAGICAL UNIVERSE - COMPLE.txt
│   ├── Pollys_Wingscrolls_Worldbuilding.markdown
│   ├── Unified Worldbuilding Master Framew.txt
│   └── __Geography and Natural Lore__.pdf
│
├── writing_drafts/            # Novel manuscripts & outlines
│   ├── DarkSetting_Happy_Ending_Complete_Chronicle.txt
│   ├── spiral-of-pollyoneth-novel.md
│   └── [Multiple manuscript PDFs]
│
├── docs/                      # Project documentation
│   ├── PROJECT_ROADMAP.md     # Development timeline & milestones
│   ├── AUTOMATION_GUIDE.md    # CI/CD & integration workflows
│   ├── AI_SESSION_HANDOFF.md  # AI assistant collaboration protocols
│   └── GAME_DEVELOPMENT_MASTER_REFERENCE.md
│
├── archive/                   # Historical materials & backups
│   └── [Conversation logs, legacy exports]
│
└── .github/                   # GitHub configuration
    ├── workflows/             # GitHub Actions CI/CD
    ├── agents/                # Custom agent definitions
    └── COPILOT_INSTRUCTIONS.md # AI development guidelines
```

---

## 2. Technology Stack

### Production Systems

| Component | Technology | Purpose | Status |
|-----------|-----------|---------|--------|
| **Web Game** | HTML5 + Vanilla JS | Instant-play browser version | ✅ Production |
| **Mobile Game** | ChoiceScript | iOS/Android app store distribution | ⏳ Development |
| **Version Control** | Git + GitHub | Source control & collaboration | ✅ Active |
| **CI/CD** | GitHub Actions | Automated testing & deployment | ✅ Configured |
| **Documentation** | Markdown | Technical & project docs | ✅ Maintained |

### Development Tools

- **ChoiceScript IDE**: Professional game engine (Choice of Games LLC)
- **VS Code**: Primary development environment
- **Git**: Distributed version control
- **Node.js**: Local development server for ChoiceScript
- **Zapier**: (Planned) Automated workflow integrations

### Deployment Targets

1. **GitHub Pages** - HTML version hosting (current)
2. **Hosted Games Platform** - Mobile app store distribution (target)
3. **Itch.io** - Alternative web distribution (planned)

---

## 3. Development Workflow

### Branch Strategy

```
main                    # Production-ready code only
├── copilot/*          # GitHub Copilot agent branches
├── claude/*           # Claude AI assistant branches
└── feature/*          # Human contributor feature branches
```

**Branching Convention:**
- `copilot/[task-description]` - Automated AI development work
- `claude/[task]-[session-id]` - AI assistant sessions
- `feature/[feature-name]` - Human development work

### Commit Standards

All commits should follow conventional commit format:

```
<type>: <description>

Types:
- feat: New game content or features
- fix: Bug fixes
- docs: Documentation updates
- refactor: Code restructuring
- test: Test additions or updates
- chore: Maintenance tasks
```

### Pull Request Process

1. **Branch Creation**: Create from `main` with descriptive name
2. **Development**: Make focused, incremental changes
3. **Testing**: Verify game logic and paths locally
4. **Documentation**: Update relevant docs (ROADMAP, HANDOFF)
5. **PR Creation**: Use template with checklist
6. **Review**: Address feedback from automated checks
7. **Merge**: Squash merge to main after approval

---

## 4. CI/CD Pipeline

### GitHub Actions Workflows

#### 1. ChoiceScript Tests (`choicescript-tests.yml`)

**Trigger:** Push to `choicescript_game/scenes/**`

**Actions:**
- Runs Quicktest (ChoiceScript syntax validation)
- Runs Randomtest (gameplay path testing)
- Reports errors in PR comments

**Status:** ⏳ Placeholder (implementation pending)

#### 2. Jekyll Site CI (`jekyll-docker.yml`)

**Trigger:** Push/PR to `main`

**Actions:**
- Builds Jekyll static site
- Validates HTML structure
- Prepares for GitHub Pages deployment

**Status:** ✅ Active

### Planned Automation (Zapier)

See `docs/AUTOMATION_GUIDE.md` for detailed workflows:

- **Content Pipeline**: Google Docs → GitHub (lore updates)
- **Bug Tracking**: Google Forms → GitHub Issues
- **Release Announcements**: GitHub Release → Social Media
- **Community Feedback**: Discord → GitHub Issues

---

## 5. Security & Compliance

### Secrets Management

**Sensitive Data Locations:**
- `config/.env.example` - Template for local environment variables
- `.gitignore` - Excludes `.env`, API keys, personal files

**Security Practices:**
- ✅ No API keys in source code
- ✅ `.env` files excluded from version control
- ✅ Previous exposed keys rotated (historical commits cleaned)
- ✅ Two-factor authentication enabled on GitHub

### Content Protection

**Intellectual Property:**
- All narrative content is proprietary pre-publication
- Lore and worldbuilding materials are copyright protected
- Public repository, but content not licensed for reuse
- Will transition to open-source license post-publication (TBD)

### Dependency Security

**Current Dependencies:**
- Zero npm/package dependencies (vanilla JavaScript)
- ChoiceScript engine (external, downloaded locally, gitignored)
- Jekyll (Docker-based, no persistent dependencies)

---

## 6. Quality Assurance

### Testing Strategy

**Automated Testing:**
- [ ] ChoiceScript Quicktest (syntax validation)
- [ ] ChoiceScript Randomtest (10,000 random playthroughs)
- [ ] HTML validation (Jekyll build)

**Manual Testing:**
- Complete playthroughs of all 14 endings
- Stat tracking verification
- Relationship progression testing
- Mobile responsiveness validation

### Quality Standards

Every scene must include:
- ✅ Vivid environmental descriptions (2-3 sentences minimum)
- ✅ Character voice consistency (especially Polly's commentary)
- ✅ Meaningful choices with consequences
- ✅ Proper stat modifications
- ✅ Connection to overall narrative arc

**Word Count Targets:**
- Expedition scenes: 500+ lines each
- Ending scenes: 30-50 lines each
- Total game: 30,000+ words (Hosted Games minimum)
- **Current Status:** 40,000+ words ✅

---

## 7. Team Collaboration

### Roles & Responsibilities

**Repository Owner:** [@issdandavis](https://github.com/issdandavis)
- Project direction & vision
- Final content approval
- Publishing coordination

**AI Development Agents:**
- GitHub Copilot: Code generation & scene expansion
- Claude AI: Complex narrative development & lore consistency
- Custom Agents: Specialized tasks (lore curation, conversion engineering)

**Contributors:** (Open for beta testers Phase 4)
- Proofreading & editing
- Bug reporting
- Feedback on game balance

### Communication Channels

**Documentation-First:**
- `docs/AI_SESSION_HANDOFF.md` - Session transition logs
- `docs/NEXT_TASKS.md` - Prioritized work queue
- `docs/PROJECT_ROADMAP.md` - Timeline & milestones

**GitHub Issues:**
- Bug reports
- Feature requests
- Community feedback (future)

**Discord:** (Planned for Phase 4 - Beta Testing)
- Beta tester community
- Real-time development updates
- Player feedback collection

---

## 8. AI-Assisted Development

### Multi-Agent Coordination

The project uses a specialized multi-AI collaboration system documented in `.github/agents/`:

**Defined Roles:**
1. **Lore Curator (Claude)** - Validates narrative consistency against established canon
2. **Conversion Engineer (Copilot)** - Translates HTML to ChoiceScript format
3. **Structural Reviewer (Cody)** - Ensures scene parity and stat consistency
4. **Quality Balancer** - Equalizes difficulty and stat thresholds
5. **Automation Planner** - Maintains workflow documentation

**Coordination Artifacts:**
- `STATUS_CONTEXT.md` - Weekly snapshot (to be created)
- `SCENE_PARITY_CHECKLIST.md` - HTML vs ChoiceScript tracking (to be created)
- `STATS_MATRIX.md` - Choice impact tracking (to be created)

**Hand-off Conventions:**
- Inline TODOs: `// TODO:[ROLE]: description`
- Commit prefixes: `Lore:`, `Convert:`, `Struct:`, `Balance:`, `Auto:`
- Session logging in `docs/AI_SESSION_HANDOFF.md`

---

## 9. Publishing Pipeline

### Phase Overview

| Phase | Status | Timeline | Deliverables |
|-------|--------|----------|--------------|
| **Phase 1: Foundation** | ✅ Complete | Nov 2025 | HTML game, ChoiceScript scaffold |
| **Phase 2: Content** | ⏳ Active | Dec 2025 - Jan 2026 | All expeditions & endings |
| **Phase 3: Polish** | 📋 Planned | Feb 2026 | Proofing, balancing, testing |
| **Phase 4: Beta** | 📋 Planned | Mar-Apr 2026 | Community testing, iteration |
| **Phase 5: Publication** | 📋 Planned | May-Jun 2026 | Hosted Games submission |
| **Phase 6: Launch** | 📋 Planned | Q3 2026 | App store release |

### Submission Requirements (Hosted Games)

- ✅ 30,000+ word minimum (currently 40,000+)
- ✅ Choice-based interactive fiction format
- ✅ Multiple meaningful endings (14 planned)
- ✅ No AI-generated content (human-written, AI-assisted editing only)
- ⏳ Professional ChoiceScript formatting
- ⏳ Community beta testing (2-4 weeks)
- ⏳ Editor review & revision cycle

**Submission Contact:** submit@hostedgames.org

---

## 10. Metrics & Analytics

### Development Metrics

**Current Progress:**
- ✅ 11 complete scenes (HTML)
- ✅ 2 complete scenes (ChoiceScript professional format)
- ⏳ 3 expedition scenes in development
- 📋 14 ending scenes planned
- **Completion:** ~35% (ChoiceScript version)

**Repository Stats:**
- **Files:** 100+ markdown/text/code files
- **Lore Documents:** 8 major reference files
- **Commits:** 865+ (as of current branch)
- **Lines of Code:** 5,000+ (ChoiceScript), 1,500+ (HTML/JS)

### Target Launch Metrics

**Success Criteria:**
- ✅ Bug-free playthrough of all 14 paths
- ✅ 80%+ positive beta feedback
- ✅ Accepted by Hosted Games editorial team
- 🎯 1,000+ downloads in first month
- 🎯 4+ star average rating
- 🎯 10,000+ total downloads (year 1)

---

## 11. Risk Management

### Technical Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| ChoiceScript syntax errors | Medium | High | Automated Quicktest/Randomtest |
| Stat tracking bugs | Medium | High | Comprehensive manual testing |
| Scene continuity breaks | Low | Medium | Scene parity checklist |
| GitHub Actions failures | Low | Low | Fallback to manual testing |

### Business Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Hosted Games rejection | Low | High | Early beta testing, quality standards |
| Insufficient word count | Very Low | High | Already exceeded minimum |
| Copyright concerns | Very Low | Critical | All original content, documented sources |
| Timeline delays | Medium | Medium | Phased rollout, flexible milestones |

---

## 12. Disaster Recovery

### Backup Strategy

**Primary Backup:** GitHub cloud hosting (automatic)

**Secondary Backups:**
- Local clones on development machines
- Archive folder for historical materials
- Exported releases tagged in Git

**Recovery Procedures:**

1. **Lost Local Work:**
   ```bash
   git fetch origin
   git reset --hard origin/main
   ```

2. **Corrupted Repository:**
   - Clone fresh from GitHub
   - Restore from latest release tag

3. **Accidental Deletion:**
   - Check `archive/` folder
   - Recover from Git history: `git reflog`

**Data Protection:**
- No sensitive data in repository (all in local `.env`)
- Regular commits ensure minimal work loss
- Multiple AI agents can reconstruct content from lore if needed

---

## 13. Scalability & Future Plans

### Phase 6: Expansion (Post-Launch)

**DLC Content:**
- "The Second Thread" - Advanced student storyline
- "Ravencrest Chronicles" - Aria Ravencrest perspective
- "The Third Thread" - Multi-character epic conclusion

**Cross-Media:**
- Full novel series (in development: `writing_drafts/`)
- Audio drama adaptation (potential)
- Illustrated novel version (potential)
- Merchandise (if successful)

### Repository Evolution

**Planned Additions:**
- `assets/` folder for images, audio (Phase 3)
- `releases/` folder for versioned builds (Phase 4)
- `tests/` folder for automated test suites (Phase 3)
- Enhanced CI/CD with automated deployment (Phase 5)

---

## 14. Compliance & Governance

### GitHub Enterprise Features

**Utilized Features:**
- ✅ GitHub Actions (CI/CD automation)
- ✅ Branch protection rules (planned for main)
- ✅ Issue templates (configured)
- ✅ PR templates (configured)
- ✅ Custom agents (Copilot integration)

**Advanced Security:**
- [ ] Dependabot alerts (not needed - zero dependencies)
- [ ] Code scanning (not applicable - narrative content)
- [ ] Secret scanning (enabled by default)

**Organization Settings:**
- Repository visibility: Public (pre-publication)
- Will remain public post-publication (community engagement)
- No external collaborators (AI agents only)

### Audit Trail

**Change Tracking:**
- All commits logged in Git history
- AI sessions documented in `docs/AI_SESSION_HANDOFF.md`
- Major decisions recorded in `docs/PROJECT_ROADMAP.md`

**Compliance Documentation:**
- This file (ENTERPRISE_README.md)
- `CONTRIBUTING.md` - Contribution guidelines
- `CHANGELOG.md` - Release notes
- `.gitignore` - Security exclusions

---

## 15. Quick Reference

### Essential Commands

**Local Development:**
```bash
# Clone repository
git clone https://github.com/issdandavis/Avalon.git

# Play HTML version
open game/index.html

# Set up ChoiceScript (requires Node.js)
cd game
./bootstrap_choicescript.sh
./sync_scenes.sh
```

**Testing:**
```bash
# Run ChoiceScript tests (when implemented)
cd choicescript_game
# Quicktest: validates syntax
# Randomtest: 10,000 random playthroughs
```

**Deployment:**
```bash
# GitHub Pages automatically deploys from main branch
# No manual deployment needed for web version
```

### Key Documents

| Document | Purpose | Audience |
|----------|---------|----------|
| `README.md` | Game overview & player guide | Players, contributors |
| `ENTERPRISE_README.md` | Technical & organizational docs | Stakeholders, DevOps |
| `START_HERE.md` | Quickest play instructions | New players |
| `docs/PROJECT_ROADMAP.md` | Development timeline | Project team |
| `docs/AUTOMATION_GUIDE.md` | CI/CD & integrations | DevOps, developers |
| `.github/COPILOT_INSTRUCTIONS.md` | AI development guidelines | AI agents |

### Support Contacts

**Project Owner:** [@issdandavis](https://github.com/issdandavis)

**External Partners:**
- **Choice of Games LLC** - Publishing platform
- **Hosted Games** - Submission & distribution

**Community:** (Phase 4 - Beta Testing)
- Discord server (TBD)
- GitHub Issues

---

## 16. Appendix

### Glossary

**ChoiceScript:** Proprietary scripting language for Choice of Games interactive fiction  
**Hosted Games:** Publishing platform for community-authored ChoiceScript games  
**Polly:** Polymnia Aetheris - sarcastic raven narrator and main character  
**Spiral of Pollyoneth:** Overarching universe name (4-generation epic)  
**Collaboration Stat:** Core game mechanic tracking cooperative vs. solo magic approach  

### Related Projects

- **Spiral of Pollyoneth Novel Series** (manuscripts in `writing_drafts/`)
- **Aethermoor Chronicles** (generation 2-4 storylines)
- **Izack's Magical Universe** (foundational lore)

### Version History

- **v1.0 (Current)** - Phase 2 development, ChoiceScript conversion in progress
- **v0.9** - HTML game complete, 40,000+ words
- **v0.5** - Initial ChoiceScript scaffold
- **v0.1** - Project initialization

---

## 17. License & Copyright

**Copyright © 2025 @issdandavis**

**Current Status:** All rights reserved (pre-publication)

**Post-Publication Plans:**
- Game content: May remain proprietary (Hosted Games licensing)
- Lore/worldbuilding: Potentially Creative Commons (TBD)
- Code/engine: May open-source HTML version (TBD)

**Attribution:**
- ChoiceScript engine © Choice of Games LLC
- All narrative content original work

---

## Conclusion

The Avalon Codex represents a comprehensive, multi-format narrative project with professional publishing goals. The repository is structured for scalability, maintainability, and collaboration between human developers and AI agents.

**Current Focus:** Complete ChoiceScript professional version (Phase 2)  
**Next Milestone:** Singing Dunes expedition complete  
**Target Launch:** Q2-Q3 2026 via Hosted Games platform  

For game playing instructions, see `README.md`.  
For development tasks, see `docs/PROJECT_ROADMAP.md`.  
For AI collaboration, see `.github/COPILOT_INSTRUCTIONS.md`.

---

*"The spiral continues. Every commit writes another thread."*

**Last Updated:** November 24, 2025  
**Document Owner:** Enterprise Architecture  
**Review Cycle:** Monthly (aligned with phase transitions)
