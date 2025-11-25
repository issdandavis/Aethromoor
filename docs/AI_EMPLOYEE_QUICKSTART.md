# AI Employee System - Quick Start Guide

**Welcome to your AI Enterprise!** This guide shows you how to work with your AI employee team.

---

## Your AI Team

### 👤 Avalon Lore Steward (Your Main Contact)
**What they do**: Act as your personal assistant, handle lore questions, organize files, route complex tasks
**When to use**: First point of contact for any request
**How to summon**: Tag `@my-agent` or just ask naturally in issues/PRs

### 🎯 Enterprise Manager
**What they do**: Orchestrate workflows across all AI employees, manage task routing
**When to use**: Complex multi-step projects, workflow optimization
**How to summon**: Tag `@enterprise-manager` or route through Lore Steward

### 📚 Lore Curator
**What they do**: Validate narrative consistency, check canon, prevent plot holes
**When to use**: Adding new lore, checking character details, timeline questions
**How to summon**: Tag `@lore-curator` or route through Enterprise Manager

### 🔧 Conversion Engineer
**What they do**: Convert HTML game content to ChoiceScript, expand scenes
**When to use**: Need new scenes created, HTML→ChoiceScript translation
**How to summon**: Tag `@conversion-engineer` or route through Enterprise Manager

### ⚖️ Quality Balancer
**What they do**: Balance stats, check gameplay fairness, ensure endings are achievable
**When to use**: Game feels too hard/easy, stat concerns, balance issues
**How to summon**: Tag `@quality-balancer` or route through Enterprise Manager

### 📖 Documentation Maintainer
**What they do**: Keep all docs current, update guides, maintain knowledge base
**When to use**: Docs outdated, need new documentation, can't find something
**How to summon**: Tag `@documentation-maintainer` or route through Enterprise Manager

---

## How to Work with Your AI Team

### Simple Requests (Use Lore Steward)

Just create an issue or comment naturally:

```
"Where should I put the new character backstory I wrote?"

"What's the canonical spelling of Izack's last name?"

"Can you show me the current game development status?"
```

The Lore Steward will:
- Answer directly if simple
- Route to specialists if complex
- Keep you updated on progress
- Coordinate the AI team for you

### Complex Projects (Use Enterprise Manager)

For multi-step work, tag the Enterprise Manager:

```
@enterprise-manager I want to add a fourth expedition to the game 
featuring a mountain realm with crystal magic. Can you coordinate this?
```

The Enterprise Manager will:
1. Break down the project into tasks
2. Route to appropriate AI employees
3. Manage handoffs between agents
4. Keep you updated on each phase
5. Deliver the completed work

### Specialist Requests

If you know exactly which specialist you need:

```
@lore-curator Can you verify if this new character contradicts 
existing lore about the Singing Dunes?

@quality-balancer Is the Collaborative Master ending too hard 
to achieve? Should we lower the threshold from 80 to 75?

@documentation-maintainer Please update STATUS_CONTEXT.md to 
reflect that we've finished all three expeditions.
```

---

## Common Scenarios

### Scenario 1: "I wrote a new character. Where does it go?"

**Your ask**: "@my-agent I wrote a new character named Soren who's a wind mage. Where should I put this?"

**What happens**:
1. Lore Steward receives your request
2. Suggests: `lore/characters/` directory
3. Asks: "Should I create a new file `lore/characters/soren.md` for you?"
4. Once you approve, creates the file
5. Routes to Lore Curator to verify no canon conflicts
6. Routes to Documentation Maintainer to update character lists

**Result**: New character file created, verified, and documented ✅

### Scenario 2: "The game feels unbalanced"

**Your ask**: "@my-agent Players are saying the best ending is too hard to get"

**What happens**:
1. Lore Steward receives complaint
2. Routes to Enterprise Manager for coordination
3. Enterprise Manager tasks Quality Balancer to analyze
4. Quality Balancer reviews STATS_MATRIX.md
5. Quality Balancer provides analysis + recommendations
6. You decide which fix to implement
7. Conversion Engineer implements the changes
8. Quality Balancer verifies fix
9. Documentation Maintainer updates balance docs

**Result**: Game balance improved with full analysis and documentation ✅

### Scenario 3: "I want to add new content"

**Your ask**: "@enterprise-manager I want to add a new scene between first_lesson and the expeditions where players practice collaborative magic"

