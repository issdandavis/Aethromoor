#!/usr/bin/env python3
"""
Custom Agent Example for Avalon Project

This script demonstrates how to create a custom GitHub agent that:
- Reviews ChoiceScript files
- Checks lore consistency
- Validates game logic
- Provides automated feedback

Usage:
    python examples/custom_agent.py --file choicescript_game/scenes/arrival.txt
    python examples/custom_agent.py --pr 123
    python examples/custom_agent.py --all-scenes
"""

import os
import re
import sys
import argparse
from typing import List, Dict, Tuple
from pathlib import Path

# Configuration
CANONICAL_CHARACTERS = {
    "Izack Thorne": ["Izack", "Izack Thorne", "Professor Thorne"],
    "Polly": ["Polly", "Polymnia", "Polymnia Aetheris"],
    "Aria Luminette": ["Aria", "Aria Luminette", "Professor Luminette"],
    "Zara Thornveil": ["Zara", "Zara Thornveil", "Professor Thornveil"],
    "Magnus": ["Magnus", "Professor Magnus"]
}

CANONICAL_LOCATIONS = [
    "Avalon Academy",
    "Singing Dunes",
    "Verdant Tithe",
    "Rune Glacier",
    "Aethermoor"
]

MAGIC_TERMS = [
    "collaborative casting",
    "dimensional theory",
    "First Tongue",
    "Spiral of Pollyoneth",
    "wingscroll"
]


class ChoiceScriptValidator:
    """Validates ChoiceScript scene files"""
    
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.errors = []
        self.warnings = []
        self.suggestions = []
        
    def validate(self) -> Dict:
        """Run all validation checks"""
        with open(self.filepath, 'r', encoding='utf-8') as f:
            self.content = f.read()
            self.lines = self.content.split('\n')
        
        self.check_title()
        self.check_syntax()
        self.check_choices()
        self.check_variables()
        self.check_lore()
        
        return {
            'file': self.filepath,
            'errors': self.errors,
            'warnings': self.warnings,
            'suggestions': self.suggestions
        }
    
    def check_title(self):
        """Verify scene starts with *title"""
        if not self.content.strip().startswith('*title'):
            self.errors.append({
                'line': 1,
                'message': 'Scene must start with *title command',
                'severity': 'error'
            })
    
    def check_syntax(self):
        """Check for common syntax errors"""
        for i, line in enumerate(self.lines, 1):
            # Check for space before command
            if re.match(r'^\s*\*\s+\w+', line):
                self.warnings.append({
                    'line': i,
                    'message': f'Extra space after * in command: "{line.strip()}"',
                    'severity': 'warning'
                })
            
            # Check for unbalanced parentheses in conditions
            if '*if' in line:
                open_parens = line.count('(')
                close_parens = line.count(')')
                if open_parens != close_parens:
                    self.errors.append({
                        'line': i,
                        'message': 'Unbalanced parentheses in *if condition',
                        'severity': 'error'
                    })
    
    def check_choices(self):
        """Validate choice blocks"""
        i = 0
        while i < len(self.lines):
            line = self.lines[i].strip()
            
            if line.startswith('*choice'):
                # Check if next non-empty line is an option
                j = i + 1
                found_option = False
                
                while j < len(self.lines) and not found_option:
                    next_line = self.lines[j].strip()
                    if next_line:
                        if next_line.startswith('#'):
                            found_option = True
                        else:
                            break
                    j += 1
                
                if not found_option:
                    self.errors.append({
                        'line': i + 1,
                        'message': '*choice block must have at least one #option',
                        'severity': 'error'
                    })
            
            i += 1
    
    def check_variables(self):
        """Check for common variable issues"""
        # Find all variable references
        var_pattern = r'\*\s*set\s+(\w+)|{(\w+)}'
        variables_used = set()
        
        for i, line in enumerate(self.lines, 1):
            matches = re.findall(var_pattern, line)
            for match in matches:
                var_name = match[0] or match[1]
                if var_name:
                    variables_used.add(var_name)
        
        # Check for common typos
        typos = {
            'colaboration': 'collaboration',
            'refrence': 'reference',
            'postion': 'position'
        }
        
        for wrong, correct in typos.items():
            if wrong in variables_used:
                self.warnings.append({
                    'line': 0,
                    'message': f'Possible typo: "{wrong}" should be "{correct}"',
                    'severity': 'warning'
                })
    
    def check_lore(self):
        """Validate lore consistency"""
        # Check character names
        for i, line in enumerate(self.lines, 1):
            # Common misspellings
            if 'Isaac' in line and 'Izack' not in line:
                self.warnings.append({
                    'line': i,
                    'message': 'Possible misspelling: "Isaac" should be "Izack"',
                    'severity': 'warning'
                })
        
        # Suggest using canonical terms
        content_lower = self.content.lower()
        if 'magic' in content_lower and 'collaborative casting' not in content_lower:
            self.suggestions.append({
                'line': 0,
                'message': 'Consider using canonical term "collaborative casting"',
                'severity': 'info'
            })


