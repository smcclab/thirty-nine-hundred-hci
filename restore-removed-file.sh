#!/bin/bash

# Check if a file path was provided
if [ -z "$1" ]; then
    echo "Usage: $0 <file_path>"
    exit 1
fi

FILE_PATH="$1"

# 1. Find the most recent commit hash that affected this file
LAST_COMMIT=$(git log -n 1 --pretty=format:%H -- "$FILE_PATH")

if [ -z "$LAST_COMMIT" ]; then
    echo "Error: No history found for '$FILE_PATH'."
    exit 1
fi

# 2. Check if the file is currently missing (deleted)
if [ ! -f "$FILE_PATH" ]; then
    echo "File is missing. Recovering from the version just before it was deleted..."
    # The '^' suffix points to the commit immediately before the deletion
    git checkout "$LAST_COMMIT"^ -- "$FILE_PATH"
else
    echo "File exists. Reverting it to its last known committed state ($LAST_COMMIT)..."
    git checkout "$LAST_COMMIT" -- "$FILE_PATH"
fi

# Verify success
if [ $? -eq 0 ]; then
    echo "Success: '$FILE_PATH' restored."
else
    echo "Failed to restore '$FILE_PATH'. Ensure the path is correct."
fi
