# 138 · Wave Divider — 波浪分隔線

Multiple wave layers at the bottom of a section flow slowly at different speeds

- Component: Shapes · SVG (`shape`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Background Decoration, Transitions
- Style / keywords: Wave Divider Section Separator Water Wave Ocean Wave Wave Divider Section Separator Liquid
- Tag: SVG wave
- Example text: "Wave Divider" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Wave Divider (波浪分隔線)" motion effect: A wave shape separates two sections. The wave is made of 3 layers — the back layer paler and taller, the front layer more solid and lower — and the three layers flow slowly left and right at different speeds (about 6, 9, and 13 seconds per cycle), in not entirely the same direction, creating a sense of depth like water, looping seamlessly. (CSS: each layer is an SVG path 200% wide containing two full wavelengths, using a linear infinite animation of translateX(0 → -50%) for seamlessness; different layers are given different animation-duration and direction)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx138">`, preview text "Wave Divider". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Wave Divider".

### JavaScript — `FX[138]` from `site/fx.js`

```js
138(s,x){const W='M0,20 C25,8 25,8 50,20 C75,32 75,32 100,20 C125,8 125,8 150,20 C175,32 175,32 200,20 L200,40 L0,40 Z';s.append(T(x,Math.min(10,50/chars(x).length)));
  s.insertAdjacentHTML('beforeend',`<div class="wv">${[0,1,2].map(i=>`<svg viewBox="0 0 200 40" preserveAspectRatio="none" class="w${i}"><path d="${W}"/></svg>`).join('')}</div>`)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx138` rules from `site/fx.css`

```css
.fx138 .t{color:#fff;margin-bottom:16cqw}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #138
