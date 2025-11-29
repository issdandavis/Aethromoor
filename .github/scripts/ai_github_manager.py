#!/usr/bin/env python3
"""
AI GitHub Manager Bot
Handles all GitHub notifications using configured AI services
"""

import os
import json
import requests
from datetime import datetime, timedelta
from typing import Dict, List, Optional

class AIGitHubManager:
    """Main bot that manages GitHub inbox using AI services"""
    
    def __init__(self, config_path: str = "config/ai-services-config.json"):
        """Initialize the AI GitHub Manager"""
        with open(config_path, 'r') as f:
            self.config = json.load(f)
        
        self.github_token = os.getenv('GITHUB_TOKEN')
        self.anthropic_key = os.getenv('ANTHROPIC_API_KEY')
        self.openai_key = os.getenv('OPENAI_API_KEY')
        
        # Determine active AI service
        self.primary_ai = self._get_primary_ai()
        self.mode = self._get_automation_mode()
        
    def _get_primary_ai(self) -> str:
        """Determine which AI service to use"""
        ai_services = self.config['ai_services']
        
        if ai_services['anthropic_claude']['enabled'] and self.anthropic_key:
            return 'claude'
        elif ai_services['openai_chatgpt']['enabled'] and self.openai_key:
            return 'openai'
        elif ai_services['github_copilot']['enabled']:
            return 'copilot'
        else:
            return 'none'
    
    def _get_automation_mode(self) -> str:
        """Get the active automation mode"""
        modes = self.config['automation_modes']
        
        if modes['full_autopilot']['enabled']:
            return 'full_autopilot'
        elif modes['assisted_mode']['enabled']:
            return 'assisted'
        elif modes['monitoring_only']['enabled']:
            return 'monitoring'
        else:
            return 'assisted'  # Default
    
    def process_notification(self, notification: Dict) -> Dict:
        """Process a single GitHub notification using AI"""
        
        notification_type = notification.get('subject', {}).get('type', 'unknown')
        title = notification.get('subject', {}).get('title', '')
        url = notification.get('subject', {}).get('url', '')
        
        # Categorize using AI
        category = self._categorize_with_ai(title, notification_type)
        
        # Determine priority
        priority = self._assess_priority(title, category)
        
        # Generate response if auto-reply is enabled
        response = None
        if self._should_auto_reply(notification_type):
            response = self._generate_ai_response(title, category, notification_type)
        
        return {
            'category': category,
            'priority': priority,
            'response': response,
            'labels': self._suggest_labels(category, priority),
            'action': self._determine_action(priority, category)
        }
    
    def _categorize_with_ai(self, title: str, type: str) -> str:
        """Use AI to categorize the notification"""
        
        if self.primary_ai == 'claude':
            return self._categorize_with_claude(title, type)
        elif self.primary_ai == 'openai':
            return self._categorize_with_openai(title, type)
        else:
            return self._categorize_with_rules(title, type)
    
    def _categorize_with_claude(self, title: str, type: str) -> str:
        """Categorize using Claude AI"""
        
        prompt = f"""Categorize this GitHub {type}:
        Title: {title}
        
        Choose ONE category: bug, feature, question, documentation, security, discussion
        Respond with just the category name, nothing else."""
        
        try:
            response = requests.post(
                'https://api.anthropic.com/v1/messages',
                headers={
                    'x-api-key': self.anthropic_key,
                    'anthropic-version': '2023-06-01',
                    'content-type': 'application/json'
                },
                json={
                    'model': 'claude-3-5-sonnet-20241022',
                    'max_tokens': 10,
                    'messages': [{'role': 'user', 'content': prompt}]
                }
            )
            
            if response.status_code == 200:
                category = response.json()['content'][0]['text'].strip().lower()
                return category if category in ['bug', 'feature', 'question', 'documentation', 'security', 'discussion'] else 'question'
            
        except Exception as e:
            print(f"Claude API error: {e}")
        
        return self._categorize_with_rules(title, type)
    
    def _categorize_with_openai(self, title: str, type: str) -> str:
        """Categorize using OpenAI"""
        
        prompt = f"""Categorize this GitHub {type}:
        Title: {title}
        
        Choose ONE: bug, feature, question, documentation, security, discussion
        Respond with just the category."""
        
        try:
            response = requests.post(
                'https://api.openai.com/v1/chat/completions',
                headers={
                    'Authorization': f'Bearer {self.openai_key}',
                    'Content-Type': 'application/json'
                },
                json={
                    'model': 'gpt-4-turbo-preview',
                    'messages': [{'role': 'user', 'content': prompt}],
                    'max_tokens': 10,
                    'temperature': 0.3
                }
            )
            
            if response.status_code == 200:
                category = response.json()['choices'][0]['message']['content'].strip().lower()
                return category if category in ['bug', 'feature', 'question', 'documentation', 'security', 'discussion'] else 'question'
                
        except Exception as e:
            print(f"OpenAI API error: {e}")
        
        return self._categorize_with_rules(title, type)
    
    def _categorize_with_rules(self, title: str, type: str) -> str:
        """Fallback rule-based categorization"""
        
        title_lower = title.lower()
        
        # Security keywords
        if any(word in title_lower for word in ['security', 'vulnerability', 'cve', 'exploit', 'xss', 'sql injection']):
            return 'security'
        
        # Bug keywords
        if any(word in title_lower for word in ['bug', 'error', 'crash', 'broken', 'not working', 'fails', 'issue']):
            return 'bug'
        
        # Feature keywords
        if any(word in title_lower for word in ['feature', 'enhancement', 'add', 'implement', 'support for']):
            return 'feature'
        
        # Documentation keywords
        if any(word in title_lower for word in ['docs', 'documentation', 'readme', 'guide', 'tutorial']):
            return 'documentation'
        
        # Question keywords
        if any(word in title_lower for word in ['how to', 'how do i', 'question', 'help', '?']):
            return 'question'
        
        return 'discussion'
    
    def _assess_priority(self, title: str, category: str) -> str:
        """Assess priority level"""
        
        title_lower = title.lower()
        
        # Critical keywords
        if any(word in title_lower for word in ['critical', 'urgent', 'emergency', 'security', 'production', 'down']):
            return 'critical'
        
        # High priority
        if category == 'security' or any(word in title_lower for word in ['high priority', 'important', 'breaking']):
            return 'high'
        
        # Low priority
        if category in ['documentation', 'question'] or any(word in title_lower for word in ['minor', 'typo', 'cosmetic']):
            return 'low'
        
        return 'medium'
    
    def _generate_ai_response(self, title: str, category: str, type: str) -> str:
        """Generate AI response based on configuration"""
        
        template_config = self.config['ai_response_templates'].get(f"new_{type.lower()}", 
                                                                    self.config['ai_response_templates']['new_issue'])
        
        if self.primary_ai == 'claude':
            return self._generate_response_with_claude(title, category, template_config)
        elif self.primary_ai == 'openai':
            return self._generate_response_with_openai(title, category, template_config)
        else:
            return self._generate_template_response(category, template_config)
    
    def _generate_response_with_claude(self, title: str, category: str, template: Dict) -> str:
        """Generate response using Claude"""
        
        prompt = f"""Generate a professional GitHub auto-reply for this {category}:
        Title: {title}
        
        Guidelines:
        - Tone: {template.get('tone', 'helpful_and_professional')}
        - Acknowledge receipt: {template.get('acknowledge_receipt', True)}
        - Response time: {template.get('estimated_response_time', '24-48 hours')}
        - Be concise (2-3 sentences max)
        - Be warm and helpful
        
        Generate the reply:"""
        
        try:
            response = requests.post(
                'https://api.anthropic.com/v1/messages',
                headers={
                    'x-api-key': self.anthropic_key,
                    'anthropic-version': '2023-06-01',
                    'content-type': 'application/json'
                },
                json={
                    'model': 'claude-3-5-sonnet-20241022',
                    'max_tokens': 200,
                    'messages': [{'role': 'user', 'content': prompt}]
                }
            )
            
            if response.status_code == 200:
                return response.json()['content'][0]['text'].strip()
                
        except Exception as e:
            print(f"Claude response generation error: {e}")
        
        return self._generate_template_response(category, template)
    
    def _generate_response_with_openai(self, title: str, category: str, template: Dict) -> str:
        """Generate response using OpenAI"""
        
        prompt = f"""Write a professional GitHub auto-reply for this {category}:
        Title: {title}
        
        Tone: {template.get('tone', 'helpful_and_professional')}
        Keep it brief (2-3 sentences)
        
        Reply:"""
        
        try:
            response = requests.post(
                'https://api.openai.com/v1/chat/completions',
                headers={
                    'Authorization': f'Bearer {self.openai_key}',
                    'Content-Type': 'application/json'
                },
                json={
                    'model': 'gpt-4-turbo-preview',
                    'messages': [{'role': 'user', 'content': prompt}],
                    'max_tokens': 150,
                    'temperature': 0.7
                }
            )
            
            if response.status_code == 200:
                return response.json()['choices'][0]['message']['content'].strip()
                
        except Exception as e:
            print(f"OpenAI response generation error: {e}")
        
        return self._generate_template_response(category, template)
    
    def _generate_template_response(self, category: str, template: Dict) -> str:
        """Generate template-based response (fallback)"""
        
        responses = {
            'bug': "Thanks for reporting this issue! We'll investigate and get back to you within 24-48 hours. If you have any additional information that might help us reproduce the problem, please feel free to add it.",
            'feature': "Thanks for the feature suggestion! We appreciate you taking the time to share this idea. We'll review it and discuss it with the team. Check back for updates!",
            'question': "Thanks for your question! We'll get back to you with an answer within 24 hours. In the meantime, you might find helpful information in our documentation.",
            'security': "⚠️ Thanks for reporting this security concern. We take security seriously. Our team will review this privately and get back to you ASAP. Please DO NOT share details publicly until we've addressed it.",
            'documentation': "Thanks for helping improve our documentation! We'll review your suggestions and make updates as needed. Clear docs help everyone!",
            'discussion': "Thanks for starting this discussion! We're looking forward to hearing everyone's thoughts on this topic."
        }
        
        return responses.get(category, "Thanks for your contribution! We'll review this and get back to you soon.")
    
    def _suggest_labels(self, category: str, priority: str) -> List[str]:
        """Suggest labels based on category and priority"""
        
        labels = [category]
        
        if priority in ['critical', 'high']:
            labels.append('priority:' + priority)
        
        return labels
    
    def _determine_action(self, priority: str, category: str) -> str:
        """Determine what action to take"""
        
        if priority == 'critical':
            return 'escalate_immediately'
        elif priority == 'high' and category == 'security':
            return 'escalate_security_team'
        elif self.mode == 'full_autopilot':
            return 'auto_handle'
        elif self.mode == 'assisted':
            return 'draft_for_review'
        else:
            return 'notify_only'
    
    def _should_auto_reply(self, notification_type: str) -> bool:
        """Check if auto-reply is enabled for this type"""
        
        routing = self.config['notification_routing']
        type_key = f"github_{notification_type.lower().replace(' ', '_')}s"
        
        return routing.get(type_key, {}).get('auto_reply', True)
    
    def generate_daily_summary(self, notifications: List[Dict]) -> str:
        """Generate daily summary email"""
        
        total = len(notifications)
        auto_handled = sum(1 for n in notifications if n.get('action') == 'auto_handle')
        needs_attention = sum(1 for n in notifications if n.get('action') in ['escalate_immediately', 'escalate_security_team'])
        
        summary = f"""
📊 GitHub Activity Summary - {datetime.now().strftime('%B %d, %Y')}

✅ Auto-Handled ({auto_handled} items)
"""
        
        for notif in [n for n in notifications if n.get('action') == 'auto_handle'][:5]:
            summary += f"  - {notif.get('title', 'Notification')}: {notif.get('category', 'general')}\n"
        
        if needs_attention > 0:
            summary += f"\n⚠️ Needs Your Attention ({needs_attention} items)\n"
            for notif in [n for n in notifications if n.get('action') in ['escalate_immediately', 'escalate_security_team']]:
                summary += f"  - {notif.get('title', 'Urgent')}: {notif.get('reason', 'review needed')}\n"
        
        summary += f"""
📈 Stats
  - {total} new notifications
  - {auto_handled} handled automatically
  - {needs_attention} flagged for you

[View Full Details on GitHub]
"""
        
        return summary


if __name__ == "__main__":
    # Initialize the bot
    manager = AIGitHubManager()
    
    print(f"AI GitHub Manager initialized")
    print(f"Primary AI: {manager.primary_ai}")
    print(f"Mode: {manager.mode}")
    print(f"Ready to process notifications!")
