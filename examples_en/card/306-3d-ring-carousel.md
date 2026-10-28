# 306 · 3D Ring Carousel — 3D 環形輪播

Cards form a ring and slowly rotate in 3D space, and can be dragged left and right with the mouse to spin them

- Component: Cards · Groups (`card`)
- Timing: Loop · Idle, Drag Gesture
- Tech: GSAP
- Uses: Headline · Hero, UI Interaction
- Style / keywords: 3D Ring Carousel Carousel Ring Ring Carousel 3D Rotate Gallery Drag Cards Group
- Tag: GSAP 3D
- Example text: "Seaside Mountains Night Sky Afternoon City Forest Lakeside Desert" (stage background: dark)
- Added: 2026-10-20

**AI prompt (English copy format):**

```text
"3D Ring Carousel (3D 環形輪播)" motion effect: Eight image cards form a ring in 3D space, and the whole ring slowly rotates on its own at about 24 seconds per revolution; cards at the front are larger and nearer, cards at the back are smaller and farther, and cards facing away from the viewer are hidden; the user can press and drag left and right to rotate the ring, and on release it continues rotating on its own from the current angle. (CSS 3D: perspective on the container, transform-style:preserve-3d on the ring, each card rotateY(i × 360/N) translateZ(radius), backface-visibility:hidden; GSAP loops the ring's rotationY, and Draggable pauses it while dragging and sets the angle from the displacement)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx306">`, preview text "Seaside Mountains Night Sky Afternoon City Forest Lakeside Desert". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "3D Ring Carousel".

### JavaScript — `FX[306]` from `site/fx.js`

```js
306(s,x,card){const ws=words(x);const sc=el('div','abs gl cg-rs');const ring=el('div','cg-rg');const N=8;const cs=[...Array(N)].map((_,i)=>{const c=el('div','cg-rc');c.innerHTML=mdImg(i)+'<b></b>';c.querySelector('b').textContent=ws[i%ws.length];c.style.transform=`rotateY(${i*360/N}deg) translateZ(var(--r))`;ring.append(c);return c});sc.append(ring);s.append(sc);
  const tw=gsap.to(ring,{rotationY:-360,duration:24,ease:'none',repeat:-1});const dr=Draggable.create(el('div'),{trigger:sc,type:'x',onPress(){tw.pause();this.r0=gsap.getProperty(ring,'rotationY')},onDrag(){gsap.set(ring,{rotationY:this.r0+(this.x-this.startX)*.4})},onRelease(){const r=gsap.getProperty(ring,'rotationY');tw.progress(((-r%360)+360)%360/360).resume()}})[0];card._kill.push(()=>dr.kill())}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx306` rules from `site/fx.css`

_No dedicated `.fx306` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #306
