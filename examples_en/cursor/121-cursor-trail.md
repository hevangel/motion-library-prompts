# 121 · Cursor Trail — 游標拖尾軌跡

A line trails behind the cursor, growing thinner and fainter

- Component: Cursor (`cursor`)
- Timing: Hover · Click, Loop · Idle
- Tech: Canvas
- Uses: UI Interaction, Background Decoration
- Style / keywords: Cursor Trail Trajectory Line Afterimage Cursor Trail Line Comet Canvas
- Tag: Canvas trail
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Cursor Trail (游標拖尾軌跡)" motion effect: When the cursor moves, a smooth line trails behind it — thicker and clearer the closer it is to the cursor, thinner and more transparent toward the tail, like a comet's tail; when the cursor stops, the tail gradually retracts to the cursor's position; the cursor itself is a small dot. (Canvas 2D: each frame, push the cursor coordinates into an array and keep only the most recent ~28 points, draw line segments in sequence, with line width and opacity increasing with the index; set the canvas size according to devicePixelRatio; the container uses cursor:none)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx121">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Cursor Trail".

### JavaScript — `FX[121]` from `site/fx.js`

```js
121(s,x,card){const cv=el('canvas','pnet trail');s.append(cv);const ctx=cv.getContext('2d');const col=getComputedStyle(s).getPropertyValue('--a').trim()||'#ff7a2f';let pts=[],m=null;
  cv.addEventListener('pointermove',e=>{const r=cv.getBoundingClientRect();m=[e.clientX-r.left,e.clientY-r.top]});cv.addEventListener('pointerleave',()=>m=null);
  ticks.set(card,t=>{const dpr=devicePixelRatio||1,W=s.offsetWidth,H=s.offsetHeight;if(!W)return;if(cv.width!==Math.round(W*dpr)){cv.width=Math.round(W*dpr);cv.height=Math.round(H*dpr)}
    const p=m||[W*(.5+.38*Math.sin(t*1.7)),H*(.5+.3*Math.sin(t*2.6+1))];pts.push(p);if(pts.length>28)pts.shift();
    ctx.setTransform(dpr,0,0,dpr,0,0);ctx.clearRect(0,0,W,H);ctx.lineCap='round';ctx.strokeStyle=col;
    for(let i=1;i<pts.length;i++){const k=i/pts.length;ctx.globalAlpha=k;ctx.lineWidth=k*W*.022;ctx.beginPath();ctx.moveTo(...pts[i-1]);ctx.lineTo(...pts[i]);ctx.stroke()}
    ctx.globalAlpha=1;ctx.fillStyle='#fff';ctx.beginPath();ctx.arc(p[0],p[1],W*.012,0,7);ctx.fill()})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx121` rules from `site/fx.css`

_No dedicated `.fx121` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #121
