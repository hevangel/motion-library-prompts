# 260 · Gooey Trail — 黏液拖尾

A trail of balls follows the cursor, merging and stretching like goo between each other

- Component: Cursor (`cursor`)
- Timing: Hover · Click
- Tech: CSS
- Uses: Headline · Hero, Background Decoration
- Style / keywords: Goo Fusion Trail Liquid Gooey Blob Trail Cursor SVG Filter Liquid Cursor Mouse
- Tag: SVG goo filter
- Example text: "Gooey" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Gooey Trail (黏液拖尾)" motion effect: Behind the cursor follows a string of balls decreasing in size, the first tightly following the mouse and each subsequent one following the one before it, forming a tail; through a blur-plus-contrast filter the balls fuse together, looking like a blob of goo being stretched long and pulling into thin strands, and shrinking back into a blob when it stops. Foreground text uses a blend mode, and the parts covered by the goo are inverted. (SVG filter: feGaussianBlur with stdDeviation about 6 + feColorMatrix amplifying alpha (for example 0 0 0 22 −9) creates the goo effect, applied to the container wrapping all the balls; JS makes each ball lerp toward the previous one every frame)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx260">`, preview text "Gooey". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Gooey Trail".

### JavaScript — `FX[260]` from `site/fx.js`

```js
260(s,x,card){const id='cg'+Math.random().toString(36).slice(2);const l=el('div','abs cr-go');l.innerHTML=`<svg width="0" height="0" style="position:absolute"><filter id="${id}"><feGaussianBlur in="SourceGraphic" stdDeviation="6"/><feColorMatrix values="1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 22 -9"/></filter></svg><div class="cr-gb" style="filter:url(#${id})"></div>`;const gb=l.querySelector('.cr-gb');
  const N=8,B=[...Array(N)].map((_,i)=>{const b=el('i');b.style.setProperty('--s',1-i/N*.7);gb.append(b);return{e:b,x:0,y:0}});const t=T(x,Math.min(12,52/chars(x).length));t.classList.add('cr-gt');l.append(t);s.append(l);let tx=0,ty=0;
  vpointer(l,card,(px,py)=>{tx=px;ty=py});const prev=ticks.get(card);ticks.set(card,tm=>{prev&&prev(tm);let ax=tx,ay=ty;B.forEach((b,i)=>{b.x+=(ax-b.x)*(i?.45:.3);b.y+=(ay-b.y)*(i?.45:.3);b.e.style.transform=`translate(${b.x}px,${b.y}px) translate(-50%,-50%) scale(var(--s))`;ax=b.x;ay=b.y})})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx260` rules from `site/fx.css`

_No dedicated `.fx260` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #260
