# Makefile for generating lecture presentations

# Directories
LECTURES_DIR = lectures
RESOURCES_DIR = resources
ASSESSMENTS_DIR = assessments
WORKSHOPS_DIR = workshops
TEMPLATES_DIR = templates
IMAGES_DIR = img
OUTPUT_DIR = build
LECTURES_OUT = $(OUTPUT_DIR)/lectures
ASSESSMENTS_OUT = $(OUTPUT_DIR)/assessments
WORKSHOPS_OUT = $(OUTPUT_DIR)/workshops
RESOURCES_OUT = $(OUTPUT_DIR)/resources
OUTPUT_IMAGES_DIR = $(LECTURES_OUT)/$(IMAGES_DIR)

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
							-V transition=fade \
							-V backgroundTransition=fade \
							-V hash=true \
							-V history=false \
							-V slideNumber=true \
							--css charles_reveal_dark.css

# --include-in-header css/slides.css \
# -V theme=night

BEAMER_OPTS = -t beamer \
              -V aspectratio=169 \
							-V theme=metropolis \
							-V colortheme=owl \
							--resource-path=$(LECTURES_DIR) \
              --pdf-engine=xelatex

# options for the pandoc HTML writer
HTML_OPTS = -V mainfont="system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"

# Find all markdown lecture files
LECTURE_MDS = $(wildcard $(LECTURES_DIR)/*.md)
REVEAL_HTMLS = $(patsubst $(LECTURES_DIR)/%.md,$(LECTURES_OUT)/%.html,$(LECTURE_MDS))
BEAMER_PDFS = $(patsubst $(LECTURES_DIR)/%.md,$(LECTURES_OUT)/%.pdf,$(LECTURE_MDS))

# Find all markdown resources
RESOURCES_MDS = $(wildcard $(RESOURCES_DIR)/*.md)
RESOURCES_HTMLS = $(patsubst $(RESOURCES_DIR)/%.md,$(RESOURCES_OUT)/%.html,$(RESOURCES_MDS))

$(RESOURCES_OUT)/%.html: $(RESOURCES_DIR)/%.md
	$(PANDOC) $(PANDOC_COMMON_OPTS) $(HTML_OPTS) $< -o $@

# Generate resources
.PHONY: resources
resources: $(RESOURCES_OUT) $(RESOURCES_HTMLS)

# Find all markdown assessments
ASSESSMENTS_MDS = $(wildcard $(ASSESSMENTS_DIR)/*.md)
ASSESSMENTS_HTMLS = $(patsubst $(ASSESSMENTS_DIR)/%.md,$(ASSESSMENTS_OUT)/%.html,$(ASSESSMENTS_MDS))

$(ASSESSMENTS_OUT)/%.html: $(ASSESSMENTS_DIR)/%.md
	$(PANDOC) $(PANDOC_COMMON_OPTS) $(HTML_OPTS) $< -o $@

# Generate assessments
.PHONY: assessments
assessments: $(ASSESSMENTS_OUT) $(ASSESSMENTS_HTMLS)

# Find all markdown workshops
WORKSHOPS_MDS = $(wildcard $(WORKSHOPS_DIR)/*.md)
WORKSHOPS_HTMLS = $(patsubst $(WORKSHOPS_DIR)/%.md,$(WORKSHOPS_OUT)/%.html,$(WORKSHOPS_MDS))

$(WORKSHOPS_OUT)/%.html: $(WORKSHOPS_DIR)/%.md
	$(PANDOC) $(PANDOC_COMMON_OPTS) $(HTML_OPTS) $< -o $@

# Generate workshops
.PHONY: workshops
workshops: $(WORKSHOPS_OUT) $(WORKSHOPS_HTMLS)

# Create output directories including images
.PHONY: directories
directories: $(LECTURES_OUT) $(WORKSHOPS_OUT) $(ASSESSMENTS_OUT) $(RESOURCES_OUT) $(OUTPUT_IMAGES_DIR)

# Copy images to output directory
.PHONY: images
images: directories
	cp -r $(LECTURES_DIR)/$(IMAGES_DIR)/* $(OUTPUT_IMAGES_DIR)/

# Create output directories
$(LECTURES_OUT) $(WORKSHOPS_OUT) $(ASSESSMENTS_OUT) $(RESOURCES_OUT) $(OUTPUT_IMAGES_DIR):
	mkdir -p $@

# Generate Reveal.js presentations
.PHONY: reveal
reveal: $(LECTURES_OUT) $(REVEAL_HTMLS) images $(LECTURES_OUT)/charles_reveal_dark.css

$(LECTURES_OUT)/%.html: $(LECTURES_DIR)/%.md
	$(PANDOC) $(PANDOC_COMMON_OPTS) $(REVEAL_OPTS) $< -o $@

# Generate Beamer PDFs
.PHONY: beamer
beamer: $(LECTURES_OUT) $(BEAMER_PDFS)

$(LECTURES_OUT)/%.pdf: $(LECTURES_DIR)/%.md
	$(PANDOC) $(PANDOC_COMMON_OPTS) $(BEAMER_OPTS) $< -o $@

$(INDEX_HTML): $(LECTURE_MDS) $(ASSESSMENTS_MDS) $(WORKSHOPS_MDS) $(RESOURCES_MDS) $(INDEX_GENERATOR)
	python3 $(INDEX_GENERATOR) $@ $(OUTPUT_DIR)

.PHONY: index
index: $(INDEX_HTML)

# Styles
%/charles_reveal_dark.css: css/charles_reveal_dark.scss
	sass --style=compressed css/charles_reveal_dark.scss $@

# phony targets
.PHONY: all
all: reveal beamer assessments resources workshops index

.PHONY: public
public: reveal index

.PHONY: html
html: reveal assessments resources workshops index

.PHONY: clean
clean:
	rm -rf $(OUTPUT_DIR)
