# 173 · Flow Field — 流場線條

Hundreds of fine lines flow slowly along an invisible current; the cursor stirs the flow

- Component: Background · Ambience (`bg`)
- Timing: Loop · Idle, Hover · Click
- Tech: Canvas
- Uses: Background Decoration, Headline · Hero
- Style / keywords: flow field current lines generative art organic Flow Field Generative Art Perlin Noise Lines Canvas particles particles requestAnimationFrame interactive background
- Tag: Canvas trails
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Flow Field (流場線條)" motion effect: The background is filled with hundreds of invisible small particles. Each particle advances according to the 'flow direction' at its location (determined by smoothly varying noise or trigonometric functions, and changing slowly over time) and leaves a very fine trail. The trails fade out gradually, and the whole flows continuously like patterns of wind or water; the flow direction near the cursor is twisted, forming a stirred vortex. (Canvas 2D: each frame first cover the screen with a low-opacity background color to create trails, then let each particle advance a small step according to angle = f(x, y, t) and draw a line; particles respawn when their lifespan ends or they go out of bounds; simplex noise can be used to make the flow field more natural)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx173">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Flow Field".

### JavaScript — `FX[173]` from `site/fx.js`

```js
173(s,x,card){cfx(s,card,{init:(c,W,H)=>{c.fillStyle=`rgb(${BGD})`;c.fillRect(0,0,W,H);return{P:[...Array(700)].map(()=>({x:rnd(0,W),y:rnd(0,H),l:rnd(0,200)})),c:accRGB(s)}},
  frame:(c,W,H,t,dt,m,o)=>{c.fillStyle=`rgba(${BGD},.06)`;c.fillRect(0,0,W,H);c.lineWidth=1;const [mx,my]=demoPt(t,W,H,m),R=W*.18;
    o.P.forEach((p,i)=>{let a=(Math.sin(p.x*.012+t*.25)+Math.cos(p.y*.014-t*.18)+Math.sin((p.x+p.y)*.006))*Math.PI*.8;const dx=p.x-mx,dy=p.y-my,d=Math.hypot(dx,dy);if(d<R)a+=(1-d/R)*Math.PI*.9;
      const nx=p.x+Math.cos(a)*W*.0025,ny=p.y+Math.sin(a)*W*.0025;c.strokeStyle=i%3?`rgba(${o.c},.55)`:'rgba(255,255,255,.35)';c.beginPath();c.moveTo(p.x,p.y);c.lineTo(nx,ny);c.stroke();p.x=nx;p.y=ny;
      if(--p.l<0||p.x<0||p.x>W||p.y<0||p.y>H){p.x=rnd(0,W);p.y=rnd(0,H);p.l=rnd(100,260)}})}})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx173` rules from `site/fx.css`

_No dedicated `.fx173` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #173
