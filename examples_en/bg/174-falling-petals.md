# 174 · Falling Petals — 飄落花瓣

Petals drift down slowly while rotating; the cursor passing by blows them away

- Component: Background · Ambience (`bg`)
- Timing: Loop · Idle, Hover · Click
- Tech: Canvas
- Uses: Background Decoration, Headline · Hero
- Style / keywords: petals sakura falling snow weather season Petals Sakura Snow Weather Falling Particles Canvas particles particles requestAnimationFrame interactive background
- Tag: Canvas particles
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Falling Petals (飄落花瓣)" motion effect: Dozens of petals drift slowly down from the top of the background. Each sways side to side, flips over (simulating a flip with scaling) and rotates individually, with slightly different speeds and sizes; when the cursor passes by, it blows nearby petals away according to its movement direction and speed, after which the petals slowly return to their natural falling. It can also be swapped for weather particles such as snowflakes or raindrops. (Canvas 2D: each petal has a position, velocity, angle and sway phase; cursor velocity = the difference between this frame's and the previous frame's coordinates, petals within range receive a push according to distance, which then decays gradually; when a petal falls past the bottom of the screen it returns to the top and respawns)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx174">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Falling Petals".

### JavaScript — `FX[174]` from `site/fx.js`

```js
174(s,x,card){cfx(s,card,{init:(c,W,H)=>({P:[...Array(90)].map(()=>({x:rnd(0,W),y:rnd(-H,H),vx:0,vy:rnd(.3,.8),r:rnd(.006,.013)*W,a:rnd(0,6.3),va:rnd(-1.5,1.5),ph:rnd(0,6.3)}))}),
  frame:(c,W,H,t,dt,m,o)=>{c.clearRect(0,0,W,H);const [mx,my]=demoPt(t,W,H,m);const wx=m.in?(m.x-m.px):Math.cos(t*.8)*2.2,wy=m.in?(m.y-m.py):Math.sin(t*1.6)*1.2;
    o.P.forEach(p=>{const d=Math.hypot(p.x-mx,p.y-my);if(d<W*.15){const k=1-d/(W*.15);p.vx+=wx*k*.08;p.vy+=wy*k*.05}p.vx*=.96;p.vy+=(.55-p.vy)*.02;
      p.x+=p.vx+Math.sin(t*1.3+p.ph)*.35;p.y+=p.vy*H*.004;p.a+=p.va*dt;if(p.y>H+20){p.y=-20;p.x=rnd(0,W)}if(p.x<-20)p.x=W+20;if(p.x>W+20)p.x=-20;
      c.save();c.translate(p.x,p.y);c.rotate(p.a);c.scale(1,.6+.4*Math.sin(t*2+p.ph));c.fillStyle='rgba(255,183,213,.9)';c.beginPath();c.ellipse(0,0,p.r,p.r*.62,0,0,7);c.fill();c.fillStyle='rgba(255,140,190,.9)';c.beginPath();c.ellipse(p.r*.35,0,p.r*.3,p.r*.2,0,0,7);c.fill();c.restore()})}})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx174` rules from `site/fx.css`

_No dedicated `.fx174` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #174
