# 082 · Grid Stagger — 格狀擴散

Cells scale in waves outward from the center

- Component: Background · Ambience (`bg`)
- Timing: Loop · Idle
- Tech: GSAP
- Uses: Background Decoration
- Style / keywords: 
- Tag: Grid stagger
- Example text: "Motion" (stage background: acc)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Grid Stagger (格狀擴散)" motion effect: The same character is arranged in a 10×5 grid, shrinking, rotating, and fading in waves outward from the center, then enlarging and rotating back inward from the edges, forming a ripple. (GSAP: stagger { grid: [5,10], from: "center" / "edges", amount: 1 })
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage acc fx82">`, preview text "Motion". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Grid Stagger".

### JavaScript — `FX[82]` from `site/fx.js`

```js
82(s,x){const g=el('div','gg');const ch=chars(x)[0];for(let i=0;i<50;i++){const e=el('span');e.textContent=ch;g.append(e)}s.append(g);const c=g.children;
  gsap.timeline({repeat:-1}).to(c,{scale:.2,rotation:180,opacity:.3,duration:.7,ease:'power2.inOut',stagger:{grid:[5,10],from:'center',amount:1}}).to(c,{scale:1,rotation:360,opacity:1,duration:.7,ease:'power2.inOut',stagger:{grid:[5,10],from:'edges',amount:1}}).set(c,{rotation:0})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx82` rules from `site/fx.css`

_No dedicated `.fx82` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #82
