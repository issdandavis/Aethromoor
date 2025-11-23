#!/bin/bash
# Quick script to play the HTML game locally
# Opens the game in your default browser

GAME_FILE="game/index.html"

if [ ! -f "$GAME_FILE" ]; then
    echo "Error: $GAME_FILE not found!"
    echo "Make sure you're running this from the Avalon root directory."
    exit 1
fi

echo "🎮 Opening Polly's Wingscroll..."

# Detect OS and open accordingly
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    open "$GAME_FILE"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    if command -v xdg-open > /dev/null; then
        xdg-open "$GAME_FILE"
    else
        echo "Please open $GAME_FILE in your browser"
    fi
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    # Windows
    start "$GAME_FILE"
else
    echo "Please open $GAME_FILE in your browser"
fi

echo "✓ Game should open in your default browser"
echo "If not, manually open: $(pwd)/$GAME_FILE"
