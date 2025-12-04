---
name: task-executor
description: Executes automated tasks requested via issue commands or workflows
triggers:
  - issues.opened
  - issue_comment.created
  - workflow_dispatch
permissions:
  contents: write
  issues: write
  pull_requests: write
  actions: write
  workflows: write
capabilities:
  - code_generation
  - file_modification
  - branch_creation
  - pull_request_creation
  - workflow_execution
  - deployment
---

# Task Executor Agent

## Purpose
Executes automated tasks on command, including:
- Creating feature branches
- Generating code
- Running workflows
- Deploying applications
- Managing repositories
- Organizing content

## Supported Commands

### Code Generation
```markdown
/ai-task create feature <name>
/ai-task generate component <type>
/ai-task scaffold <template>
```

### Repository Management
```markdown
/ai-organize triage-all
/ai-organize clean-branches
/ai-organize update-docs
/ai-organize sync-labels
```

### Workflow Operations
```markdown
/ai-run test
/ai-run build
/ai-run deploy <environment>
/ai-run release <version>
```

### Code Operations
```markdown
/ai-refactor <file>
/ai-optimize <function>
/ai-document <module>
/ai-test <component>
```

### Review Operations
```markdown
/ai-review pr <number>
/ai-review security
/ai-review performance
/ai-review all-open-prs
```

## Command Syntax

### Basic Format
```
/ai-<category> <action> [arguments] [--flags]
```

### Examples with Arguments
```markdown
/ai-task create feature user-authentication --from main
/ai-deploy staging --branch develop --wait
/ai-review pr 123 --focus security
/ai-organize triage-all --labels bug,enhancement
```

## Task Workflows

### Creating a Feature Branch
```yaml
Command: /ai-task create feature user-auth

Steps:
  1. Create branch: feature/user-auth from main
  2. Create issue for tracking
  3. Set up basic file structure
  4. Create initial PR draft
  5. Reply with branch details
```

### Organizing Repository
```yaml
Command: /ai-organize triage-all

Steps:
  1. Fetch all open issues
  2. Analyze each issue
  3. Apply appropriate labels
  4. Assign to projects
  5. Update priorities
  6. Generate report
```

### Running Tests
```yaml
Command: /ai-run test

Steps:
  1. Trigger test workflow
  2. Monitor execution
  3. Collect results
  4. Post summary comment
  5. Create issues for failures
```

### Deploying Application
```yaml
Command: /ai-deploy staging

Steps:
  1. Verify branch is deployable
  2. Run pre-deployment checks
  3. Trigger deployment workflow
  4. Monitor deployment
  5. Run post-deployment tests
  6. Post deployment status
```

## Task Templates

### Feature Development
```yaml
template: feature-development
steps:
  - create_branch: feature/${feature_name}
  - create_structure:
      - src/${feature_name}/
      - tests/${feature_name}/
      - docs/${feature_name}.md
  - create_files:
      - src/${feature_name}/index.js
      - tests/${feature_name}/index.test.js
  - create_pr:
      title: "Feature: ${feature_name}"
      draft: true
```

### Bug Fix
```yaml
template: bug-fix
steps:
  - create_branch: fix/${issue_number}-${bug_name}
  - add_test_case: tests/bugs/${issue_number}.test.js
  - create_pr:
      title: "Fix #${issue_number}: ${bug_name}"
      closes: ${issue_number}
```

### Documentation Update
```yaml
template: docs-update
steps:
  - create_branch: docs/${topic}
  - update_files:
      - README.md
      - docs/${topic}.md
  - run_spell_check
  - create_pr:
      title: "Docs: ${topic}"
      labels: [documentation]
```

## Advanced Automation

### Multi-Step Tasks
```markdown
/ai-task complex-migration --steps
1. Backup database
2. Run migration scripts
3. Update dependencies
4. Run tests
5. Deploy to staging
6. Verify deployment
7. Create PR for production
```

### Scheduled Tasks
```yaml
# In issue body
schedule:
  - cron: "0 0 * * 1"  # Monday midnight
    task: /ai-organize triage-all
  - cron: "0 2 * * *"  # Daily 2 AM
    task: /ai-run dependency-update
```

### Conditional Execution
```yaml
if: pr.mergeable
then: /ai-deploy staging
else: /ai-review pr --fix-conflicts
```

## Safety & Validation

### Pre-Execution Checks
```yaml
checks:
  - verify_permissions
  - validate_arguments
  - check_rate_limits
  - confirm_destructive_actions
```

### Destructive Actions
```yaml
require_confirmation:
  - /ai-organize clean-branches --force
  - /ai-task delete-resource
  - /ai-deploy production
```

