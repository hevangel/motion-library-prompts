# 226 · Pulse Rings — 同心圓擴散

A center point pulses regularly, and rings expand outward one after another and fade out

- Component: Background · Ambience (`bg`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Background Decoration, Emphasis, App Interface
- Style / keywords: Concentric Circles Expand Pulse Radar Sound Waves Live Location Signal Pulse Rings Ripple Radar Signal Live Background Atmosphere
- Tag: CSS keyframes
- Example text: "Live" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Pulse Rings (同心圓擴散)" motion effect: At the center of the screen is a solid dot that gently pulses regularly; from its position, thin rings continuously expand outward one after another, growing larger and gradually fading away, with multiple rings offset in time to form continuous ripples, like radar, sound waves, or a "live" signal; a short label can be placed on the center dot. (CSS: 3-4 rings share the same keyframes: scale 0.15 to 1.25, opacity 0.9 to 0, evenly offset with negative animation-delay; the center dot uses another scale keyframes)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx226">`, preview text "Live". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Pulse Rings".

### JavaScript — `FX[226]` from `site/fx.js`

```js
226(s,x){const w=el('div','abs bga-pr');for(let i=0;i<4;i++){const r=el('i');r.style.animationDelay=(-i).toFixed(1)+'s';w.append(r)}w.append(el('b'));s.append(w);const t=T(x,Math.min(9,44/chars(x).length));t.classList.add('bga-pt');s.append(t)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx226` rules from `site/fx.css`

_No dedicated `.fx226` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #226
