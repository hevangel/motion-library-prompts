# 095 · Magnetic Button — 磁吸按鈕

The button is pulled toward the cursor and springs back

- Component: Button (`button`)
- Timing: Hover · Click
- Tech: GSAP
- Uses: UI Interaction
- Style / keywords: 
- Tag: quickTo·Elastic
- Example text: "Press Me" (stage background: cream)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Magnetic Button (磁吸按鈕)" motion effect: When the cursor approaches the button, the button is pulled toward the cursor's direction, while the text inside the button moves less, creating a layered effect, and it switches to the accent color at the same time; when the cursor leaves, it returns to its original position with elasticity. (GSAP: gsap.quickTo controls x/y, ease elastic.out(1,0.4))
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage cream fx95">`, preview text "Press Me". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Magnetic Button".

### JavaScript — `FX[95]` from `site/fx.js`

```js
95(s,x){const l=layer(s);const b=el('button','mbtn');const sp=el('span');sp.textContent=x;b.append(sp);l.append(b);const q=(e,k)=>gsap.quickTo(e,k,{duration:.7,ease:'elastic.out(1,.4)'});const bx=q(b,'x'),by=q(b,'y'),tx=q(sp,'x'),ty=q(sp,'y');
  pointer(l,(px,py)=>{const W=l.offsetWidth,H=l.offsetHeight,dx=px-W/2,dy=py-H/2,on=Math.hypot(dx,dy)<W*.26;bx(on?dx*.4:0);by(on?dy*.4:0);tx(on?dx*.2:0);ty(on?dy*.2:0);b.classList.toggle('on',on)},[[.15,.25],[.42,.45],[.56,.56],[.5,.5],[.85,.3],[.62,.62],[.2,.8]])}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx95` rules from `site/fx.css`

_No dedicated `.fx95` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #95
