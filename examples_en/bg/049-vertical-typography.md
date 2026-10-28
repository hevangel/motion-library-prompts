# 049 · Vertical Typography — 直書逆走

Vertical text flows in opposite directions

- Component: Background · Ambience (`bg`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Background Decoration
- Style / keywords: Flowing Background
- Tag: Eastern·Stillness and Motion
- Example text: "Silence" (stage background: acc)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Vertical Typography (直書逆走)" motion effect: Multiple columns of vertical text, thick and thin columns alternating, adjacent columns flowing in opposite directions — one up, one down — in a serif (Mincho) typeface. The large columns are slow (about 11 seconds), the small columns fast (about 6 seconds), an Eastern sense of stillness and motion.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage acc fx49">`, preview text "Silence". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Vertical Typography".

### JavaScript — `FX[49]` from `site/fx.js`

```js
49(s,x){const c=el('div','cols');for(let i=0;i<6;i++){const e=el('div','col'+(i%2?' rev':''));const w=i%2?'疾走':x;e.innerHTML=chars(rep(w+'　',8)).join('<br>');e.style.fontSize=(i%2?5:9)+'cqw';e.style.setProperty('--dur',(i%2?6:11)+'s');c.append(e)}s.append(c)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx49` rules from `site/fx.css`

```css
.fx49 .cols{position:absolute;inset:0;display:flex;justify-content:space-around;overflow:hidden}
.fx49 .col{align-self:flex-start;text-align:center;font-family:"Noto Serif JP",serif;font-weight:900;color:#111;line-height:1;white-space:nowrap;animation:mqv var(--dur) linear infinite}
.fx49 .col.rev{animation-direction:reverse}
@keyframes mqv{to{transform:translateY(-50%)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #49
