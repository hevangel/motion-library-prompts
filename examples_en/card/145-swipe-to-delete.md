# 145 · Swipe to Delete — 滑動刪除

Swiping a list item left reveals delete; swiping all the way collapses and removes it

- Component: Cards · Groups (`card`)
- Timing: Drag Gesture, Exit
- Tech: GSAP
- Uses: App Interface, UI Interaction
- Style / keywords: Swipe Delete Swipe Left List Gesture Collapse Swipe Delete Gesture List Dismiss App Mobile Mobile Device Micro-interaction Mobile App Micro-interaction
- Tag: Draggable
- Example text: "Meeting Reminder Billing Notice New Message" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Swipe to Delete (滑動刪除)" motion effect: List items can be swiped left with a finger, revealing a warning-colored 'Delete' button behind the item; if released with less than half the distance swiped, it springs back into place; if released past the threshold (about 30%), the item slides entirely off the screen to the left, then that row's height collapses to 0 and the items below smoothly move up to fill in. (GSAP: Draggable type:"x", restricted to leftward only, edgeResistance 0.8; onRelease, judge the threshold, then xPercent:-100, then tween height to 0; on mobile, set touch-action:pan-y so vertical scrolling is not affected)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx145">`, preview text "Meeting Reminder Billing Notice New Message". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Swipe to Delete".

### JavaScript — `FX[145]` from `site/fx.js`

```js
145(s,x,card){const ws=words(x);const l=el('div','swl');const rows=[0,1,2].map(i=>{const r=el('div','swr');r.innerHTML='<div class="del">刪除</div><div class="fr"><i></i><span><b></b><em></em></span></div>';r.querySelector('i').style.background=GC[i];r.querySelector('b').textContent=ws[i%ws.length];l.append(r);return r});s.append(l);let idle=0;
  const kill=r=>{const f=r.querySelector('.fr');gsap.timeline().to(f,{xPercent:-100,duration:.3,ease:'power2.in'}).to(r,{height:0,opacity:0,duration:.3,ease:'power2.inOut'}).set(f,{x:0,xPercent:0},'+=.9').to(r,{height:'auto',opacity:1,duration:.4,ease:'power2.out'})};
  const ds=rows.map(r=>Draggable.create(r.querySelector('.fr'),{type:'x',bounds:{minX:-r.offsetWidth*.6,maxX:0},edgeResistance:.8,onPress(){idle=Date.now()+4000},onRelease(){if(this.x<-r.offsetWidth*.3)kill(r);else gsap.to(this.target,{x:0,duration:.3,ease:'power3.out'})}})[0]);card._kill.push(()=>ds.forEach(d=>d.kill()));
  let k=0;card._timers.push(setInterval(()=>{if(Date.now()<idle)return;const r=rows[k++%3],f=r.querySelector('.fr');gsap.timeline().to(f,{x:-r.offsetWidth*.24,duration:.45,ease:'power2.out'}).add(()=>kill(r),'+=.7')},3200))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx145` rules from `site/fx.css`

_No dedicated `.fx145` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #145
