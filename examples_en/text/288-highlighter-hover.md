# 288 · Highlighter Hover — 螢光筆劃記

When hovering over key words in a paragraph, a stroke like a highlighter pen sweeps behind them from left to right

- Component: Text (`text`)
- Timing: Hover · Click
- Tech: CSS
- Uses: Emphasis
- Style / keywords: Highlighter Mark Highlighting highlight Key Point Highlighter Marker Hover Emphasis Text hover Hovering Hover Over
- Tag: background-size
- Example text: "Good Design Is Easy To Grasp At A Glance" (stage background: dark)
- Added: 2026-10-20

**AI prompt (English copy format):**

```text
"Highlighter Hover (螢光筆劃記)" motion effect: Several key words in a paragraph of text; when the mouse hovers over them, behind them a color block with a slight slant, a little lower than the text's midline, sweeps quickly like a highlighter pen from left to right, and the text color inverts at the same time to stay readable; when moving away the color block retracts. About 0.55 seconds. (CSS: the mark element's background uses linear-gradient to draw a color band with a slanted edge, background-size transitions from 0% to 100%, background-position set lower so it looks like a hand-drawn highlighter)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx288">`, preview text "Good Design Is Easy To Grasp At A Glance". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Highlighter Hover".

### JavaScript — `FX[288]` from `site/fx.js`

```js
288(s,x,card){const p=el('p','ho-hl');const ws=words(x);p.innerHTML=ws.map((t,i)=>i%2?`<mark></mark>`:'<span></span>').join(' ');[...p.children].forEach((c,i)=>c.textContent=ws[i]);s.append(p);autoHover(p,[...p.querySelectorAll('mark')],card,1100)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx288` rules from `site/fx.css`

_No dedicated `.fx288` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #288