class LoreConsistencyChecker:
    """Checks narrative consistency across files"""
    
    def __init__(self, lore_dir: str = 'lore'):
        self.lore_dir = lore_dir
        self.lore_index = self._build_lore_index()
    
    def _build_lore_index(self) -> Dict:
        """Build index of canonical lore"""
        index = {
            'characters': CANONICAL_CHARACTERS,
            'locations': CANONICAL_LOCATIONS,
            'magic_terms': MAGIC_TERMS
        }
        return index
    
    def check_file(self, filepath: str) -> List[Dict]:
        """Check a file for lore consistency"""
        issues = []
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')
        
        # Check character mentions
        for canonical, variants in self.lore_index['characters'].items():
            # Find mentions that don't match any variant
            pattern = r'\b(I[sz]a+[ck]+)\b'  # Common Isaac/Izack variations
            for i, line in enumerate(lines, 1):
                matches = re.findall(pattern, line)
                for match in matches:
                    if match not in ['Izack', 'Isaac']:
                        continue
                    if match == 'Isaac' and 'Izack' not in variants:
                        issues.append({
                            'file': filepath,
                            'line': i,
                            'message': f'Use "Izack" instead of "Isaac"',
                            'severity': 'warning'
                        })
        
        return issues


class AgentReport:
    """Generate formatted report for agent findings"""
    
    def __init__(self):
        self.results = []
    
    def add_result(self, result: Dict):
        """Add validation result"""
        self.results.append(result)
    
    def generate_markdown(self) -> str:
        """Generate markdown report"""
        report = ["# Custom Agent Report\n"]
        
        total_errors = sum(len(r['errors']) for r in self.results)
        total_warnings = sum(len(r['warnings']) for r in self.results)
        total_suggestions = sum(len(r['suggestions']) for r in self.results)
        
        report.append(f"**Files Checked:** {len(self.results)}\n")
        report.append(f"**Errors:** {total_errors}\n")
        report.append(f"**Warnings:** {total_warnings}\n")
        report.append(f"**Suggestions:** {total_suggestions}\n\n")
        
        if total_errors + total_warnings + total_suggestions == 0:
            report.append("✅ No issues found! Great work!\n")
            return ''.join(report)
        
        for result in self.results:
            if not (result['errors'] or result['warnings'] or result['suggestions']):
                continue
            
            report.append(f"## File: `{result['file']}`\n\n")
            
            if result['errors']:
                report.append("### ❌ Errors\n\n")
                for error in result['errors']:
                    line_info = f"Line {error['line']}: " if error['line'] else ""
                    report.append(f"- {line_info}{error['message']}\n")
                report.append("\n")
            
            if result['warnings']:
                report.append("### ⚠️ Warnings\n\n")
                for warning in result['warnings']:
                    line_info = f"Line {warning['line']}: " if warning['line'] else ""
                    report.append(f"- {line_info}{warning['message']}\n")
                report.append("\n")
            
            if result['suggestions']:
                report.append("### 💡 Suggestions\n\n")
                for suggestion in result['suggestions']:
                    line_info = f"Line {suggestion['line']}: " if suggestion['line'] else ""
                    report.append(f"- {line_info}{suggestion['message']}\n")
                report.append("\n")
        
        return ''.join(report)
    
    def print_summary(self):
        """Print summary to console"""
        print("\n" + "="*50)
        print("CUSTOM AGENT SUMMARY")
        print("="*50)
        
        for result in self.results:
            status = "✅" if not (result['errors'] or result['warnings']) else "❌"
            print(f"{status} {result['file']}")
            
            if result['errors']:
                print(f"   Errors: {len(result['errors'])}")
            if result['warnings']:
                print(f"   Warnings: {len(result['warnings'])}")
            if result['suggestions']:
                print(f"   Suggestions: {len(result['suggestions'])}")
        
        print("="*50 + "\n")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description='Custom Agent for Avalon Project')
    parser.add_argument('--file', help='Check specific file')
    parser.add_argument('--pr', type=int, help='Check files in PR number')
    parser.add_argument('--all-scenes', action='store_true', help='Check all scene files')
    parser.add_argument('--output', help='Output file for report')
    
    args = parser.parse_args()
    
    files_to_check = []
    
    if args.file:
        files_to_check.append(args.file)
    elif args.all_scenes:
        scenes_dir = Path('choicescript_game/scenes')
        files_to_check = list(scenes_dir.glob('*.txt'))
    elif args.pr:
        # Would integrate with GitHub API to get PR files
        print(f"PR checking not yet implemented. Use --file or --all-scenes")
        sys.exit(1)
    else:
        print("Please specify --file, --pr, or --all-scenes")
        parser.print_help()
        sys.exit(1)
    
    # Run validation
    report = AgentReport()
    
    for filepath in files_to_check:
        print(f"Checking {filepath}...")
        validator = ChoiceScriptValidator(str(filepath))
        result = validator.validate()
        report.add_result(result)
    
    # Generate report
    markdown_report = report.generate_markdown()
    
    if args.output:
        with open(args.output, 'w') as f:
            f.write(markdown_report)
        print(f"Report saved to {args.output}")
    else:
        print(markdown_report)
    
    report.print_summary()


if __name__ == '__main__':
    main()
