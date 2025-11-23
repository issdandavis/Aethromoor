# Auto-Commit Configuration File
# Copy this file to scripts/auto-commit-config.sh and customize as needed

# Prefix for auto-generated commit messages
COMMIT_MESSAGE_PREFIX="Auto-commit:"

# Automatically push after committing (true/false)
AUTO_PUSH=true

# Include untracked files in commits (true/false)
INCLUDE_UNTRACKED=true

# Maximum file size in MB (files larger than this will trigger a warning)
MAX_FILE_SIZE_MB=10

# Patterns to exclude from auto-commits (space-separated)
# These should already be in .gitignore, but this provides extra safety
EXCLUDE_PATTERNS="*.log *.tmp node_modules/ .env .DS_Store"

# Dry run mode - set to true to see what would be committed without actually committing
DRY_RUN=false
