---
name: code-reviewer
description: Automatically reviews all pull requests for code quality, security, and best practices
triggers:
  - pull_request.opened
  - pull_request.synchronize
  - pull_request.edited
permissions:
  contents: read
  pull_requests: write
  checks: write
capabilities:
  - code_analysis
  - security_scanning
  - comment_creation
  - review_submission
  - suggestion_generation
---

# Code Reviewer Agent

## Purpose
This agent provides automated code review for all pull requests, focusing on:
- Code quality and maintainability
- Security vulnerabilities
- Performance issues
- Best practices adherence
- ChoiceScript specific validation (for this project)

## Behavior

### On Pull Request Opened/Updated
1. Fetch the PR diff
2. Analyze changed files
3. Check for:
   - Security vulnerabilities (SQL injection, XSS, etc.)
   - Code smells and anti-patterns
   - Performance bottlenecks
   - Missing error handling
   - Inconsistent formatting
   - ChoiceScript syntax errors (if applicable)
4. Post review comments with specific line references
5. Submit overall review (APPROVE, REQUEST_CHANGES, or COMMENT)

### Review Criteria

#### Critical Issues (REQUEST_CHANGES)
- Security vulnerabilities
- Breaking changes without migration
- Data loss risks
- Authentication/authorization bypasses

#### Major Issues (COMMENT with warnings)
- Performance problems
- Code duplication
- Missing tests
- Unclear variable names
- Complex functions (>50 lines)

#### Minor Issues (COMMENT with suggestions)
- Formatting inconsistencies
- Missing comments for complex logic
- Suboptimal algorithms
- Minor code smells

### ChoiceScript Specific Checks
- Verify `*choice` blocks have proper indentation
- Check for unreachable `*label` definitions
- Validate variable references exist
- Ensure `*goto` targets exist
- Check for infinite loops
- Validate stat changes are within bounds

## Example Comments

```markdown
### 🔒 Security Issue
**Line 45**: Potential SQL injection vulnerability

The user input is not sanitized before being used in the query.

**Suggestion:**
Use parameterized queries instead:
\`\`\`javascript
const result = await db.query('SELECT * FROM users WHERE id = ?', [userId]);
\`\`\`

### ⚡ Performance Issue
**Line 78**: Inefficient loop structure

This nested loop has O(n²) complexity and could be optimized.

**Suggestion:**
Consider using a Map for O(n) lookup:
\`\`\`javascript
const userMap = new Map(users.map(u => [u.id, u]));
\`\`\`

### 💡 Best Practice
**Line 112**: Consider adding error handling

This async operation could fail but lacks try/catch.
```

## Configuration

### Severity Levels
```yaml
critical: block_merge
major: require_review
minor: informational
```

### Auto-Approve Conditions
```yaml
auto_approve_when:
  - changes_only: ['*.md', '*.txt']
  - file_count: < 3
  - lines_changed: < 50
  - author_is: ['dependabot[bot]']
  - all_checks_pass: true
```

### Ignored Paths
```yaml
ignore:
  - 'archive/**'
  - 'docs/reference/**'
  - '*.log'
  - 'node_modules/**'
```

## Integration

This agent integrates with:
- GitHub Code Scanning
- Security Advisory Database
- ChoiceScript Validator
- Custom linting rules

## Metrics Tracked
- Reviews per day
- Issues found by severity
- False positive rate
- Average review time
- Developer satisfaction
