# 326 · Organic Blob — 有機流動色塊

An irregular, soft blob keeps slowly morphing, with another fainter shadow layer behind it

- Component: Shapes · SVG (`shape`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Background Decoration, Headline · Hero, Emphasis
- Style / keywords: Organic Blob Spot Flowing Morphing Liquid Blob Organic Shape Morph Liquid Graphics SVG
- Tag: JS + SVG
- Example text: "Blob" (stage background: dark)
- Added: 2026-10-21

**AI prompt (English copy format):**

```text
"Organic Blob (有機流動色塊)" motion effect: An organic, irregular blob (like soft liquid or jelly) whose edges are driven by multiple sets of sine waves at different frequencies, continuously and slowly morphing and never repeating; behind it there is also a slightly larger, fainter shadow layer in the same color morphing at a different rhythm, adding depth; text is placed in the center of the blob. (JS requestAnimationFrame: take 8 control points distributed around a circle, radius = base + the sum of several sin(time + index × phase) values, and use Catmull-Rom to convert them into a smooth cubic Bézier curve written into the path's d)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx326">`, preview text "Blob". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Organic Blob".

### JavaScript — `FX[326]` from `site/fx.js`

```js
326(s,x,card){const w=el('div','sv-blw');w.innerHTML='<svg viewBox="-60 -60 120 120"><path class="b2"/><path class="b1"/></svg>';const t=T(x,Math.min(11,50/chars(x).length));t.classList.add('sv-blt');w.append(t);s.append(w);const [p2,p1]=w.querySelectorAll('path');
  const shape=(t,R,seed)=>{const N=8,pts=[];for(let i=0;i<N;i++){const a=i/N*Math.PI*2,r=R+R*.16*Math.sin(t*1.1+i*1.7+seed)+R*.1*Math.sin(t*.7+i*2.9+seed*2);pts.push([Math.cos(a)*r,Math.sin(a)*r])}
    let d='';for(let i=0;i<N;i++){const p0=pts[(i-1+N)%N],a=pts[i],b=pts[(i+1)%N],c=pts[(i+2)%N];if(!i)d+=`M${a[0].toFixed(1)},${a[1].toFixed(1)}`;d+=`C${(a[0]+(b[0]-p0[0])/6).toFixed(1)},${(a[1]+(b[1]-p0[1])/6).toFixed(1)} ${(b[0]-(c[0]-a[0])/6).toFixed(1)},${(b[1]-(c[1]-a[1])/6).toFixed(1)} ${b[0].toFixed(1)},${b[1].toFixed(1)}`}return d+'Z'};
  ticks.set(card,t=>{p1.setAttribute('d',shape(t,40,0));p2.setAttribute('d',shape(t*.8,46,3))})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx326` rules from `site/fx.css`

_No dedicated `.fx326` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #326
