# 155 · Count Up on Scroll — 數據捲到才計數

Numbers only start counting up from zero when the data section scrolls into view

- Component: Cards · Groups (`card`)
- Timing: Scroll-triggered, Entrance
- Tech: GSAP
- Uses: Numbers & Data, Scroll Effects
- Style / keywords: Data Statistics Count Numbers Results KPI Count Up Stats Numbers On Scroll Scroll Scroll scroll ScrollTrigger scrub Scroll-triggered
- Tag: ScrollTrigger
- Example text: "Projects Completed Client Satisfaction Average Rating" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Count Up on Scroll (數據捲到才計數)" motion effect: A results-data section in the middle of the page (three cells: a number + a label). When scrolled to the point where the data section is about 80% into the viewport, the three cells fade in from below in sequence while the numbers count up from 0 to their target values at the same time (for example 128, 99%, 4.9, decimals allowed), about 1.6 seconds, decelerating; scrolling back up out of view resets it, so it plays again the next time it is scrolled to (or plays only once). (GSAP: ScrollTrigger.create { start:"top 80%", onEnter, onLeaveBack }; the number tweens an object value + onUpdate, using toFixed to control the number of decimal places)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx155">`, preview text "Projects Completed Client Satisfaction Average Rating". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Count Up on Scroll".

### JavaScript — `FX[155]` from `site/fx.js`

```js
155(s,x){const sc=el('div','scr nopad');const ws=words(x);const T3=[[128,'',0],[99,'%',0],[4.9,'',1]];sc.innerHTML='<div class="sp1">↓ 往下捲到數據區</div><div class="stg"></div><div class="sp2"></div>';const g=sc.querySelector('.stg');
  const its=T3.map(([v,u,d],i)=>{const e=el('div','sti');e.innerHTML='<b>0</b><span></span>';e.querySelector('span').textContent=ws[i%ws.length];g.append(e);return [e,v,u,d]});s.append(sc);
  const play=()=>{gsap.fromTo(its.map(a=>a[0]),{y:16,opacity:0},{y:0,opacity:1,duration:.6,stagger:.12,ease:'power2.out',overwrite:true});its.forEach(([e,v,u,d])=>{const o={v:0},b=e.querySelector('b');gsap.to(o,{v,duration:1.6,ease:'power2.out',onUpdate:()=>b.textContent=o.v.toFixed(d)+u})})};
  const reset=()=>its.forEach(([e])=>{gsap.set(e,{opacity:0});e.querySelector('b').textContent='0'});reset();
  ScrollTrigger.create({trigger:g,scroller:sc,start:'top 80%',onEnter:play,onLeaveBack:reset});autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx155` rules from `site/fx.css`

_No dedicated `.fx155` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #155
