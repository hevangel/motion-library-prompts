# 069 · Outline Text — 空心字

Hollow text fills up line by line

- Component: Background · Ambience (`bg`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Background Decoration
- Style / keywords: Flowing Background
- Tag: Texture·MV
- Example text: "Storm and Fury" (stage background: dark)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Outline Text (空心字)" motion effect: The frame is covered with multiple lines of repeated outlined hollow text, each line slowly shifting horizontally in a different direction, and filling with color line by line from top to bottom before returning to hollow. About 3.2 seconds per cycle, with a textured MV feel.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx69">`, preview text "Storm and Fury". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Outline Text".

### JavaScript — `FX[69]` from `site/fx.js`

```js
69(s,x){const r=el('div','rows');for(let i=0;i<5;i++){const m=mqRow(rep(x+'・',6),11,10+i*2,i%2);m.className+=' row';m.style.setProperty('--i',i);r.append(m)}s.append(r)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx69` rules from `site/fx.css`

```css
.fx69 .rows{position:absolute;inset:-4% 0;display:flex;flex-direction:column;justify-content:space-between}
.fx69 .row{font-weight:900;font-size:11cqw;line-height:1.05;-webkit-text-stroke:.25cqw var(--a);color:transparent;animation:ofill 3.2s calc(var(--i)*.35s) infinite}
@keyframes ofill{0%,8%{color:transparent}18%,60%{color:var(--a)}72%,100%{color:transparent}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #69
