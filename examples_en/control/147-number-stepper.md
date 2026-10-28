# 147 · Number Stepper — 數量步進器

Tapping plus or minus gives button feedback, and the number rolls up or down to switch

- Component: Form · Controls (`control`)
- Timing: Hover · Click, Switch
- Tech: CSS
- Uses: App Interface, UI Interaction, Numbers & Data
- Style / keywords: Quantity Plus Minus Stepper Cart Count Stepper Counter Quantity Plus Minus Cart App Mobile Mobile Device Micro-interaction Mobile App Micro-interaction
- Tag: Stepper
- Example text: "Quantity" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Number Stepper (數量步進器)" motion effect: A quantity selector for a shopping cart: minus and plus round buttons on the left and right, and a number in the middle; when a button is pressed, the button shrinks and switches to the accent color as feedback, and the number scrolls to switch according to direction — when increasing, the old number slides out upward and the new number slides in from below; when decreasing, the direction is reversed — about 0.3 seconds; at the upper and lower limits, the number no longer changes. (CSS: the number container has overflow:hidden; the old and new numbers each use keyframes with translateY ±100% to enter and exit, and the old element is removed when finished)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx147">`, preview text "Quantity". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Number Stepper".

### JavaScript — `FX[147]` from `site/fx.js`

```js
147(s,x,card){const w=el('div','stw');w.innerHTML='<span class="sl2"></span><div class="stp2"><button aria-label="減少">−</button><div class="nv2"><b>1</b></div><button aria-label="增加">+</button></div>';w.querySelector('.sl2').textContent=x;s.append(w);
  const box=w.querySelector('.nv2'),[m,p]=w.querySelectorAll('button');let n=1,real=0,dir=1;
  const set=(d,btn)=>{btn.classList.add('pr');setTimeout(()=>btn.classList.remove('pr'),150);const nn=Math.max(0,Math.min(9,n+d));if(nn===n)return;const o=box.lastChild;const nb=el('b',d>0?'in-up':'in-dn');nb.textContent=nn;o.className=d>0?'out-up':'out-dn';box.append(nb);setTimeout(()=>o.remove(),300);n=nn};
  m.onclick=()=>{real=Date.now();set(-1,m)};p.onclick=()=>{real=Date.now();set(1,p)};card._timers.push(setInterval(()=>{if(Date.now()-real<3000)return;if(n>=4)dir=-1;if(n<=1)dir=1;set(dir,dir>0?p:m)},900))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx147` rules from `site/fx.css`

_No dedicated `.fx147` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #147
