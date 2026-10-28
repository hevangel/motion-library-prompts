# 144 · Tab Bar Indicator — 底部導覽列切換

When a tab is tapped, the pill indicator stretches and slides to the new position, and the icon pops

- Component: Layout · Pages (`layout`)
- Timing: Switch, Hover · Click
- Tech: GSAP
- Uses: App Interface, UI Interaction
- Style / keywords: Bottom Navigation Bar Tabs tab bar Navigation Indicator Switch Bottom Navigation Indicator Gooey App Mobile Mobile Device Micro-interaction Mobile App Micro-interaction
- Tag: Tab bar
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Tab Bar Indicator (底部導覽列切換)" motion effect: An app's pill-shaped bottom navigation bar has 4 icons, with a pill indicator under the current tab; when another tab is tapped, the indicator first stretches toward the target, covering both the old and new positions at once (about 0.18 seconds), then contracts onto the new tab (about 0.34 seconds, decelerating), flowing across like liquid; the new tab's icon simultaneously pops back from 0.7x to its original size, contrasting with the indicator. (GSAP: a two-stage timeline changes the indicator's x and width; the icon scale uses back.out(3))
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx144">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Tab Bar Indicator".

### JavaScript — `FX[144]` from `site/fx.js`

```js
144(s,x,card){const IC=['<path d="M3 11l9-8 9 8"/><path d="M5 10v10h14V10"/>','<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/>','<path d="M12 20s-7-4.5-9-9a5 5 0 0 1 9-3 5 5 0 0 1 9 3c-2 4.5-9 9-9 9z"/>','<circle cx="12" cy="8" r="4"/><path d="M4 21c1-4 4.5-6 8-6s7 2 8 6"/>'];
  const bar=el('div','tbar');const ind=el('i','tind');bar.append(ind);const tabs=IC.map((d,i)=>{const t=el('button','tab');t.innerHTML=`<svg viewBox="0 0 24 24">${d}</svg>`;bar.append(t);return t});s.append(bar);let cur=0,real=0;
  const go=(j,first)=>{const a=tabs[cur],b=tabs[j];tabs.forEach((t,k)=>t.classList.toggle('on',k===j));if(first||!b.offsetWidth){gsap.set(ind,{x:b.offsetLeft,width:b.offsetWidth});cur=j;return}
    const L=Math.min(a.offsetLeft,b.offsetLeft),R=Math.max(a.offsetLeft+a.offsetWidth,b.offsetLeft+b.offsetWidth);
    gsap.timeline().to(ind,{x:L,width:R-L,duration:.18,ease:'power2.in'}).to(ind,{x:b.offsetLeft,width:b.offsetWidth,duration:.34,ease:'power3.out'});gsap.fromTo(b.querySelector('svg'),{scale:.7},{scale:1,duration:.45,ease:'back.out(3)'});cur=j};
  tabs.forEach((t,i)=>t.onclick=()=>{real=Date.now();go(i)});go(0,true);card._timers.push(setInterval(()=>{if(Date.now()-real>3000)go((cur+1)%4)},1300))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx144` rules from `site/fx.css`

_No dedicated `.fx144` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #144
