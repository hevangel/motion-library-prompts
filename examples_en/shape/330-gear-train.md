# 330 · Gear Train — 齒輪連動

Three gears of different sizes mesh together, driving each other at different speeds according to their tooth-count ratio

- Component: Shapes · SVG (`shape`)
- Timing: Loop · Idle
- Tech: GSAP
- Uses: Background Decoration, Numbers & Data
- Style / keywords: Gears Linked Mechanism Running Settings System Gears Cogs Mechanism Rotation Settings Graphics SVG
- Tag: GSAP
- Example text: "System Running" (stage background: dark)
- Added: 2026-10-21

**AI prompt (English copy format):**

```text
"Gear Train (齒輪連動)" motion effect: Three gears of different sizes and tooth counts mesh with each other: the largest gear rotates clockwise at a fixed speed, and the two smaller gears meshing with it rotate counterclockwise at higher speeds according to their tooth-count ratio (the one with fewer teeth turns faster), with tooth aligned to tooth and no clipping, like a mechanical system in operation; suitable for "processing", settings or system-status screens. (SVG: generate each gear's outline path programmatically from its radius and tooth count; GSAP loops each gear's rotation infinitely, with a small gear's angular velocity = the large gear × (large tooth count ÷ small tooth count), in the opposite direction, and sets the initial phase so the teeth align)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx330">`, preview text "System Running". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Gear Train".

### JavaScript — `FX[330]` from `site/fx.js`

```js
330(s,x){const gear=(r,n,d)=>{let p='';const st=Math.PI*2/n;for(let i=0;i<n;i++){const a=i*st;const pts=[[a,r-d],[a+st*.15,r],[a+st*.45,r],[a+st*.6,r-d]];pts.forEach(([aa,rr],k)=>p+=(i||k?'L':'M')+(Math.cos(aa)*rr).toFixed(2)+','+(Math.sin(aa)*rr).toFixed(2))}return p+'Z'};
  const G=[[0,0,34,16,'a'],[49,-8,20,10,'b'],[-40,22.6,16,8,'c']];
  s.insertAdjacentHTML('beforeend',`<div class="sv-gr"><svg viewBox="-90 -60 180 120">${G.map(([cx,cy,r,n,c])=>`<g transform="translate(${cx},${cy})"><g class="sv-g ${c}"><path d="${gear(r,n,r*.16)}"/><circle r="${r*.32}"/>${r>25?[0,1,2,3,4,5].map(i=>`<circle class="hl" r="${r*.1}" cx="${(Math.cos(i*Math.PI/3)*r*.58).toFixed(1)}" cy="${(Math.sin(i*Math.PI/3)*r*.58).toFixed(1)}"/>`).join(''):''}</g></g>`).join('')}</svg><b></b></div>`);
  const gr=s.querySelector('.sv-gr');gr.querySelector('b').textContent=x;const [a,b2,c]=gr.querySelectorAll('.sv-g');const T0=8;
  gsap.to(a,{rotation:360,duration:T0,ease:'none',repeat:-1,svgOrigin:'0 0'});gsap.fromTo(b2,{rotation:11},{rotation:11-360*16/10,duration:T0,ease:'none',repeat:-1,svgOrigin:'0 0'});gsap.fromTo(c,{rotation:6},{rotation:6-360*16/8,duration:T0,ease:'none',repeat:-1,svgOrigin:'0 0'})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx330` rules from `site/fx.css`

_No dedicated `.fx330` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #330
