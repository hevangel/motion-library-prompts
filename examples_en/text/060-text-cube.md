# 060 · Text Cube — 方塊

A cube with text on four faces flips vertically

- Component: Text (`text`)
- Timing: Switch
- Tech: CSS
- Uses: Transitions, Numbers & Data
- Style / keywords: Text Switching
- Tag: Switching·3D
- Example text: "Spring Summer Fall Winter" (stage background: cream)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Text Cube (方塊)" motion effect: A 3D cube with one character written on each of its four faces flips 90 degrees around a horizontal axis each time to switch to the next face, pausing after each flip, at a slightly tilted viewing angle, the cube with thick borders. About 1.5 seconds per face.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage cream fx60">`, preview text "Spring Summer Fall Winter". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Text Cube".

### JavaScript — `FX[60]` from `site/fx.js`

```js
60(s,x){const c=el('div','cube');const cs=chars(x);for(let i=0;i<4;i++){const e=el('span');e.textContent=cs[i%cs.length];e.style.setProperty('--a2',-i*90+'deg');c.append(e)}s.append(c)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx60` rules from `site/fx.css`

```css
.fx60 .cube{position:relative;width:24cqw;height:24cqw;transform-style:preserve-3d;animation:cube 6s infinite}
.fx60 .cube span{position:absolute;inset:0;display:grid;place-items:center;font-weight:900;font-size:16cqw;background:var(--a);color:#111;border:.4cqw solid #111;transform:rotateX(var(--a2)) translateZ(12cqw)}
@keyframes cube{0%,18%{transform:rotateX(-18deg) rotateY(-24deg) rotateX(0)}25%,43%{transform:rotateX(-18deg) rotateY(-24deg) rotateX(90deg)}50%,68%{transform:rotateX(-18deg) rotateY(-24deg) rotateX(180deg)}75%,93%{transform:rotateX(-18deg) rotateY(-24deg) rotateX(270deg)}100%{transform:rotateX(-18deg) rotateY(-24deg) rotateX(360deg)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #60