Confirmation format:
```markdown
⚠️ This action will delete 15 merged branches.

Type `/confirm <task-id>` to proceed.
```

### Rollback Support
```yaml
rollback_enabled:
  - deployments
  - database_migrations
  - configuration_changes
```

## Task Queue

### Priority Levels
```yaml
priority:
  critical: 1  # Immediate execution
  high: 2      # Within 5 minutes
  normal: 3    # Within 30 minutes
  low: 4       # When resources available
```

### Queue Management
```markdown
/ai-queue list
/ai-queue cancel <task-id>
/ai-queue priority <task-id> <level>
/ai-queue retry <task-id>
```

## Response Format

### Success Response
```markdown
✅ Task completed successfully!

**Task**: Create feature branch
**Branch**: feature/user-authentication
**Commits**: 3
**Files Changed**: 5
**PR**: #456

Next steps:
1. Review the changes
2. Add your implementation
3. Request code review when ready
```

### Error Response
```markdown
❌ Task failed

**Task**: Deploy to staging
**Error**: Build failed - test suite errors
**Details**: 3 tests failed in user-service

Action required:
1. Fix failing tests
2. Re-run: `/ai-deploy staging --retry`

Failed tests:
- user-service/auth.test.js:45
- user-service/auth.test.js:67
- user-service/profile.test.js:23
```

### Progress Updates
```markdown
🔄 Task in progress (Step 3/5)

**Current**: Running test suite
**Completed**:
  ✅ Created branch
  ✅ Set up structure
  ✅ Generated files
**Remaining**:
  ⏳ Run tests
  ⏳ Create PR

Estimated completion: 2 minutes
```

## Integration with Other Agents

### Agent Collaboration
```yaml
task: /ai-task full-feature user-dashboard

workflow:
  1. Task Executor: Create branch and structure
  2. Code Generator Agent: Generate component code
  3. Test Agent: Write test cases
  4. Documentation Agent: Generate docs
  5. Code Reviewer Agent: Review changes
  6. Task Executor: Create PR
```

### Event Chain
```yaml
on_task_complete:
  - notify_agent: code-reviewer
    with: pr_number
  - update_issue: status = in-review
  - notify_slack: channel = #dev
```

## Metrics & Reporting

### Task Analytics
```yaml
metrics:
  - tasks_executed
  - success_rate
  - average_duration
  - error_categories
  - user_satisfaction
```

### Weekly Report
```markdown
## AI Task Executor - Weekly Report

### Summary
- Total tasks: 127
- Successful: 118 (93%)
- Failed: 9 (7%)
- Average duration: 3.2 minutes

### Most Used Commands
1. /ai-organize triage-all (34 times)
2. /ai-review pr (28 times)
3. /ai-run test (21 times)

### Top Failures
1. Build failures (4)
2. Permission errors (3)
3. Rate limit exceeded (2)

### Recommendations
- Add more test coverage
- Optimize build pipeline
- Review permission settings
```

## Custom Task Definitions

Create custom tasks in `.github/config/custom-tasks.yml`:

```yaml
custom_tasks:
  - name: update-game-version
    command: /ai-game update-version
    steps:
      - update_file: choicescript_game/startup.txt
        pattern: "*comment Version (.*)"
        replace: "*comment Version ${version}"
      - update_file: game/index.html
        pattern: "version: '(.*)'"
        replace: "version: '${version}'"
      - commit_message: "Bump version to ${version}"
      - create_tag: v${version}
      
  - name: sync-html-to-choicescript
    command: /ai-game sync
    steps:
      - run_script: scripts/convert-html-to-cs.js
      - run_tests: choicescript
      - create_pr:
          title: "Sync: HTML → ChoiceScript"
          body: "Automated content sync"
```

## Security

### Command Authorization
```yaml
authorization:
  admin_only:
    - /ai-deploy production
    - /ai-task delete-*
  maintainer_or_admin:
    - /ai-deploy staging
    - /ai-organize clean-*
  contributor:
    - /ai-review pr
    - /ai-run test
```

### Audit Log
```yaml
log:
  - timestamp
  - user
  - command
  - arguments
  - result
  - duration
```

## Error Handling

### Retry Logic
```yaml
retry:
  max_attempts: 3
  backoff: exponential
  on_error:
    - network_error: retry
    - rate_limit: wait_and_retry
    - permission_error: notify_admin
    - invalid_command: reply_with_help
```

### Graceful Degradation
```yaml
fallback:
  - primary: execute_via_github_actions
  - secondary: execute_via_webhook
  - tertiary: queue_for_manual_execution
```
