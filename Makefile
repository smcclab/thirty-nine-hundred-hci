# Makefile for generating lecture presentations

# Directories
LECTURES_DIR = lectures
TEMPLATES_DIR = templates
IMAGES_DIR = img
OUTPUT_DIR = build
REVEAL_DIR = $(OUTPUT_DIR)/reveal
BEAMER_DIR = $(OUTPUT_DIR)/beamer
OUTPUT_IMAGES_DIR = $(REVEAL_DIR)/$(IMAGES_DIR)
# DZ_DIR = output/dz

# Index generation
INDEX_HTML = $(OUTPUT_DIR)/index.html
INDEX_GENERATOR = generate_index.py

# Pandoc settings
# -V revealjs-url=https://unpkg.com/reveal.js@4.5.0
PANDOC = pandoc
PANDOC_COMMON_OPTS = --standalone --slide-level 2
REVEAL_OPTS = -t revealjs \
							-V controls=true \
							-V progress=true \
							-V center=false \
							-V width=1920 \
							-V height=1080 \
							-V margin=0.1 \
							--include-in-header css/slides.css \
              -V theme=night

DZ_OPTS = -t dzslides
# -V colortheme=nord \
 
BEAMER_OPTS = -t beamer \
              -V aspectratio=169 \
							-V theme=metropolis \
							-V colortheme=owl \
              --pdf-engine=xelatex

# Find all markdown lecture files
LECTURE_MDS = $(wildcard $(LECTURES_DIR)/*.md)
REVEAL_HTMLS = $(patsubst $(LECTURES_DIR)/%.md,$(REVEAL_DIR)/%.html,$(LECTURE_MDS))
BEAMER_PDFS = $(patsubst $(LECTURES_DIR)/%.md,$(BEAMER_DIR)/%.pdf,$(LECTURE_MDS))
DZ_HTMLS = $(patsubst $(LECTURES_DIR)/%.md,$(DZ_DIR)/%.html,$(LECTURE_MDS))

# Default target
.PHONY: all
all: reveal beamer index

# Create output directories including images
.PHONY: directories
directories:
	mkdir -p $(REVEAL_DIR)
	mkdir -p $(BEAMER_DIR)
	mkdir -p $(OUTPUT_IMAGES_DIR)

# Copy images to output directory
.PHONY: images
images: directories
	cp -r $(IMAGES_DIR)/* $(OUTPUT_IMAGES_DIR)/

# Create output directories
$(REVEAL_DIR) $(BEAMER_DIR):
	mkdir -p $@

# Generate Reveal.js presentations
.PHONY: reveal
reveal: $(REVEAL_DIR) $(REVEAL_HTMLS) images

$(REVEAL_DIR)/%.html: $(LECTURES_DIR)/%.md
	$(PANDOC) $(PANDOC_COMMON_OPTS) $(REVEAL_OPTS) $< -o $@

# Generate Beamer PDFs
.PHONY: beamer
beamer: $(BEAMER_DIR) $(BEAMER_PDFS)

$(BEAMER_DIR)/%.pdf: $(LECTURES_DIR)/%.md
	$(PANDOC) $(PANDOC_COMMON_OPTS) $(BEAMER_OPTS) $< -o $@

$(INDEX_HTML): $(LECTURE_MDS) $(REVEAL_HTMLS) $(BEAMER_PDFS) $(INDEX_GENERATOR)
	python3 $(INDEX_GENERATOR) $@ $(LECTURE_MDS)

.PHONY: index
index: $(INDEX_HTML)

# Clean up generated files
.PHONY: clean
clean:
	rm -rf $(REVEAL_DIR) $(BEAMER_DIR) $(OUTPUT_IMAGES_DIR) $(INDEX_HTML)