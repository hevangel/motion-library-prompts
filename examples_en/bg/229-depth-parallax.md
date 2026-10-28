# 229 · Depth Parallax — 景深視差圖層

Three layers of graphics, front, middle and back, move in reverse following the cursor at different magnitudes according to distance, creating a sense of depth

- Component: Background · Ambience (`bg`)
- Timing: Hover · Click
- Tech: CSS
- Uses: Headline · Hero, Background Decoration
- Style / keywords: Parallax Depth Layers Three-Dimensional Mouse Cursor Mouse Parallax Depth Layers 3D Hero Background Atmosphere
- Tag: JS parallax
- Example text: "Depth" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Depth Parallax (景深視差圖層)" motion effect: A Hero background made of three layers of decorative graphics: the far layer is a blurred large circle, the middle layer is a rounded square, and the front layer is a hollow ring, with the title sandwiched between the middle and front layers; when the cursor moves inside the section, each layer moves in the opposite direction from the cursor, with layers closer to the viewer moving more (for example far layer 15%, middle layer 45%, front layer 100%), and the title moves only slightly, creating a three-dimensional sense of depth, with smooth delayed following in the movement. (JS: mousemove calculates the cursor's ratio relative to the center, -0.5 to 0.5; each layer's translate = -ratio x that layer's coefficient, smoothed with a CSS transition or lerp)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx229">`, preview text "Depth". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Depth Parallax".

### JavaScript — `FX[229]` from `site/fx.js`

```js
229(s,x,card){const w=el('div','abs bga-dp');const L=[[.15,7,'o'],[.45,5,'s'],[1,4,'r']].map(([k,n,cl],li)=>{const l=el('div','abs bga-dl');l._k=k;for(let i=0;i<n;i++){const e=el('i','bga-'+cl);e.style.cssText=`left:${(i+.5)/n*100+rnd(-8,8)}%;top:${rnd(10,85)}%;--z:${(li+1)*3+rnd(0,3)}cqw;background:${cl==='r'?'transparent':li===1?'var(--a)':GC[(i+li)%5]}`;l.append(e)}w.append(l);return l});
  const t=T(x,Math.min(12,56/chars(x).length));t.classList.add('bga-dt');w.insertBefore(t,L[2]);s.append(w);
  vpointer(w,card,(px,py)=>{const W=w.offsetWidth,H=w.offsetHeight,dx=px/W-.5,dy=py/H-.5;L.forEach(l=>l.style.transform=`translate(${-dx*l._k*14}cqw,${-dy*l._k*9}cqw)`);t.style.transform=`translate(${-dx*3}cqw,${-dy*2}cqw)`})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx229` rules from `site/fx.css`

_No dedicated `.fx229` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #229
