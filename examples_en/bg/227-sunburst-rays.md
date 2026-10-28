# 227 · Sunburst Rays — 旋轉光芒

Radial rays slowly rotate behind the title, brightest at the center and fading outward

- Component: Background · Ambience (`bg`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Headline · Hero, Emphasis, Background Decoration
- Style / keywords: Rays Radiate Sunlight Rotating Celebration Award Prize Draw Sunburst Rays Rotating God Rays Conic Background Atmosphere
- Tag: conic-gradient
- Example text: "WINNER" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Sunburst Rays (旋轉光芒)" motion effect: Behind the title is a ring of ray stripes radiating outward from the center; the whole ring slowly rotates at a speed of about 30 seconds per revolution, brightest at the center and gradually blending into the background outward, like the spotlight effect of an award, prize draw, or celebration scene. (CSS: repeating-conic-gradient draws the radial stripes and is enlarged beyond the container, keyframes rotate 360deg linear infinite; a radial-gradient layer on top makes the center bright and the edges dark)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx227">`, preview text "WINNER". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Sunburst Rays".

### JavaScript — `FX[227]` from `site/fx.js`

```js
227(s,x){s.append(el('div','abs bga-ray'),el('div','abs bga-rg'),T(x,Math.min(12,56/chars(x).length)))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx227` rules from `site/fx.css`

```css
.fx222 .t,.fx224 .t,.fx227 .t,.fx231 .t{color:#fff;z-index:1;text-shadow:0 .4cqw 2cqw #0006}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #227
