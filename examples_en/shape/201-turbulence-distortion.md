# 201 · Turbulence Distortion — SVG 濾鏡水波扭曲

Text continuously ripples and distorts as if seen through a water surface

- Component: Shapes · SVG (`shape`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Headline · Hero, Background Decoration
- Style / keywords: filter distortion water ripple liquid heat haze psychedelic SVG Filter Turbulence Displacement Distortion Liquid SVG graphic
- Tag: feTurbulence
- Example text: "Rippled Distortion" (stage background: dark)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Turbulence Distortion (SVG 濾鏡水波扭曲)" motion effect: A large title continuously ripples and distorts as if seen through a water surface or a heat haze. The distortion's texture and intensity change slowly; the text remains legible but has a liquid, psychedelic feel. (SVG filter: feTurbulence generates noise, feDisplacementMap displaces the source image according to the noise, use animate to cycle baseFrequency and scale between values; apply it to HTML elements with CSS filter:url(#id); watch performance, and avoid applying it to large areas or many elements)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx201">`, preview text "Rippled Distortion". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Turbulence Distortion".

### JavaScript — `FX[201]` from `site/fx.js`

```js
201(s,x){const id='tb'+Math.random().toString(36).slice(2);s.insertAdjacentHTML('beforeend',`<svg width="0" height="0" style="position:absolute"><filter id="${id}" x="-10%" y="-10%" width="120%" height="120%"><feTurbulence type="fractalNoise" baseFrequency="0.012 0.04" numOctaves="2" seed="3"><animate attributeName="baseFrequency" dur="6s" values="0.012 0.045;0.025 0.08;0.012 0.045" repeatCount="indefinite"/></feTurbulence><feDisplacementMap in="SourceGraphic" scale="20"><animate attributeName="scale" dur="3s" values="8;22;8" repeatCount="indefinite"/></feDisplacementMap></filter></svg>`);
  const t=T(x,Math.min(15,64/chars(x).length));t.classList.add('tbt');t.style.filter=`url(#${id})`;s.append(t)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx201` rules from `site/fx.css`

_No dedicated `.fx201` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #201
