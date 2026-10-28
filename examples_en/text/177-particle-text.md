# 177 · Particle Text — 文字粒子化

Text is made of many small dots; the cursor blows them apart up close, and they gather back when it leaves

- Component: Text (`text`)
- Timing: Hover · Click, Entrance
- Tech: Canvas
- Uses: Headline · Hero, Logo · Brand
- Style / keywords: text particles dot matrix scatter assemble interactive title Particle Text Interactive Typography Scatter Canvas particles particles requestAnimationFrame interactive background
- Tag: Canvas particles
- Example text: "HELLO" (stage background: dark)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Particle Text (文字粒子化)" motion effect: A large title made up of thousands of small square dots: on entry, the dots fly in from all over the screen and assemble into text; when the cursor approaches, nearby dots are pushed away and scatter, and after it leaves they spring back into place like a spring, and dots pushed away from their original position temporarily switch to an accent color. Suitable as an interactive title on a portfolio homepage. (Canvas 2D: first draw the text on an offscreen canvas, sample opaque points every few pixels as target positions; each particle returns to its target with a spring force, is subject to a repulsive force based on the cursor distance, and has damping added)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx177">`, preview text "HELLO". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Particle Text".

### JavaScript — `FX[177]` from `site/fx.js`

```js
177(s,x,card){cfx(s,card,{init:(c,W,H)=>{const off=document.createElement('canvas');off.width=W;off.height=H;const oc=off.getContext('2d');const fs=Math.min(H*.42,W*1.5/Math.max(2,chars(x).length));
    oc.font=`900 ${fs}px "Noto Sans JP",sans-serif`;oc.textAlign='center';oc.textBaseline='middle';oc.fillText(x,W/2,H/2);const px=oc.getImageData(0,0,W,H).data,gap=Math.max(3,Math.round(W/150)),P=[];
    for(let y=0;y<H;y+=gap)for(let xx=0;xx<W;xx+=gap)if(px[(y*W+xx)*4+3]>128)P.push({tx:xx,ty:y,x:rnd(0,W),y:rnd(0,H),vx:0,vy:0});return{P,gap,c:accRGB(s)}},
  frame:(c,W,H,t,dt,m,o)=>{c.clearRect(0,0,W,H);const [mx,my]=demoPt(t,W,H,m),R=W*.12,sz=o.gap*.7;
    o.P.forEach((p,i)=>{const dx=p.x-mx,dy=p.y-my,d=Math.hypot(dx,dy)||1;if(d<R){const f=(1-d/R)*6;p.vx+=dx/d*f;p.vy+=dy/d*f}p.vx+=(p.tx-p.x)*.06;p.vy+=(p.ty-p.y)*.06;p.vx*=.82;p.vy*=.82;p.x+=p.vx;p.y+=p.vy;
      const off=Math.min(1,Math.hypot(p.x-p.tx,p.y-p.ty)/(W*.05));c.fillStyle=off>.15?`rgb(${o.c})`:'#fff';c.fillRect(p.x-sz/2,p.y-sz/2,sz,sz)})}})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx177` rules from `site/fx.css`

_No dedicated `.fx177` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #177
