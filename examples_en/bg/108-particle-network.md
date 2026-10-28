# 108 · Particle Network — 粒子連線

Floating particles automatically connect when close; the cursor attracts nearby particles

- Component: Background · Ambience (`bg`)
- Timing: Loop · Idle, Hover · Click
- Tech: Canvas
- Uses: Background Decoration, Headline · Hero
- Style / keywords: Background Particles Connecting Lines Network Constellation Particles Network Constellation particles.js Canvas
- Tag: Canvas 2D
- Example text: "Network" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Particle Network (粒子連線)" motion effect: Dozens of small particles in the background drift slowly and randomly, bouncing off the boundaries; when two particles are close enough they automatically connect with a line — the closer they are, the clearer the line, the farther, the fainter; when the cursor moves in, nearby particles are gently drawn toward it and connect to it, forming an effect like a constellation network. The foreground title stays clear. (Canvas 2D: requestAnimationFrame updates the positions every frame, lines are drawn by computing pairwise distances with opacity adjusted by distance; note the canvas size should be set according to devicePixelRatio)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx108">`, preview text "Network". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Particle Network".

### JavaScript — `FX[108]` from `site/fx.js`

```js
108(s,x,card){const cv=el('canvas','pnet');s.append(cv,T(x,Math.min(13,56/chars(x).length)));const ctx=cv.getContext('2d');const col=getComputedStyle(s).getPropertyValue('--a').trim()||'#3dd9b8';let P=[],m={x:-1e4,y:-1e4};
  cv.addEventListener('pointermove',e=>{const r=cv.getBoundingClientRect();m={x:(e.clientX-r.left)*devicePixelRatio,y:(e.clientY-r.top)*devicePixelRatio}});cv.addEventListener('pointerleave',()=>m={x:-1e4,y:-1e4});
  ticks.set(card,()=>{const dpr=devicePixelRatio||1,W=s.offsetWidth*dpr,H=s.offsetHeight*dpr;if(!W)return;
    if(cv.width!==W){cv.width=W;cv.height=H;P=[...Array(46)].map(()=>({x:Math.random()*W,y:Math.random()*H,vx:(Math.random()-.5)*.6*dpr,vy:(Math.random()-.5)*.6*dpr}))}
    const D=W*.16;ctx.clearRect(0,0,W,H);ctx.fillStyle=ctx.strokeStyle=col;
    P.forEach(p=>{p.x+=p.vx;p.y+=p.vy;if(p.x<0||p.x>W)p.vx*=-1;if(p.y<0||p.y>H)p.vy*=-1;const dm=Math.hypot(p.x-m.x,p.y-m.y);if(dm<D*1.4){p.x+=(m.x-p.x)*.012;p.y+=(m.y-p.y)*.012}});
    for(let i=0;i<P.length;i++){for(let j=i+1;j<P.length;j++){const d=Math.hypot(P[i].x-P[j].x,P[i].y-P[j].y);if(d<D){ctx.globalAlpha=(1-d/D)*.6;ctx.lineWidth=dpr;ctx.beginPath();ctx.moveTo(P[i].x,P[i].y);ctx.lineTo(P[j].x,P[j].y);ctx.stroke()}}
      const dm=Math.hypot(P[i].x-m.x,P[i].y-m.y);if(dm<D*1.4){ctx.globalAlpha=(1-dm/(D*1.4))*.9;ctx.beginPath();ctx.moveTo(P[i].x,P[i].y);ctx.lineTo(m.x,m.y);ctx.stroke()}
      ctx.globalAlpha=.9;ctx.beginPath();ctx.arc(P[i].x,P[i].y,1.8*dpr,0,7);ctx.fill()}ctx.globalAlpha=1})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx108` rules from `site/fx.css`

```css
.fx108 .t{color:#fff;z-index:1;pointer-events:none}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #108
