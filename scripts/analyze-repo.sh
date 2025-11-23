#!/bin/bash
# Analyzes the repository for issues and suggests improvements

echo "📊 Analyzing Avalon Repository..."
echo "=================================="
echo ""

# Function to format bytes
format_bytes() {
    if [ $1 -ge 1048576 ]; then
        echo "$(($1 / 1048576))MB"
    elif [ $1 -ge 1024 ]; then
        echo "$(($1 / 1024))KB"
    else
        echo "${1}B"
    fi
}

echo "1. Repository Size Analysis"
echo "---------------------------"
total_size=$(du -sb . 2>/dev/null | cut -f1)
archive_size=$(du -sb archive 2>/dev/null | cut -f1)
docs_size=$(du -sb docs 2>/dev/null | cut -f1)
game_size=$(du -sb game 2>/dev/null | cut -f1)

echo "Total repository: $(format_bytes $total_size)"
echo "  - archive/: $(format_bytes $archive_size) ($(($archive_size * 100 / $total_size))%)"
echo "  - docs/: $(format_bytes $docs_size) ($(($docs_size * 100 / $total_size))%)"
echo "  - game/: $(format_bytes $game_size) ($(($game_size * 100 / $total_size))%)"
echo ""

echo "2. File Type Distribution"
echo "-------------------------"
echo "Text files (.txt): $(find . -name "*.txt" -not -path "./.git/*" | wc -l)"
echo "Markdown files (.md): $(find . -name "*.md" -not -path "./.git/*" | wc -l)"
echo "PDF files (.pdf): $(find . -name "*.pdf" -not -path "./.git/*" | wc -l)"
echo "JavaScript files (.js): $(find . -name "*.js" -not -path "./.git/*" | wc -l)"
echo "HTML files (.html): $(find . -name "*.html" -not -path "./.git/*" | wc -l)"
echo ""

echo "3. Large Files (>1MB)"
echo "---------------------"
find . -type f -size +1M -not -path "./.git/*" -exec du -h {} \; | sort -hr | head -10
echo ""

echo "4. Code Complexity"
echo "------------------"
if [ -f "game/game.js" ]; then
    lines=$(wc -l < game/game.js)
    functions=$(grep -c "function " game/game.js || echo 0)
    nodes=$(grep -c "^[[:space:]]*[a-zA-Z_].*:.*{" game/game.js || echo 0)
    
    echo "game.js metrics:"
    echo "  - Lines of code: $lines"
    echo "  - Functions: $functions"
    echo "  - Story nodes: $nodes"
    
    if [ $lines -gt 2000 ]; then
        echo "  ⚠ WARNING: File is very large. Consider modularization."
    fi
fi
echo ""

echo "5. Recommendations"
echo "------------------"

# Provide specific recommendations
if [ $archive_size -gt 10485760 ]; then  # > 10MB
    echo "⚠ archive/ is very large ($(format_bytes $archive_size))"
    echo "  Consider using Git LFS or external storage"
fi

if [ $(find . -name "*.pdf" -not -path "./.git/*" | wc -l) -gt 50 ]; then
    echo "⚠ Many PDF files found"
    echo "  Consider consolidating or using external document storage"
fi

echo ""
echo "✓ Analysis complete!"
