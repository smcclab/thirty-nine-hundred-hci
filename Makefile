# Makefile for generating lecture presentations

# =============================================================================
# Directories
# =============================================================================

LECTURES_DIR    = lectures
ASSESSMENTS_DIR = assessments
WORKSHOPS_DIR   = workshops
RESOURCES_DIR   = resources
TEMPLATES_DIR   = templates
FILTERS_DIR     = filters
OUTPUT_DIR      = build
IMAGE_DIR       = img

LECTURES_OUT    = $(OUTPUT_DIR)/lectures
ASSESSMENTS_OUT = $(OUTPUT_DIR)/assessments
WORKSHOPS_OUT   = $(OUTPUT_DIR)/workshops
RESOURCES_OUT   = $(OUTPUT_DIR)/resources

# =============================================================================
# Course metadata
# =============================================================================

REFERENCES = references.bib
CONFIG     = _config.toml
CONFIG_AUTHOR := $(shell python3 -c "import tomllib; f=open('$(CONFIG)','rb'); d=tomllib.load(f); print(d['author'])")
CONFIG_YEAR   := $(shell python3 -c "import tomllib; f=open('$(CONFIG)','rb'); d=tomllib.load(f); print(d['year'])")

INDEX_HTML      = $(OUTPUT_DIR)/index.html
INDEX_GENERATOR = generate_index.py

# =============================================================================
# Pandoc configuration
# =============================================================================

PANDOC = pandoc

# -V revealjs-url=https://unpkg.com/reveal.js@4.5.0
# Everything except --standalone. The Canvas fragment build (see canvas-html)
# needs the same citation/resource handling but must NOT be standalone, so the
# shared part lives here and --standalone is added back on the next line.
PANDOC_BASE_OPTS = --slide-level 2 \
                   --citeproc \
                   --bibliography=$(REFERENCES) \
                   --csl=apa.csl \
                   -M link-citations=true \
                   --resource-path=.:$(LECTURES_DIR):$(ASSESSMENTS_DIR):$(RESOURCES_DIR):$(WORKSHOPS_DIR)

PANDOC_COMMON_OPTS = --standalone $(PANDOC_BASE_OPTS)

# `# References {.allowframebreaks}` splits itself over as many frames as it
# needs in Beamer. Reveal.js has no equivalent, so a filter chunks the
# bibliography into slides; without it the entries overflow off the slide.
REVEAL_FILTER = $(FILTERS_DIR)/reveal-refs-split.lua

REVEAL_OPTS = -t revealjs \
              --lua-filter=$(REVEAL_FILTER) \
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

# Beamer has no native equivalent of reveal.js's background-image attributes, so
# a Lua filter translates them into TikZ background overlays. Without it the
# backgrounds are silently dropped from the PDFs.
BEAMER_FILTER = $(FILTERS_DIR)/beamer-background.lua

BEAMER_OPTS = -t beamer \
              -V aspectratio=169 \
              -V theme=metropolis \
              -V colortheme=owl \
              --pdf-engine=lualatex \
              -V mainfont="Noto Sans" \
              -V mainfontfallback="NotoColorEmoji:mode=harf" \
              --lua-filter=$(BEAMER_FILTER)

# --pdf-engine=xelatex

PDF_OPTS = --metadata date="$(shell date '+%Y-%m-%d')" \
           --number-sections=true \
           -V 'geometry: left=2.5cm,right=2.5cm,top=2.5cm,bottom=2.5cm' \
           -V 'papersize: a4' \
           -V 'fontsize:11pt' \
           -V 'pagestyle:headings' \
           --pdf-engine=lualatex \
           -V mainfont="Linux Libertine O" \
           -V sansfont="Noto Sans" \
           -V mainfontfallback="NotoColorEmoji:mode=harf"

# -V 'fontfamily:libertine,sourcecodepro'

HTML_OPTS = -V mainfont="system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"

# =============================================================================
# Top-level targets
# =============================================================================

.PHONY: all
all: reveal beamer assessments resources workshops images index

.PHONY: public
public: reveal beamer assessments workshops images index

.PHONY: html
html: reveal assessments resources workshops images index

.PHONY: clean
clean:
	rm -rf $(OUTPUT_DIR)

# =============================================================================
# Lectures — Reveal.js HTML + Beamer PDF
# =============================================================================

