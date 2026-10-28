# 270 · Photo Stack Shuffle — 拍立得洗牌

A stack of slightly crooked Polaroid photos; click and the top one is pulled out and tucked back to the bottom

- Component: Images · Media (`media`)
- Timing: Switch
- Tech: GSAP
- Uses: UI Interaction, Headline · Hero
- Style / keywords: Polaroid Photo Stack Shuffle Album Polaroid Photo Stack Shuffle Deck Image Media
- Tag: GSAP timeline
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Photo Stack Shuffle (拍立得洗牌)" motion effect: A stack of Polaroid-style photos (with a wide border all around and a small caption written in the wider space at the bottom), each slightly crooked at a different angle and stacked together; when clicked, the top one is pulled out to the right and rotated, then returns to the very bottom of the stack, while the other photos simultaneously adjust their positions and angles to fill in, forming a shuffle effect that can be clicked repeatedly. (GSAP timeline: the top one x +120%, rotation 18 → adjust z-index to place it at the bottom → return to the stack position; each photo sets rotation and small x/y offsets according to stacking order)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx270">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Photo Stack Shuffle".

### JavaScript — `FX[270]` from `site/fx.js`

```js
270(s,x,card){const w=el('div','md-pd');const ps=[0,1,2,3].map(i=>{const d=el('div','md-pp');d.innerHTML=mdImg(i)+'<small></small>';d.querySelector('small').textContent=['夏日','旅行','夜晚','午後'][i];d.style.setProperty('--r',(i-1.5)*5+'deg');w.append(d);return d});s.append(w);let order=[...ps],busy=false,real=0;
  const lay=()=>order.forEach((d,k)=>{d.style.zIndex=k;gsap.to(d,{rotation:(k-1.5)*5+(k===3?0:0),x:(k-1.5)*3,y:-k*2,duration:.4,ease:'power2.out'})});lay();
  const shuffle=()=>{if(busy)return;busy=true;const t=order[3];gsap.timeline({onComplete:()=>{busy=false}}).to(t,{x:'+=120%',rotation:18,duration:.35,ease:'power2.in'}).add(()=>{order=[t,...order.slice(0,3)];lay()}).to(t,{x:-4.5,duration:.4,ease:'power3.out'})};
  w.onclick=()=>{real=Date.now();shuffle()};card._timers.push(setInterval(()=>{if(Date.now()-real>5000)shuffle()},2200))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx270` rules from `site/fx.css`

_No dedicated `.fx270` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #270
