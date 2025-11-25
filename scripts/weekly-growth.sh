#!/bin/bash
# Weekly Content Growth Report
# Tracks content growth and suggests priorities

echo "📈 WEEKLY CONTENT GROWTH REPORT"
echo "Generated: $(date)"
echo "========================================"
echo ""

cd "$(dirname "$0")/.." || exit

# Current metrics
current_words=$(find choicescript_game/scenes -name "*.txt" -exec wc -w {} + | tail -1 | awk '{print $1}')
current_scenes=$(find choicescript_game/scenes -name "*.txt" | wc -l)

echo "CURRENT STATUS:"
echo "  Total Words: $current_words"
echo "  Total Scenes: $current_scenes"
echo "  Target: 50,000 words"
echo "  Progress: $(( current_words * 100 / 50000 ))%"
echo ""

# Find content gaps
echo "🎯 PRIORITY AREAS FOR EXPANSION:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

echo ""
echo "1. Shortest Scenes (Expand These First):"
find choicescript_game/scenes -name "*.txt" -exec wc -w {} \; | \
    sort -n | head -5 | \
    while read -r words file; do
        echo "   - $(basename "$file"): $words words"
    done

echo ""
echo "2. Scenes with Few Choices (Add Branching):"
for scene in choicescript_game/scenes/*.txt; do
    choices=$(grep -c "^\s*#" "$scene" 2>/dev/null || echo 0)
    if [ "$choices" -lt 3 ]; then
        echo "   - $(basename "$scene"): only $choices choices"
    fi
done

echo ""
echo "3. Missing Content (Check These):"
grep -r "TODO\|PLACEHOLDER" choicescript_game/scenes 2>/dev/null | \
    cut -d: -f1 | sort -u | \
    while read -r file; do
        echo "   - $(basename "$file")"
    done

echo ""
echo "📊 GROWTH RECOMMENDATIONS:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

needed=$((50000 - current_words))
echo "  Remaining words needed: $needed"
echo "  Suggested weekly target: $(( needed / 4 )) words/week"
echo "  Average per scene: $(( needed / current_scenes )) words/scene"

echo ""
echo "✨ QUALITY CHECKS:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Character balance
echo ""
echo "  Character Mentions (for balance):"
for char in Polly Izack Aria Zara; do
    count=$(grep -roi "$char" choicescript_game/scenes | wc -l)
    echo "    - $char: $count mentions"
done

echo ""
echo "Report Complete!"
