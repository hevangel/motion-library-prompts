# 313 · Step Progress — 步驟進度條

Step dots above a multi-step form: completed ones get a checkmark, the current step enlarges, and the connecting line fills along with it

- Component: Layout · Pages (`layout`)
- Timing: Switch
- Tech: CSS
- Uses: UI Interaction, App Interface
- Style / keywords: Steps Progress Multi-step Form Checkout Wizard Stepper Multi Step Form Wizard Progress Checkout Layout Page
- Tag: CSS transition
- Example text: "Account Details Payment Done" (stage background: dark)
- Added: 2026-10-21

**AI prompt (English copy format):**

```text
"Step Progress (步驟進度條)" motion effect: A step indicator above a multi-step form (for example sign-up or checkout): a row of circular step numbers connected by a line; the dots of completed steps fill in and a checkmark appears with a bounce-back, the current step's outer ring lights up and it enlarges slightly, and steps not yet reached stay faint; the filled length of the connecting line smoothly extends along with the steps; below there are "Previous / Next" buttons. (CSS: the connecting line's inner layer uses transform:scaleX(current index / (total − 1)), transition 0.5 seconds; steps switch styles with .done / .on classes, and the checkmark uses keyframes from scale 0 → 1)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx313">`, preview text "Account Details Payment Done". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Step Progress".

### JavaScript — `FX[313]` from `site/fx.js`

```js
313(s,x,card){const ws=words(x).slice(0,4);const w=el('div','pg-st');w.innerHTML='<div class="pg-sl"><i></i></div>'+ws.map((t,i)=>`<div class="pg-sp"><b>${i+1}</b><span></span></div>`).join('')+'<div class="pg-sb"><button class="pv">上一步</button><button class="nx">下一步</button></div>';w.querySelectorAll('.pg-sp span').forEach((sp,i)=>sp.textContent=ws[i]);s.append(w);
  const ps=[...w.querySelectorAll('.pg-sp')],fill=w.querySelector('.pg-sl i');let cur=0,real=0;const go=i=>{cur=Math.max(0,Math.min(ps.length-1,i));ps.forEach((p,j)=>{p.classList.toggle('done',j<cur);p.classList.toggle('on',j===cur)});fill.style.transform=`scaleX(${cur/(ps.length-1)})`};go(0);
  w.querySelector('.nx').onclick=()=>{real=Date.now();go(cur+1)};w.querySelector('.pv').onclick=()=>{real=Date.now();go(cur-1)};card._timers.push(setInterval(()=>{if(Date.now()-real>5000)go(cur===ps.length-1?0:cur+1)},1300))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx313` rules from `site/fx.css`

_No dedicated `.fx313` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #313
