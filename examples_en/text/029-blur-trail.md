# 029 · Blur Trail — 殘影疾走

Races past trailing afterimages

- Component: Text (`text`)
- Timing: Entrance
- Tech: CSS
- Uses: Transitions
- Style / keywords: Flowing Background
- Tag: Speed · Racing
- Example text: "Racing" (stage background: dark)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Blur Trail (殘影疾走)" motion effect: The text rushes at high speed from outside the left of the screen into the center, leaning in italics, stops briefly, then rushes out to the right, dragging 4 layers of semi-transparent blurred afterimages behind it, while horizontal speed lines flash across the background. About 2.6 seconds per cycle, with a sense of racing speed.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx29">`, preview text "Racing". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Blur Trail".

### JavaScript — `FX[29]` from `site/fx.js`

```js
29(s,x){s.append(el('div','lines'));const w=el('div','w');for(let k=4;k>=1;k--){const g=T(x,20);g.classList.add('g');g.style.setProperty('--op',(.5/k).toFixed(2));g.style.animation=`dash 2.6s ${-0.035*k}s infinite cubic-bezier(.7,0,.3,1)`;w.append(g)}w.append(T(x,20));s.append(w)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx29` rules from `site/fx.css`

```css
.fx29 .w{position:relative}
.fx29 .t{animation:dash 2.6s infinite cubic-bezier(.7,0,.3,1);color:#fff}
.fx29 .g{position:absolute;left:0;top:0;color:var(--a);filter:blur(3px);opacity:var(--op)}
.fx29 .lines{position:absolute;inset:0;background:repeating-linear-gradient(0deg,transparent 0 9%,#ffffff10 9% 10%);animation:fl2 2.6s infinite}
@keyframes dash{0%{transform:translateX(-130cqw) skewX(-20deg)}45%{transform:translateX(0) skewX(-12deg)}55%{transform:translateX(0) skewX(0)}62%{transform:translateX(-2cqw)}100%{transform:translateX(140cqw) skewX(-20deg)}}
@keyframes fl2{0%,30%,60%,100%{opacity:0}40%,90%{opacity:1}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #29
