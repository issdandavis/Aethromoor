---
name: deployment-agent
description: Manages automated deployments to staging and production environments
triggers:
  - push
  - release
  - workflow_dispatch
  - pull_request.closed
permissions:
  contents: write
  deployments: write
  actions: write
  environments: write
capabilities:
  - deployment_execution
  - environment_management
  - rollback_handling
  - health_monitoring
  - deployment_notifications
---

# Deployment Agent

## Purpose
Automates the deployment pipeline:
- Build and test code
- Deploy to staging/production
- Monitor deployments
- Handle rollbacks
- Manage environments

## Deployment Workflows

### Staging Deployment
```yaml
trigger:
  - push_to: develop
  - manual: /ai-deploy staging

workflow:
  1. Run linting
  2. Run tests
  3. Build application
  4. Deploy to staging
  5. Run smoke tests
  6. Notify team
```

### Production Deployment
```yaml
trigger:
  - release_published
  - manual: /ai-deploy production --confirm

workflow:
  1. Verify staging deployment
  2. Run full test suite
  3. Create deployment
  4. Build production assets
  5. Deploy with blue-green
  6. Run health checks
  7. Switch traffic
  8. Monitor metrics
  9. Notify stakeholders
```

## Deployment Strategies

### Blue-Green Deployment
```yaml
strategy: blue_green

steps:
  1. Deploy to "green" environment
  2. Run health checks on green
  3. Route 10% traffic to green
  4. Monitor metrics for 5 minutes
  5. If healthy, route 50% traffic
  6. Monitor for 10 minutes
  7. If healthy, route 100% traffic
  8. Keep "blue" running for 1 hour
  9. Decommission old version
```

### Canary Deployment
```yaml
strategy: canary

steps:
  1. Deploy new version to subset
  2. Route 5% traffic to canary
  3. Monitor error rates
  4. If error_rate < threshold:
     - Increase to 25%
  5. If error_rate < threshold:
     - Increase to 50%
  6. If error_rate < threshold:
     - Increase to 100%
  7. If error_rate > threshold:
     - Rollback immediately
```

### Rolling Deployment
```yaml
strategy: rolling

steps:
  1. Update 1 server at a time
  2. Wait for health check
  3. Move to next server
  4. Continue until all updated
  5. Monitor throughout process
```

## Environment Management

### Environment Configuration
```yaml
environments:
  staging:
    url: https://staging.avalon.issdandavis.dev
    protection_rules: []
    secrets:
      - API_KEY
      - DATABASE_URL
    deployment_branch: develop
    
  production:
    url: https://avalon.issdandavis.dev
    protection_rules:
      - required_reviewers: 1
      - wait_timer: 5  # minutes
      - allowed_branches: [main]
    secrets:
      - API_KEY
      - DATABASE_URL
      - ANALYTICS_KEY
    deployment_branch: main
```

### Secrets Management
```yaml
secret_rotation:
  schedule: every_90_days
  
  workflow:
    1. Generate new secret
    2. Update in vault
    3. Deploy to staging
    4. Test with new secret
    5. Deploy to production
    6. Revoke old secret after 24h
```

## Pre-Deployment Checks

### Automated Checks
```yaml
pre_deployment:
  - all_tests_pass: required
  - code_coverage: >= 80%
  - no_security_vulnerabilities: required
  - build_successful: required
  - staging_healthy: required_for_prod
  - documentation_updated: recommended
```

### Manual Approvals
```yaml
production_deployment:
  require_approval:
    - role: maintainer
    - count: 1
  
  approval_timeout: 24_hours
  
  on_timeout: cancel_deployment
```

## Deployment Process

### Build Phase
```yaml
build:
  1. Checkout code
  2. Install dependencies
  3. Run linters
  4. Run tests
  5. Build artifacts
  6. Generate documentation
  7. Create deployment package
```

### Deploy Phase
```yaml
deploy:
  1. Validate package
  2. Create deployment record
  3. Upload artifacts
  4. Update infrastructure
  5. Deploy application
  6. Update routing
  7. Verify deployment
```

### Verification Phase
```yaml
verify:
  1. Health check endpoints
  2. Smoke tests
  3. Integration tests
  4. Performance tests
  5. Security scans
  6. Monitor error rates
  7. Check resource usage
```

## Health Checks

### Endpoint Monitoring
```yaml
health_checks:
  - endpoint: /health
    interval: 30s
    timeout: 5s
    healthy_threshold: 2
    unhealthy_threshold: 3
  
  - endpoint: /api/status
    interval: 1m
    expect_response: 200
  
  - endpoint: /metrics
    interval: 1m
    check_metrics:
      - response_time < 500ms
      - error_rate < 1%
```

### Application Metrics
```yaml
monitor:
  - cpu_usage < 70%
  - memory_usage < 80%
  - disk_usage < 85%
  - response_time < 1000ms
  - error_rate < 0.5%
  - active_connections < 1000
```

## Rollback Procedures

### Automatic Rollback
```yaml
rollback_triggers:
  - health_check_failed: 3_consecutive
  - error_rate > 5%
  - response_time > 3000ms
  - critical_bug_detected
  
rollback_workflow:
  1. Detect failure
  2. Alert team
  3. Stop new deployments
  4. Revert to previous version
  5. Verify rollback
  6. Update status
  7. Investigate issue
```

