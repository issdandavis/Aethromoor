#!/bin/bash
# Daily Content Health Check
# Automatically analyzes Avalon content and generates health report

echo "╔════════════════════════════════════════════════════════════╗"
echo "║      AVALON CONTENT HEALTH REPORT                         ║"
echo "║      Generated: $(date '+%Y-%m-%d %H:%M:%S')                      ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Navigate to project root
cd "$(dirname "$0")/.." || exit

# 1. Total Content Metrics
echo "📊 TOTAL CONTENT METRICS"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

total_words=$(find choicescript_game/scenes -name "*.txt" -exec wc -w {} + 2>/dev/null | tail -1 | awk '{print $1}' || echo 0)
total_scenes=$(find choicescript_game/scenes -name "*.txt" 2>/dev/null | wc -l)
lore_words=$(find lore -name "*.txt" -o -name "*.md" 2>/dev/null | xargs wc -w 2>/dev/null | tail -1 | awk '{print $1}' || echo 0)

echo "  Game Scenes:     $total_scenes files"
echo "  Game Words:      $total_words words"
echo "  Lore Words:      $lore_words words"
echo "  Publication Min: 30,000 words"

if [ "$total_words" -ge 30000 ]; then
    echo "  Status:          ✅ READY FOR SUBMISSION"
else
    remaining=$((30000 - total_words))
    echo "  Status:          ⚠️  Need $remaining more words"
fi

echo ""

# 2. Scene Analysis
echo "🎮 SCENE BREAKDOWN"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

for scene in choicescript_game/scenes/*.txt; do
    [ -f "$scene" ] || continue
    filename=$(basename "$scene")
    words=$(wc -w < "$scene" 2>/dev/null || echo 0)
    # Remove any newlines from grep output
    choices=$(grep -c "^[[:space:]]*#" "$scene" 2>/dev/null | tr -d '\n' || echo "0")
    
    # Color code by size
    if [ "$words" -gt 2000 ]; then
        status="✅"
    elif [ "$words" -gt 1000 ]; then
        status="🟡"
    else
        status="🔴"
    fi
    
    printf "  %-30s %6d words  %2d choices  %s\n" "$filename" "$words" "$choices" "$status"
done

echo ""

# 3. Content Quality Indicators
echo "✨ QUALITY INDICATORS"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Count TODOs
todos=$(grep -r "TODO\|FIXME\|EXPAND\|PLACEHOLDER" choicescript_game/scenes lore 2>/dev/null | wc -l)
echo "  TODOs/FIXMEs:    $todos items"

# Count character mentions
polly_count=$(grep -roi "polly" choicescript_game/scenes | wc -l)
izack_count=$(grep -roi "izack" choicescript_game/scenes | wc -l)
aria_count=$(grep -roi "aria" choicescript_game/scenes | wc -l)
zara_count=$(grep -roi "zara" choicescript_game/scenes | wc -l)

echo "  Character Balance:"
echo "    - Polly:       $polly_count mentions"
echo "    - Izack:       $izack_count mentions"
echo "    - Aria:        $aria_count mentions"
echo "    - Zara:        $zara_count mentions"

echo ""

# 4. Recent Activity
echo "⚡ RECENT ACTIVITY (Last 7 days)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

recent=$(find choicescript_game/scenes lore docs -type f -mtime -7 2>/dev/null | wc -l)
echo "  Modified Files:  $recent files"

if [ "$recent" -gt 0 ]; then
    echo "  Recently Changed:"
    find choicescript_game/scenes lore docs -type f -mtime -7 -exec ls -lh {} \; 2>/dev/null | \
        awk '{print "    - " $9 " (" $5 ")"}'
fi

echo ""

# 5. Next Steps Recommendation
echo "🎯 RECOMMENDED NEXT STEPS"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Find smallest scenes
echo "  Expand These Scenes (< 1000 words):"
for scene in choicescript_game/scenes/*.txt; do
    [ -f "$scene" ] || continue
    words=$(wc -w < "$scene" 2>/dev/null || echo "0")
    # Only process if we got a valid number
    if [ "$words" -gt 0 ] 2>/dev/null && [ "$words" -lt 1000 ]; then
        echo "    - $(basename "$scene"): $words words"
    fi
done

# Show TODO count
if [ "$todos" -gt 0 ]; then
    echo ""
    echo "  Address TODOs:"
    grep -rn "TODO\|FIXME\|EXPAND" choicescript_game/scenes 2>/dev/null | head -5 | \
        awk -F: '{print "    - " $1 ":" $2 ": " substr($0, index($0,$3))}'
fi

echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║  Report Complete - Save or review above metrics           ║"
echo "╚════════════════════════════════════════════════════════════╝"
