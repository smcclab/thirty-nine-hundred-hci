#!/bin/bash
for file in lectures/*.md; do
  count=$(grep -E '^(# |## )' "$file" | grep -v '^### ' | wc -l)
  echo "$(basename "$file"): $count"
done
