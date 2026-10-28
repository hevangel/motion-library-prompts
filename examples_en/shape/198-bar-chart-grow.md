# 198 · Bar Chart Grow — 長條圖成長

Bars grow upward from the bottom in sequence with a slight rebound, and the values accumulate in sync

- Component: Shapes · SVG (`shape`)
- Timing: Entrance, Scroll-triggered
- Tech: GSAP
- Uses: Numbers & Data
- Style / keywords: bar chart column chart chart data statistics Dashboard Bar Chart Column Graph Data SVG graphic
- Tag: Stagger
- Example text: "Monthly Page Views" (stage background: dark)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Bar Chart Grow (長條圖成長)" motion effect: Bar chart entrance: each bar grows upward from the baseline in sequence (0.1 seconds apart) with a slight overshoot and rebound, while the value at the top of the bar accumulates from 0 to the actual number at the same time, with month labels shown below. Suitable for reports and results pages. (GSAP: the bars' transform-origin is at the bottom, fromTo scaleY 0 to 1, ease back.out(1.6); the values tween an object value + onUpdate; it can be played when scrolled to, paired with ScrollTrigger)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx198">`, preview text "Monthly Page Views". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Bar Chart Grow".

### JavaScript — `FX[198]` from `site/fx.js`

```js
198(s,x){const V=[42,65,38,80,58,92],L=['1月','2月','3月','4月','5月','6月'];const w=el('div','bcw');w.innerHTML='<b></b><div class="bars">'+V.map((v,i)=>`<div class="bc"><span>0</span><i style="height:${v}%"></i><em>${L[i]}</em></div>`).join('')+'</div>';w.querySelector('b').textContent=x;s.append(w);
  const tl=gsap.timeline({repeat:-1,repeatDelay:.4}).set(w,{opacity:1},0);w.querySelectorAll('.bc').forEach((c,i)=>{const o={v:0},sp=c.querySelector('span');tl.fromTo(c.querySelector('i'),{scaleY:0},{scaleY:1,duration:.8,ease:'back.out(1.6)'},i*.1).fromTo(o,{v:0},{v:V[i],duration:.8,ease:'power2.out',onUpdate:()=>sp.textContent=Math.round(o.v)},i*.1)});tl.to(w,{opacity:0,duration:.5},'+=1.8')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx198` rules from `site/fx.css`

_No dedicated `.fx198` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #198