**What happens**:
1. Enterprise Manager receives project
2. Creates task breakdown:
   - Lore Curator: Verify this fits timeline
   - Conversion Engineer: Create new scene file
   - Quality Balancer: Determine stat impact
   - Documentation Maintainer: Update scene lists
3. Coordinates each phase
4. Manages handoffs between agents
5. Delivers complete, tested, documented scene

**Result**: New scene added with full integration ✅

### Scenario 4: "I need to find something"

**Your ask**: "Where is the document that explains the magic system?"

**What happens**:
1. Lore Steward searches docs/
2. Finds: `docs/GAME_DEVELOPMENT_MASTER_REFERENCE.md`
3. Provides direct link with relevant section
4. Asks: "Do you want me to improve the description in FILE_LOCATIONS.txt so it's easier to find next time?"

**Result**: Document found + navigation improved ✅

---

## Communication Best Practices

### ✅ Good Communication

```
Clear request:
"@my-agent Can you update the README to reflect that we now have 14 endings instead of 12?"

Specific question:
"@lore-curator Does the new forest character conflict with the Thoughtvines' ability to read minds?"

Actionable ask:
"@quality-balancer Please analyze if the Singing Dunes path grants too many collaboration points"
```

### ❌ Unclear Communication

```
Too vague:
"Fix the thing"

Multiple mixed requests:
"Update docs and also check lore and maybe balance the stats or something?"
(Better to split into separate requests)

No context:
"Is this right?"
(Better to specify what "this" is)
```

---

## Task Routing Guide

**Use this flowchart to decide who to ask:**

```
Start: Do you have a question or request?
    ↓
Is it about lore/canon/story?
    YES → @lore-curator (or @my-agent to route)
    NO → Continue
    ↓
Is it about game balance/stats?
    YES → @quality-balancer (or @my-agent to route)
    NO → Continue
    ↓
Is it about creating/converting scenes?
    YES → @conversion-engineer (or @my-agent to route)
    NO → Continue
    ↓
Is it about documentation?
    YES → @documentation-maintainer (or @my-agent to route)
    NO → Continue
    ↓
Is it a complex multi-step project?
    YES → @enterprise-manager
    NO → Continue
    ↓
Not sure? → @my-agent (Lore Steward will route it correctly!)
```

**Pro tip**: When in doubt, always start with `@my-agent`. The Lore Steward will route your request to the right specialist.

---

## Tracking Progress

### Check Current Status

All AI work is tracked in:
- **`docs/STATUS_CONTEXT.md`** - Weekly snapshot of current work
- **`docs/AI_COORDINATION_LOG.md`** - Detailed agent activity log
- **GitHub Issues** - Individual tasks and requests
- **Pull Requests** - Code changes and reviews

### Monitor Agent Activity

Each agent logs their work in `docs/AI_COORDINATION_LOG.md`:

```markdown
### [Date] - [Agent Name]

**Task**: [What they worked on]
**Completed**: [What was delivered]
**Next**: [What happens next]
**Handoff to**: [Which agent gets it next]
```

### Request Status Updates

Just ask!

```
"@my-agent What's the status of the new mountain expedition?"

"@enterprise-manager Can you give me a progress update on the balance refinement project?"
```

---

## Advanced Features

### Automated Validation

Every time you push code or create a PR, the AI Employee Validation workflow runs:

- ✅ Lore consistency checks
- ✅ Scene parity verification (HTML ↔ ChoiceScript)
- ✅ Stats balance validation
- ✅ Documentation currency checks
- ✅ Enterprise system health

View results in GitHub Actions tab.

### Multi-Agent Workflows

For complex projects, agents work together automatically:

```
Example: Adding a new ending

1. You request via @enterprise-manager
2. Lore Curator verifies it fits canon
3. Conversion Engineer implements in ChoiceScript
4. Quality Balancer checks stat requirements
5. Documentation Maintainer updates ending lists
6. You get notified when complete
```

### Knowledge Accumulation

Your AI team learns and remembers:
- All lore decisions are logged
- Balance adjustments are documented
- Workflow improvements are captured
- Best practices are shared

Check `docs/AI_COORDINATION_LOG.md` for the full knowledge base.

---

## Troubleshooting

### "My request wasn't understood"

Try:
1. Rephrase more specifically
2. Add more context
3. Break into smaller requests
4. Ask @my-agent to help clarify what you need

### "Work is taking too long"

Check:
1. `docs/AI_COORDINATION_LOG.md` for current status
2. If there's a blocker mentioned
3. Ask @enterprise-manager for progress update

