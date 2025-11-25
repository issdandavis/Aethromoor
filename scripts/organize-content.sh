#!/bin/bash
# Content Organization Helper
# Auto-categorizes and organizes content files

echo "🗂️  AVALON CONTENT ORGANIZER"
echo "=============================="
echo ""

cd "$(dirname "$0")/.." || exit

# Create organized directory structure if needed
mkdir -p lore/characters
mkdir -p lore/locations
mkdir -p lore/magic_systems
mkdir -p lore/timeline

echo "📁 Analyzing content..."
echo ""

# Find uncategorized files
uncategorized=$(find . -maxdepth 1 -name "*.txt" -o -name "*.md" | grep -v README)

if [ -n "$uncategorized" ]; then
    echo "⚠️  Found uncategorized files in root:"
    echo "$uncategorized"
    echo ""
    echo "Suggestions (review before moving):"
    
    echo "$uncategorized" | while read -r file; do
        filename=$(basename "$file")
        
        # Suggest category based on content
        if grep -qi "character\|personality\|background" "$file"; then
            echo "  → Move $filename to lore/characters/ (contains character info)"
        elif grep -qi "location\|place\|geography\|realm" "$file"; then
            echo "  → Move $filename to lore/locations/ (contains location info)"
        elif grep -qi "magic\|spell\|dimensional\|rune" "$file"; then
            echo "  → Move $filename to lore/magic_systems/ (contains magic info)"
        elif grep -qi "timeline\|history\|year\|era" "$file"; then
            echo "  → Move $filename to lore/timeline/ (contains historical info)"
        else
            echo "  ? Review $filename manually"
        fi
    done
else
    echo "✅ All content appears organized!"
fi

echo ""
echo "📊 Current Organization:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━"

for dir in lore/characters lore/locations lore/magic_systems lore/timeline; do
    if [ -d "$dir" ]; then
        count=$(find "$dir" -type f | wc -l)
        echo "  $dir: $count files"
    fi
done

echo ""
echo "💡 TIP: Use 'gh copilot suggest' to get commands for moving files"
echo "   Example: gh copilot suggest \"move character files to lore/characters/\""
