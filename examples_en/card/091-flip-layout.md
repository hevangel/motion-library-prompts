# 091 · Flip Layout — 版面重排

Smoothly rearranges between a grid and a single row

- Component: Cards · Groups (`card`)
- Timing: Switch
- Tech: GSAP
- Uses: UI Interaction, Transitions
- Style / keywords: 
- Tag: Flip
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Flip Layout (版面重排)" motion effect: 8 blocks switch between two layouts — a "4×2 grid" and "a single row" — while their order is randomly shuffled at the same time; each block smoothly slides to its new position and new size. (GSAP: Flip.getState to record → change the class and DOM order → Flip.from to tween)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx91">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Flip Layout".

### JavaScript — `FX[91]` from `site/fx.js`

```js
91(s,x,card){const g=el('div','fg');for(let i=0;i<8;i++){const e=el('div','ft');e.textContent=i+1;e.style.background=GC[i%4];g.append(e)}s.append(g);let k=0;
  card._timers.push(setInterval(()=>{const ts=[...g.children];const st=Flip.getState(ts);g.classList.toggle('alt',++k%2===1);gsap.utils.shuffle(ts).forEach(e=>g.append(e));Flip.from(st,{duration:.8,ease:'power3.inOut',stagger:.03})},1900))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx91` rules from `site/fx.css`

_No dedicated `.fx91` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #91
