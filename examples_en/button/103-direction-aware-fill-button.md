# 103 · Direction-aware Fill Button — 游標擴散填滿按鈕

Spreads to fill from the point where the mouse entered, and retracts toward the exit point on leave

- Component: Button (`button`)
- Timing: Hover · Click
- Tech: CSS
- Uses: UI Interaction, Emphasis
- Style / keywords: Button hover Direction-aware Spread Fill Ripple From Mouse Position Direction Aware Hover Fill Ripple Button CTA
- Tag: CSS + JS
- Example text: "Contact Now" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Direction-aware Fill Button (游標擴散填滿按鈕)" motion effect: An outlined pill button. When the mouse moves in, an accent-colored circle enlarges starting from "the exact point where the cursor entered the button", spreading until it fills the whole button, while the text color switches at the same time to a color that contrasts with the fill; when the mouse moves out, the circle shrinks away centered on "the point where the cursor left", so the color retracts toward whichever side it exits from. About 0.55 seconds, ease-in-out. (How it works: the button has overflow:hidden; on pointerenter / pointerleave, getBoundingClientRect is used to calculate the cursor's coordinates inside the button and write them into the CSS variables --x and --y, the circle's diameter is taken as "distance to the farthest corner × 2" to ensure full coverage; the circle uses transform:scale(0→1) as a transition)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx103">`, preview text "Contact Now". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Direction-aware Fill Button".

### JavaScript — `FX[103]` from `site/fx.js`

```js
103(s,x,card){const b=el('button','fbtn');b.setAttribute('aria-label',x);b.style.fontSize=Math.min(5,40/chars(x).length)+'cqw';const f=el('span','fl');const t=el('span','ft2');t.textContent=x;b.append(f,t);
  const cur=el('div','vcur');cur.style.transition='transform .35s ease,opacity .2s';cur.innerHTML='<svg viewBox="0 0 24 24"><path d="M3 2l17 9-7.5 2L9 20z" fill="#fff" stroke="#111" stroke-width="1.6" stroke-linejoin="round"/></svg>';s.append(b,cur);
  // 把圓心設在進入（或離開）的位置，半徑取到最遠的角，保證能蓋滿整顆按鈕
  const at=(px,py,on)=>{const W=b.offsetWidth,H=b.offsetHeight,r=Math.hypot(Math.max(px,W-px),Math.max(py,H-py));b.style.setProperty('--x',px+'px');b.style.setProperty('--y',py+'px');b.style.setProperty('--r',r*2+'px');b.classList.toggle('on',on)};
  const rel=e=>{const r=b.getBoundingClientRect();return[e.clientX-r.left,e.clientY-r.top]};let real=false,on=false;
  b.addEventListener('pointerenter',e=>{real=true;cur.style.opacity=0;at(...rel(e),true)});b.addEventListener('pointerleave',e=>{at(...rel(e),false);real=false;on=false;cur.style.opacity=''});
  // 示範：游標從按鈕隨機一邊進來、再從另一邊出去
  const edge=()=>{const W=b.offsetWidth,H=b.offsetHeight,k=Math.floor(Math.random()*4),r=Math.random();return[[0,r*H],[W,r*H],[r*W,0],[r*W,H]][k]};
  card._timers.push(setInterval(()=>{if(real)return;const[px,py]=edge();on=!on;cur.style.transform=`translate(${b.offsetLeft+px}px,${b.offsetTop+py}px)`;setTimeout(()=>{if(!real)at(px,py,on)},350)},1400))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx103` rules from `site/fx.css`

_No dedicated `.fx103` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #103
