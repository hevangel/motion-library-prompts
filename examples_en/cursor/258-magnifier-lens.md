# 258 · Magnifier Lens — 放大鏡游標

The cursor becomes a round magnifying glass, and the content inside the lens is shown enlarged

- Component: Cursor (`cursor`)
- Timing: Hover · Click
- Tech: CSS
- Uses: UI Interaction
- Style / keywords: Magnifying Glass Magnify Lens Details Product Magnifier Lens Zoom Loupe Cursor Product Cursor Mouse
- Tag: JS + CSS
- Example text: "Magnified View" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Magnifier Lens (放大鏡游標)" motion effect: The cursor becomes a round magnifying glass with a border and shadow, and inside the lens the content below the cursor is displayed enlarged about 2.2 times; when moving, the lens content shifts in sync so small text or product details can be seen clearly. (JS + CSS: place a copy of the content inside the lens, set to the same width and height as the original content, transform-origin: 0 0, transform = translate(radius − cursor x × magnification, radius − cursor y × magnification) scale(magnification); the lens has border-radius: 50%, overflow: hidden, pointer-events: none)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx258">`, preview text "Magnified View". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Magnifier Lens".

### JavaScript — `FX[258]` from `site/fx.js`

```js
258(s,x,card){const l=el('div','abs cr-mg');const base=el('div','abs gl cr-mb');base.append(T(x,Math.min(9,40/chars(x).length)));const sm=el('small','cr-fine');sm.textContent='細節放大看得更清楚 · Details matter';base.append(sm);
  const lens=el('div','cr-ln');const inner=base.cloneNode(true);inner.classList.add('cr-li');lens.append(inner);l.append(base,lens);s.append(l);const Z=2.2;
  vpointer(l,card,(px,py)=>{const R=lens.offsetWidth/2;lens.style.transform=`translate(${px-R}px,${py-R}px)`;inner.style.width=l.offsetWidth+'px';inner.style.height=l.offsetHeight+'px';inner.style.transform=`translate(${R-px*Z}px,${R-py*Z}px) scale(${Z})`})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx258` rules from `site/fx.css`

_No dedicated `.fx258` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #258
