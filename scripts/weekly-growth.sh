#!/bin/bash
# Weekly Content Growth Report
# Tracks content growth and suggests priorities

echo "📈 WEEKLY CONTENT GROWTH REPORT"
echo "Generated: $(date)"
echo "========================================"
echo ""

cd "$(dirname "$0")/.." || exit

# Current metrics
current_words=$(find choicescript_game/scenes -name "*.txt" -exec wc -w {} + 2>/dev/null | tail -1 | awk '{print $1}' || echo 0)
current_scenes=$(find choicescript_game/scenes -name "*.txt" 2>/dev/null | wc -l)

echo "CURRENT STATUS:"
echo "  Total Words: $current_words"
echo "  Total Scenes: $current_scenes"
echo "  Target: 50,000 words"
if [ "$current_words" -gt 0 ] 2>/dev/null; then
    progress=$(( current_words * 100 / 50000 ))
    echo "  Progress: ${progress}%"
else
    echo "  Progress: 0%"
fi
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
    [ -f "$scene" ] || continue
    choices=$(grep -c "^[[:space:]]*#" "$scene" 2>/dev/null | tr -d '\n' || echo "0")
    if [ "$choices" -lt 3 ] && [ "$choices" -ge 0 ]; then
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
if [ "$needed" -le 0 ]; then
    echo "  🎉 Target exceeded! You have $(( current_words - 50000 )) extra words!"
else
    echo "  Remaining words needed: $needed"
    echo "  Suggested weekly target: $(( needed / 4 )) words/week"
    if [ "$current_scenes" -gt 0 ]; then
        echo "  Average per scene: $(( needed / current_scenes )) words/scene"
    fi
fi

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
