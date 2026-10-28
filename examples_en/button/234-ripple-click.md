# 234 · Ripple Click — 按鈕漣漪回饋

A ripple spreads out from the exact position the finger taps, the classic Material Design feedback

- Component: Button (`button`)
- Timing: Hover · Click
- Tech: CSS
- Uses: UI Interaction, App Interface
- Style / keywords: Ripple Water Wave Click Feedback Material Design Ripple Click Feedback Ink Button
- Tag: JS + CSS
- Example text: "Submit Form" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Ripple Click (按鈕漣漪回饋)" motion effect: When the button is clicked, a circular ripple spreads out from the exact point the finger (cursor) pressed, semi-transparent, growing from small to large enough to cover the whole button while fading out at the same time, about 0.7 seconds; consecutive clicks can produce multiple ripples at once. (JS: on pointerdown, calculate the click position and the distance to the farthest corner x 2 as the diameter, insert a circular span, CSS keyframes scale 0 to 1 with opacity fading, and remove it on animationend; the button has overflow:hidden)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx234">`, preview text "Submit Form". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Ripple Click".

### JavaScript — `FX[234]` from `site/fx.js`

```js
234(s,x,card){const b=bxBtn('bx-rp',x);s.append(b);const rip=(px,py)=>{const r=el('i');const W=b.offsetWidth,H=b.offsetHeight,d=Math.hypot(Math.max(px,W-px),Math.max(py,H-py))*2;r.style.cssText=`left:${px}px;top:${py}px;width:${d}px;height:${d}px`;b.append(r);r.addEventListener('animationend',()=>r.remove())};
  b.addEventListener('pointerdown',e=>{const r=b.getBoundingClientRect();rip(e.clientX-r.left,e.clientY-r.top)});bxDemo(b,card,()=>rip(rnd(.15,.85)*b.offsetWidth,rnd(.2,.8)*b.offsetHeight),1100)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx234` rules from `site/fx.css`

_No dedicated `.fx234` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #234
