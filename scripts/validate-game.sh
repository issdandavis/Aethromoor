#!/bin/bash
# Game Validation Script for Polly's Wingscroll
# Validates both HTML and ChoiceScript versions before committing

set -e

echo "🎮 Validating Polly's Wingscroll Game Files..."
echo "================================================"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

ERRORS=0
WARNINGS=0

# Function to print colored output
print_error() {
    echo -e "${RED}✗ ERROR: $1${NC}"
    ((ERRORS++))
}

print_warning() {
    echo -e "${YELLOW}⚠ WARNING: $1${NC}"
    ((WARNINGS++))
}

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

# Check if we're in the right directory
if [ ! -f "game/index.html" ]; then
    print_error "Must run from Avalon root directory"
    exit 1
fi

echo ""
echo "1. Validating HTML Game..."
echo "----------------------------"

# Check HTML file exists and has content
if [ -f "game/index.html" ]; then
    if [ $(wc -l < "game/index.html") -lt 10 ]; then
        print_error "game/index.html is too short"
    else
        print_success "game/index.html exists and has content"
    fi
else
    print_error "game/index.html not found"
fi

# Check JavaScript syntax
if [ -f "game/game.js" ]; then
    if node -c game/game.js 2>/dev/null; then
        print_success "game.js has valid syntax"
    else
        print_error "game.js has syntax errors"
    fi
    
    # Check file size (warn if too large)
    SIZE=$(wc -l < game/game.js)
    if [ $SIZE -gt 1500 ]; then
        print_warning "game.js is very large ($SIZE lines). Consider splitting into modules."
    fi
else
    print_error "game/game.js not found"
fi

# Check for required story nodes
if [ -f "game/game.js" ]; then
    required_nodes=("start" "ending_collaborative_master" "field_expedition_offer")
    for node in "${required_nodes[@]}"; do
        if grep -q "$node:" game/game.js; then
            print_success "Found required node: $node"
        else
            print_error "Missing required node: $node"
        fi
    done
fi

echo ""
echo "2. Validating ChoiceScript Game..."
echo "-----------------------------------"

# Check startup.txt exists
if [ -f "choicescript_game/startup.txt" ]; then
    print_success "choicescript_game/startup.txt exists"
    
    # Check for required ChoiceScript commands
    if grep -q '\\*create' choicescript_game/startup.txt; then
        print_success "Startup file has stat definitions"
    else
        print_warning "No *create commands found in startup.txt"
    fi
else
    print_error "choicescript_game/startup.txt not found"
fi

# Check scenes directory
if [ -d "choicescript_game/scenes" ]; then
    SCENE_COUNT=$(find choicescript_game/scenes -name "*.txt" | wc -l)
    print_success "Found $SCENE_COUNT scene files"
    
    if [ $SCENE_COUNT -lt 3 ]; then
        print_warning "Only $SCENE_COUNT scenes found. More content needed."
    fi
else
    print_error "choicescript_game/scenes directory not found"
fi

echo ""
echo "3. File Organization Check..."
echo "------------------------------"

# Check for duplicate files
DUPLICATES=$(find . -type f \( -name "*.duplicate" -o -name "*copy*" -o -name "*backup*" \) -not -path "./.git/*" | wc -l)
if [ $DUPLICATES -gt 0 ]; then
    print_warning "Found $DUPLICATES potential duplicate files"
fi

# Check for large files
LARGE_FILES=$(find . -type f -size +5M -not -path "./.git/*" -not -path "./archive/*" | wc -l)
if [ $LARGE_FILES -gt 0 ]; then
    print_warning "Found $LARGE_FILES files larger than 5MB outside archive"
fi

# Summary
echo ""
echo "================================================"
echo "Validation Summary:"
echo "-------------------"
echo "Errors: $ERRORS"
echo "Warnings: $WARNINGS"
echo ""

if [ $ERRORS -eq 0 ]; then
    echo -e "${GREEN}✓ All critical validations passed!${NC}"
    if [ $WARNINGS -gt 0 ]; then
        echo -e "${YELLOW}⚠ However, there are $WARNINGS warnings to review${NC}"
    fi
    exit 0
else
    echo -e "${RED}✗ Validation failed with $ERRORS errors${NC}"
    exit 1
fi
