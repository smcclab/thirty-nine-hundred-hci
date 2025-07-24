#!/bin/bash
# Usage: ./count_slides.sh filename.md

if [ $# -ne 1 ]; then
  echo "Usage: $0 filename.md"
  exit 1
fi

grep -E '^#{1,2} ' "$1" | grep -v '^#{3,}' | wc -l
