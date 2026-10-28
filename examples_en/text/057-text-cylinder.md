# 057 · Text Cylinder — 圓柱

Text cylinders rotate in opposite directions

- Component: Text (`text`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Logo · Brand
- Style / keywords: 3D Spatial Rotation
- Tag: 3D·Logo
- Example text: "Spin Around" (stage background: cream)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Text Cylinder (圓柱)" motion effect: Three 3D cylinders made of text (the same character ringing a full circle), rotating along a horizontal axis, adjacent cylinders in opposite directions, the middle one in an accent color. About 4 seconds per revolution, with a three-dimensional logo feel.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage cream fx57">`, preview text "Spin Around". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Text Cylinder".

### JavaScript — `FX[57]` from `site/fx.js`

```js
57(s,x){const w=el('div','w');chars(x).slice(0,3).forEach((c,k)=>{const cy=el('div','cy'+(k%2?' rev':''));for(let i=0;i<10;i++){const e=el('span');e.textContent=c;e.style.setProperty('--a2',i*36+'deg');cy.append(e)}w.append(cy)});s.append(w)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx57` rules from `site/fx.css`

```css
.fx57 .w{display:flex;gap:9cqw;transform-style:preserve-3d}
.fx57 .cy{position:relative;width:9cqw;height:9cqw;transform-style:preserve-3d;animation:cyl 4s linear infinite}
.fx57 .cy.rev{animation-direction:reverse}
.fx57 .cy span{position:absolute;inset:0;display:grid;place-items:center;font-weight:900;font-size:8cqw;color:#111;backface-visibility:hidden;transform:rotateX(var(--a2)) translateZ(13cqw)}
.fx57 .cy:nth-child(2) span{color:var(--a)}
@keyframes cyl{to{transform:rotateX(360deg)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #57
