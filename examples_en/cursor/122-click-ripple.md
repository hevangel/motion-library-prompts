# 122 · Click Ripple — 點擊漣漪

Clicking anywhere on screen spreads a ripple from the click point

- Component: Cursor (`cursor`)
- Timing: Hover · Click
- Tech: CSS
- Uses: UI Interaction
- Style / keywords: Cursor Click Ripple Wave Feedback Click Ripple Wave Feedback Material
- Tag: Click ripple
- Example text: "Click Anywhere" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Click Ripple (點擊漣漪)" motion effect: When clicking anywhere inside the section, a translucent solid circle and an outline ring spread out from the click point at the same time (the outline ring slightly later, by 0.12 seconds), both scaling from 0 up to several times the size of a thumb and fading out, in about 0.85 seconds with strong deceleration, giving the user clear click feedback; rapid repeated clicks are possible, and the ripples overlap. (How it works: on pointerdown, create circular elements at the click coordinates, CSS keyframes do scale(0→1) + opacity(1→0), and the elements are removed when the animation ends)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx122">`, preview text "Click Anywhere". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Click Ripple".

### JavaScript — `FX[122]` from `site/fx.js`

```js
122(s,x,card){const l=el('div','abs gl rp');l.append(T(x,Math.min(9,50/chars(x).length)));const cur=el('div','vcur');cur.style.transition='transform .35s ease,opacity .2s';cur.innerHTML=ARROW;l.append(cur);s.append(l);let real=0;
  const ripple=(px,py)=>{for(let k=0;k<2;k++){const r=el('i','rpl'+(k?'':' f'));r.style.left=px+'px';r.style.top=py+'px';r.style.animationDelay=k*.12+'s';l.append(r);setTimeout(()=>r.remove(),1100)}};
  l.addEventListener('pointerdown',e=>{const r=l.getBoundingClientRect();real=Date.now();cur.style.opacity=0;ripple(e.clientX-r.left,e.clientY-r.top)});l.addEventListener('pointerleave',()=>cur.style.opacity='');
  card._timers.push(setInterval(()=>{if(Date.now()-real<3000)return;cur.style.opacity='';const W=l.offsetWidth,H=l.offsetHeight,px=W*(.2+Math.random()*.6),py=H*(.25+Math.random()*.5);cur.style.transform=`translate(${px}px,${py}px)`;setTimeout(()=>ripple(px,py),380)},1100))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx122` rules from `site/fx.css`

_No dedicated `.fx122` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #122
