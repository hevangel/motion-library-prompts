# 070 · Glitch Slices — 故障切片

Large text is cut into several offset slices

- Component: Text (`text`)
- Timing: Exit
- Tech: CSS
- Uses: Emphasis, Transitions
- Style / keywords: Dissipating Exit
- Tag: Impact·MV
- Example text: "Glitch" (stage background: acc)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Glitch Slices (故障切片)" motion effect: The large text is normally still, but occasionally it suddenly cuts into 6 horizontal slices, each slice offset randomly left or right with chromatic aberration (RGB split), flashing once before recovering, at an irregular frequency. The glitch flickers about every 0.1 seconds, with an impactful MV feel.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage acc fx70">`, preview text "Glitch". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Glitch Slices".

### JavaScript — `FX[70]` from `site/fx.js`

```js
70(s,x,card){const w=el('div','w');const base=T(x,22);w.append(base);const sl=[];for(let i=0;i<6;i++){const e=T(x,22);e.classList.add('sl');e.style.clipPath=`inset(${i*100/6}% 0 ${100-(i+1)*100/6}% 0)`;w.append(e);sl.push(e)}s.append(w);
  card._timers.push(setInterval(()=>{const g=Math.random()<.32;base.style.opacity=g?0:1;sl.forEach(e=>{e.style.transform=g?`translateX(${rnd(-9,9)}cqw)`:'none';e.style.color=g&&Math.random()<.4?'#fff':'#111';e.style.textShadow=g?'.8cqw 0 #3cf,-.8cqw 0 #f24':'none';e.style.opacity=g?1:0})},110))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx70` rules from `site/fx.css`

```css
.fx70 .w{position:relative}
.fx70 .t{color:#111}
.fx70 .sl{position:absolute;left:0;top:0;transition:none}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #70
