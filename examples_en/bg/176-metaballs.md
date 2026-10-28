# 176 · Metaballs — 融合球

Several spheres float and move; when they get close, they stick together like liquid

- Component: Background · Ambience (`bg`)
- Timing: Loop · Idle, Hover · Click
- Tech: Canvas
- Uses: Background Decoration, Headline · Hero
- Style / keywords: metaballs liquid goo organic lava lamp Metaballs Liquid Blob Gooey Lava Lamp Canvas particles particles requestAnimationFrame interactive background
- Tag: Canvas field
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Metaballs (融合球)" motion effect: Several spheres of different sizes float slowly in the background and bounce off the boundaries. When two spheres come close, their edges smoothly stick together like liquid, pulling out a connecting neck, and break apart again when they separate; one of the spheres follows the cursor, so you can go and 'stick' to the other spheres. An organic feel like a lava lamp. (Canvas: on a low-resolution grid, calculate each cell's field strength Σ r²/d², fill with color where it exceeds a threshold and soften the edges for a smooth transition, then scale up and draw to the canvas; or use the gooey technique with a CSS filter blur + contrast)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx176">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Metaballs".

### JavaScript — `FX[176]` from `site/fx.js`

```js
176(s,x,card){cfx(s,card,{init:(c,W,H,m)=>{const g=4,gw=Math.ceil(W/g),gh=Math.ceil(H/g),off=document.createElement('canvas');off.width=gw;off.height=gh;const oc=off.getContext('2d');
    return{g,gw,gh,off,oc,img:oc.createImageData(gw,gh),c:accRGB(s),B:[...Array(5)].map(()=>({x:rnd(.2,.8)*gw,y:rnd(.2,.8)*gh,vx:rnd(-12,12),vy:rnd(-9,9),r:rnd(.09,.14)*gh}))}},
  frame:(c,W,H,t,dt,m,o)=>{const{gw,gh,img,B}=o,d=img.data,[mx,my]=demoPt(t,W,H,m);B.forEach(b=>{b.x+=b.vx*dt;b.y+=b.vy*dt;if(b.x<b.r||b.x>gw-b.r)b.vx*=-1;if(b.y<b.r||b.y>gh-b.r)b.vy*=-1});
    const all=[...B,{x:mx/o.g,y:my/o.g,r:gh*.13}];const[R,G,Bc]=o.c;
    for(let y=0;y<gh;y++)for(let x=0;x<gw;x++){let f=0;for(const b of all){const dx=x-b.x,dy=y-b.y;f+=b.r*b.r/(dx*dx+dy*dy+1)}const i=(y*gw+x)*4,k=Math.max(0,Math.min(1,(f-.9)*6));
      d[i]=21+(R-21)*k;d[i+1]=22+(G-22)*k;d[i+2]=26+(Bc-26)*k;d[i+3]=255}
    o.oc.putImageData(img,0,0);c.imageSmoothingEnabled=true;c.drawImage(o.off,0,0,W,H)}})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx176` rules from `site/fx.css`

_No dedicated `.fx176` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #176
