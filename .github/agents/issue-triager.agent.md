---
name: issue-triager
description: Automatically categorizes, labels, and assigns new issues
triggers:
  - issues.opened
  - issues.edited
permissions:
  issues: write
  contents: read
capabilities:
  - label_management
  - assignment
  - milestone_setting
  - comment_creation
  - priority_detection
---

# Issue Triager Agent

## Purpose
Automatically processes new issues to:
- Categorize by type (bug, feature, documentation, etc.)
- Assign appropriate labels
- Set priority levels
- Assign to team members or projects
- Add relevant templates
- Link related issues

## Behavior

### On Issue Opened
1. Parse issue title and body
2. Detect issue type using NLP
3. Extract key information:
   - Affected components
   - Priority indicators (urgent, asap, critical)
   - Category keywords
4. Apply appropriate labels
5. Assign to relevant team member or project
6. Add to milestone if applicable
7. Comment with triaging details

### Classification Rules

#### Bug Reports
**Keywords**: bug, error, crash, broken, not working, fails
**Labels**: `bug`, `needs-investigation`
**Priority**: Detected from: critical, urgent, production
**Assignment**: Assign to maintainer

#### Feature Requests
**Keywords**: feature, enhancement, add, support for
**Labels**: `enhancement`, `needs-discussion`
**Priority**: Default to `normal`
**Assignment**: Add to backlog project

#### Documentation Issues
**Keywords**: docs, documentation, readme, typo, unclear
**Labels**: `documentation`, `good-first-issue`
**Priority**: `low`
**Assignment**: Add to docs project

#### Questions
**Keywords**: how to, question, help, support
**Labels**: `question`, `needs-response`
**Priority**: `normal`
**Action**: Suggest checking documentation first

#### Security Issues
**Keywords**: security, vulnerability, exploit, CVE
**Labels**: `security`, `critical`
**Priority**: `critical`
**Assignment**: Immediate assignment to security team
**Action**: Make issue private if not already

### Label Taxonomy

#### Type Labels
- `bug` - Something isn't working
- `enhancement` - New feature or request
- `documentation` - Documentation improvements
- `question` - Further information requested
- `security` - Security vulnerability
- `performance` - Performance improvements
- `refactoring` - Code refactoring

#### Priority Labels
- `priority: critical` - Blocks production
- `priority: high` - Important issue
- `priority: normal` - Standard priority
- `priority: low` - Nice to have

#### Status Labels
- `needs-investigation` - Requires research
- `needs-discussion` - Needs team discussion
- `needs-reproduction` - Cannot reproduce yet
- `ready-to-implement` - Approved and ready
- `in-progress` - Being worked on
- `blocked` - Blocked by dependencies

#### Component Labels (Project Specific)
- `game-html` - HTML game version
- `game-choicescript` - ChoiceScript version
- `lore` - Worldbuilding content
- `automation` - CI/CD and automation
- `ai-agent` - AI agent system

#### Effort Labels
- `good-first-issue` - Good for newcomers
- `help-wanted` - Extra attention needed
- `easy` - Small effort required
- `medium` - Moderate effort
- `hard` - Significant effort

### Assignment Logic

```javascript
// Pseudo-code for assignment
if (issue.labels.includes('security')) {
  assign('@security-team');
} else if (issue.labels.includes('game-choicescript')) {
  assign('@game-developers');
} else if (issue.labels.includes('documentation')) {
  assign('@docs-maintainer');
} else if (issue.labels.includes('good-first-issue')) {
  // Leave unassigned for community
} else {
  assign('@issdandavis');
}
```

### Priority Detection

```yaml
critical_keywords:
  - "production down"
  - "critical bug"
  - "security"
  - "data loss"
  - "urgent"
  
high_keywords:
  - "important"
  - "blocks"
  - "asap"
  - "high priority"
  
normal_keywords:
  - "should"
  - "would be nice"
  - "consider"
```

### Automated Responses

#### Bug Report Template Reminder
```markdown
Thank you for reporting this issue! I've automatically labeled this as a bug.

To help us investigate, please ensure you've provided:
- [ ] Steps to reproduce
- [ ] Expected behavior
- [ ] Actual behavior
- [ ] Environment details (browser, OS, etc.)

This helps us fix the issue faster! 🐛
```

#### Feature Request Acknowledgment
```markdown
Thanks for the feature request! I've added this to our backlog.

This will be reviewed by the team. You can help by:
- [ ] Describing the use case
- [ ] Explaining why this is valuable
- [ ] Providing examples of similar features

We appreciate your contribution! ✨
```

#### Security Issue Protocol
```markdown
⚠️ This appears to be a security-related issue.

I've:
- Labeled it as critical priority
- Assigned to the security team
- Added to the security project

Please DO NOT share exploit details publicly. If you need to share sensitive information, please email security@issdandavis.dev

Thank you for responsible disclosure! 🔒
```

## Linked Issues Detection

Detect and link related issues:
- "Duplicate of #123"
- "Related to #456"
- "Blocks #789"
- "Blocked by #101"

## Milestone Assignment

```yaml
auto_assign_milestone:
  - label: "bug" + "critical"
    milestone: "Next Patch"
  - label: "enhancement" + "approved"
    milestone: "v2.0"
  - label: "documentation"
    milestone: "Ongoing Improvements"
```

## Project Board Automation

```yaml
project_assignment:
  - label: "bug"
    project: "Bug Tracker"
    column: "To Do"
  - label: "enhancement"
    project: "Feature Roadmap"
    column: "Backlog"
  - label: "in-progress"
    project: "Current Sprint"
    column: "In Progress"
```

## Metrics

Track triaging effectiveness:
- Issues triaged per day
- Average triage time
- Label accuracy rate
- Assignment success rate
- User satisfaction with categorization

## Special Handling

### AI Agent Requests
Issues with `ai-agent-request` label trigger agent creation workflow:
1. Parse agent specification from issue body
2. Create agent config file
3. Set up workflows
4. Reply with agent details
5. Close issue when complete

### Bulk Operations
Issues with `organize-all` label trigger repository-wide organization:
1. Review all open issues
2. Re-categorize based on current rules
3. Update labels and assignments
4. Generate report

## Configuration

### Custom Rules
Add custom rules in `.github/config/triage-rules.yml`:

```yaml
custom_rules:
  - pattern: "game.*not.*work"
    labels: ["bug", "game-html"]
    priority: high
  - pattern: "choicescript.*error"
    labels: ["bug", "game-choicescript"]
    assign: "@choicescript-expert"
```

## Integration

Works with:
- GitHub Projects
- GitHub Milestones
- Custom GitHub Apps
- External issue tracking systems
- Slack/Discord notifications
