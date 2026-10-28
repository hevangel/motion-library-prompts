# 011 · Letter Rain — 文字雨

Text falls like rain

- Component: Background · Ambience (`bg`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Background Decoration
- Style / keywords: Flowing Background
- Tag: Fantasy · Background
- Example text: "あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろ" (stage background: cream, fixed text)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Letter Rain (文字雨)" motion effect: The entire block's background is covered with vertical columns of kana text falling continuously from top to bottom like rain, each column at a different speed (about 3–5 seconds to fall), a few columns in an accent color and the rest in low-contrast tones, for a fantastical background feel.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage cream fx11">`, preview text "あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろ". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Letter Rain".

### JavaScript — `FX[11]` from `site/fx.js`

```js
11(s,x){s.classList.add('fx11');const pool=chars(x);for(let i=0;i<13;i++){const c=el('div','col'+(Math.random()<.25?' a':''));let str='';for(let j=0;j<12;j++)str+=pool[Math.floor(Math.random()*pool.length)];c.textContent=str;c.style.left=(i*7.8+1)+'%';const d=rnd(2.8,5.5);c.style.animationDuration=d+'s';c.style.animationDelay=-rnd(0,d)+'s';s.append(c)}}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx11` rules from `site/fx.css`

```css
.fx11 .col{position:absolute;top:0;writing-mode:vertical-rl;font-weight:700;font-size:5.4cqw;line-height:1.1;letter-spacing:.1em;animation:rain linear infinite;color:#222}
.fx11 .col.a{color:var(--a)}
.fx11{container-type:size}
@keyframes rain{from{transform:translateY(-100%)}to{transform:translateY(110cqh)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #11
