# 315 · Push Navigation — 推入換頁

Click a list item and the new page pushes in from the right while the old page retreats to the left and darkens; pressing back reverses it

- Component: Layout · Pages (`layout`)
- Timing: Switch
- Tech: GSAP
- Uses: Transitions, App Interface
- Style / keywords: Push In Page Change Back Navigation iOS Stack Push Pop Navigation Stack Page Transition App Layout Page
- Tag: GSAP
- Example text: "Settings Notifications Privacy About" (stage background: dark)
- Added: 2026-10-21

**AI prompt (English copy format):**

```text
"Push Navigation (推入換頁)" motion effect: Simulate an app's page-stack navigation: when you click an item in the list, the detail page pushes in as a full page from the right (with a shadow on its left side), while the original list page simultaneously moves about 30% to the left and darkens, as if covered over by the new page; clicking "‹ Back" in the top-left reverses it: the detail page exits to the right, and the list page moves back into place and regains its brightness. About 0.5 seconds, ease-in-out. (GSAP: the new page xPercent 100 → 0, the old page xPercent 0 → −30 with filter: brightness(.6); the reverse when going back)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx315">`, preview text "Settings Notifications Privacy About". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Push Navigation".

### JavaScript — `FX[315]` from `site/fx.js`

```js
315(s,x,card){const f=lyPage(s);const ws=words(x);const vw=el('div','pg-vw');vw.innerHTML='<div class="pg-p a"><ul></ul></div><div class="pg-p b"><button class="pg-back">‹ 返回</button><div class="pg-hero">'+mdImg(2)+'</div><b></b><i class="ly-bl"></i><i class="ly-bl s"></i></div>';const ul=vw.querySelector('ul');ws.slice(0,4).forEach((t,i)=>{const li=el('li');li.innerHTML='<i></i><b></b><span>›</span>';li.querySelector('b').textContent=t;ul.append(li)});f.append(vw);
  const A=vw.querySelector('.a'),B=vw.querySelector('.b'),bt=B.querySelector('b');let inB=false,busy=false,real=0;gsap.set(B,{xPercent:100});
  const push=t=>{if(busy||inB)return;busy=true;inB=true;bt.textContent=t;gsap.timeline({onComplete:()=>busy=false}).to(A,{xPercent:-30,filter:'brightness(.6)',duration:.5,ease:'power3.inOut'},0).to(B,{xPercent:0,duration:.5,ease:'power3.inOut'},0)};
  const pop=()=>{if(busy||!inB)return;busy=true;inB=false;gsap.timeline({onComplete:()=>busy=false}).to(A,{xPercent:0,filter:'brightness(1)',duration:.45,ease:'power3.inOut'},0).to(B,{xPercent:100,duration:.45,ease:'power3.inOut'},0)};
  ul.querySelectorAll('li').forEach(li=>li.onclick=()=>{real=Date.now();push(li.querySelector('b').textContent)});B.querySelector('.pg-back').onclick=()=>{real=Date.now();pop()};let k=0;
  card._timers.push(setInterval(()=>{if(Date.now()-real<5000)return;inB?pop():push(ws[k++%ws.length])},1700))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx315` rules from `site/fx.css`

_No dedicated `.fx315` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #315
