# 181 · Fireworks — 煙火

Fireworks rise to the clicked position and burst; they launch automatically when there is no interaction

- Component: Background · Ambience (`bg`)
- Timing: Hover · Click, Loop · Idle
- Tech: Canvas
- Uses: Emphasis, Background Decoration
- Style / keywords: fireworks celebration explosion particles event festival Fireworks Celebration Particles Explosion Click Canvas particles particles requestAnimationFrame interactive background
- Tag: Canvas particles
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Fireworks (煙火)" motion effect: A night-sky background. When you click any position, a firework is launched from the bottom of the screen, rises to the clicked spot, and upon arrival bursts into dozens of sparks. The sparks scatter in all directions, fall under gravity, slow down due to drag and gradually fade out, leaving brief trails; when there is no interaction, they launch automatically at random. Suitable for event pages and completion celebrations. (Canvas 2D: the rocket rises with ease-out interpolation, on explosion an array of particles is created, each frame the velocity (× drag, + gravity) and lifespan are updated; each frame the screen is covered with a translucent background color for trails)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx181">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Fireworks".

### JavaScript — `FX[181]` from `site/fx.js`

```js
181(s,x,card){let auto=0;cfx(s,card,{init:(c,W,H,m)=>{c.fillStyle=`rgb(${BGD})`;c.fillRect(0,0,W,H);const o={R:[],P:[]};m.click=(px,py)=>{auto=Date.now();launch(o,W,H,px,py)};return o},
  frame:(c,W,H,t,dt,m,o)=>{c.fillStyle=`rgba(${BGD},.2)`;c.fillRect(0,0,W,H);if(Date.now()-auto>2500&&Math.random()<dt*1.3)launch(o,W,H,rnd(.2,.8)*W,rnd(.15,.5)*H);
    o.R=o.R.filter(r=>{r.t+=dt/.7;const k=Math.min(1,r.t),e=1-(1-k)**3,y=r.sy+(r.ty-r.sy)*e,xx=r.sx+(r.tx-r.sx)*e;c.fillStyle=`hsl(${r.h},100%,80%)`;c.beginPath();c.arc(xx,y,2,0,7);c.fill();
      if(k>=1){for(let i=0;i<70;i++){const a=rnd(0,6.3),v=rnd(.5,1)*W*.006;o.P.push({x:r.tx,y:r.ty,vx:Math.cos(a)*v,vy:Math.sin(a)*v,l:1,h:r.h+rnd(-20,20)})}return false}return true});
    o.P=o.P.filter(p=>{p.vx*=.97;p.vy=p.vy*.97+W*.00009;p.x+=p.vx;p.y+=p.vy;p.l-=dt*.7;c.fillStyle=`hsla(${p.h},100%,65%,${p.l})`;c.beginPath();c.arc(p.x,p.y,1.8,0,7);c.fill();return p.l>0})}});
  function launch(o,W,H,tx,ty){o.R.push({sx:tx+rnd(-W*.05,W*.05),sy:H,tx,ty,t:0,h:rnd(0,360)})}}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx181` rules from `site/fx.css`

_No dedicated `.fx181` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #181
