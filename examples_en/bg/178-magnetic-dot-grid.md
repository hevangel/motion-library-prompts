# 178 · Magnetic Dot Grid — 磁力點陣

A full screen of small dots; as the cursor passes, they are pushed away and grow larger

- Component: Background · Ambience (`bg`)
- Timing: Hover · Click
- Tech: Canvas
- Uses: Background Decoration, UI Interaction
- Style / keywords: dot grid dots grid magnetic repel interactive background Dot Grid Repel Magnetic Interactive Background Canvas particles particles requestAnimationFrame interactive background
- Tag: Canvas spring
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Magnetic Dot Grid (磁力點陣)" motion effect: The background is a neat arrangement of fine dots. When the cursor moves, nearby dots are pushed outward and become larger and switch to an accent color — the closer they are, the farther they are pushed — and after it leaves they return to their original positions with a spring-like motion, forming a dent that flows with the cursor. A low-key background with a strong sense of interaction. (Canvas 2D: each dot records its original position, target position = original position + direction away from the cursor × influence coefficient, use velocity + damping for spring rebound; size and opacity are interpolated according to distance)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx178">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Magnetic Dot Grid".

### JavaScript — `FX[178]` from `site/fx.js`

```js
178(s,x,card){cfx(s,card,{init:(c,W,H)=>{const g=W/34,D=[];for(let y=g/2;y<H;y+=g)for(let xx=g/2;xx<W;xx+=g)D.push({ox:xx,oy:y,x:xx,y,vx:0,vy:0});return{D,g,c:accRGB(s)}},
  frame:(c,W,H,t,dt,m,o)=>{c.clearRect(0,0,W,H);const [mx,my]=demoPt(t,W,H,m),R=W*.14;
    o.D.forEach(p=>{const dx=p.ox-mx,dy=p.oy-my,d=Math.hypot(dx,dy)||1,k=Math.max(0,1-d/R);const tx=p.ox+dx/d*k*R*.45,ty=p.oy+dy/d*k*R*.45;p.vx+=(tx-p.x)*.15;p.vy+=(ty-p.y)*.15;p.vx*=.75;p.vy*=.75;p.x+=p.vx;p.y+=p.vy;
      c.fillStyle=k>.02?`rgba(${o.c},${.4+k*.6})`:'rgba(255,255,255,.22)';c.beginPath();c.arc(p.x,p.y,o.g*(.12+k*.22),0,7);c.fill()})}})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx178` rules from `site/fx.css`

_No dedicated `.fx178` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #178
