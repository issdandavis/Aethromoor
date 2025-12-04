#!/usr/bin/env python3
"""
Workflow Performance Analyzer
Analyzes GitHub Actions workflows for optimization opportunities
"""

import yaml
import json
from pathlib import Path
from collections import defaultdict
from typing import Dict, List

class WorkflowAnalyzer:
    """Analyzes workflows for performance issues"""
    
    def __init__(self, repo_path: Path = None):
        self.repo_path = repo_path or Path.cwd()
        self.workflows_dir = self.repo_path / ".github" / "workflows"
        self.issues = []
        self.stats = defaultdict(int)
    
    def analyze_all_workflows(self) -> Dict:
        """Analyze all workflow files"""
        print("🔍 Analyzing GitHub Actions workflows...\n")
        
        results = {
            "total_workflows": 0,
            "total_issues": 0,
            "workflows": {},
            "recommendations": []
        }
        
        for workflow_file in self.workflows_dir.glob("*.yml"):
            if workflow_file.name.startswith('.'):
                continue
            
            print(f"Analyzing {workflow_file.name}...")
            analysis = self.analyze_workflow(workflow_file)
            results["workflows"][workflow_file.name] = analysis
            results["total_workflows"] += 1
            results["total_issues"] += len(analysis["issues"])
        
        # Generate recommendations
        results["recommendations"] = self.generate_recommendations()
        
        return results
    
    def analyze_workflow(self, workflow_path: Path) -> Dict:
        """Analyze a single workflow file"""
        with open(workflow_path, 'r') as f:
            try:
                workflow = yaml.safe_load(f)
            except yaml.YAMLError as e:
                return {"error": f"YAML parse error: {e}", "issues": []}
        
        issues = []
        
        # Check for missing caching
        if not self.uses_caching(workflow):
            issues.append({
                "severity": "medium",
                "type": "no_caching",
                "message": "Workflow doesn't use dependency caching",
                "recommendation": "Add cache action for pip/npm dependencies"
            })
            self.stats["missing_cache"] += 1
        
        # Check for redundant checkouts
        checkout_count = self.count_checkouts(workflow)
        if checkout_count > 3:
            issues.append({
                "severity": "low",
                "type": "excessive_checkouts",
                "message": f"Workflow has {checkout_count} checkout actions",
                "recommendation": "Consider using artifacts to share data between jobs"
            })
            self.stats["excessive_checkouts"] += 1
        
        # Check for missing work detection
        if not self.has_work_detection(workflow):
            issues.append({
                "severity": "medium",
                "type": "no_work_detection",
                "message": "Workflow may run when no work is needed",
                "recommendation": "Add early exit check for pending work"
            })
            self.stats["no_work_detection"] += 1
        
        # Check for missing parallel execution
        if self.can_parallelize(workflow):
            issues.append({
                "severity": "low",
                "type": "sequential_jobs",
                "message": "Some jobs could potentially run in parallel",
                "recommendation": "Review job dependencies and enable parallelization"
            })
            self.stats["can_parallelize"] += 1
        
        # Check for large workflow files
        file_size = workflow_path.stat().st_size
        if file_size > 15000:  # 15KB
            issues.append({
                "severity": "low",
                "type": "large_file",
                "message": f"Large workflow file ({file_size} bytes)",
                "recommendation": "Consider splitting into reusable workflows"
            })
            self.stats["large_files"] += 1
        
        # Check for high frequency schedules
        schedule = workflow.get('on', {}).get('schedule', [])
        if schedule:
            for item in schedule:
                cron = item.get('cron', '')
                if '*/1' in cron or '*/2' in cron:
                    issues.append({
                        "severity": "high",
                        "type": "high_frequency",
                        "message": f"Very frequent schedule: {cron}",
                        "recommendation": "Consider increasing interval or adding work detection"
                    })
                    self.stats["high_frequency"] += 1
        
        return {
            "issues": issues,
            "file_size": file_size,
            "jobs_count": len(workflow.get('jobs', {})),
            "has_schedule": bool(schedule)
        }
    
    def uses_caching(self, workflow: Dict) -> bool:
        """Check if workflow uses caching"""
        jobs = workflow.get('jobs', {})
        for job_name, job_config in jobs.items():
            steps = job_config.get('steps', [])
            for step in steps:
                uses = step.get('uses', '')
                if 'cache@' in uses or 'setup-python-deps' in uses:
                    return True
        return False
    
    def count_checkouts(self, workflow: Dict) -> int:
        """Count number of checkout actions"""
        count = 0
        jobs = workflow.get('jobs', {})
        for job_name, job_config in jobs.items():
            steps = job_config.get('steps', [])
            for step in steps:
                uses = step.get('uses', '')
                if 'checkout@' in uses:
                    count += 1
        return count
    
    def has_work_detection(self, workflow: Dict) -> bool:
        """Check if workflow has early exit work detection"""
        jobs = workflow.get('jobs', {})
        for job_name, job_config in jobs.items():
            steps = job_config.get('steps', [])
            for step in steps:
                name = step.get('name', '').lower()
                if 'check' in name and 'work' in name:
                    return True
                if 'pending' in name or 'detect' in name:
                    return True
        return False
    
    def can_parallelize(self, workflow: Dict) -> bool:
        """Check if jobs could potentially run in parallel"""
        jobs = workflow.get('jobs', {})
        if len(jobs) <= 1:
            return False
        
        # Check if jobs have explicit dependencies
        jobs_with_deps = 0
        for job_name, job_config in jobs.items():
            if 'needs' in job_config:
                jobs_with_deps += 1
        
        # If we have multiple jobs but few dependencies, parallelization is possible
        return len(jobs) > 2 and jobs_with_deps < len(jobs) - 1
    
    def generate_recommendations(self) -> List[str]:
        """Generate overall recommendations"""
        recommendations = []
        
        if self.stats["missing_cache"] > 0:
            recommendations.append(
                f"🎯 HIGH PRIORITY: {self.stats['missing_cache']} workflows missing dependency caching. "
                "Add .github/actions/setup-python-deps to reduce runtime by 40-60%"
            )
        
        if self.stats["no_work_detection"] > 0:
            recommendations.append(
                f"⚡ MEDIUM PRIORITY: {self.stats['no_work_detection']} workflows lack work detection. "
                "Add early exit checks to reduce wasted runs by 30%"
            )
        
        if self.stats["high_frequency"] > 0:
            recommendations.append(
                f"⚠️ HIGH PRIORITY: {self.stats['high_frequency']} workflows run very frequently. "
                "Consider intelligent scheduling or work detection to reduce API usage"
            )
        
        if self.stats["large_files"] > 0:
            recommendations.append(
                f"📦 LOW PRIORITY: {self.stats['large_files']} large workflow files. "
                "Consider modularization with reusable workflows for better maintainability"
            )
        
        if self.stats["can_parallelize"] > 0:
            recommendations.append(
                f"🚀 MEDIUM PRIORITY: {self.stats['can_parallelize']} workflows could benefit from parallelization. "
                "Review job dependencies to enable concurrent execution"
            )
        
        return recommendations
    
    def print_summary(self, results: Dict):
        """Print analysis summary"""
        print("\n" + "="*80)
        print("📊 WORKFLOW ANALYSIS SUMMARY")
        print("="*80)
        print(f"\nTotal Workflows Analyzed: {results['total_workflows']}")
        print(f"Total Issues Found: {results['total_issues']}")
        print(f"\nIssue Breakdown:")
        print(f"  - Missing Caching: {self.stats['missing_cache']}")
        print(f"  - No Work Detection: {self.stats['no_work_detection']}")
        print(f"  - High Frequency: {self.stats['high_frequency']}")
        print(f"  - Can Parallelize: {self.stats['can_parallelize']}")
        print(f"  - Large Files: {self.stats['large_files']}")
        print(f"  - Excessive Checkouts: {self.stats['excessive_checkouts']}")
        
        print("\n" + "="*80)
        print("🎯 RECOMMENDATIONS")
        print("="*80)
        for i, rec in enumerate(results['recommendations'], 1):
            print(f"\n{i}. {rec}")
        
        print("\n" + "="*80)
    
    def save_report(self, results: Dict, output_path: Path):
        """Save analysis report as JSON"""
        with open(output_path, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"\n✅ Full report saved to: {output_path}")

def main():
    """Main entry point"""
    analyzer = WorkflowAnalyzer()
    results = analyzer.analyze_all_workflows()
    analyzer.print_summary(results)
    
    # Save report
    report_path = analyzer.repo_path / "logs" / "workflow-analysis.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    analyzer.save_report(results, report_path)

if __name__ == "__main__":
    main()
