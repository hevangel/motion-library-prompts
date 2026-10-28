# 088 · Draw Highlight — 手繪圈重點

A hand-drawn circle and underline are drawn in

- Component: Shapes · SVG (`shape`)
- Timing: Entrance
- Tech: GSAP
- Uses: Emphasis
- Style / keywords: 
- Tag: DrawSVG
- Example text: "Key Point Here" (stage background: cream)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Draw Highlight (手繪圈重點)" motion effect: A hand-drawn-style line draws a circle around the key text, then draws an underline beneath it; after a pause, the lines retract in the direction of their starting point, with round line caps. (GSAP: DrawSVGPlugin, drawSVG "0%"→"100%", then to "100% 100%")
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage cream fx88">`, preview text "Key Point Here". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Draw Highlight".

### JavaScript — `FX[88]` from `site/fx.js`

```js
88(s,x){const w=el('div','dr');w.append(T(x,Math.min(13,56/chars(x).length)));w.insertAdjacentHTML('beforeend','<svg viewBox="0 0 200 100" preserveAspectRatio="none"><path d="M150,20 C120,4 48,6 24,30 C2,54 30,88 100,90 C172,92 198,66 188,42 C180,22 142,10 104,12"/><path d="M34,104 C74,98 130,100 172,103"/></svg>');s.append(w);const ps=w.querySelectorAll('path');
  gsap.timeline({repeat:-1,repeatDelay:.4}).fromTo(ps,{drawSVG:'0%'},{drawSVG:'100%',duration:1,ease:'power2.inOut',stagger:.6}).to(ps,{drawSVG:'100% 100%',duration:.6,ease:'power2.in',stagger:.1},'+=1.3')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx88` rules from `site/fx.css`

_No dedicated `.fx88` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #88
