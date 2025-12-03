#!/usr/bin/env python3
"""
Auto-fix Code Quality Issues
Automatically fixes common code quality issues in Python scripts
"""

# REMOVED: import os
import sys
import subprocess
import re
from pathlib import Path


def run_autopep8(filepath, aggressive=True):
    """Run autopep8 to fix PEP8 issues"""
    cmd = ['python3', '-m', 'autopep8', '--in-place']
    if aggressive:
        cmd.extend(['--aggressive', '--aggressive'])
    cmd.append(str(filepath))

    try:
        subprocess.run(cmd, capture_output=True, text=True, check=True)
        return True, "Fixed with autopep8"
    except subprocess.CalledProcessError as e:
        return False, f"autopep8 failed: {e.stderr}"


def fix_unused_imports(filepath):
    """Remove unused imports from Python file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Get list of unused imports from flake8
    result = subprocess.run(
        ['python3', '-m', 'flake8', '--select=F401', str(filepath)],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        return True, "No unused imports"

    # Parse flake8 output to find unused imports
    lines = content.splitlines(keepends=True)
    modified = False

    for line in result.stdout.splitlines():
        # Parse: filename:line:col: F401 'module' imported but unused
        match = re.search(
            r':(\d+):\d+: F401 \'([^\']+)\' imported but unused', line)
        if match:
            line_num = int(match.group(1)) - 1  # 0-indexed
            module = match.group(2)

            # Check if import is on that line and remove it
            import_line = lines[line_num]
            if f'import {module}' in import_line or f'from {module}' in import_line:
                # Comment out instead of removing to be safe
                if not import_line.strip().startswith('#'):
                    lines[line_num] = f'# REMOVED: {import_line}'
                    modified = True

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        return True, "Removed unused imports"

    return True, "No changes needed"


def fix_fstring_placeholders(filepath):
    """Fix f-strings without placeholders by converting to regular strings"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace f-strings without placeholders
    # Match "..." or '...' where there are no {braces}
    modified = False
    lines = content.splitlines(keepends=True)

    for i, line in enumerate(lines):
        # Simple regex to find f-strings without placeholders
        # This is a basic implementation, might need refinement
        new_line = re.sub(r'"([^"{]*)"', r'"\1"', line)
        new_line = re.sub(r"'([^'{]*)'", r"'\1'", new_line)

        if new_line != line:
            lines[i] = new_line
            modified = True

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        return True, "Fixed f-string placeholders"

    return True, "No f-string issues"


def fix_bare_except(filepath):
    """Fix bare except clauses"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace bare except: with except Exception:
    new_content = re.sub(
        r'except:\s*$',
        'except Exception:',
        content,
        flags=re.MULTILINE)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True, "Fixed bare except clauses"

    return True, "No bare except clauses"


def autofix_file(filepath):
    """Auto-fix all issues in a Python file"""
    print(f"\n{'=' * 80}")
    print(f"Processing: {filepath}")
    print(f"{'=' * 80}")

    # Run autopep8 first (fixes most issues)
    success, msg = run_autopep8(filepath)
    print(f"  autopep8: {msg}")

    # Fix unused imports
    success, msg = fix_unused_imports(filepath)
    print(f"  Unused imports: {msg}")

    # Fix f-string issues
    success, msg = fix_fstring_placeholders(filepath)
    print(f"  F-strings: {msg}")

    # Fix bare except
    success, msg = fix_bare_except(filepath)
    print(f"  Bare except: {msg}")

    # Run autopep8 again to clean up
    run_autopep8(filepath, aggressive=False)

    return True


def check_with_flake8(filepath):
    """Check file with flake8 and return issues count"""
    result = subprocess.run(
        ['python3', '-m', 'flake8', '--max-line-length=120', str(filepath)],
        capture_output=True,
        text=True
    )

    issues = result.stdout.strip().splitlines()
    return len(issues), issues


def main():
    """Main execution"""
    scripts_dir = Path(__file__).parent

    print("=" * 80)
    print("🔧 AUTO-FIX CODE QUALITY ISSUES")
    print("=" * 80)

    # Check if autopep8 is installed
    try:
        subprocess.run(['python3', '-m', 'autopep8', '--version'],
                       capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("\n❌ ERROR: autopep8 not installed")
        print("Install with: python3 -m pip install autopep8")
        sys.exit(1)

    # Get all Python files in the scripts directory
    python_files = list(scripts_dir.glob("*.py"))

    if not python_files:
        print("No Python files found in the scripts directory")
        sys.exit(0)

    print(f"\nFound {len(python_files)} Python files to process\n")

    # Before counts
    total_issues_before = 0
    for filepath in python_files:
        count, _ = check_with_flake8(filepath)
        total_issues_before += count

    print(f"Total issues before: {total_issues_before}\n")

    # Process each file
    for filepath in python_files:
        autofix_file(filepath)

    # After counts
    print("\n" + "=" * 80)
    print("📊 RESULTS")
    print("=" * 80)

    total_issues_after = 0
    for filepath in python_files:
        count, issues = check_with_flake8(filepath)
        total_issues_after += count

        if count > 0:
            print(f"\n{filepath.name}: {count} issues remaining")
            for issue in issues[:5]:  # Show first 5
                print(f"  {issue}")
            if count > 5:
                print(f"  ... and {count - 5} more")
        else:
            print(f"\n{filepath.name}: ✅ No issues")

    print("\n" + "=" * 80)
    print(f"Issues before: {total_issues_before}")
    print(f"Issues after:  {total_issues_after}")
    print(f"Fixed:         {total_issues_before - total_issues_after}")
    print("=" * 80)

    if total_issues_after == 0:
        print("\n✅ All code quality issues fixed!")
        sys.exit(0)
    else:
        print(
            f"\n⚠️  {total_issues_after} issues remaining (may require manual fixing)")
        sys.exit(0)


if __name__ == '__main__':
    main()
