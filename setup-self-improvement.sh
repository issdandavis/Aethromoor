#!/bin/bash
# Setup Self-Improving System
# Run this script to enable all self-improvement features

set -e

echo "🚀 Setting up Self-Improving System for Aethromoor"
echo "=================================================="

# Check Python version
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "✅ Python $PYTHON_VERSION detected"

# Install development dependencies
echo ""
echo "📦 Installing development dependencies..."
pip install -r requirements-dev.txt --quiet

# Setup pre-commit hooks
echo ""
echo "🔧 Setting up pre-commit hooks..."
pre-commit install
pre-commit install --hook-type commit-msg

# Initialize secrets baseline
echo ""
echo "🔐 Initializing secrets detection baseline..."
if [ ! -f .secrets.baseline ]; then
    detect-secrets scan > .secrets.baseline || echo "{}" > .secrets.baseline
fi

# Create metrics directory
echo ""
echo "📊 Creating metrics directory..."
mkdir -p .github/metrics

# Run initial quality check
echo ""
echo "🔍 Running initial code quality check..."
echo "This may take a moment..."

# Count current issues
ISSUES=$(flake8 . --max-line-length=120 --count --exclude=.git,venv,.venv 2>&1 | tail -1 || echo "0")
echo "Current code quality issues: $ISSUES"

# Optional: Auto-fix all files
read -p "Would you like to auto-fix all code quality issues now? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo ""
    echo "🤖 Running auto-fix on all Python files..."
    
    # Find and fix all Python files
    find . -name "*.py" -type f ! -path "./.git/*" ! -path "./venv/*" ! -path "./.venv/*" -exec autopep8 --in-place --aggressive --aggressive {} \;
    
    # Fix imports
    isort .
    
    echo "✅ Auto-fix complete"
    
    # Recount issues
    ISSUES_AFTER=$(flake8 . --max-line-length=120 --count --exclude=.git,venv,.venv 2>&1 | tail -1 || echo "0")
    echo "Issues remaining: $ISSUES_AFTER"
fi

# Generate initial dashboard
echo ""
echo "📊 Generating initial dashboard..."
python3 << 'EOF'
import json
from datetime import datetime
from pathlib import Path

metrics_dir = Path('.github/metrics')
metrics_dir.mkdir(parents=True, exist_ok=True)

today = datetime.now().strftime('%Y-%m-%d')
metrics = {
    'date': today,
    'issue_count': 0,
    'python_file_count': 0,
    'status': 'initialized'
}

with open(metrics_dir / f'daily_{today}.json', 'w') as f:
    json.dump(metrics, f, indent=2)

print(f"✅ Initial metrics saved for {today}")
EOF

# Summary
echo ""
echo "=================================================="
echo "✨ Self-Improving System Setup Complete!"
echo "=================================================="
echo ""
echo "Next steps:"
echo "1. Your commits will now be automatically checked and fixed"
echo "2. Push your changes to trigger GitHub Actions workflows"
echo "3. Check DASHBOARD.md daily for health metrics"
echo "4. Review .github/SELF_IMPROVEMENT_GUIDE.md for full documentation"
echo ""
echo "Quick commands:"
echo "  - Run all pre-commit checks: pre-commit run --all-files"
echo "  - Check code quality: flake8 . --max-line-length=120"
echo "  - Auto-fix issues: python .github/scripts/autofix_code_quality.py"
echo ""
echo "🎉 Happy coding!"
