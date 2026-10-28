# 007 · Text Kaleido — 文字萬花筒

Text rotates in a kaleidoscope

- Component: Text (`text`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Background Decoration, Logo · Brand
- Style / keywords: 3D Spatial Rotation
- Tag: Psychedelic · MV
- Example text: "Kaleido" (stage background: cream)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Text Kaleido (文字萬花筒)" motion effect: The same word is copied 12 times, arranged radially around a center point in the shape of a flower; the whole group keeps rotating slowly while each copy stretches outward and breathes back in at the same time, forming a kaleidoscope effect, with adjacent copies alternating between light and dark tones. One full rotation takes about 7 seconds.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage cream fx7">`, preview text "Kaleido". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Text Kaleido".

### JavaScript — `FX[7]` from `site/fx.js`

```js
7(s,x){const k=el('div','k');for(let i=0;i<12;i++){const sp=el('span');sp.innerHTML=`<span class="in">${x}</span>`;sp.style.transform=`rotate(${i*30}deg) translateY(-50%)`;k.append(sp)}s.append(k)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx7` rules from `site/fx.css`

```css
.fx7 .k{position:relative;width:1px;height:1px;animation:spin 7s linear infinite}
.fx7 .k span{position:absolute;left:0;top:0;font-weight:900;font-size:6cqw;transform-origin:0 0;white-space:nowrap;color:#2a3a12}
.fx7 .k span:nth-child(odd){color:#7a9a1c}
.fx7 .k .in{display:inline-block;animation:kpulse 2.4s ease-in-out infinite}
@keyframes kpulse{0%,100%{transform:translateX(2cqw)}50%{transform:translateX(8cqw)}}
@keyframes spin{to{transform:rotate(360deg)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #7
