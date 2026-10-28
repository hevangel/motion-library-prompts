# 213 · Swipe Card Stack — 左右滑卡

The top card can be dragged and flung out, and the next one moves up to take its place

- Component: Cards · Groups (`card`)
- Timing: Drag Gesture, Exit
- Tech: GSAP
- Uses: UI Interaction, App Interface
- Style / keywords: Swipe Cards Swipe Left Right Dating Tinder Card Stack Fling Swipe Cards Stack Like Dislike Cards Group
- Tag: Draggable
- Example text: "Tokyo Kyoto Seoul Tainan" (stage background: dark)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Swipe Card Stack (左右滑卡)" motion effect: A stack of cards; the top card can be dragged with a finger or mouse, and while dragging the card tilts following the horizontal displacement; when dragged right, a "Like" stamp fades in at the top-left corner, and when dragged left, a "Skip" stamp fades in at the top-right; on release, if it exceeds the threshold it accelerates and is flung off-screen in that direction, and the cards below move up in order to fill in and scale up; if it does not exceed the threshold it springs back to its original position. (GSAP Draggable: onDrag sets rotation and stamp opacity based on x, onRelease checks the threshold then tweens it off-screen, then moves that card to the bottom layer and rearranges the whole stack)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx213">`, preview text "Tokyo Kyoto Seoul Tainan". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Swipe Card Stack".

### JavaScript — `FX[213]` from `site/fx.js`

```js
213(s,x,card){const ws=words(x);const w=el('div','kd-sw');let order=[...Array(4)].map((_,i)=>{const c=el('div','kd-sc');c.style.background=`linear-gradient(160deg,${GC[i%5]},${GC[(i+3)%5]})`;c.innerHTML='<em class="y">喜歡</em><em class="n">略過</em><b></b>';c.querySelector('b').textContent=ws[i%ws.length];w.append(c);return c});s.append(w);let idle=0,dr;
  const stack=()=>{order.forEach((c,i)=>{const k=order.length-1-i;gsap.to(c,{x:0,y:k*-2.4+'%',scale:1-k*.05,rotation:0,duration:.4,ease:'power3.out',overwrite:true});c.style.zIndex=i;gsap.set(c.querySelectorAll('em'),{opacity:0})});bind()};
  const fly=(c,dir)=>{gsap.to(c,{x:dir*w.offsetWidth*1.4,rotation:dir*25,duration:.45,ease:'power2.in',onComplete:()=>{order=[c,...order.filter(o=>o!==c)];w.prepend(c);gsap.set(c,{x:0,rotation:0});stack()}})};
  const bind=()=>{dr&&dr.kill();const top=order[order.length-1];dr=Draggable.create(top,{type:'x,y',onPress(){idle=Date.now()+4000},onDrag(){gsap.set(top,{rotation:this.x*.06});gsap.set(top.querySelector('.y'),{opacity:Math.max(0,this.x/80)});gsap.set(top.querySelector('.n'),{opacity:Math.max(0,-this.x/80)})},onRelease(){if(Math.abs(this.x)>w.offsetWidth*.25)fly(top,Math.sign(this.x));else stack()}})[0]};
  card._kill.push(()=>dr&&dr.kill());stack();let dir=1;card._timers.push(setInterval(()=>{if(Date.now()<idle)return;const top=order[order.length-1];gsap.timeline().to(top,{x:dir*w.offsetWidth*.18,rotation:dir*8,duration:.35,ease:'power2.out'}).to(top.querySelector(dir>0?'.y':'.n'),{opacity:1,duration:.2},'<').add(()=>fly(top,dir),'+=.25');dir*=-1},2300))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx213` rules from `site/fx.css`

_No dedicated `.fx213` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #213
