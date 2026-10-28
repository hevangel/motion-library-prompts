# 016 · Circle Text — 圓環文字

Rings of text rotate in opposite directions

- Component: Text (`text`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Logo · Brand, Background Decoration
- Style / keywords: 3D Spatial Rotation
- Tag: Logo · Hypnotic
- Example text: "CIRCLE TEXT ✦ " (stage background: dark, fixed text)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Circle Text (圓環文字)" motion effect: Two rings of circularly arranged text: the outer ring rotates slowly clockwise and the inner ring rotates faster counterclockwise, with the inner and outer rings distinguished by different tones. The outer ring takes about 9 seconds per revolution and the inner ring about 6 seconds, with a hypnotic logo feel.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx16">`, preview text "CIRCLE TEXT ✦ ". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Circle Text".

### JavaScript — `FX[16]` from `site/fx.js`

```js
16(s,x){s.append(ringOf(x.repeat(Math.max(1,Math.round(28/chars(x).length))),18,4,'cw'),ringOf(x.repeat(Math.max(1,Math.round(18/chars(x).length))),11,3.4,'ccw'))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx16` rules from `site/fx.css`

```css
.fx16 .ring2.ccw span{color:var(--a)}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #16
