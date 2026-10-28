# 062 · Split Flap — 翻牌

Flips into place like a station timetable

- Component: Text (`text`)
- Timing: Switch
- Tech: CSS
- Uses: Numbers & Data
- Style / keywords: Text Switching
- Tag: Retro·Station
- Example text: "On Time" (stage background: dark)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Split Flap (翻牌)" motion effect: Each character sits in a split-flap cell (with a divider line in the middle) and, like a station timetable, rapidly flips through many random characters, stopping in sequence from left to right on the correct character; after lingering, it flips again. The flipping is fast, with everything settled in about 1.5 seconds.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx62">`, preview text "On Time". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Split Flap".

### JavaScript — `FX[62]` from `site/fx.js`

```js
62(s,x,card){const tg=chars(x).slice(0,6);const w=el('div','w');const cells=tg.map(()=>{const c=el('div','fl');c.innerHTML='<span></span>';w.append(c);return c});s.append(w);const pool=[...'準時延誤出發抵達東西南北甲乙丙丁一二三四五ABC0123'];let f=0;
  card._timers.push(setInterval(()=>{f=(f+1)%70;cells.forEach((c,i)=>{const stop=12+i*7;if(f<stop){c.firstChild.textContent=pool[Math.floor(Math.random()*pool.length)];c.classList.remove('f');void c.offsetWidth;c.classList.add('f')}else c.firstChild.textContent=tg[i]})},85))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx62` rules from `site/fx.css`

```css
.fx62 .w{display:flex;gap:1.2cqw}
.fx62 .fl{position:relative;width:15cqw;height:18cqw;background:#f4f4f0;color:#111;border-radius:1.2cqw;display:grid;place-items:center;font-weight:900;font-size:12cqw;line-height:1;overflow:hidden}
.fx62 .fl::after{content:"";position:absolute;left:0;right:0;top:50%;height:.3cqw;background:#2b2b2b}
.fx62 .fl.f span{animation:flap .09s}
@keyframes flap{from{transform:rotateX(70deg) scaleY(.6)}to{transform:none}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #62
