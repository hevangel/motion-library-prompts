# 207 · Directional Tabs — 分頁標籤切換

The underline indicator slides to the new tab, and the content alternates sliding left or right depending on the switch direction

- Component: Layout · Pages (`layout`)
- Timing: Switch
- Tech: GSAP
- Uses: UI Interaction, App Interface
- Style / keywords: Pagination Tab Label tab Switch Direction Content Tabs Directional Slide Indicator Layout Page Web Structure
- Tag: GSAP
- Example text: "Design Development Marketing" (stage background: dark)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Directional Tabs (分頁標籤切換)" motion effect: A set of tabs; when another tab is clicked, the underline indicator below the tabs smoothly slides to the new tab and adjusts to its width; the content area slides according to the switch direction - when switching to a tab on the right, the old content slides out to the left and fades out, and the new content slides in from the right and fades in, and the opposite when switching left, so the user feels the before-and-after order of the tabs. About 0.45 seconds. (GSAP: compare the old and new indexes to decide the direction d, tween the old content to xPercent -30 x d and fade it out before removing it, bring the new content in from xPercent 30 x d; set the indicator's transform and width using offsetLeft / offsetWidth)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx207">`, preview text "Design Development Marketing". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Directional Tabs".

### JavaScript — `FX[207]` from `site/fx.js`

```js
207(s,x,card){const ws=words(x).slice(0,3);const w=el('div','ly-tabs');w.innerHTML='<div class="ly-th"><i class="ly-ti"></i></div><div class="ly-tp"></div>';const th=w.firstChild,tp=w.lastChild;const hs=ws.map(v=>{const b=el('button');b.textContent=v;th.append(b);return b});s.append(w);let cur=0,real=0;
  const panel=i=>{const p=el('div','ly-pn');p.innerHTML='<b></b><i class="ly-bl"></i><i class="ly-bl s"></i><div class="ly-gr"><i></i><i></i><i></i></div>';p.querySelector('b').textContent=ws[i]+' 的內容';p.querySelectorAll('.ly-gr i').forEach((e,j)=>e.style.background=GC[(i+j)%5]);return p};
  tp.append(panel(0));const ind=th.querySelector('.ly-ti');const mv=i=>{ind.style.width=hs[i].offsetWidth+'px';ind.style.transform=`translateX(${hs[i].offsetLeft}px)`;hs.forEach((h,j)=>h.classList.toggle('on',j===i))};requestAnimationFrame(()=>mv(0));
  const go=i=>{if(i===cur)return;const d=i>cur?1:-1;const old=tp.firstChild,nw=panel(i);tp.append(nw);gsap.to(old,{xPercent:-30*d,opacity:0,duration:.35,ease:'power2.in',onComplete:()=>old.remove()});gsap.fromTo(nw,{xPercent:30*d,opacity:0},{xPercent:0,opacity:1,duration:.45,ease:'power3.out',delay:.15});mv(i);cur=i};
  hs.forEach((h,i)=>h.onclick=()=>{real=Date.now();go(i)});card._timers.push(setInterval(()=>{if(Date.now()-real>4000)go((cur+1)%hs.length)},1700))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx207` rules from `site/fx.css`

_No dedicated `.fx207` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #207
