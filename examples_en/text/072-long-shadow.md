# 072 · Long Shadow — 長陰影

A long, long shadow turns a full circle

- Component: Text (`text`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Logo · Brand
- Style / keywords: Textured Fill
- Tag: Flat Style
- Example text: "Light and Shadow" (stage background: dark)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Long Shadow (長陰影)" motion effect: A very long flat shadow trails behind the text, the shadow's direction continuously rotating a full circle around the text. About 7 seconds per revolution, in a flat design style.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx72">`, preview text "Light and Shadow". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Long Shadow".

### JavaScript — `FX[72]` from `site/fx.js`

```js
72(s,x,card){const t=T(x);s.append(t);ticks.set(card,tt=>{const a=tt*.9;const fs=parseFloat(getComputedStyle(t).fontSize)||40;const st=fs/40;let sh=[];for(let k=1;k<=34;k++)sh.push(`${(Math.cos(a)*k*st).toFixed(1)}px ${(Math.sin(a)*k*st).toFixed(1)}px 0 ${k<3?'#f47fae':'#c4527f'}`);t.style.textShadow=sh.join(',')})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx72` rules from `site/fx.css`

```css
.fx72 .t{color:#fff}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #72
