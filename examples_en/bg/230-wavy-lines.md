# 230 · Wavy Lines — 起伏線條

A whole field of fine lines undulates like fabric, and the places the cursor passes are gently arched up

- Component: Background · Ambience (`bg`)
- Timing: Loop · Idle, Hover · Click
- Tech: Canvas
- Uses: Headline · Hero, Background Decoration
- Style / keywords: Lines Waves Undulate Fabric Terrain Contour Lines Wavy Lines Wave Field Terrain Canvas Interactive Background requestAnimationFrame Background Atmosphere
- Tag: Canvas 2D
- Example text: "Flow" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Wavy Lines (起伏線條)" motion effect: The entire background is about 26 horizontal fine lines, each undulating from the superposition of two sets of sine waves of different frequencies and flowing slowly over time, with adjacent lines slightly offset in phase, so the whole field looks like flowing fabric or terrain lines; among them, every few lines are accented with a thicker, brighter line; where the cursor passes, nearby lines are smoothly arched upward, and recover after it leaves. (Canvas 2D: each line takes 80 points, y = baseline + sin(x*f1 + t + j*phase) * A1 + sin(x*f2 - t + j*phase) * A2, minus a Gaussian function centered on the cursor times height)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx230">`, preview text "Flow". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Wavy Lines".

### JavaScript — `FX[230]` from `site/fx.js`

```js
230(s,x,card){cfx(s,card,{init:()=>({c:accRGB(s)}),
  frame:(c,W,H,t,dt,m,o)=>{c.fillStyle=`rgb(${BGD})`;c.fillRect(0,0,W,H);const N=26,[mx,my]=demoPt(t,W,H,m),R=W*.16;
    for(let j=0;j<N;j++){const by=H*(.08+j/N*.9),k=j/N;c.strokeStyle=j%6===3?`rgba(${o.c},.9)`:`rgba(255,255,255,${.12+k*.3})`;c.lineWidth=j%6===3?1.6:1;c.beginPath();
      for(let i=0;i<=80;i++){const X=i/80*W;let y=by+Math.sin(X*.011+t*.7+j*.35)*H*.025+Math.sin(X*.004-t*.4+j*.2)*H*.04;const d=X-mx,dy=by-my,g=Math.exp(-(d*d+dy*dy)/(2*R*R));y-=g*H*.09;i?c.lineTo(X,y):c.moveTo(X,y)}c.stroke()}}});
  const tx=T(x,Math.min(11,52/chars(x).length));tx.classList.add('cvt');s.append(tx)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx230` rules from `site/fx.css`

_No dedicated `.fx230` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #230
