--[[
seo-meta.lua — per-page metadata for the HTML outputs (doc pages and reveal.js
decks). Applied via HTML_OPTS and REVEAL_OPTS in the Makefile; a no-op for
PDF/Beamer/gfm output.

What it adds, all driven by metadata the Makefile passes with -M:
  site_url   public base URL with trailing slash (from _config.toml)
  site_name  course title (from _config.toml)

  * lang="en-AU" on <html> unless the document sets its own `lang`.
  * <meta name="description"> — uses the document's `description` if it has
    one, otherwise the first paragraph of body text, cut to ~200 characters.
    (pandoc derives description-meta from `description` for the template.)
  * <link rel="canonical">, Open Graph and Twitter card tags, and a
    <link rel="alternate" type="text/markdown"> pointing at the rendered
    markdown sibling that the `markdown` Makefile target publishes.

The page URL is site_url + the last two components of the output path
(build/<section>/<name>.html → <section>/<name>.html), so this assumes the
one-level build layout the Makefile produces.
]]

local stringify = pandoc.utils.stringify

if not (FORMAT:match("html") or FORMAT:match("revealjs")) then
  return {}
end

local MAX_DESC = 200

local function has_image(block)
  local found = false
  block:walk({ Image = function() found = true end })
  return found
end

-- First body paragraph of real prose: long enough to be a sentence, and not a
-- figure caption (a Para wrapping an Image, which is how pandoc represents
-- captioned images and how most lecture decks open).
local function first_paragraph(blocks)
  for _, b in ipairs(blocks) do
    if (b.t == "Para" or b.t == "Plain") and not has_image(b) then
      local s = stringify(b):gsub("%s+", " ")
      if #s > 40 then return s end
    elseif b.t == "Div" or b.t == "BlockQuote" then
      local s = first_paragraph(b.content)
      if s then return s end
    end
  end
  return nil
end

local function truncate(s, n)
  if #s <= n then return s end
  local cut = s:sub(1, n):match("^(.*)%s%S*$") or s:sub(1, n)
  return cut:gsub("[,;:%s]+$", "") .. "…"
end

local function page_path()
  local out = PANDOC_STATE.output_file
  if not out then return nil end
  local section, name = out:match("([^/]+)/([^/]+)$")
  if section and name then return section .. "/" .. name end
  return name or out
end

function Pandoc(doc)
  local meta = doc.meta

  if not meta.lang then
    meta.lang = pandoc.MetaString("en-AU")
  end

  if not meta.description then
    local para = first_paragraph(doc.blocks)
    if para then
      meta.description = pandoc.MetaString(truncate(para, MAX_DESC))
    end
  end

  local site_url = meta.site_url and stringify(meta.site_url)
  if site_url and site_url ~= "" then
    local path = page_path()
    local url = site_url .. (path or "")
    local title = meta.pagetitle and stringify(meta.pagetitle)
      or (meta.title and stringify(meta.title)) or ""
    local site_name = meta.site_name and stringify(meta.site_name) or ""
    local desc = meta.description and stringify(meta.description) or ""
    local esc = function(s)
      return (s:gsub("&", "&amp;"):gsub('"', "&quot;"):gsub("<", "&lt;"))
    end
    local lines = {
      string.format('<link rel="canonical" href="%s">', esc(url)),
    }
    -- pandoc's html5 template writes <meta name="description"> itself from
    -- description-meta; the revealjs template does not, so add it here.
    if FORMAT:match("revealjs") and desc ~= "" then
      lines[#lines + 1] = string.format('<meta name="description" content="%s">', esc(desc))
    end
    for _, l in ipairs({
      string.format('<meta property="og:type" content="article">'),
      string.format('<meta property="og:url" content="%s">', esc(url)),
      string.format('<meta property="og:title" content="%s">', esc(title)),
      string.format('<meta name="twitter:card" content="summary">'),
    }) do lines[#lines + 1] = l end
    if site_name ~= "" then
      lines[#lines + 1] = string.format('<meta property="og:site_name" content="%s">', esc(site_name))
    end
    if desc ~= "" then
      lines[#lines + 1] = string.format('<meta property="og:description" content="%s">', esc(desc))
    end
    if path and path:match("%.html$") then
      lines[#lines + 1] = string.format(
        '<link rel="alternate" type="text/markdown" href="%s" title="Markdown source">',
        esc(site_url .. path:gsub("%.html$", ".md")))
    end
    local block = pandoc.RawBlock("html", table.concat(lines, "\n  "))
    local hi = meta["header-includes"]
    if hi == nil then
      meta["header-includes"] = pandoc.MetaList({ pandoc.MetaBlocks({ block }) })
    elseif hi.t == "MetaList" then
      hi:insert(pandoc.MetaBlocks({ block }))
    else
      meta["header-includes"] = pandoc.MetaList({ hi, pandoc.MetaBlocks({ block }) })
    end
  end

  doc.meta = meta
  return doc
end
