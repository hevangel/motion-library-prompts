# 038 · Text Mosaic — 字體樣本

Different fonts light up in sequence

- Component: Text (`text`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Background Decoration
- Style / keywords: Textured Fill
- Tag: Font Specimen · Design
- Example text: "愛夢光風花月海空" (stage background: acc, fixed text)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Text Mosaic (字體樣本)" motion effect: 8 characters are arranged in a 4×2 grid, each cell using a different font (sans-serif, serif, dot-matrix, rounded, brush, and so on), lighting up inverted and enlarging slightly one cell at a time in sequence, then dimming back down. About 3.2 seconds per cycle.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage acc fx38">`, preview text "愛夢光風花月海空". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Text Mosaic".

### JavaScript — `FX[38]` from `site/fx.js`

```js
38(s,x){const F=['"Noto Sans JP";font-weight:900','"Noto Serif JP";font-weight:900','"DotGothic16"','"Zen Maru Gothic";font-weight:700','"Yuji Syuku"','"Rampart One"','"Reggae One"','"Kaisei Decol";font-weight:700'];const g=el('div','g');chars(x).slice(0,8).forEach((c,i)=>{const e=el('span');e.textContent=c;e.style.cssText+=`;font-family:${F[i%8]}`;e.style.setProperty('--i',i);g.append(e)});s.append(g)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx38` rules from `site/fx.css`

```css
.fx38 .g{display:grid;grid-template-columns:repeat(4,1fr);gap:1.6cqw;width:88%}
.fx38 .g span{font-size:11cqw;line-height:1.5;text-align:center;border-radius:1.4cqw;background:#0000000f;color:#6b4a00;animation:lit 3.2s calc(var(--i)*.4s) infinite}
@keyframes lit{0%,6%{background:#fff;color:#111;transform:scale(1.08)}22%,100%{background:#0000000f;color:#6b4a00;transform:none}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #38
