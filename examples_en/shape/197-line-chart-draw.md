# 197 · Line Chart Draw — 折線圖繪製

A line chart is drawn from left to right, data points pop out in sequence, and the area below fades in

- Component: Shapes · SVG (`shape`)
- Timing: Entrance, Scroll-triggered
- Tech: GSAP
- Uses: Numbers & Data
- Style / keywords: line chart chart data growth trend Dashboard Line Chart Graph Data Visualization SVG graphic
- Tag: DrawSVG
- Example text: "Monthly Revenue Growth" (stage background: dark)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Line Chart Draw (折線圖繪製)" motion effect: Line chart entrance: there are faint horizontal grid lines in the background, and the line is drawn from left to right (about 1.6 seconds). Each data point pops out from 0 in sequence as the line passes it, and when the line reaches its later section, the area below the line fades in with a gradient, and finally a growth value label floats up above the endpoint. (GSAP: DrawSVGPlugin draws the line path; the data points' stagger time = drawing time / number of points; the area uses the same path, closed along the bottom edge and filled with a gradient fading from top to bottom; on a real website it can be played when scrolled to, paired with ScrollTrigger)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx197">`, preview text "Monthly Revenue Growth". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Line Chart Draw".

### JavaScript — `FX[197]` from `site/fx.js`

```js
197(s,x){const V=[22,34,28,46,40,58,52,72],N=V.length,pts=V.map((v,i)=>[10+i*(140/(N-1)),80-v]);const d='M'+pts.map(p=>p.join(',')).join(' L');const id='ag'+Math.random().toString(36).slice(2);
  s.insertAdjacentHTML('beforeend',`<div class="lcw"><b></b><svg viewBox="0 0 160 90"><defs><linearGradient id="${id}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" class="s1"/><stop offset="1" class="s2"/></linearGradient></defs>${[20,40,60,80].map(y=>`<path class="gd" d="M10,${y}H150"/>`).join('')}<path class="ar" d="${d} L150,80 L10,80 Z" fill="url(#${id})"/><path class="ln" d="${d}"/>${pts.map(([cx,cy])=>`<circle class="pt" cx="${cx}" cy="${cy}" r="2.4"/>`).join('')}<text class="vl" x="${pts[N-1][0]-2}" y="${pts[N-1][1]-6}">+72%</text></svg></div>`);
  const w=s.querySelector('.lcw');w.querySelector('b').textContent=x;const q=c=>w.querySelector(c);
  gsap.timeline({repeat:-1,repeatDelay:.4}).set(w,{opacity:1},0).fromTo(q('.ln'),{drawSVG:'0%'},{drawSVG:'100%',duration:1.6,ease:'power1.inOut'},0).fromTo(w.querySelectorAll('.pt'),{scale:0,transformOrigin:'50% 50%'},{scale:1,duration:.35,ease:'back.out(3)',stagger:1.6/N},.05)
    .fromTo(q('.ar'),{opacity:0},{opacity:1,duration:.6},1.2).fromTo(q('.vl'),{opacity:0,y:4},{opacity:1,y:0,duration:.4},1.5).to(w,{opacity:0,duration:.5},'+=1.8')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx197` rules from `site/fx.css`

_No dedicated `.fx197` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #197
