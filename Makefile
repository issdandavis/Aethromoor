# Makefile for Avalon Project
# Provides convenient shortcuts for common tasks

.PHONY: help validate play analyze serve test clean

# Default target - show help
help:
	@echo "🎮 Avalon Project - Available Commands"
	@echo "======================================="
	@echo ""
	@echo "  make play       - Open the game in your browser"
	@echo "  make validate   - Run all validation checks"
	@echo "  make analyze    - Analyze repository health"
	@echo "  make serve      - Start local web server (port 8000)"
	@echo "  make test       - Run tests (same as validate)"
	@echo "  make clean      - Clean temporary files"
	@echo ""
	@echo "  make help       - Show this help message"
	@echo ""

# Play the game
play:
	@./scripts/play-game.sh

# Validate game files
validate:
	@./scripts/validate-game.sh

# Analyze repository
analyze:
	@./scripts/analyze-repo.sh

# Start local server
serve:
	@echo "🌐 Starting local server on http://localhost:8000"
	@echo "Press Ctrl+C to stop"
	@cd game && python3 -m http.server 8000 || python -m SimpleHTTPServer 8000

# Run tests (alias for validate)
test: validate

# Clean temporary files
clean:
	@echo "🧹 Cleaning temporary files..."
	@find . -name "*.tmp" -delete
	@find . -name "*.bak" -delete
	@find . -name "*~" -delete
	@find . -name ".DS_Store" -delete
	@echo "✓ Cleanup complete"

# Quick commit workflow (after validation)
commit-check:
	@./scripts/validate-game.sh && echo "✓ Ready to commit!" || echo "✗ Fix errors before committing"
