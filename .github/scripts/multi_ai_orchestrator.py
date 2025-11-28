#!/usr/bin/env python3
"""
Multi-AI Integration Orchestrator
Coordinates work between multiple AI providers (Claude, GPT, Copilot, etc.)
for 24/7 continuous project improvement
"""

import os
import json
import hashlib
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional
import time

class MultiAIOrchestrator:
    """
    Orchestrates work distribution across multiple AI providers
    to ensure 24/7 continuous development with no conflicts
    """
    
    def __init__(self, repo_path: Path = None):
        self.repo_path = repo_path or Path.cwd()
        self.config_file = self.repo_path / "config" / "multi-ai-config.json"
        self.state_file = self.repo_path / "logs" / "multi-ai" / "orchestrator-state.json"
        self.task_queue_file = self.repo_path / "docs" / "AI_TASK_QUEUE.md"
        
        # Ensure log directory exists
        self.state_file.parent.mkdir(parents=True, exist_ok=True)
        
        # AI Provider configurations
        self.providers = {
            "claude": {
                "name": "Anthropic Claude",
                "api_key_env": "ANTHROPIC_API_KEY",
                "strengths": ["creative_writing", "scene_development", "lore_consistency"],
                "rate_limit_rpm": 50,  # requests per minute
                "cost_per_1k_tokens": 0.015,
                "priority": 1,  # Higher number = higher priority
                "enabled": True
            },
            "gpt4": {
                "name": "OpenAI GPT-4",
                "api_key_env": "OPENAI_API_KEY",
                "strengths": ["code_optimization", "bug_fixing", "documentation"],
                "rate_limit_rpm": 60,
                "cost_per_1k_tokens": 0.03,
                "priority": 2,
                "enabled": False  # Enable when API key is available
            },
            "copilot": {
                "name": "GitHub Copilot",
                "api_key_env": "GITHUB_TOKEN",
                "strengths": ["code_completion", "refactoring", "test_generation"],
                "rate_limit_rpm": 100,
                "cost_per_1k_tokens": 0.0,  # Included in subscription
                "priority": 3,
                "enabled": True
            },
            "local": {
                "name": "Local Rule-Based",
                "api_key_env": None,
                "strengths": ["syntax_checking", "formatting", "simple_tasks"],
                "rate_limit_rpm": 1000,
                "cost_per_1k_tokens": 0.0,
                "priority": 4,
                "enabled": True
            }
        }
        
        self.load_state()
    
    def load_state(self):
        """Load orchestrator state from disk"""
        if self.state_file.exists():
            with open(self.state_file, 'r') as f:
                self.state = json.load(f)
        else:
            self.state = {
                "last_run": None,
                "active_sessions": {},
                "completed_tasks": [],
                "provider_usage": {p: {"calls": 0, "tokens": 0, "cost": 0.0} for p in self.providers},
                "conflicts_detected": 0,
                "conflicts_resolved": 0
            }
    
    def save_state(self):
        """Save orchestrator state to disk"""
        self.state["last_run"] = datetime.now().isoformat()
        with open(self.state_file, 'w') as f:
            json.dump(self.state, f, indent=2)
    
    def get_available_providers(self) -> List[str]:
        """Get list of currently available AI providers"""
        available = []
        for provider_id, config in self.providers.items():
            if not config["enabled"]:
                continue
            
            # Check if API key is available (if required)
            if config["api_key_env"]:
                if os.environ.get(config["api_key_env"]):
                    available.append(provider_id)
            else:
                available.append(provider_id)
        
        # Sort by priority
        available.sort(key=lambda p: self.providers[p]["priority"])
        return available
    
    def select_provider_for_task(self, task: Dict) -> Optional[str]:
        """
        Intelligently select the best AI provider for a given task
        based on task type, provider strengths, and current load
        """
        task_type = task.get("type", "general")
        available = self.get_available_providers()
        
        if not available:
            print("⚠️ No AI providers available!")
            return None
        
        # Score each provider
        scores = {}
        for provider_id in available:
            config = self.providers[provider_id]
            score = 0
            
            # Base score from priority
            score += config["priority"] * 10
            
            # Bonus for matching strengths
            for strength in config["strengths"]:
                if strength in task_type or task_type in strength:
                    score += 50
            
            # Penalty for high current usage (load balancing)
            usage = self.state["provider_usage"].get(provider_id, {})
            recent_calls = usage.get("calls", 0)
            if recent_calls > 100:
                score -= 20
            
            # Bonus for lower cost
            score += (1.0 / (config["cost_per_1k_tokens"] + 0.001)) * 5
            
            scores[provider_id] = score
        
        # Select provider with highest score
        best_provider = max(scores, key=scores.get)
        return best_provider
    
    def check_for_conflicts(self) -> List[Dict]:
        """
        Detect potential conflicts between active AI sessions
        Returns list of conflicts with resolution suggestions
        """
        conflicts = []
        active = self.state.get("active_sessions", {})
        
        # Check for same-file editing conflicts
        file_locks = {}
        for session_id, session in active.items():
            files = session.get("files_being_edited", [])
            for file_path in files:
                if file_path in file_locks:
                    conflicts.append({
                        "type": "file_conflict",
                        "file": file_path,
                        "sessions": [file_locks[file_path], session_id],
                        "severity": "high",
                        "suggestion": f"Queue {session_id} until {file_locks[file_path]} completes"
                    })
                else:
                    file_locks[file_path] = session_id
        
        # Check for task dependency conflicts
        # (e.g., trying to polish a scene that's still being written)
        for session_id, session in active.items():
            task_type = session.get("task_type", "")
            target = session.get("target", "")
            
            for other_id, other in active.items():
                if session_id == other_id:
                    continue
                
                other_type = other.get("task_type", "")
                other_target = other.get("target", "")
                
                # Polish shouldn't run on actively writing scenes
                if "polish" in task_type and "write" in other_type and target == other_target:
                    conflicts.append({
                        "type": "dependency_conflict",
                        "sessions": [session_id, other_id],
                        "severity": "medium",
                        "suggestion": f"Defer {session_id} until {other_id} completes"
                    })
        
        return conflicts
    
    def resolve_conflicts(self, conflicts: List[Dict]):
        """Attempt to automatically resolve conflicts"""
        for conflict in conflicts:
            if conflict["type"] == "file_conflict":
                # Put lower-priority session on hold
                sessions = conflict["sessions"]
                # Session with higher index is newer, put it on hold
                session_to_pause = sessions[-1]
                print(f"🔒 Pausing session {session_to_pause} due to file conflict")
                # Implementation: mark session as paused
            
            elif conflict["type"] == "dependency_conflict":
                # Implement dependency-based queueing
                print(f"⏸️ Deferring dependent task: {conflict['suggestion']}")
            
            self.state["conflicts_resolved"] += 1
    
    def create_ai_session(self, provider: str, task: Dict) -> str:
        """
        Create a new AI work session with conflict tracking
        Returns session ID
        """
        session_id = hashlib.md5(
            f"{provider}_{task.get('title', 'unknown')}_{datetime.now().isoformat()}".encode()
        ).hexdigest()[:12]
        
        session = {
            "id": session_id,
            "provider": provider,
            "task": task,
            "started_at": datetime.now().isoformat(),
            "status": "active",
            "files_being_edited": task.get("files", []),
            "task_type": task.get("type", "general"),
            "target": task.get("target", ""),
            "estimated_completion": (datetime.now() + timedelta(minutes=30)).isoformat()
        }
        
        self.state["active_sessions"][session_id] = session
        self.save_state()
        
        return session_id
    
    def close_session(self, session_id: str, result: Dict):
        """Mark a session as complete"""
        if session_id in self.state["active_sessions"]:
            session = self.state["active_sessions"].pop(session_id)
            session["completed_at"] = datetime.now().isoformat()
            session["result"] = result
            self.state["completed_tasks"].append(session)
            
            # Update usage stats
            provider = session["provider"]
            if provider in self.state["provider_usage"]:
                self.state["provider_usage"][provider]["calls"] += 1
                self.state["provider_usage"][provider]["tokens"] += result.get("tokens_used", 0)
                
                tokens = result.get("tokens_used", 0)
                cost_per_1k = self.providers[provider]["cost_per_1k_tokens"]
                cost = (tokens / 1000.0) * cost_per_1k
                self.state["provider_usage"][provider]["cost"] += cost
            
            self.save_state()
    
    def generate_handoff_context(self, from_session: str, to_provider: str) -> Dict:
        """
        Generate context for handing off work between AI providers
        Ensures seamless continuation of work
        """
        if from_session not in self.state["active_sessions"]:
            # Check completed tasks
            for task in self.state["completed_tasks"]:
                if task["id"] == from_session:
                    return {
                        "previous_session": from_session,
                        "previous_provider": task["provider"],
                        "work_completed": task["result"],
                        "files_modified": task["files_being_edited"],
                        "next_steps": task.get("next_steps", []),
                        "context": task.get("context", ""),
                        "handoff_type": "continuation"
                    }
        
        session = self.state["active_sessions"].get(from_session, {})
        return {
            "previous_session": from_session,
            "previous_provider": session.get("provider", "unknown"),
            "current_state": session.get("status", "unknown"),
            "files_in_progress": session.get("files_being_edited", []),
            "handoff_type": "takeover"
        }
    
    def get_next_task_with_provider(self) -> Optional[tuple]:
        """
        Get next task from queue and assign best provider
        Returns (task, provider) or None
        """
        # Parse task queue
        if not self.task_queue_file.exists():
            return None
        
        with open(self.task_queue_file, 'r') as f:
            content = f.read()
        
        # Find first uncompleted task
        for line in content.split('\n'):
            if '- [ ]' in line:
                # Extract task info
                task = {
                    "title": line.split('- [ ]')[1].strip() if '- [ ]' in line else "Unknown task",
                    "type": self._infer_task_type(line),
                    "priority": self._infer_priority(content, line),
                    "raw_line": line
                }
                
                # Select provider
                provider = self.select_provider_for_task(task)
                if provider:
                    return (task, provider)
        
        return None
    
    def _infer_task_type(self, task_line: str) -> str:
        """Infer task type from description"""
        line_lower = task_line.lower()
        if any(word in line_lower for word in ["write", "scene", "content"]):
            return "scene_development"
        elif any(word in line_lower for word in ["polish", "enhance", "improve"]):
            return "content_polish"
        elif any(word in line_lower for word in ["test", "validate", "check"]):
            return "testing"
        elif any(word in line_lower for word in ["stat", "balance"]):
            return "stat_balancing"
        elif any(word in line_lower for word in ["doc", "guide", "readme"]):
            return "documentation"
        else:
            return "general"
    
    def _infer_priority(self, full_content: str, task_line: str) -> int:
        """Infer priority from task queue structure"""
        lines_before = full_content[:full_content.index(task_line)].split('\n')
        
        # Check for priority markers in preceding lines
        for line in reversed(lines_before):
            if "PRIORITY 1" in line or "CRITICAL" in line:
                return 1
            elif "PRIORITY 2" in line or "IMPORTANT" in line:
                return 2
            elif "PRIORITY 3" in line:
                return 3
        
        return 4
    
    def generate_status_report(self) -> Dict:
        """Generate comprehensive status report"""
        available_providers = self.get_available_providers()
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "providers": {
                "available": len(available_providers),
                "enabled": sum(1 for p in self.providers.values() if p["enabled"]),
                "details": [
                    {
                        "id": pid,
                        "name": self.providers[pid]["name"],
                        "available": pid in available_providers,
                        "usage": self.state["provider_usage"].get(pid, {})
                    }
                    for pid in self.providers
                ]
            },
            "sessions": {
                "active": len(self.state.get("active_sessions", {})),
                "completed": len(self.state.get("completed_tasks", [])),
                "details": list(self.state.get("active_sessions", {}).values())
            },
            "conflicts": {
                "detected": self.state.get("conflicts_detected", 0),
                "resolved": self.state.get("conflicts_resolved", 0),
                "current": len(self.check_for_conflicts())
            },
            "cost_tracking": {
                "total_cost": sum(
                    usage.get("cost", 0.0) 
                    for usage in self.state["provider_usage"].values()
                ),
                "by_provider": {
                    pid: usage.get("cost", 0.0)
                    for pid, usage in self.state["provider_usage"].items()
                }
            },
            "health": self._calculate_health_score()
        }
        
        return report
    
    def _calculate_health_score(self) -> Dict:
        """Calculate system health score 0-100"""
        score = 100
        issues = []
        
        # Check if providers are available
        available = len(self.get_available_providers())
        if available == 0:
            score -= 50
            issues.append("No AI providers available")
        elif available == 1:
            score -= 20
            issues.append("Only one provider available (no redundancy)")
        
        # Check for unresolved conflicts
        conflicts = len(self.check_for_conflicts())
        if conflicts > 0:
            score -= 10 * conflicts
            issues.append(f"{conflicts} active conflicts")
        
        # Check session health
        active_sessions = len(self.state.get("active_sessions", {}))
        if active_sessions > 5:
            score -= 15
            issues.append(f"High session count ({active_sessions})")
        
        return {
            "score": max(0, score),
            "status": "healthy" if score >= 80 else "warning" if score >= 50 else "critical",
            "issues": issues
        }
    
    def run_orchestration_cycle(self):
        """Execute one orchestration cycle"""
        print("🤖 Multi-AI Orchestrator Starting...")
        
        # Check for conflicts
        conflicts = self.check_for_conflicts()
        if conflicts:
            print(f"⚠️ Detected {len(conflicts)} conflicts")
            self.state["conflicts_detected"] += len(conflicts)
            self.resolve_conflicts(conflicts)
        
        # Get next task
        result = self.get_next_task_with_provider()
        if not result:
            print("✅ No pending tasks in queue")
            return
        
        task, provider = result
        print(f"📋 Task: {task['title']}")
        print(f"🤖 Assigned to: {self.providers[provider]['name']}")
        
        # Create session
        session_id = self.create_ai_session(provider, task)
        print(f"🆔 Session: {session_id}")
        
        # Generate status report
        report = self.generate_status_report()
        print(f"💚 Health Score: {report['health']['score']}/100")
        
        # Save report
        report_file = self.repo_path / "logs" / "multi-ai" / f"report-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
        report_file.parent.mkdir(parents=True, exist_ok=True)
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"📊 Report saved: {report_file}")
        
        self.save_state()
        print("✅ Orchestration cycle complete")

def main():
    """Main entry point"""
    orchestrator = MultiAIOrchestrator()
    orchestrator.run_orchestration_cycle()

if __name__ == "__main__":
    main()
