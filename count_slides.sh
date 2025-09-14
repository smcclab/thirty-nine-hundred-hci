#!/bin/bash

for file in lectures/*.md; do
    # Count slides (lines starting with # or ## but not ###)
    slide_count=$(grep -E '^(# |## )' "$file" | grep -v '^### ' | wc -l)    
    word_count=$(wc -w < "$file")    
    image_count=$(grep -o '!\[.*\](' "$file" | wc -l)
    
    # Calculate averages (avoid division by zero)
    if [ "$slide_count" -gt 0 ]; then
        avg_words=$((word_count / slide_count))
        avg_images=$(echo "scale=3; $image_count / $slide_count" | bc 2>/dev/null || echo "0")
        echo "$(basename "$file"): $slide_count slides, $word_count words (avg $avg_words/slide), $image_count images (avg $avg_images/slide)"
    else
        echo "$(basename "$file"): 0 slides, $word_count words, $image_count images, no slides found"
    fi
done