### "Agents gave conflicting information"

This shouldn't happen, but if it does:
1. Tag @enterprise-manager to investigate
2. They'll coordinate with affected agents
3. Correct information will be documented
4. Conflict resolution logged for future reference

### "I need help using the system"

Ask @my-agent (Lore Steward):
```
"@my-agent How do I request a balance check?"
"@my-agent Which agent handles documentation updates?"
"@my-agent Can you explain how the Enterprise Manager works?"
```

---

## Quick Reference

### Agent Summoning

| Need | Tag |
|------|-----|
| General help | `@my-agent` |
| Complex project | `@enterprise-manager` |
| Lore question | `@lore-curator` |
| Scene creation | `@conversion-engineer` |
| Balance issue | `@quality-balancer` |
| Docs update | `@documentation-maintainer` |

### Key Documents

| Document | Purpose |
|----------|---------|
| `STATUS_CONTEXT.md` | Current project state |
| `AI_COORDINATION_LOG.md` | Agent activity history |
| `SCENE_PARITY_CHECKLIST.md` | Game version tracking |
| `STATS_MATRIX.md` | Balance data |
| `.github/agents/` | Agent definitions |

### Communication Templates

**Simple Request**:
```
@my-agent [clear question or request]
```

**Complex Project**:
```
@enterprise-manager I need to [high-level goal].

Details:
- [Requirement 1]
- [Requirement 2]

Timeline: [if urgent]
```

**Specialist Request**:
```
@[specific-agent] Please [specific action]

Context: [why this is needed]
Related files: [if applicable]
```

---

## Examples in Action

### Real Request Example 1

```
Issue Title: Add new Polly commentary to first lesson

@my-agent Can you add more of Polly's sarcastic comments 
to the first_lesson.txt scene? She should react when players 
try to control the magic instead of collaborating with it.
```

**AI Response**:
```
✅ Got it! I'll coordinate this:

1. Routing to Conversion Engineer to add Polly commentary
2. They'll add 2-3 new Polly reaction lines when player 
   chooses control path
3. Lore Curator will verify voice consistency
4. Documentation Maintainer will update word count

I'll update you when complete (est. 30-45 min).
```

### Real Request Example 2

```
@quality-balancer I'm concerned that the Heartwood Guardian 
ending might be too hard to achieve. Can you analyze the 
requirements and recommend adjustments if needed?
```

**AI Response**:
```
📊 Balance Analysis: Heartwood Guardian Ending

Current Requirements:
- Collaboration: 70+
- Izack Relationship: 50+
- Verdant Tithe expedition: Heartwood path
- Deep forest bond: Accepted

Analysis:
- Starting collab: 50
- Forest max gain: +63 (Heartwood path)
- Can reach: 113 (capped at 100)
- ✅ Requirements are achievable

Accessibility:
- Best path: 50 → 113 (capped 100) ✅ Can reach 70+
- Average path: 50 → 70 ✅ Just barely achievable
- Poor path: 50 → 40 ❌ Can't reach 70

Recommendation:
⚠️ Ending is achievable but requires very good Forest choices.
Consider:
A) Lower threshold to 65 (more accessible)
B) Keep at 70 (rewards excellent play)
C) Add alternate path with relationship requirement

Your call! I can implement any option.
```

---

## Getting Started Now

### Your First Step

1. Create an issue or comment: 
   ```
   @my-agent Can you explain the current state of the Avalon project?
   ```

2. The Lore Steward will provide a comprehensive status update

3. Ask follow-up questions about anything unclear

### Your Second Step

Try a simple request:
```
@my-agent Can you show me where all the lore documents are located?
```

### Your Third Step

Try a specialist request:
```
@quality-balancer Can you give me an overview of how game balance 
is tracked in this project?
```

---

## Support

### Need More Help?

- Read the agent definitions: `.github/agents/[agent-name].agent.md`
- Check the coordination log: `docs/AI_COORDINATION_LOG.md`
- Review status context: `docs/STATUS_CONTEXT.md`
- Ask @my-agent for clarification on anything

### System Health

Check `.github/workflows/ai-employee-validation.yml` runs to ensure:
- All agents are defined ✅
- Shared artifacts are current ✅
- Documentation is up-to-date ✅
- System is operational ✅

---

**Welcome to your AI-powered enterprise! Your team is ready to help you build the Avalon Codex.**

*Questions? Just ask @my-agent anytime!*
