# AI Agent Orchestration System
## Avalon Codex - Multi-Agent Automation Platform

## Overview

This system coordinates multiple specialized AI agents working together 24/7 to grow, organize, and maintain the Avalon Codex project. Each agent has a specific role, and they collaborate to ensure content is continuously generated, organized, and refined.

## Agent Roles

### 1. Content Organizer Agent
**Purpose:** File management and organization
**Location:** `.github/agents/content-organizer.agent.md`

**Responsibilities:**
- Automatically categorize and file new content
- Maintain clean directory structure
- Generate metadata and indexes
- Prevent duplicate files
- Monitor repository for misplaced content

**Trigger:** New file detected, scheduled cleanup, manual dispatch

### 2. Lore Curator Agent
**Purpose:** Canon maintenance and consistency
**Location:** `.github/agents/lore-curator.agent.md`

**Responsibilities:**
- Verify lore consistency across all content
- Expand worldbuilding based on identified gaps
- Validate new content against established canon
- Maintain character chronicles and timelines
- Cross-reference related lore elements

**Trigger:** New lore commits, weekly scan, PR reviews

### 3. Content Generator Agent
**Purpose:** Active content creation
**Location:** `.github/agents/content-generator.agent.md`

**Responsibilities:**
- Generate new game scenes from outlines
- Expand placeholder content
- Create lore entries for identified gaps
- Generate dialogue variations
- Produce documentation

**Trigger:** Daily generation queue, weekly sprints, on-demand requests

### 4. Scene Converter Agent (Existing)
**Purpose:** HTML to ChoiceScript conversion
**Location:** Custom agent (my-agent)

**Responsibilities:**
- Convert HTML game content to ChoiceScript format
- Maintain narrative parity between versions
- Implement proper stat tracking
- Preserve choice logic and branching

**Trigger:** Manual requests for scene conversion

## Agent Coordination Workflows

### Workflow 1: New Content Pipeline
```mermaid
New Content Added
    ↓
Content Organizer: Categorize & File
    ↓
Lore Curator: Validate Canon
    ↓
Content Generator: Identify Related Gaps
    ↓
Content Organizer: Update Indexes
    ↓
Notification Sent
```

### Workflow 2: Daily Content Generation
```mermaid
Daily Schedule Trigger (2 AM)
    ↓
Content Generator: Create New Content
    ↓
Lore Curator: Validate Against Canon
    ↓
Content Organizer: File in Correct Location
    ↓
GitHub PR Created for Review
    ↓
Notification to Project Channel
```

### Workflow 3: Repository Cleanup
```mermaid
Weekly Schedule Trigger (Sunday)
    ↓
Content Organizer: Scan for Misplaced Files
    ↓
Content Organizer: Move to Correct Locations
    ↓
Content Organizer: Update All Indexes
    ↓
Lore Curator: Validate Cross-References
    ↓
Summary Report Generated
```

### Workflow 4: Scene Expansion Sprint
```mermaid
Manual Trigger OR Weekly Schedule
    ↓
Content Generator: Identify Priority Scene
    ↓
Scene Converter: Convert HTML to ChoiceScript (if needed)
    ↓
Content Generator: Expand to 500+ Lines
    ↓
Lore Curator: Validate Character Voices & Canon
    ↓
Content Organizer: File and Tag
    ↓
PR Created with Quality Report
```

## Automation Schedule

### Daily Operations (Every Day at 2 AM UTC)
```yaml
daily_tasks:
  content_generator:
    - Generate 1 new lore entry
    - Expand 1 scene by 100-200 lines
    - Create 3-5 dialogue variations
    - Generate worldbuilding details
  
  lore_curator:
    - Scan commits for canon conflicts
    - Validate new additions
    - Update cross-references
    - Generate consistency report
  
  content_organizer:
    - Check root directory for new files
    - Organize misplaced content
    - Update indexes
    - Clean temporary files
```

### Weekly Operations (Every Sunday at Midnight UTC)
```yaml
weekly_tasks:
  content_generator:
    - Complete 1 full expedition scene (500+ lines)
    - Generate 2-3 character development moments
    - Create 1 new ending variation
    - Expand 5 minor lore entries
  
  lore_curator:
    - Full canon audit
    - Identify top 5 lore gaps
    - Generate expansion recommendations
    - Update master chronicles
  
  content_organizer:
    - Deep directory scan
    - Regenerate all indexes
    - Archive superseded content
    - Generate organization report
```

### Monthly Operations (1st of Each Month)
```yaml
monthly_tasks:
  all_agents:
    - Performance metrics review
    - Quality assessment
    - Strategy adjustment
    - Comprehensive report generation
  
  lore_curator:
    - Complete timeline validation
    - Character relationship map update
    - Magic system documentation review
    - Canon snapshot creation
  
  content_organizer:
    - Directory structure optimization
    - Naming convention audit
    - Metadata cleanup
    - Archive maintenance
```

