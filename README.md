# motion-library

Clone of the KittenJam **Motion Library 動態收藏** — every AI prompt and every
animated example extracted from
<https://kittenjam-motion-library.vercel.app>.

**▶ Live on GitHub Pages: <https://hevangel.github.io/motion-library-prompts/>**
— the animated demo runs at
<https://hevangel.github.io/motion-library-prompts/site/> (中文 / EN toggle
included; English directly at
<https://hevangel.github.io/motion-library-prompts/site/?lang=en>).

> Source credit: collected and curated by **Hannah** (UI/UX Designer,
> [portfolio](https://hannahchao-portfolio.vercel.app/)). Per the source
> site's footer, the names and descriptions are the original author's
> curation and the preview animations are recreations, provided for personal
> reference and learning. This repo preserves that attribution.

## What's inside — 327 effects

Extracted 2026-10-28. The source numbers its effects 1–331; ids
**225, 259, 300 and 303 do not exist on the source site**, so 327 is the
complete set.

| File / folder | Contents |
|---|---|
| [`prompts.md`](prompts.md) | The whole catalog in one readable document, grouped by component — names (中文 + English), description, timing, tech, uses, example text, and the full AI prompt for all 327 effects. |
| [`prompts.json`](prompts.json) | The same catalog as structured data, including each effect's example JavaScript (`FX[id]`) and direct CSS. Start here for programmatic use. |
| [`prompts.csv`](prompts.csv) | Flat table version (327 rows) for spreadsheets. |
| [`examples/`](examples/README.md) | One file per effect, grouped by component (e.g. [`examples/text/001-lightning-strike.md`](examples/text/001-lightning-strike.md)): full prompt + preview settings + its own animated-example code. |
| [`site/`](site/README.md) | A runnable copy of the original site — open it to see every example animated live, with search and filters. |
| [`tools/extract.py`](tools/extract.py) | The extractor that produced all of the above. Re-run it to refresh from the live site. |

Every prompt is stored exactly as the site's 「複製 AI 提示詞」 button copies
it: `「<中文名>（<English>）」動態效果：<prompt>` plus the site's standard
palette line 「配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。」
The raw prompt without that wrapper is in the `prompt` field of
`prompts.json` / `prompts.csv`.

## English version

The original is in Chinese; a full English version was added 2026-10-28:

| File / folder | Contents |
|---|---|
| [`prompts_en.md`](prompts_en.md) / [`prompts_en.json`](prompts_en.json) / [`prompts_en.csv`](prompts_en.csv) | The whole catalog in English — translated description, prompt, tag, style keywords and preview text for all 327 effects (Chinese fields kept alongside for reference). |
| [`examples_en/`](examples_en/README.md) | All 327 example files regenerated in English, mirroring `examples/`. |
| [`translations/en.json`](translations/en.json) | The translation source data (`desc_en`, `prompt_en`, `tag_en`, `style_en`, `txt_en` per effect) that the English files and the site toggle are built from. |
| [`tools/build_en.py`](tools/build_en.py) | Builds all of the above plus `site/data_en.js`, and injects the toggle hooks into `site/index.html`. |

**Language toggle on the site:** the `site/` version has a **中文 / EN**
button at the top. It switches everything — page UI, component/timing/use
labels, card names, descriptions and tags, search (both languages stay
searchable), the animated previews' sample text, and the prompt the copy
button produces:

```text
"<English name> (<中文名>)" motion effect: <English prompt>
Colors: please match the website's existing theme colors and style
yourself; do not specify any additional colors.
```

Chinese is the default; the choice is remembered (localStorage) and can be
forced with `?lang=en` / `?lang=zh`. Three preview texts stay in CJK by
design — they are glyph sets, not words (#11 hiragana set, #28 four-season
characters, #38 mosaic kanji). 50 effects have no preview text and 22 have
no style keywords in the original; their English fields are empty too.

## Breakdown

By component （元件）:

| Component | Count |
|---|---:|
| 文字 Text | 105 |
| 卡片・群組 Card / Group | 39 |
| 版面・頁面 Layout / Page | 37 |
| 背景・氛圍 Background | 36 |
| 圖形・SVG Shape / SVG | 35 |
| 按鈕 Button | 21 |
| 圖片・媒體 Media | 21 |
| 表單・控制項 Control | 17 |
| 游標 Cursor | 16 |

By technology: CSS 194 · GSAP 119 · Canvas 14

## Run the examples

Live: <https://hevangel.github.io/motion-library-prompts/site/> — or locally:

```bash
cd site
python3 -m http.server 8000
# open http://localhost:8000
```

GSAP and web fonts load from CDNs, so the demo needs an internet connection.
See [`site/README.md`](site/README.md) for notes on the copy and the
language toggle.

## Re-extract / refresh

```bash
python3 tools/extract.py            # fetch the live site and rebuild everything
python3 tools/extract.py --local DIR  # rebuild from a previously saved copy
python3 tools/build_en.py           # then rebuild the English version + toggle data
```

(`extract.py` restores `site/` to the verbatim original; `build_en.py`
re-injects the language-toggle hooks into `site/index.html` afterwards.)

The extractor parses `data.js` (`ITEMS`), pulls each effect's `FX[id]`
function out of `fx.js` (brace-balanced, string-aware), and collects the
direct `.fx<id>` rules plus their referenced `@keyframes` from `fx.css`.
Effects whose styling lives in the shared category CSS (prefixes `ly-`,
`kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`,
`pg-`, `sv-`) say so in their example file — the full stylesheet is in
`site/fx.css`.

## Notes

- The original page's 「我要投稿」 submission form was **removed from this
  clone** (owner's decision, 2026-10-28): it posted through FormSubmit to
  the original author's email, and this clone does not collect
  submissions. `tools/build_en.py` re-applies the removal (button, dialog,
  its CSS, and the FormSubmit logic in `app.js`) after every
  `extract.py` refresh.
- `site/tracking.js` and the `/_vercel/insights/` script tag are the original
  site's analytics plumbing; they are inert outside Vercel.
