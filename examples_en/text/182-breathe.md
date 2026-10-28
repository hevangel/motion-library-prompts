# 182 · Breathe — 呼吸

An element slowly scales up and down, cycling like breathing

- Component: Text (`text`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Emphasis, Logo · Brand
- Style / keywords: breathing pulse scale up and down idle Pulse Breathing Idle Canva style Canva Breathe breathing presentation social post animation
- Tag: CSS keyframes
- Example text: "Deep Breath" (stage background: cream)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Breathe (呼吸)" motion effect: Text or an element continuously scales up slowly to about 1.07x and then back down, while its opacity fluctuates slightly between 0.82 and 1, one cycle taking about 3.2 seconds, easing in and out at both ends, like breathing. Suitable for emphasizing a key point or an idle state. (CSS: keyframes 0%/100% scale(1), 50% scale(1.07), ease-in-out, infinite)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage cream fx182">`, preview text "Deep Breath". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Breathe".

### JavaScript — `FX[182]` from `site/fx.js`

```js
182(s,x){const w=el('div','brw');w.append(T(x,Math.min(12,52/chars(x).length)));s.append(w)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx182` rules from `site/fx.css`

_No dedicated `.fx182` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #182