## Communication Protocol

### Agent-to-Agent Communication
```yaml
protocol:
  format: JSON message passing
  channels:
    - GitHub Actions workflow data
    - Shared state files in .github/agents/state/
    - PR comments and tags
    - Issue labels and assignments
  
  message_types:
    - task_request: Agent requests another agent perform task
    - validation_needed: Content needs review
    - task_complete: Agent finished assigned work
    - conflict_detected: Issue requiring resolution
    - gap_identified: Opportunity for content generation
```

### Agent-to-Human Communication
```yaml
notification_channels:
  github:
    - Pull requests for content review
    - Issues for conflicts or questions
    - Discussions for strategic decisions
    
  external (if configured):
    - Discord: Daily summaries, important alerts
    - Slack: Team notifications
    - Email: Weekly reports, critical issues
```

## Integration Points

### GitHub Actions
All agents can be triggered via GitHub Actions workflows located in `.github/workflows/`:

```yaml
# Example: Daily Content Generation
name: Daily Content Generation
on:
  schedule:
    - cron: '0 2 * * *'  # 2 AM UTC daily
  workflow_dispatch:  # Manual trigger

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run Content Generator
        run: |
          # Agent execution logic
      - name: Validate with Lore Curator
        run: |
          # Validation logic
      - name: Organize with Content Organizer
        run: |
          # Organization logic
      - name: Create PR
        uses: peter-evans/create-pull-request@v5
```

### External Automation (Zapier Integration)
```yaml
zapier_triggers:
  - Google Docs updated → Notify Content Organizer
  - Notion database changed → Trigger Content Generator
  - Discord command → Manual agent dispatch
  - Form submission → Create content request
```

### API Endpoints (Future)
```yaml
api_endpoints:
  - POST /api/generate/scene
  - POST /api/organize/content
  - GET /api/validate/lore
  - POST /api/convert/scene
  - GET /api/status/agents
```

## State Management

### Agent State Files
Location: `.github/agents/state/`

```yaml
content_organizer_state.json:
  last_run: timestamp
  files_organized: count
  pending_reviews: list
  
lore_curator_state.json:
  last_canon_check: timestamp
  identified_gaps: list
  validation_queue: list
  
content_generator_state.json:
  last_generation: timestamp
  scenes_generated: count
  current_priority: scene_name
  generation_queue: list
```

### Shared Context
Location: `.github/agents/context/`

```yaml
shared_context.json:
  project_priorities: list
  active_scenes: list
  blocked_tasks: list
  completed_milestones: list
  
generation_targets.json:
  scenes_needed: list
  lore_gaps: list
  documentation_tasks: list
```

## Quality Gates

### Before Content Commit
```yaml
required_checks:
  - Lore Curator: Canon validation passed
  - Content Organizer: Properly filed and tagged
  - Syntax Validator: ChoiceScript/Markdown valid
  - Quality Metrics: Meets minimum standards
  
approval_process:
  auto_merge_if:
    - All quality gates passed
    - Content type is minor update
    - Confidence score > 95%
  
  human_review_if:
    - Major canon additions
    - Character voice concerns
    - Confidence score 75-95%
  
  reject_if:
    - Canon conflicts detected
    - Quality score < 60%
    - Syntax errors
```

## Error Handling

### Agent Failure Recovery
```yaml
on_agent_failure:
  1. Log error details
  2. Create GitHub issue with failure context
  3. Notify human maintainer
  4. Attempt automatic retry (max 3 attempts)
  5. Fallback to manual process if critical
  
failure_types:
  - syntax_error: Flag for human fix
  - canon_conflict: Lore curator manual review
  - file_conflict: Content organizer escalation
  - api_limit: Queue for next cycle
```

### Conflict Resolution
```yaml
conflict_types:
  
  file_conflict:
    - Preserve both versions with timestamps
    - Create issue for human decision
    - Tag with 'conflict-resolution' label
  
  canon_conflict:
    - Lore curator documents both versions
    - Create issue with analysis
    - Tag with 'canon-decision-needed'
  
  quality_conflict:
    - Document quality concerns
    - Request human review
    - Tag with 'quality-review'
```

## Monitoring & Reporting

### Daily Reports
```yaml
generated_at: 2 AM UTC + 30 minutes
contains:
  - Content generated (word count, files)
  - Organization actions (files moved, tags added)
  - Canon checks performed (conflicts found, gaps identified)
  - Quality metrics (acceptance rate, revision count)
  
delivery:
  - GitHub Discussion post
  - Discord/Slack channel (if configured)
  - Email summary (weekly rollup)
```

