-- Split the citeproc bibliography across several reveal.js slides.
--
-- Lectures end with `# References {.allowframebreaks}`. In Beamer that
-- attribute is native: LaTeX measures the bibliography and breaks it over as
-- many frames as it needs. Reveal.js has no equivalent, so a lecture with more
-- than a handful of citations simply runs the entries off the bottom of the
-- slide, where they are invisible and unreachable.
--
-- This filter does the breaking by hand: it chunks the entries of the `#refs`
-- div into slide-sized groups and puts a continuation heading before each group
-- after the first. Pandoc builds slides from headers *after* filters run, so the
-- inserted headers become real slides.
--
-- Sizing is an estimate, not a measurement — a Lua filter cannot know the
-- rendered height. The two constants below were calibrated by measuring the
-- rendered bibliography in a headless browser at the 1920x1080 slide size the
-- Makefile sets, against `.csl-bib-body` in css/charles_reveal_dark.scss. Change
-- either the font size or the slide dimensions and they need recalibrating; a
-- too-large value overflows silently, which is the bug this filter exists to
-- fix, so both are set with some slack.
--
-- Only applies to reveal.js output: run over Beamer it would fight
-- allowframebreaks, and over plain HTML it would break a document that scrolls
-- perfectly well already.

-- Wrapped lines of bibliography to put on one slide. The heading leaves 929px,
-- an entry line is 31px and each entry adds ~10px of margin, so 25 lines fill
-- the slide exactly — set lower so the last entry is not jammed against the
-- bottom edge and the navigation arrows.
local LINES_PER_SLIDE = 21

-- Characters per rendered line at the `.csl-bib-body` font size on a 1920px
-- slide. Measured at ~167; rounded down because hanging indent shortens every
-- line after an entry's first.
local CHARS_PER_LINE = 155

-- Wrapped-line count for one bibliography entry. Deliberately crude: entry
-- length is what varies, and a one-line error per entry is absorbed by the
-- slack left in LINES_PER_SLIDE.
local function entry_lines(entry)
  local text = pandoc.utils.stringify(entry)
  return math.max(1, math.ceil(utf8.len(text) / CHARS_PER_LINE))
end

-- Greedily fill slides up to `budget` lines each. Groups are index ranges into
-- `lines`, carrying their own line total so rebalancing can adjust them cheaply.
local function pack(lines, budget)
  local groups = {}
  local first, sum = 1, 0

  for i, n in ipairs(lines) do
    -- Never emit an empty group: an entry taller than a whole slide has to
    -- overflow somewhere, and its own slide is the least bad place.
    if sum > 0 and sum + n > budget then
      table.insert(groups, { first = first, last = i - 1, sum = sum })
      first, sum = i, 0
    end
    sum = sum + n
  end
  table.insert(groups, { first = first, last = #lines, sum = sum })
  return groups
end

-- Even the groups out by pushing entries off the end of each slide onto the
-- next. Greedy packing fills early slides to the budget, so it tends to leave a
-- straggler: a "References (cont.)" slide holding a single entry. Moving an
-- entry only when it lowers the larger of the two totals makes the imbalance
-- strictly decrease, so this terminates.
local function rebalance(groups, lines, budget)
  local moved = true
  while moved do
    moved = false
    for i = #groups, 2, -1 do
      local prev, cur = groups[i - 1], groups[i]
      local n = lines[prev.last]
      if prev.last > prev.first
        and cur.sum + n <= budget
        and prev.sum > cur.sum + n then
        prev.last, prev.sum = prev.last - 1, prev.sum - n
        cur.first, cur.sum = cur.first - 1, cur.sum + n
        moved = true
      end
    end
  end
  return groups
end

-- Spread the entries as evenly as possible over the fewest slides that hold them.
local function split_entries(entries)
  local lines, total = {}, 0
  for i, entry in ipairs(entries) do
    lines[i] = entry_lines(entry)
    total = total + lines[i]
  end

  -- Packing at the full budget gives the fewest slides the entries will fit on.
  -- Deriving the count this way rather than from total/LINES_PER_SLIDE matters:
  -- entry lengths rarely divide neatly, so the arithmetic minimum is often one
  -- slide short of anything actually packable.
  local groups = pack(lines, LINES_PER_SLIDE)
  local slides = #groups
  if slides < 2 then
    return { entries }
  end

  -- Then the smallest budget that still fits in that many slides, so the entries
  -- spread out instead of piling onto the first slide.
  for budget = math.ceil(total / slides), LINES_PER_SLIDE do
    local candidate = pack(lines, budget)
    if #candidate <= slides then
      groups = rebalance(candidate, lines, budget)
      break
    end
  end

  local chunks = {}
  for i, group in ipairs(groups) do
    chunks[i] = {}
    for j = group.first, group.last do
      table.insert(chunks[i], entries[j])
    end
  end
  return chunks
end

function Div(div)
  if not FORMAT:match('revealjs') then
    return nil
  end
  if div.identifier ~= 'refs' then
    return nil
  end

  local chunks = split_entries(div.content)
  if #chunks < 2 then
    return nil
  end

  local blocks = pandoc.Blocks({})
  for i, chunk in ipairs(chunks) do
    local attr = div.attr:clone()
    if i > 1 then
      -- One `id="refs"` only; the citation backlinks target per-entry ids
      -- (`#ref-foo`), which stay unique wherever the entry lands.
      attr.identifier = 'refs-' .. i
      blocks:insert(pandoc.Header(1, 'References (cont.)',
        pandoc.Attr('references-cont-' .. i, { 'unnumbered' })))
    end
    blocks:insert(pandoc.Div(chunk, attr))
  end
  return blocks
end
