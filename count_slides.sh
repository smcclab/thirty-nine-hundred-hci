#!/bin/bash

for file in lectures/*.md; do
    # Count slides (lines starting with # or ## but not ###)
    slide_count=$(grep -E '^(# |## )' "$file" | grep -v '^### ' | wc -l)
    
    # Count total words in the file
    word_count=$(wc -w < "$file")
    
    # Calculate average words per slide (avoid division by zero)
    if [ "$slide_count" -gt 0 ]; then
        avg_words=$((word_count / slide_count))
        echo "$(basename "$file"): $slide_count slides, $word_count words, avg $avg_words words/slide"
    else
        echo "$(basename "$file"): 0 slides, $word_count words, no slides found"
    fi
done
