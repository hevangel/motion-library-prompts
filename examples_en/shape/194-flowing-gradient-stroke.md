# 194 · Flowing Gradient Stroke — 漸層光流線條

A gradient flows continuously along a line, and a point of light travels around the line

- Component: Shapes · SVG (`shape`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Background Decoration, Logo · Brand
- Style / keywords: gradient line flow light point comet infinity symbol Gradient Stroke Flow Comet Infinity Loop SVG graphic
- Tag: SVG gradient
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Flowing Gradient Stroke (漸層光流線條)" motion effect: A closed, infinity-symbol-shaped curve. The line itself is a multicolored gradient, and the gradient flows continuously along the direction of the line; at the same time a small, bright point of light travels around the line like a comet, with a slight glow. Suitable for brand decoration or a tech-feel background. (SVG: linearGradient set to gradientUnits="userSpaceOnUse", spreadMethod="repeat", animate the gradientTransform translation with animateTransform; for the point of light use a second identical path with a stroke-dasharray of one short solid segment, and change stroke-dashoffset with keyframes)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx194">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Flowing Gradient Stroke".

### JavaScript — `FX[194]` from `site/fx.js`

```js
194(s){const id='gs'+Math.random().toString(36).slice(2),P='M20,45 C20,10 70,10 80,45 S140,80 140,45 S100,10 80,45 S20,80 20,45 Z';
  s.insertAdjacentHTML('beforeend',`<svg class="gfl" viewBox="0 0 160 90"><defs><linearGradient id="${id}" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="160" y2="0" spreadMethod="repeat"><stop offset="0" stop-color="#7c5cff"/><stop offset=".33" stop-color="#00c8ff"/><stop offset=".66" stop-color="#ff4fd8"/><stop offset="1" stop-color="#7c5cff"/><animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="160 0" dur="2.4s" repeatCount="indefinite"/></linearGradient></defs><path class="base" d="${P}" stroke="url(#${id})"/><path class="cmt" d="${P}"/></svg>`)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx194` rules from `site/fx.css`

_No dedicated `.fx194` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #194