### Manual Rollback
```yaml
command: /ai-rollback <deployment-id>

workflow:
  1. Confirm rollback
  2. Identify previous good version
  3. Create rollback deployment
  4. Switch traffic
  5. Verify health
  6. Document reason
```

## Deployment Notifications

### Slack Notifications
```yaml
notify_slack:
  on_start:
    channel: "#deployments"
    message: "🚀 Deployment to {env} started"
  
  on_success:
    channel: "#deployments"
    message: "✅ Deployment to {env} succeeded"
  
  on_failure:
    channel: "#deployments"
    message: "❌ Deployment to {env} failed"
    mention: "@team"
```

### GitHub Status
```yaml
update_status:
  - create_deployment
  - update_deployment_status
  - add_comment_to_pr
  - update_release_notes
```

## Deployment Commands

### Manual Deployment
```markdown
/ai-deploy staging
  → Deploy current branch to staging

/ai-deploy production --confirm
  → Deploy to production (requires confirmation)

/ai-deploy staging --branch feature/new-ui
  → Deploy specific branch to staging
```

### Deployment Control
```markdown
/ai-rollback production
  → Rollback production to previous version

/ai-deploy status
  → Show current deployment status

/ai-deploy history
  → Show deployment history
```

## Deployment Logs

### Logging
```yaml
log_events:
  - deployment_started
  - build_completed
  - tests_passed
  - artifacts_uploaded
  - deployment_completed
  - health_checks_passed
  - traffic_switched
  - deployment_verified
```

### Audit Trail
```yaml
record:
  - who: deployer_name
  - what: deployed_version
  - when: timestamp
  - where: environment
  - why: reason/trigger
  - how: deployment_method
  - result: success/failure
```

## Performance Optimization

### Build Optimization
```yaml
optimize:
  - cache_dependencies: true
  - parallel_tests: true
  - incremental_builds: true
  - artifact_compression: true
```

### Deployment Speed
```yaml
improve:
  - use_cdn: for_static_assets
  - preload_containers: true
  - parallel_deployment: when_safe
  - skip_unchanged: true
```

## Disaster Recovery

### Backup Strategy
```yaml
backups:
  database:
    frequency: hourly
    retention: 30_days
  
  application:
    frequency: per_deployment
    retention: 10_versions
  
  configuration:
    frequency: on_change
    retention: all_versions
```

### Recovery Procedures
```yaml
disaster_recovery:
  1. Assess damage
  2. Activate DR plan
  3. Failover to backup
  4. Restore from backup
  5. Verify functionality
  6. Communicate status
  7. Post-mortem analysis
```

## Compliance & Security

### Deployment Security
```yaml
security:
  - sign_artifacts: required
  - verify_signatures: required
  - scan_for_vulnerabilities: required
  - audit_all_deployments: required
  - encrypt_secrets: required
```

### Compliance Checks
```yaml
compliance:
  - change_approval: production_only
  - deployment_window: business_hours
  - blackout_periods: respect
  - documentation: required
  - notification: all_stakeholders
```

## Metrics & Analytics

### Deployment Metrics
```yaml
track:
  - deployment_frequency
  - lead_time_for_changes
  - mean_time_to_recovery
  - change_failure_rate
  - deployment_success_rate
  - average_deployment_time
```

### DORA Metrics
```yaml
dora_metrics:
  deployment_frequency:
    target: multiple_per_day
    current: 5_per_day
  
  lead_time:
    target: < 1_hour
    current: 45_minutes
  
  mttr:
    target: < 1_hour
    current: 30_minutes
  
  change_failure_rate:
    target: < 15%
    current: 8%
```

## Configuration

### Deployment Config
```yaml
# .github/config/deployment.yml
deployment:
  strategy: blue_green
  
  environments:
    - staging
    - production
  
  automation:
    staging: full
    production: requires_approval
  
  notifications:
    - slack
    - github
    - email
  
  rollback:
    automatic: true
    threshold:
      error_rate: 5%
      response_time: 3000ms
```

## Best Practices

### Pre-Deployment
```markdown
- [ ] All tests passing
- [ ] Code reviewed and approved
- [ ] Documentation updated
- [ ] Changelog updated
- [ ] Staging deployment successful
- [ ] Team notified
- [ ] Backup created
```

### During Deployment
```markdown
- [ ] Monitor metrics continuously
- [ ] Watch error rates
- [ ] Check health endpoints
- [ ] Verify functionality
- [ ] Communicate progress
```

### Post-Deployment
```markdown
- [ ] Verify all services healthy
- [ ] Check logs for errors
- [ ] Monitor for 1 hour
- [ ] Update status page
- [ ] Document any issues
- [ ] Send completion notice
```

## Troubleshooting

### Common Issues

**Deployment Failed**
```yaml
check:
  - build_logs
  - test_results
  - environment_variables
  - network_connectivity
  - resource_availability
```

**Health Checks Failing**
```yaml
check:
  - application_logs
  - database_connectivity
  - external_service_status
  - configuration_correctness
```

**Slow Deployment**
```yaml
check:
  - build_cache_hit_rate
  - network_bandwidth
  - resource_allocation
  - parallel_execution
```
