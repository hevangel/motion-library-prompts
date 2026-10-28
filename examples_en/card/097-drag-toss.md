# 097 · Drag & Toss — 拖曳甩動

Cards can be dragged and tossed with inertia

- Component: Cards · Groups (`card`)
- Timing: Drag Gesture
- Tech: GSAP
- Uses: UI Interaction
- Style / keywords: 
- Tag: Draggable·Inertia
- Example text: "Try Dragging" (stage background: acc)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Drag & Toss (拖曳甩動)" motion effect: Several cards can be dragged with the mouse or a finger; on release they glide with inertia according to the toss velocity, decelerating and bouncing back at the boundaries, and the card being dragged floats to the top layer. (GSAP: Draggable.create { bounds, inertia:true, edgeResistance }, requires InertiaPlugin)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage acc fx97">`, preview text "Try Dragging". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Drag & Toss".

### JavaScript — `FX[97]` from `site/fx.js`

```js
97(s,x,card){const l=layer(s);const cs=[x,'✦','●'].map((v,i)=>{const c=el('div','dcard');c.textContent=v;c.style.left=[10,40,66][i]+'%';c.style.top=[22,52,18][i]+'%';l.append(c);return c});let idle=true,it;
  const ds=Draggable.create(cs,{bounds:l,inertia:true,edgeResistance:.7,zIndexBoost:true,onPress(){idle=false;clearTimeout(it);gsap.killTweensOf(this.target)},onRelease(){it=setTimeout(()=>idle=true,4000)}});card._kill.push(()=>ds.forEach(d=>d.kill()));
  card._timers.push(setInterval(()=>{if(!idle)return;const c=gsap.utils.random(cs);const W=l.offsetWidth,H=l.offsetHeight;gsap.to(c,{x:gsap.utils.random(-W*.15,W*.15),y:gsap.utils.random(-H*.15,H*.15),rotation:gsap.utils.random(-14,14),duration:1,ease:'power3.out'})},1600))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx97` rules from `site/fx.css`

_No dedicated `.fx97` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #97
