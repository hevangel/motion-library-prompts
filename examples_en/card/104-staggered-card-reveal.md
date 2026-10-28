# 104 · Staggered Card Reveal — 卡片依序浮現

A group of cards floats up in sequence from top-left to bottom-right, going from blurry to clear

- Component: Cards · Groups (`card`)
- Timing: Entrance, Exit
- Tech: GSAP
- Uses: UI Interaction, Transitions
- Style / keywords: Card Group List Entrance In Sequence Staggered Emerge Fade In Stagger Fade Up Grid Reveal List Entrance
- Tag: Grid stagger
- Example text: "Brand Website App Poster Packaging Illustration" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Staggered Card Reveal (卡片依序浮現)" motion effect: Work cards in 3 columns × 2 rows (a thumbnail on top, a title and two lines of text below); on entrance, each card floats up from a state 30px below, at 95% size, blurred and transparent, becoming clear, in a sequence staggered diagonally from top-left to bottom-right (about 0.6 seconds in total); the thumbnail, title and text lines inside each card then catch up one by one with a slight extra delay; after a pause, they fade out upward in reverse, starting from the last card. Ease-out (power3.out). (GSAP: stagger { grid:[2,3], from:"start", amount:0.6 }, fromTo y / opacity / scale / filter:blur; on a real site, pair this with ScrollTrigger so it plays when scrolled into view, or use ScrollTrigger.batch to bring lists in in batches)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx104">`, preview text "Brand Website App Poster Packaging Illustration". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Staggered Card Reveal".

### JavaScript — `FX[104]` from `site/fx.js`

```js
104(s,x){const g=el('div','cg');const ws=words(x);for(let i=0;i<6;i++){const c=el('div','cgc');c.innerHTML='<i class="th"></i><b></b><span class="ln"></span><span class="ln s"></span>';c.querySelector('b').textContent=ws[i%ws.length];c.querySelector('.th').style.background=GC[i%5];g.append(c)}s.append(g);
  const cs=g.children,inner=g.querySelectorAll('.th,b,.ln'),grid={grid:[2,3]};
  gsap.timeline({repeat:-1,repeatDelay:.4})
    .fromTo(cs,{y:30,opacity:0,scale:.94,filter:'blur(6px)'},{y:0,opacity:1,scale:1,filter:'blur(0px)',duration:.7,ease:'power3.out',stagger:{...grid,from:'start',amount:.6}})
    .fromTo(inner,{y:8,opacity:0},{y:0,opacity:1,duration:.4,ease:'power2.out',stagger:.02},'-=.65')
    .to(cs,{y:-16,opacity:0,duration:.4,ease:'power2.in',stagger:{...grid,from:'end',amount:.3}},'+=1.6')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx104` rules from `site/fx.css`

_No dedicated `.fx104` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #104
