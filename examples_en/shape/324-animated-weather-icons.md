# 324 · Animated Weather Icons — 天氣圖示動畫

A sunny sun slowly rotates, clouds drift, raindrops fall, and lightning flashes

- Component: Shapes · SVG (`shape`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: UI Interaction, App Interface, Numbers & Data
- Style / keywords: Weather Icons Sun Cloud Rain Lightning icon Weather Icons Animated Sun Cloud Rain Thunder Graphics SVG
- Tag: CSS keyframes
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-21

**AI prompt (English copy format):**

```text
"Animated Weather Icons (天氣圖示動畫)" motion effect: A set of weather icon cards: in the sunny one, the sun and its rays slowly rotate on their own; in the cloudy one, the clouds drift gently left and right; in the rainy one, raindrops continuously fall from below the cloud at staggered times and fade out; in the thunderstorm one, the lightning is dim most of the time and occasionally flashes twice quickly. The weather name is labeled below each icon. (SVG + CSS keyframes: the sun rotates, one revolution in 10 seconds; the clouds move back and forth with translateX; the raindrops use translateY + opacity with staggered animation-delay; the lightning flickers using keyframes with steps(1))
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx324">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Animated Weather Icons".

### JavaScript — `FX[324]` from `site/fx.js`

```js
324(s,x){const w=el('div','sv-wx');const L=[['晴','<g class="sun"><circle r="9"/>'+[...Array(8)].map((_,i)=>`<line x1="0" y1="-14" x2="0" y2="-19" transform="rotate(${i*45})"/>`).join('')+'</g>'],['多雲','<g class="sun s2"><circle cx="-6" cy="-6" r="7"/></g><path class="cl" d="M-14,8 A7,7 0 0 1 -9,-4 A9,9 0 0 1 8,-6 A7,7 0 0 1 14,8 Z"/>'],['雨','<path class="cl" d="M-14,2 A7,7 0 0 1 -9,-10 A9,9 0 0 1 8,-12 A7,7 0 0 1 14,2 Z"/>'+[-8,0,8].map((xx,i)=>`<line class="rd" style="--i:${i}" x1="${xx}" y1="7" x2="${xx-2}" y2="13"/>`).join('')],['雷','<path class="cl" d="M-14,0 A7,7 0 0 1 -9,-12 A9,9 0 0 1 8,-14 A7,7 0 0 1 14,0 Z"/><path class="bolt" d="M2,2 L-4,11 L1,11 L-3,19 L6,8 L1,8 L4,2Z"/>']];
  w.innerHTML=L.map(([l,g])=>`<div class="sv-wi"><svg viewBox="-22 -22 44 44">${g}</svg><span>${l}</span></div>`).join('');s.append(w)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx324` rules from `site/fx.css`

_No dedicated `.fx324` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #324