### Weekly Reports
```yaml
generated_at: Sunday midnight + 1 hour
contains:
  - Week's productivity summary
  - Content acceptance rate
  - Canon compliance score
  - Top quality metrics
  - Upcoming priorities
  - Identified bottlenecks
  
delivery:
  - GitHub Release notes
  - Comprehensive email report
  - Project dashboard update
```

### Monthly Analytics
```yaml
generated_at: 1st of month
contains:
  - Full productivity metrics
  - Quality trend analysis
  - Canon expansion report
  - Agent performance comparison
  - Strategic recommendations
  
delivery:
  - Detailed report in docs/
  - Stakeholder presentation format
  - GitHub Project update
```

## Configuration

### Agent Configuration Files
Location: `.github/agents/config/`

```yaml
# content_organizer_config.yml
confidence_threshold: 0.85
auto_organize_threshold: 0.85
manual_review_threshold: 0.60
monitored_paths:
  - "/"
  - "/temp/"
exclude_paths:
  - ".git/"
  - "node_modules/"

# lore_curator_config.yml
strictness_level: high
auto_expand_gaps: true
max_daily_expansions: 3
canon_sources:
  - "lore/IZACK_MASTER_CHRONICLE_UPDATED.txt"
  - "docs/AETHERMOOR_CHRONICLES.md"

# content_generator_config.yml
daily_scene_lines: 200
weekly_scene_lines: 500
min_quality_score: 70
voice_consistency_weight: 0.3
canon_compliance_weight: 0.4
creativity_weight: 0.3
```

## Security & Privacy

### API Key Management
```yaml
required_keys:
  - ANTHROPIC_API_KEY (for Claude-based agents)
  - OPENAI_API_KEY (for GPT-based agents)
  - GITHUB_TOKEN (for automation)

storage:
  - GitHub Secrets for Actions
  - Environment variables for local dev
  - Never commit to repository

rotation:
  - Monthly key rotation recommended
  - Audit access logs quarterly
```

### Access Control
```yaml
permissions:
  content_generator:
    - Write to generated_content/
    - Create PRs
    - Read from lore/, writing_drafts/, game/
  
  lore_curator:
    - Read all lore and writing
    - Write to lore/ (via PR only)
    - Comment on PRs
  
  content_organizer:
    - Read/write all content directories
    - Manage tags and metadata
    - Update indexes
```

## Getting Started

### Initial Setup
```bash
# 1. Configure API keys
cp config/.env.example config/.env
# Edit config/.env and add your API keys

# 2. Review agent configurations
ls .github/agents/config/
# Edit configs as needed

# 3. Enable GitHub Actions
# Go to repository Settings → Actions → Enable workflows

# 4. Test individual agents
gh workflow run daily-content-generation.yml

# 5. Monitor first run
gh run list --workflow=daily-content-generation.yml
```

### Customization
```yaml
to_customize:
  - Edit .github/agents/config/*.yml for agent behavior
  - Modify .github/workflows/*.yml for schedule changes
  - Update agent markdown files for capability changes
  - Adjust quality gates in orchestrator config
```

## Maintenance

### Weekly Checks
- [ ] Review generated content PRs
- [ ] Check agent error logs
- [ ] Monitor API usage and costs
- [ ] Validate organization accuracy

### Monthly Tasks
- [ ] Audit agent performance metrics
- [ ] Review and approve lore expansions
- [ ] Update agent configurations as needed
- [ ] Rotate API keys if scheduled

### Quarterly Reviews
- [ ] Full system audit
- [ ] Strategy adjustment based on results
- [ ] Documentation updates
- [ ] Stakeholder reporting

## Success Metrics

### Productivity Metrics
- Content generated per week (target: 2000+ words)
- Scenes completed per month (target: 10+)
- Lore entries created (target: 15+ per month)
- Organization actions (target: 95%+ accuracy)

### Quality Metrics
- Content acceptance rate (target: >70%)
- Canon compliance (target: >95%)
- Human edit percentage (target: <30%)
- Voice consistency (target: >85%)

### Efficiency Metrics
- Time from generation to review (target: <24 hours)
- Organization latency (target: <1 hour)
- Error rate (target: <5%)
- Human intervention needed (target: <15%)

## Support & Troubleshooting

### Common Issues

**Issue:** Agent not running on schedule
- Check GitHub Actions are enabled
- Verify workflow file syntax
- Check for API quota issues

**Issue:** Content quality below standards
- Review generator configuration
- Adjust quality thresholds
- Update voice guidelines

**Issue:** Organization errors
- Check directory permissions
- Validate file naming patterns
- Review confidence thresholds

### Getting Help
- **Documentation:** See `.github/agents/*.agent.md`
- **Issues:** Create GitHub issue with `agent-help` label
- **Discussions:** Use GitHub Discussions for questions
- **Emergency:** Tag repository maintainer in issue
