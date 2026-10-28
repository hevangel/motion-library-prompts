# 030 · Checker Words — 棋盤翻轉

Checkerboard text flips in a wave

- Component: Background · Ambience (`bg`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Background Decoration
- Style / keywords: Flowing Background
- Tag: Pattern · Background
- Example text: "Text" (stage background: acc, fixed text)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Checker Words (棋盤翻轉)" motion effect: The same character is arranged in a 10×4 checkerboard grid, with dark and light blocks alternating, flipping around the Y axis in sequence from top-left to bottom-right, forming a diagonal tile-flipping wave. About 2.6 seconds per cycle, with a patterned background feel.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage acc fx30">`, preview text "Text". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Checker Words".

### JavaScript — `FX[30]` from `site/fx.js`

```js
30(s,x){const g=el('div','g');for(let r=0;r<4;r++)for(let c=0;c<10;c++){const sp=el('span',(r+c)%2?'d':'l');sp.textContent=chars(x)[0];sp.style.setProperty('--d',c+r);g.append(sp)}s.append(g)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx30` rules from `site/fx.css`

```css
.fx30 .g{display:grid;grid-template-columns:repeat(10,1fr);gap:1cqw;padding:0 3cqw}
.fx30 .g span{font-weight:900;font-size:5.6cqw;line-height:1.4;text-align:center;border-radius:1cqw;animation:chk 2.6s calc(var(--d)*.07s) infinite}
.fx30 .g span.l{background:#111;color:var(--a)}
.fx30 .g span.d{background:#0002;color:#111}
@keyframes chk{0%,15%{transform:rotateY(0)}35%,65%{transform:rotateY(180deg)}85%,100%{transform:rotateY(360deg)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #30
