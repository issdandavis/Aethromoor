---
name: security-agent
description: Monitors and fixes security vulnerabilities automatically
triggers:
  - push
  - pull_request
  - schedule
  - dependabot_alert
  - secret_scanning_alert
  - code_scanning_alert
permissions:
  contents: write
  security_events: write
  pull_requests: write
  issues: write
capabilities:
  - vulnerability_scanning
  - dependency_updates
  - secret_detection
  - security_patch_generation
  - compliance_checking
---

# Security Agent

## Purpose
Proactively monitors and addresses security concerns:
- Dependency vulnerabilities
- Secret leaks
- Code security issues
- Compliance violations
- Security best practices

## Automatic Scanning

### Dependency Scanning
```yaml
on_schedule:
  cron: "0 0 * * *"  # Daily
  scan:
    - npm_dependencies
    - python_dependencies
    - github_dependencies
  
  on_vulnerability:
    - create_issue: priority=critical
    - create_pr: auto_update
    - notify_team: security-channel
```

### Secret Scanning
```yaml
on_push:
  scan_for:
    - api_keys
    - passwords
    - tokens
    - certificates
    - private_keys
  
  on_detection:
    - block_commit: if_high_confidence
    - alert_user: immediate
    - create_issue: security_label
    - revoke_credential: if_possible
```

### Code Scanning
```yaml
on_pr:
  run_checks:
    - sql_injection
    - xss_vulnerabilities
    - csrf_issues
    - authentication_bypass
    - authorization_flaws
    - insecure_deserialization
  
  severity_levels:
    critical: block_merge
    high: require_review
    medium: comment
    low: informational
```

## Security Checks

### Input Validation
```javascript
// Check for missing input sanitization
function checkInputValidation(code) {
  const patterns = [
    /req\.query\.(.*?)(?!.*sanitize)/,  // Unsanitized query params
    /req\.body\.(.*?)(?!.*validate)/,    // Unvalidated body
    /eval\(/,                            // Dangerous eval
    /innerHTML\s*=/,                     // XSS risk
  ];
  
  return patterns.some(p => p.test(code));
}
```

### Authentication Checks
```javascript
// Check for weak authentication
function checkAuthentication(code) {
  const issues = [];
  
  if (code.includes('password') && !code.includes('hash')) {
    issues.push('Password stored in plaintext');
  }
  
  if (code.includes('token') && !code.includes('verify')) {
    issues.push('Token not verified');
  }
  
  return issues;
}
```

### Dependency Checks
```yaml
check_dependencies:
  - outdated_packages
  - known_vulnerabilities
  - license_compliance
  - deprecated_packages
  
  actions:
    critical_vulnerability:
      - create_issue: immediately
      - create_pr: auto_patch
      - notify: security_team
    
    high_vulnerability:
      - create_issue: within_24h
      - suggest_upgrade
    
    medium_vulnerability:
      - add_to_backlog
      - schedule_update
```

## Automated Fixes

### Auto-Patching
```yaml
auto_patch_when:
  - vulnerability_severity: critical
  - fix_available: true
  - tests_pass: true
  - breaking_changes: false

workflow:
  1. Detect vulnerability
  2. Find patch version
  3. Create branch: security/patch-{cve}
  4. Update dependency
  5. Run tests
  6. Create PR if tests pass
  7. Request immediate review
```

### Secret Removal
```yaml
on_secret_detected:
  1. Identify commit with secret
  2. Create new branch
  3. Remove secret from code
  4. Replace with environment variable
  5. Update documentation
  6. Create PR
  7. Notify user to:
     - Revoke exposed secret
     - Rotate credentials
     - Update environment config
```

## Security Policies

### Password Requirements
```yaml
enforce:
  - minimum_length: 12
  - require_uppercase: true
  - require_lowercase: true
  - require_numbers: true
  - require_special: true
  - no_common_passwords: true
  - hash_algorithm: bcrypt
```

### API Security
```yaml
require:
  - rate_limiting: true
  - authentication: jwt_or_oauth
  - input_validation: all_endpoints
  - output_encoding: all_responses
  - cors_configuration: restrictive
  - https_only: true
```

### Data Protection
```yaml
enforce:
  - encryption_at_rest: sensitive_data
  - encryption_in_transit: all_data
  - data_minimization: true
  - access_control: role_based
  - audit_logging: true
```

## Vulnerability Response

### Critical Vulnerabilities
```yaml
response_time: < 4 hours

actions:
  1. Immediate notification to security team
  2. Create incident ticket
  3. Block affected deployments
  4. Generate patch PR
  5. Fast-track review
  6. Deploy emergency fix
  7. Post-mortem review
```

### High Vulnerabilities
```yaml
response_time: < 24 hours

actions:
  1. Notify maintainers
  2. Create issue with details
  3. Generate fix PR
  4. Schedule review
  5. Include in next release
```

### Medium/Low Vulnerabilities
```yaml
response_time: < 1 week

actions:
  1. Add to backlog
  2. Include in regular updates
  3. Document workarounds
  4. Plan for future patch
```

