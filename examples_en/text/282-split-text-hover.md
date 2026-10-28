# 282 · Split Text Hover — 上下切開文字

On hover, a title is cut along its horizontal midline into upper and lower halves that offset in opposite directions, revealing a line of small text in the middle

- Component: Text (`text`)
- Timing: Hover · Click
- Tech: CSS
- Uses: Headline · Hero, Emphasis
- Style / keywords: Cut Apart Split Top Bottom Offset Title clip-path Split Text Slice Hover Reveal hover Hovering Hover Over
- Tag: clip-path
- Example text: "SPLIT" (stage background: dark)
- Added: 2026-10-20

**AI prompt (English copy format):**

```text
"Split Text Hover (上下切開文字)" motion effect: A large title, which when the mouse hovers is cut along the text's horizontal midline into upper and lower halves: the upper half offsets to the upper left, the lower half offsets to the lower right (about 0.5 seconds, easing in and out), and in the gap that cracks open between the two halves, a line of small text (for example OPEN) unfolds vertically and fades in; when moving away the two halves rejoin. (CSS: the same text stacked in two layers, one layer clip-path: inset(0 0 50% 0) showing only the top half, the other inset(50% 0 0 0) showing only the bottom half, on :hover each transforms and displaces in the opposite direction)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx282">`, preview text "SPLIT". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Split Text Hover".

### JavaScript — `FX[282]` from `site/fx.js`

```js
282(s,x,card){const w=el('div','ho-sp');w.style.fontSize=Math.min(15,64/chars(x).length)+'cqw';['up','dn','m'].forEach(k=>{const d=el('span','ho-'+k);d.textContent=k==='m'?'':x;w.append(d)});w.querySelector('.ho-m').textContent='OPEN';s.append(w);autoHover(w,[w],card,1500)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx282` rules from `site/fx.css`

_No dedicated `.fx282` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #282
