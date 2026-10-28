# 302 · Drag to Reorder — 拖曳排序清單

Drag a row up or down, the other rows automatically make way, and on release it springs back into place and the numbering updates

- Component: Cards · Groups (`card`)
- Timing: Drag Gesture
- Tech: GSAP
- Uses: UI Interaction, App Interface
- Style / keywords: Drag Sorting Reorder List To-do sortable Drag Reorder List Sortable Cards Group
- Tag: Draggable
- Example text: "Planning Design Development Launch" (stage background: dark)
- Added: 2026-10-20

**AI prompt (English copy format):**

```text
"Drag to Reorder (拖曳排序清單)" motion effect: A list that can be reordered by dragging, each row with a drag handle on the left and a sequence number on the right: when you press and hold a row it enlarges slightly and lifts up (deeper shadow and outline), and can be dragged up and down; as you drag past the positions of other rows, the rows you pass smoothly move up or down to make way; on release, the dragged row lands in its new position with a bit of elasticity, and all the numbers update to the new order. (GSAP Draggable type:"y": while dragging, compute the target index from y ÷ row height, change the array order and tween the other rows to index × row height; on release, align with back.out)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx302">`, preview text "Planning Design Development Launch". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Drag to Reorder".

### JavaScript — `FX[302]` from `site/fx.js`

```js
302(s,x,card){const ws=words(x).slice(0,4);const l=el('ul','cg-dl');const items=ws.map((t,i)=>{const li=el('li');li.innerHTML='<span class="cg-hd" aria-hidden="true">⋮⋮</span><b></b><em>0'+(i+1)+'</em>';li.querySelector('b').textContent=t;l.append(li);return li});s.append(l);
  let order=[...items],H=0,real=0;const pos=(skip)=>order.forEach((li,i)=>{if(li!==skip)gsap.to(li,{y:i*H,duration:.3,ease:'power3.out'})});
  requestAnimationFrame(()=>{H=items[0].offsetHeight+6;l.style.height=H*items.length+'px';order.forEach((li,i)=>gsap.set(li,{y:i*H}));
    items.forEach(li=>Draggable.create(li,{type:'y',trigger:li,onPress(){real=Date.now()+1e9;li.classList.add('drag');gsap.to(li,{scale:1.04,duration:.2})},onDrag(){const ni=Math.max(0,Math.min(order.length-1,Math.round(this.y/H)));const oi=order.indexOf(li);if(ni!==oi){order.splice(oi,1);order.splice(ni,0,li);pos(li)}},
      onRelease(){real=Date.now();li.classList.remove('drag');gsap.to(li,{y:order.indexOf(li)*H,scale:1,duration:.35,ease:'back.out(2)'});order.forEach((o,i)=>o.querySelector('em').textContent='0'+(i+1))}}))});
  card._kill.push(()=>items.forEach(li=>{const d=Draggable.get(li);d&&d.kill()}));
  card._timers.push(setInterval(()=>{if(Date.now()-real<5000||!H)return;const a=order.pop();order.splice(Math.floor(Math.random()*order.length),0,a);order.forEach((li,i)=>{gsap.to(li,{y:i*H,duration:.5,ease:'power3.inOut'});li.querySelector('em').textContent='0'+(i+1)})},2200))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx302` rules from `site/fx.css`

_No dedicated `.fx302` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #302