## Compliance Checks

### OWASP Top 10
```yaml
scan_for:
  - A01_Broken_Access_Control
  - A02_Cryptographic_Failures
  - A03_Injection
  - A04_Insecure_Design
  - A05_Security_Misconfiguration
  - A06_Vulnerable_Components
  - A07_Auth_Failures
  - A08_Data_Integrity_Failures
  - A09_Logging_Failures
  - A10_SSRF
```

### License Compliance
```yaml
check_licenses:
  allowed:
    - MIT
    - Apache-2.0
    - BSD-3-Clause
    - ISC
  
  restricted:
    - GPL-3.0  # Copyleft
    - AGPL-3.0 # Strong copyleft
  
  prohibited:
    - Unknown
    - Proprietary
```

## Security Reporting

### Weekly Security Report
```markdown
# Security Report - Week of {DATE}

## Summary
- Vulnerabilities found: 3
- Vulnerabilities fixed: 2
- Pending fixes: 1
- Security PRs merged: 4

## Critical Issues
None

## High Priority Issues
1. CVE-2024-1234 - Outdated dependency
   - Status: PR #456 created
   - ETA: 24 hours

## Dependencies Updated
- express: 4.17.1 → 4.18.2
- axios: 0.21.1 → 1.3.0

## Recommendations
1. Enable 2FA for all users
2. Review API rate limits
3. Update security documentation
```

### Security Metrics
```yaml
track:
  - mean_time_to_detect: 2.3 hours
  - mean_time_to_patch: 18 hours
  - vulnerabilities_per_week: 1.2
  - false_positive_rate: 5%
  - auto_patch_success_rate: 87%
```

## Integration

### With Dependabot
```yaml
dependabot_integration:
  - auto_approve: security_patches
  - auto_merge: if_tests_pass
  - schedule_review: weekly
  - group_updates: by_severity
```

### With Code Scanning
```yaml
codeql_integration:
  - run_on: [push, pr, schedule]
  - languages: [javascript, python]
  - queries: security-and-quality
  - fail_on: critical
```

### With Secret Scanning
```yaml
secret_scanning:
  - scan_scope: all_commits
  - notification: immediate
  - auto_revoke: github_tokens
  - partner_patterns: enabled
```

## Best Practices

### Secure Coding
```javascript
// GOOD: Parameterized query
const user = await db.query(
  'SELECT * FROM users WHERE id = ?',
  [userId]
);

// BAD: String concatenation
const user = await db.query(
  'SELECT * FROM users WHERE id = ' + userId
);

// GOOD: Input validation
const sanitizedInput = validator.escape(userInput);

// BAD: Direct usage
const result = processInput(req.body.input);

// GOOD: Environment variables
const apiKey = process.env.API_KEY;

// BAD: Hardcoded secrets
const apiKey = '1234567890abcdef';
```

### Security Headers
```javascript
// Set security headers
app.use((req, res, next) => {
  res.setHeader('X-Content-Type-Options', 'nosniff');
  res.setHeader('X-Frame-Options', 'DENY');
  res.setHeader('X-XSS-Protection', '1; mode=block');
  res.setHeader('Strict-Transport-Security', 'max-age=31536000');
  res.setHeader('Content-Security-Policy', "default-src 'self'");
  next();
});
```

## Configuration

### Security Config
```yaml
# .github/config/security.yml
security:
  auto_patch:
    enabled: true
    severity_threshold: high
    require_tests: true
  
  scanning:
    schedule: daily
    include:
      - dependencies
      - secrets
      - code
    
  notifications:
    critical: slack + email
    high: slack
    medium: github_issue
  
  compliance:
    enforce_owasp: true
    check_licenses: true
    require_https: true
```

## Emergency Procedures

### Security Incident Response
```yaml
1. Detection:
   - Automated alert triggers
   - Manual report received

2. Assessment:
   - Determine severity
   - Identify affected systems
   - Estimate impact

3. Containment:
   - Block malicious traffic
   - Isolate affected systems
   - Prevent further damage

4. Eradication:
   - Remove vulnerability
   - Patch systems
   - Deploy fixes

5. Recovery:
   - Restore services
   - Verify security
   - Monitor for recurrence

6. Post-Incident:
   - Document incident
   - Update procedures
   - Improve defenses
```

## Training & Awareness

### Security Checklist for Developers
```markdown
Before committing code:
- [ ] No hardcoded secrets
- [ ] Input validation present
- [ ] Output encoding applied
- [ ] Authentication required
- [ ] Authorization checked
- [ ] Error handling secure
- [ ] Logging implemented
- [ ] Tests include security scenarios
```

### Security Review Checklist
```markdown
During code review:
- [ ] Sensitive data encrypted
- [ ] SQL queries parameterized
- [ ] XSS prevention implemented
- [ ] CSRF protection active
- [ ] Rate limiting configured
- [ ] Security headers set
- [ ] Dependencies up to date
- [ ] No known vulnerabilities
```