LECTURE_MDS  = $(wildcard $(LECTURES_DIR)/*.md)
REVEAL_HTMLS = $(patsubst $(LECTURES_DIR)/%.md,$(LECTURES_OUT)/%.html,$(LECTURE_MDS))
BEAMER_PDFS  = $(patsubst $(LECTURES_DIR)/%.md,$(LECTURES_OUT)/%.pdf,$(LECTURE_MDS))

.PHONY: reveal
reveal: $(LECTURES_OUT) $(REVEAL_HTMLS) images $(LECTURES_OUT)/charles_reveal_dark.css

$(LECTURES_OUT)/%.html: $(LECTURES_DIR)/%.md $(REVEAL_FILTER)
	$(PANDOC) $(PANDOC_COMMON_OPTS) $(REVEAL_OPTS) $< -o $@

.PHONY: beamer
beamer: $(LECTURES_OUT) $(BEAMER_PDFS)

$(LECTURES_OUT)/%.pdf: $(LECTURES_DIR)/%.md $(BEAMER_FILTER)
	$(PANDOC) $(PANDOC_COMMON_OPTS) $(BEAMER_OPTS) $< -o $@

# =============================================================================
# Assessments — HTML + PDF
# =============================================================================

ASSESSMENTS_MDS   = $(wildcard $(ASSESSMENTS_DIR)/*.md)
ASSESSMENTS_HTMLS = $(patsubst $(ASSESSMENTS_DIR)/%.md,$(ASSESSMENTS_OUT)/%.html,$(ASSESSMENTS_MDS))
ASSESSMENTS_PDFS  = $(patsubst $(ASSESSMENTS_DIR)/%.md,$(ASSESSMENTS_OUT)/%.pdf,$(ASSESSMENTS_MDS))

.PHONY: assessments
assessments: $(ASSESSMENTS_OUT) $(ASSESSMENTS_HTMLS) $(ASSESSMENTS_PDFS)

$(ASSESSMENTS_OUT)/%.html: $(ASSESSMENTS_DIR)/%.md
	$(PANDOC) $(PANDOC_COMMON_OPTS) $(HTML_OPTS) $< -o $@

$(ASSESSMENTS_OUT)/%.pdf: $(ASSESSMENTS_DIR)/%.md
	$(PANDOC) $(PANDOC_COMMON_OPTS) $(PDF_OPTS) $< -o $@

# =============================================================================
# Workshops — HTML only
# =============================================================================

WORKSHOPS_MDS   = $(wildcard $(WORKSHOPS_DIR)/*.md)
WORKSHOPS_HTMLS = $(patsubst $(WORKSHOPS_DIR)/%.md,$(WORKSHOPS_OUT)/%.html,$(WORKSHOPS_MDS))

# Hand-written standalone pages (e.g. interview-question-cards.html) are
# copied verbatim rather than built with pandoc.
WORKSHOPS_STATIC      = $(wildcard $(WORKSHOPS_DIR)/*.html)
WORKSHOPS_STATIC_OUT  = $(patsubst $(WORKSHOPS_DIR)/%.html,$(WORKSHOPS_OUT)/%.html,$(WORKSHOPS_STATIC))

.PHONY: workshops
workshops: $(WORKSHOPS_OUT) $(WORKSHOPS_HTMLS) $(WORKSHOPS_STATIC_OUT)

$(WORKSHOPS_OUT)/%.html: $(WORKSHOPS_DIR)/%.md $(REFERENCES)
	$(PANDOC) $(PANDOC_COMMON_OPTS) $(HTML_OPTS) $< -o $@

$(WORKSHOPS_OUT)/%.html: $(WORKSHOPS_DIR)/%.html
	cp $< $@

# =============================================================================
# Resources — HTML only
# =============================================================================

RESOURCES_MDS   = $(wildcard $(RESOURCES_DIR)/*.md)
RESOURCES_HTMLS = $(patsubst $(RESOURCES_DIR)/%.md,$(RESOURCES_OUT)/%.html,$(RESOURCES_MDS))

.PHONY: resources
resources: $(RESOURCES_OUT) $(RESOURCES_HTMLS)

$(RESOURCES_OUT)/%.html: $(RESOURCES_DIR)/%.md
	$(PANDOC) $(PANDOC_COMMON_OPTS) $(HTML_OPTS) $< -o $@

# =============================================================================
# Images — copy from source to build
# =============================================================================

LECTURES_IMG     := $(wildcard lectures/img/*.png lectures/img/*.jpg lectures/img/*.jpeg lectures/img/*.svg lectures/img/*.gif lectures/img/*.webp)
ASSESSMENTS_IMG  := $(wildcard assessments/img/*.png assessments/img/*.jpg assessments/img/*.jpeg assessments/img/*.svg assessments/img/*.gif assessments/img/*.webp)
WORKSHOPS_IMG    := $(wildcard workshops/img/*.png workshops/img/*.jpg workshops/img/*.jpeg workshops/img/*.svg workshops/img/*.gif workshops/img/*.webp)
RESOURCES_IMG    := $(wildcard resources/img/*.png resources/img/*.jpg resources/img/*.jpeg resources/img/*.svg resources/img/*.gif resources/img/*.webp)

LECTURES_BUILD_IMG    := $(patsubst lectures/img/%,build/lectures/img/%,$(LECTURES_IMG))
ASSESSMENTS_BUILD_IMG := $(patsubst assessments/img/%,build/assessments/img/%,$(ASSESSMENTS_IMG))
WORKSHOPS_BUILD_IMG   := $(patsubst workshops/img/%,build/workshops/img/%,$(WORKSHOPS_IMG))
RESOURCES_BUILD_IMG   := $(patsubst resources/img/%,build/resources/img/%,$(RESOURCES_IMG))
ALL_BUILD_IMGS        := $(LECTURES_BUILD_IMG) $(ASSESSMENTS_BUILD_IMG) $(WORKSHOPS_BUILD_IMG) $(RESOURCES_BUILD_IMG)

.PHONY: images
images: $(ALL_BUILD_IMGS)

$(OUTPUT_DIR)/$(LECTURES_DIR)/$(IMAGE_DIR)/%: $(LECTURES_DIR)/$(IMAGE_DIR)/%
	@mkdir -p $(dir $@)
	cp $< $@

$(OUTPUT_DIR)/$(ASSESSMENTS_DIR)/$(IMAGE_DIR)/%: $(ASSESSMENTS_DIR)/$(IMAGE_DIR)/%
	@mkdir -p $(dir $@)
	cp $< $@

$(OUTPUT_DIR)/$(WORKSHOPS_DIR)/$(IMAGE_DIR)/%: $(WORKSHOPS_DIR)/$(IMAGE_DIR)/%
	@mkdir -p $(dir $@)
	cp $< $@

$(OUTPUT_DIR)/$(RESOURCES_DIR)/$(IMAGE_DIR)/%: $(RESOURCES_DIR)/$(IMAGE_DIR)/%
	@mkdir -p $(dir $@)
	cp $< $@

# =============================================================================
# CSS / Styles
# =============================================================================

%/charles_reveal_dark.css: css/charles_reveal_dark.scss
	sass --style=compressed css/charles_reveal_dark.scss $@

# =============================================================================
# Output directories
# =============================================================================

.PHONY: directories
directories: $(LECTURES_OUT) $(WORKSHOPS_OUT) $(ASSESSMENTS_OUT) $(RESOURCES_OUT)

$(LECTURES_OUT) $(WORKSHOPS_OUT) $(ASSESSMENTS_OUT) $(RESOURCES_OUT):
	mkdir -p $@

# =============================================================================
# Index
# =============================================================================

.PHONY: index
index: $(INDEX_HTML)

$(INDEX_HTML): $(LECTURE_MDS) $(ASSESSMENTS_MDS) $(WORKSHOPS_MDS) $(RESOURCES_MDS) $(INDEX_GENERATOR)
	python3 $(INDEX_GENERATOR) $@ $(OUTPUT_DIR)

# =============================================================================
# Concatenated mega-files (all lectures / assessments / workshops in one file)
# =============================================================================

ALL_LECTURES    = $(OUTPUT_DIR)/all_lectures.pdf
ALL_ASSESSMENTS = $(OUTPUT_DIR)/all_assessments.pdf
ALL_WORKSHOPS   = $(OUTPUT_DIR)/all_workshops.pdf

.PHONY: bigfiles
bigfiles: $(ALL_LECTURES) $(ALL_ASSESSMENTS) $(ALL_WORKSHOPS)

$(ALL_LECTURES): $(LECTURE_MDS)
	$(PANDOC) $(PANDOC_COMMON_OPTS) $(PDF_OPTS) --metadata title="All Lectures" --metadata author="$(CONFIG_AUTHOR)" --metadata date="$(CONFIG_YEAR)" --toc=true -o $@ $^

$(ALL_ASSESSMENTS): $(ASSESSMENTS_MDS)
	$(PANDOC) $(PANDOC_COMMON_OPTS) $(PDF_OPTS) --metadata title="All Assessments" --metadata author="$(CONFIG_AUTHOR)" --metadata date="$(CONFIG_YEAR)" --toc=true -o $@ $^

$(ALL_WORKSHOPS): $(WORKSHOPS_MDS)
	$(PANDOC) $(PANDOC_COMMON_OPTS) $(PDF_OPTS) --metadata title="All Workshops" --metadata author="$(CONFIG_AUTHOR)" --metadata date="$(CONFIG_YEAR)" --toc=true -o $@ $^

ALL_LECTURES_MD    = $(OUTPUT_DIR)/all_lectures.md
ALL_ASSESSMENTS_MD = $(OUTPUT_DIR)/all_assessments.md
ALL_WORKSHOPS_MD   = $(OUTPUT_DIR)/all_workshops.md

.PHONY: bigmd
bigmd: $(OUTPUT_DIR) $(ALL_LECTURES_MD) $(ALL_ASSESSMENTS_MD) $(ALL_WORKSHOPS_MD)

$(ALL_LECTURES_MD): $(LECTURE_MDS)
	cat $^ > $@

$(ALL_ASSESSMENTS_MD): $(ASSESSMENTS_MDS)
	cat $^ > $@

$(ALL_WORKSHOPS_MD): $(WORKSHOPS_MDS)
	cat $^ > $@

# =============================================================================
# Canvas — push built content to the ANU Canvas course (canvas/ tooling)
# =============================================================================
# Requires a Canvas API token (CANVAS_TOKEN env var or ~/.config/canvas/anu-token).
# See canvas/README.md. Uploads use on_duplicate=overwrite so existing Home-page
# links keep pointing at the refreshed slides.

.PHONY: canvas-lectures canvas-lectures-dry canvas-lectures-mega canvas-inspect
.PHONY: canvas-html canvas-assignments canvas-assignments-dry

# Preview what would be pushed (reads Canvas, uploads nothing):
canvas-lectures-dry:
	python3 canvas/push_lectures.py --dry-run

# Build the lecture PDFs, then push them to Canvas:
canvas-lectures: beamer
	python3 canvas/push_lectures.py

# As above, plus the all_lectures.pdf / all_workshops.pdf bundles that the Canvas
# Home page links. Those are NOT refreshed by canvas-lectures, so without this
# they silently keep serving whatever year they were last built in.
canvas-lectures-mega: beamer bigfiles
	python3 canvas/push_lectures.py --mega

# Read-only dump of the current Canvas course structure:
canvas-inspect:
	python3 canvas/inspect_course.py

# -----------------------------------------------------------------------------
# Assignment descriptions (assessments/ + workshops/ -> Canvas Assignment pages)
# -----------------------------------------------------------------------------
# Canvas stores an assignment description as an HTML *fragment* — no <html>,
# <head> or <body>, and no title (the assignment name supplies that). So these
# builds deliberately drop --standalone, unlike every other HTML target here.
# --wrap=none keeps the payload on one line per block, which makes the dry-run
# diff against the live page readable.
#
# Image srcs are left as-is (img/foo.jpg); push_assignments.py rewrites them to
# Canvas file URLs at push time, since only it knows the Canvas file ids.

CANVAS_OUT = $(OUTPUT_DIR)/canvas

CANVAS_PANDOC_OPTS = $(PANDOC_BASE_OPTS) --wrap=none

CANVAS_ASSESSMENTS_HTMLS = $(patsubst $(ASSESSMENTS_DIR)/%.md,$(CANVAS_OUT)/$(ASSESSMENTS_DIR)/%.html,$(ASSESSMENTS_MDS))
CANVAS_WORKSHOPS_HTMLS   = $(patsubst $(WORKSHOPS_DIR)/%.md,$(CANVAS_OUT)/$(WORKSHOPS_DIR)/%.html,$(WORKSHOPS_MDS))

canvas-html: $(CANVAS_ASSESSMENTS_HTMLS) $(CANVAS_WORKSHOPS_HTMLS)

$(CANVAS_OUT)/$(ASSESSMENTS_DIR)/%.html: $(ASSESSMENTS_DIR)/%.md $(REFERENCES)
	@mkdir -p $(dir $@)
	$(PANDOC) $(CANVAS_PANDOC_OPTS) $< -o $@

$(CANVAS_OUT)/$(WORKSHOPS_DIR)/%.html: $(WORKSHOPS_DIR)/%.md $(REFERENCES)
	@mkdir -p $(dir $@)
	$(PANDOC) $(CANVAS_PANDOC_OPTS) $< -o $@

# Preview the description changes as a diff against what is live (uploads nothing):
canvas-assignments-dry: canvas-html
	python3 canvas/push_assignments.py --dry-run

# Build the fragments, then overwrite the Canvas assignment descriptions:
canvas-assignments: canvas-html
	python3 canvas/push_assignments.py
