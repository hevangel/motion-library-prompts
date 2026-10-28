# 032 · Shuffle Letters — 洗牌重排

Text swaps positions, then lines up neatly

- Component: Text (`text`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Headline · Hero
- Style / keywords: Letter-by-Letter Motion
- Tag: Game · Puzzle
- Example text: "Shuffled" (stage background: dark)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Shuffle Letters (洗牌重排)" motion effect: Each character of the text swaps positions randomly with a little bounce and tilt; after shuffling several times in a row, it returns to its place and lines up neatly, pauses, then starts shuffling again. Each swap takes about 0.6 seconds, with a game-puzzle feel.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx32">`, preview text "Shuffled". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Shuffle Letters".

### JavaScript — `FX[32]` from `site/fx.js`

```js
32(s,x,card){const cs=chars(x),n=cs.length;const t=T(x);t.classList.add('w');t.style.width=(n*1.05)+'em';const sp=cs.map((c,i)=>{const e=el('span','c');e.textContent=c;t.append(e);return e});s.append(t);
  const place=o=>sp.forEach((e,i)=>{e.style.left=(o[i]*1.05)+'em';e.style.transform=o[i]===i?'none':`translateY(${(Math.random()-.5)*40}%) rotate(${(Math.random()-.5)*30}deg)`});
  const shuf=()=>{const a=[...Array(n).keys()];for(let i=n-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a};
  let step=0;place(shuf());card._timers.push(setInterval(()=>{step=(step+1)%7;place(step<4?shuf():[...Array(n).keys()])},600))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx32` rules from `site/fx.css`

```css
.fx32 .w{position:relative;height:1.2em}
.fx32 .c{position:absolute;top:0;transition:left .45s cubic-bezier(.5,1.6,.5,1),transform .45s}
.fx32 .c:nth-child(odd){color:var(--a)}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #32
