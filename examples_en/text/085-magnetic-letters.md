# 085 · Magnetic Letters — 磁力文字

Letters are pushed away as the cursor approaches

- Component: Text (`text`)
- Timing: Hover · Click
- Tech: GSAP
- Uses: UI Interaction, Logo · Brand
- Style / keywords: 
- Tag: quickTo
- Example text: "Come Closer" (stage background: cream)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Magnetic Letters (磁力文字)" motion effect: When the cursor comes near the text, nearby letters are pushed outward and switch to the accent color — the closer the cursor, the farther they are pushed — and when the cursor leaves, they smoothly return to their original positions. (GSAP: SplitText chars, each letter's x/y controlled with gsap.quickTo, with the push force calculated from the cursor distance)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage cream fx85">`, preview text "Come Closer". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Magnetic Letters".

### JavaScript — `FX[85]` from `site/fx.js`

```js
85(s,x){const l=layer(s);const t=T(x);l.append(t);const sp=SplitText.create(t,{type:'chars'});
  const qs=sp.chars.map(c=>({c,x:gsap.quickTo(c,'x',{duration:.5,ease:'power3.out'}),y:gsap.quickTo(c,'y',{duration:.5,ease:'power3.out'})}));
  pointer(l,(px,py)=>{const r=l.getBoundingClientRect();const R=r.width*.22;qs.forEach(q=>{const b=q.c.getBoundingClientRect();const cx=b.left+b.width/2-r.left-gsap.getProperty(q.c,'x'),cy=b.top+b.height/2-r.top-gsap.getProperty(q.c,'y');const dx=cx-px,dy=cy-py,d=Math.hypot(dx,dy)||1,f=Math.max(0,1-d/R);q.x(dx/d*f*R*.7);q.y(dy/d*f*R*.7);q.c.style.color=f>.15?'var(--a)':''})})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx85` rules from `site/fx.css`

_No dedicated `.fx85` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #85
