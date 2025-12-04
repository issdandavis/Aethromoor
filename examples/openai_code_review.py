#!/usr/bin/env python3
"""
OpenAI Code Review Example for Avalon Project

This script demonstrates how to use OpenAI's API to perform automated code reviews
on ChoiceScript files, JavaScript code, and documentation.

Features:
- Reviews ChoiceScript syntax and structure
- Checks code quality and best practices
- Validates lore consistency
- Provides constructive feedback
- Integrates with GitHub PRs

Usage:
    # Review a single file
    python examples/openai_code_review.py --file choicescript_game/scenes/arrival.txt
    
    # Review all files in a PR
    python examples/openai_code_review.py --pr 123
    
    # Review with specific model
    python examples/openai_code_review.py --file game/game.js --model gpt-4
    
Environment Variables:
    OPENAI_API_KEY - Your OpenAI API key
    GITHUB_TOKEN - GitHub personal access token (for PR integration)
"""

import os
import sys
import argparse
import json
from typing import List, Dict, Optional
from pathlib import Path

try:
    from openai import OpenAI
except ImportError:
    print("Error: openai package not installed")
    print("Install with: pip install openai")
    sys.exit(1)


class OpenAICodeReviewer:
    """
    Automated code reviewer using OpenAI's API
    """
    
    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-4"):
        """
        Initialize the code reviewer
        
        Args:
            api_key: OpenAI API key (defaults to OPENAI_API_KEY env var)
            model: Model to use (gpt-4, gpt-3.5-turbo, etc.)
        """
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not set")
        
        self.client = OpenAI(api_key=self.api_key)
        self.model = model
        
    def review_file(self, filepath: str) -> Dict:
        """
        Review a single file
        
        Args:
            filepath: Path to file to review
            
        Returns:
            Dictionary with review results
        """
        # Read file content
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Determine file type
        file_ext = Path(filepath).suffix
        file_type = self._get_file_type(file_ext)
        
        # Generate review prompt
        prompt = self._generate_prompt(filepath, content, file_type)
        
        # Call OpenAI API
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": self._get_system_prompt(file_type)
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.3,  # Lower for more consistent reviews
                max_tokens=2000
            )
            
            review_text = response.choices[0].message.content
            
            # Parse review into structured format
            review_data = self._parse_review(review_text)
            
            return {
                'file': filepath,
                'file_type': file_type,
                'review': review_data,
                'raw_response': review_text,
                'model': self.model,
                'tokens_used': response.usage.total_tokens
            }
            
        except Exception as e:
            return {
                'file': filepath,
                'error': str(e),
                'success': False
            }
    
    def _get_file_type(self, ext: str) -> str:
        """Determine file type from extension"""
        type_map = {
            '.txt': 'choicescript',
            '.js': 'javascript',
            '.html': 'html',
            '.css': 'css',
            '.md': 'markdown',
            '.yml': 'yaml',
            '.yaml': 'yaml'
        }
        return type_map.get(ext, 'unknown')
    
    def _get_system_prompt(self, file_type: str) -> str:
        """Get system prompt based on file type"""
        base_prompt = """You are an expert code reviewer for the Avalon game project.

Project Context:
- ChoiceScript interactive fiction game
- Fantasy setting with established lore (Spiral of Pollyoneth universe)
- 40,000+ word narrative
- 14 unique endings
- Character-driven story with stat tracking

Your role is to provide constructive, specific feedback that helps improve code quality
while respecting the creative narrative."""

        type_specific = {
            'choicescript': """

ChoiceScript Specific Guidelines:
- Check for proper *title at start
- Verify *choice blocks have #options
- Ensure *if/*else blocks are balanced
- Validate *goto and *gosub targets exist
- Check variable naming (use snake_case)
- Verify stats are defined in startup.txt
- Maintain lore consistency (character names, locations, magic terms)

Canonical Characters:
- Izack Thorne (not Isaac)
- Polly / Polymnia Aetheris
- Aria Luminette
- Zara Thornveil
- Magnus

Canonical Locations:
- Avalon Academy
- Singing Dunes
- Verdant Tithe
- Rune Glacier""",

            'javascript': """

JavaScript Specific Guidelines:
- Check for console.log statements (remove before production)
- Verify error handling for async operations
- Check for security issues (no eval(), sanitize inputs)
- Ensure proper variable scoping
- Validate DOM manipulation efficiency""",

            'markdown': """

Documentation Guidelines:
- Check for broken links
- Verify proper heading hierarchy
- Ensure code examples are complete
- Check spelling and grammar
- Validate lore references"""
        }
        
        return base_prompt + type_specific.get(file_type, '')
    
    def _generate_prompt(self, filepath: str, content: str, file_type: str) -> str:
        """Generate review prompt"""
        # Truncate content if too long
        max_content_length = 4000
        if len(content) > max_content_length:
            content = content[:max_content_length] + "\n\n[... content truncated ...]"
        
        prompt = f"""Please review this {file_type} file from the Avalon project.

File: {filepath}

Content:
```
{content}
```

Provide a code review with:
1. Critical Issues (security, broken functionality)
2. Errors (should fix before merge)
3. Warnings (best practices, potential bugs)
4. Suggestions (improvements, optimizations)

For each issue, provide:
- Line number (if applicable)
- Description of the issue
- Why it's a problem
- How to fix it

Format your response as:

## Critical Issues
- Line X: Description

## Errors
- Line Y: Description

## Warnings
- Line Z: Description

## Suggestions
- Description

If no issues in a category, write "None found."
"""
        return prompt
    
    def _parse_review(self, review_text: str) -> Dict:
        """Parse review text into structured format"""
        sections = {
            'critical': [],
            'errors': [],
            'warnings': [],
            'suggestions': []
        }
        
        current_section = None
        
        for line in review_text.split('\n'):
            line = line.strip()
            
            # Detect section headers
            if 'Critical Issues' in line or '## Critical' in line:
                current_section = 'critical'
            elif '## Errors' in line or 'Errors' in line:
                current_section = 'errors'
            elif '## Warnings' in line or 'Warnings' in line:
                current_section = 'warnings'
            elif '## Suggestions' in line or 'Suggestions' in line:
                current_section = 'suggestions'
            elif line.startswith('- ') and current_section:
                sections[current_section].append(line[2:])
        
        return sections
    
    def generate_markdown_report(self, reviews: List[Dict]) -> str:
        """Generate markdown report from multiple reviews"""
        report = ["# AI Code Review Report\n"]
        
        # Summary
        total_files = len(reviews)
        total_critical = sum(len(r.get('review', {}).get('critical', [])) for r in reviews)
        total_errors = sum(len(r.get('review', {}).get('errors', [])) for r in reviews)
        total_warnings = sum(len(r.get('review', {}).get('warnings', [])) for r in reviews)
        
        report.append(f"**Files Reviewed:** {total_files}\n")
        report.append(f"**Model Used:** {reviews[0].get('model', 'unknown')}\n")
        report.append(f"**Critical Issues:** {total_critical}\n")
        report.append(f"**Errors:** {total_errors}\n")
        report.append(f"**Warnings:** {total_warnings}\n\n")
        
        if total_critical + total_errors + total_warnings == 0:
            report.append("✅ No issues found! Code looks great!\n\n")
        
        # Individual file reviews
        for review in reviews:
            if 'error' in review:
                report.append(f"## ❌ {review['file']}\n\n")
                report.append(f"Error: {review['error']}\n\n")
                continue
            
            review_data = review.get('review', {})
            
            # Skip if no issues
            has_issues = any(review_data.get(k) for k in ['critical', 'errors', 'warnings'])
            if not has_issues:
                report.append(f"## ✅ {review['file']}\n\n")
                report.append("No issues found.\n\n")
                continue
            
            report.append(f"## 📄 {review['file']}\n\n")
            
            # Critical issues
            if review_data.get('critical'):
                report.append("### ❌ Critical Issues\n\n")
                for issue in review_data['critical']:
                    report.append(f"- {issue}\n")
                report.append("\n")
            
            # Errors
            if review_data.get('errors'):
                report.append("### ⚠️ Errors\n\n")
                for error in review_data['errors']:
                    report.append(f"- {error}\n")
                report.append("\n")
            
            # Warnings
            if review_data.get('warnings'):
                report.append("### ⚡ Warnings\n\n")
                for warning in review_data['warnings']:
                    report.append(f"- {warning}\n")
                report.append("\n")
            
            # Suggestions
            if review_data.get('suggestions'):
                report.append("### 💡 Suggestions\n\n")
                for suggestion in review_data['suggestions']:
                    report.append(f"- {suggestion}\n")
                report.append("\n")
        
        # Cost estimate
        total_tokens = sum(r.get('tokens_used', 0) for r in reviews)
        report.append(f"\n---\n*Total tokens used: {total_tokens}*\n")
        
        return ''.join(report)


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description='OpenAI Code Review for Avalon')
    parser.add_argument('--file', help='File to review')
    parser.add_argument('--pr', type=int, help='PR number to review')
    parser.add_argument('--model', default='gpt-4', help='OpenAI model to use')
    parser.add_argument('--output', help='Output file for report')
    
    args = parser.parse_args()
    
    # Initialize reviewer
    try:
        reviewer = OpenAICodeReviewer(model=args.model)
    except ValueError as e:
        print(f"Error: {e}")
        print("Set OPENAI_API_KEY environment variable")
        sys.exit(1)
    
    # Collect files to review
    files_to_review = []
    
    if args.file:
        if not os.path.exists(args.file):
            print(f"Error: File not found: {args.file}")
            sys.exit(1)
        files_to_review.append(args.file)
    
    elif args.pr:
        # Would integrate with GitHub API
        print("PR review not yet implemented. Use --file for now.")
        sys.exit(1)
    
    else:
        print("Please specify --file or --pr")
        parser.print_help()
        sys.exit(1)
    
    # Perform reviews
    reviews = []
    
    for filepath in files_to_review:
        print(f"Reviewing {filepath}...")
        review = reviewer.review_file(filepath)
        reviews.append(review)
        
        if 'error' in review:
            print(f"  ❌ Error: {review['error']}")
        else:
            tokens = review.get('tokens_used', 0)
            print(f"  ✓ Complete ({tokens} tokens)")
    
    # Generate report
    report = reviewer.generate_markdown_report(reviews)
    
    if args.output:
        with open(args.output, 'w') as f:
            f.write(report)
        print(f"\nReport saved to {args.output}")
    else:
        print("\n" + report)


if __name__ == '__main__':
    main()
