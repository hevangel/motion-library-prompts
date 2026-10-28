# 139 · Circular Progress — 圓環進度

A ring draws to a specified percentage while the number in the middle counts up in sync

- Component: Shapes · SVG (`shape`)
- Timing: Entrance
- Tech: GSAP
- Uses: Numbers & Data
- Style / keywords: Progress Ring Percentage Gauge Data Statistics Progress Ring Donut Percentage Gauge Stats
- Tag: DrawSVG
- Example text: "Project Completion" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Circular Progress (圓環進度)" motion effect: A circular progress chart, with a low-contrast track ring underneath. On entry, the progress arc starts at the very top and draws clockwise to a specified percentage (for example 78%), with a rounded line cap; the percentage number in the middle counts up in sync from 0 to 78%, with small text underneath labeling the item's name; about 1.8 seconds, ease-in-out, stopping at the result. (GSAP: DrawSVGPlugin drawSVG "0%"→"0% 78%", the SVG as a whole rotate(-90deg) so the start point is at the top; the number tweens an object value + onUpdate to write it in, with the same timing and ease as the arc)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx139">`, preview text "Project Completion". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Circular Progress".

### JavaScript — `FX[139]` from `site/fx.js`

```js
139(s,x){const w=el('div','cpg');w.innerHTML='<svg viewBox="0 0 100 100"><circle class="tr" cx="50" cy="50" r="40"/><circle class="br" cx="50" cy="50" r="40"/></svg><div class="cv"><b>0%</b><span></span></div>';w.querySelector('span').textContent=x;s.append(w);const b=w.querySelector('b'),o={v:0};
  gsap.timeline({repeat:-1,repeatDelay:.4}).set(w,{opacity:1},0).fromTo(w.querySelector('.br'),{drawSVG:'0%'},{drawSVG:'0% 78%',duration:1.8,ease:'power2.inOut'},0).fromTo(o,{v:0},{v:78,duration:1.8,ease:'power2.inOut',onUpdate:()=>b.textContent=Math.round(o.v)+'%'},0).to(w,{opacity:0,duration:.5},'+=1.6')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx139` rules from `site/fx.css`

_No dedicated `.fx139` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #139
