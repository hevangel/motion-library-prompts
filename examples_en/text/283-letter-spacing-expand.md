# 283 · Letter Spacing Expand — 字距展開

On hover, letter spacing slowly pulls open and font weight becomes bolder, like taking a deep breath

- Component: Text (`text`)
- Timing: Hover · Click
- Tech: CSS
- Uses: UI Interaction, Emphasis
- Style / keywords: Letter Spacing Pull Open Font Weight Breathing Menu Navigation Letter Spacing Tracking Expand Weight Hover Menu hover Hovering Hover Over
- Tag: letter-spacing
- Example text: "ABOUT WORK CONTACT" (stage background: dark)
- Added: 2026-10-20

**AI prompt (English copy format):**

```text
"Letter Spacing Expand (字距展開)" motion effect: Text in a navigation bar or large menu: when the mouse hovers over an item, the letter spacing smoothly pulls open from 0 to about 0.35em, the font weight changes from thin to bold, and the text becomes clearer, expanding like taking a deep breath; when moving away it retracts. About 0.5 seconds, with a decelerating curve. (CSS: transition letter-spacing and font-weight (using a variable font gives the smoothest effect), :hover changes the values)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx283">`, preview text "ABOUT WORK CONTACT". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Letter Spacing Expand".

### JavaScript — `FX[283]` from `site/fx.js`

```js
283(s,x,card){const ws=words(x).slice(0,3);const w=el('div','ho-ls');const its=ws.map(t=>{const d=el('div','ho-li');d.textContent=t;w.append(d);return d});s.append(w);autoHover(w,its,card,1100)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx283` rules from `site/fx.css`

_No dedicated `.fx283` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #283
