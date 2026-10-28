# 322 · Map Route — 地圖路線導航

Map pins drop down in sequence on a map, a route is drawn from the start point to the end point, and a small dot advances along the route

- Component: Shapes · SVG (`shape`)
- Timing: Entrance, Loop · Idle
- Tech: GSAP
- Uses: Numbers & Data, Headline · Hero
- Style / keywords: Map Route Navigation Pin Location Journey Delivery Logistics Map Route Path Pin Delivery Journey Graphics SVG
- Tag: MotionPath
- Example text: "Taipei Taichung Kaohsiung" (stage background: dark)
- Added: 2026-10-21

**AI prompt (English copy format):**

```text
"Map Route (地圖路線導航)" motion effect: A simplified map background (faint landmass outlines and latitude/longitude grid lines), on which three map pins drop down from above in sequence and bounce to a stop, each labeled with a place name below it; then a route is drawn from the start point along a curved path all the way to the end point (about 2.2 seconds), while a small dot with a halo advances along the route; on reaching the end point, the end-point pin bounces once. (GSAP: the pins from y:-30 + bounce.out with stagger; the route uses DrawSVG 0% → 100%; the small dot uses MotionPathPlugin to move along the same path, with a duration matching the line drawing; beneath it there is also a faint dashed line indicating the full route)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx322">`, preview text "Taipei Taichung Kaohsiung". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Map Route".

### JavaScript — `FX[322]` from `site/fx.js`

```js
322(s,x){const ws=words(x);const id='rt'+Math.random().toString(36).slice(2);s.insertAdjacentHTML('beforeend',`<svg class="sv-map" viewBox="0 0 320 180"><g class="sv-land"><path d="M20,40 C60,10 120,30 150,20 C190,8 230,30 270,22 C300,18 310,60 300,90 C292,120 310,150 270,160 C220,172 170,150 120,162 C80,172 30,160 22,128 C14,100 30,80 20,40Z"/></g><g class="sv-grid">${[...Array(7)].map((_,i)=>`<path d="M${i*50},0 V180"/>`).join('')}${[...Array(4)].map((_,i)=>`<path d="M0,${i*50+15} H320"/>`).join('')}</g><path id="${id}" class="sv-rt0" d="M60,130 C90,70 130,140 165,95 C200,50 230,110 262,58"/><path class="sv-rt" d="M60,130 C90,70 130,140 165,95 C200,50 230,110 262,58"/>${[[60,130],[165,95],[262,58]].map(([cx,cy],i)=>`<g class="sv-pin" transform="translate(${cx},${cy})"><path d="M0,0 C-7,-9 -9,-13 -9,-17 A9,9 0 1 1 9,-17 C9,-13 7,-9 0,0Z"/><circle cy="-17" r="3.4"/><text y="14" text-anchor="middle"></text></g>`).join('')}<g class="sv-car"><circle r="6"/><circle r="11" class="h"/></g></svg>`);
  const sv=s.querySelector('.sv-map');sv.querySelectorAll('.sv-pin text').forEach((t,i)=>t.textContent=ws[i%ws.length]);const pins=sv.querySelectorAll('.sv-pin'),car=sv.querySelector('.sv-car'),rt=sv.querySelector('.sv-rt');
  gsap.timeline({repeat:-1,repeatDelay:1}).set(car,{opacity:0}).from(pins,{y:'-=30',opacity:0,duration:.5,ease:'bounce.out',stagger:.15}).fromTo(rt,{drawSVG:'0%'},{drawSVG:'100%',duration:2.2,ease:'power1.inOut'},'+=.1').to(car,{opacity:1,duration:.2},'<').to(car,{motionPath:{path:'#'+id,align:'#'+id,alignOrigin:[.5,.5]},duration:2.2,ease:'power1.inOut'},'<').to(pins[2],{scale:1.3,transformOrigin:'50% 100%',duration:.2,yoyo:true,repeat:1}).to([rt,car],{opacity:0,duration:.5},'+=1')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx322` rules from `site/fx.css`

_No dedicated `.fx322` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #322
