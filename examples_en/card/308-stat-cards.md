# 308 · Stat Cards — 數據儀表卡片

Three stat cards float up in sequence, the numbers count up, a mini line chart draws itself, and the growth rates fade in

- Component: Cards · Groups (`card`)
- Timing: Entrance
- Tech: GSAP
- Uses: Numbers & Data, UI Interaction
- Style / keywords: Dashboard Data Statistics KPI Line Chart sparkline Admin Dashboard Stat Cards KPI Sparkline Count Up Cards Group
- Tag: GSAP timeline
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-20

**AI prompt (English copy format):**

```text
"Stat Cards (數據儀表卡片)" motion effect: Three stat cards on an admin dashboard (revenue, orders, conversion rate): on entry they float up and fade in from below in sequence (about 0.12 seconds apart), the large number in each card counts up from 0 to its target value (including thousands separators and decimals), the mini line chart below draws itself from left to right, and finally the growth percentage fades in from the left. (GSAP timeline: cards from y:30, opacity:0, with stagger; numbers use an object tween + onUpdate formatting; the line chart's polyline uses DrawSVG 0% → 100% (or stroke-dashoffset))
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx308">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Stat Cards".

### JavaScript — `FX[308]` from `site/fx.js`

```js
308(s,x){const D=[['營收','128,400',[3,5,4,7,6,9,8,11]],['訂單','1,286',[6,5,7,6,8,7,9,10]],['轉換率','4.8%',[4,6,5,5,7,6,8,7]]];const w=el('div','cg-db');const cs=D.map(([l,v,p],i)=>{const c=el('div','cg-dc');const mx=Math.max(...p),pts=p.map((y,j)=>`${j*100/(p.length-1)},${36-y/mx*30}`).join(' ');
  c.innerHTML=`<small>${l}</small><b>${v}</b><em>▲ ${[12,8,3][i]}%</em><svg viewBox="0 0 100 40" preserveAspectRatio="none"><polyline points="${pts}"/></svg>`;w.append(c);return c});s.append(w);
  const tl=gsap.timeline({repeat:-1,repeatDelay:2});tl.from(cs,{y:30,opacity:0,duration:.6,ease:'power3.out',stagger:.12});cs.forEach((c,i)=>{const b=c.querySelector('b'),v=b.textContent,num=parseFloat(v.replace(/,/g,'')),dec=v.includes('.')?1:0,suf=v.replace(/[\d,.]/g,'');const o={n:0};
    tl.to(o,{n:num,duration:1.2,ease:'power2.out',onUpdate:()=>b.textContent=(dec?o.n.toFixed(1):Math.round(o.n).toLocaleString())+suf},.2+i*.12).fromTo(c.querySelector('polyline'),{drawSVG:'0%'},{drawSVG:'100%',duration:1,ease:'power2.inOut'},.35+i*.12).from(c.querySelector('em'),{opacity:0,x:-6,duration:.4},.9+i*.12)})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx308` rules from `site/fx.css`

_No dedicated `.fx308` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #308
