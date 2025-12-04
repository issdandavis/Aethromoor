# Custom Agents Directory

This directory contains custom agent definitions for the Avalon/Spiral of Pollyoneth project.

## What Are Custom Agents?

Custom agents are specialized AI assistants with domain-specific expertise. Unlike generic AI workers, they have:
- Deep knowledge of specific areas (lore, ChoiceScript, romance design)
- Specialized tools and validation processes
- Quality standards tailored to their domain
- Context about the Spiral of Pollyoneth universe

## Agents in This Directory

### Core Management Agents

**my-agent.agent.md** - Avalon Lore Steward
- Curates and safeguards narrative canon
- Assists with coding and file management
- Maintains lore organization

**agent-manager.agent.md** - Agent Management Coordinator
- Coordinates all 5 AI workflow workers
- Monitors system health
- Generates progress reports
- Resolves conflicts between workers

### Specialized Custom Agents (NEW)

#### Phase 1: Critical (Deploy First) ⚡

**choicescript-converter.agent.md** - ChoiceScript Conversion Specialist
- Converts HTML scenes to ChoiceScript format
- Preserves 100% narrative parity
- Maintains stat tracking and branching
- **ROI:** Saves 45 hours of manual work

**lore-guardian.agent.md** - Lore Consistency Guardian
- Validates content against 8 lore documents
- Catches timeline/character contradictions
- Ensures magic system consistency
- **ROI:** Prevents expensive rewrites

#### Phase 2: Quality (Deploy Second) ⭐

**choicescript-validator.agent.md** - ChoiceScript Technical Validator
- Runs QuickTest/RandomTest suites
- Analyzes stat progression fairness
- Detects unreachable content
- **ROI:** Saves 6 hours of QA work

**polly-voice-architect.agent.md** - Polly's Voice Architect
- Specializes in Polly's meta-commentary
- Balances sarcasm and helpfulness
- Explains dimensional magic accessibly
- **ROI:** Saves 2 hours of voice work

#### Phase 3: Enhancement (Deploy Later) 💕

**romance-orchestrator.agent.md** - Romance System Orchestrator
- Designs ethical polyamory systems
- Creates character-specific romance arcs
- Implements consent-based mechanics
- **ROI:** Saves 3 hours of specialized design

### Configuration Files

**spiralverse-omnifeather-config.yml** - Worker Configuration
- Settings for the 5 automated workflow workers
- Schedule and behavior rules

**my-agent.test.md** - Agent Testing
- Test cases for agent validation

## How to Use Custom Agents

### In GitHub Copilot Chat

Use the `@` mention syntax to invoke specific agents:

```
@choicescript-converter Convert singing_dunes.html scenes 1-3 to ChoiceScript

@lore-guardian Validate the new Verdant Tithe content against canon

@polly-voice-architect Add Polly commentary to rune_glacier scenes
```

### Deployment Strategy

**Week 1:** Deploy Phase 1 agents (Converter + Lore Guardian)
- Test on 1-2 scenes first
- Verify quality meets standards
- Scale to full deployment

**Week 2-3:** Deploy Phase 2 agents (Validator + Polly Architect)
- After Phase 1 content is complete
- Focus on quality and polish

**Week 4+:** Deploy Phase 3 agents (Romance Orchestrator)
- After expeditions are complete
- Enhancement rather than critical path

## Documentation

**Complete Guide:** `/CUSTOM_AGENTS_INDEX.md`
- Full deployment strategy
- ROI calculations
- Troubleshooting guide

**Strategy Document:** `/docs/CUSTOM_AGENT_RECOMMENDATIONS.md`
- Why each agent was chosen
- Task analysis and gap identification
- 71 hours of time savings breakdown

**Implementation Guide:** `/docs/CUSTOM_AGENT_IMPLEMENTATION_GUIDE.md`
- Step-by-step agent creation
- Test cases and validation
- Integration instructions

**Quick Reference:** `/docs/CUSTOM_AGENT_QUICK_REFERENCE.md`
- TL;DR for busy humans
- Decision points and next steps

## Agent Development Guidelines

When creating new agents:

1. **Define Clear Scope:** Agent should have one specific domain
2. **Set Quality Standards:** Define success metrics
3. **Provide Context:** Include lore/universe knowledge
4. **List Prohibited Actions:** Prevent unwanted behaviors
5. **Include Examples:** Show expected input/output
6. **Test Before Deploying:** Validate on small scope first

## Success Metrics

**Combined ROI:** 35x-71x return on investment
- **Time Saved:** 71 hours of manual work
- **Cost:** $100/month in API calls
- **Value:** $3,550-$7,100 at $50-100/hour rate

**Quality Improvements:**
- Zero canon violations in published content
- 100% ChoiceScript syntax validation pass rate
- All 14 endings reachable and balanced
- Consistent character voices across all scenes

## Questions?

See `/CUSTOM_AGENTS_INDEX.md` for complete documentation or create a GitHub issue for assistance.

---

**Status:** ✅ 5 specialized agents ready for deployment  
**Next:** Deploy Phase 1 agents and test on 1-2 scenes  
**Expected Impact:** 50-60% reduction in development time

*"Specialized agents. Accelerated development. Professional quality."*  
**Caw.** 🪶
