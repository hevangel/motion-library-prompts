# 199 · Donut Chart Segments — 圓餅圖分段

A donut chart is drawn segment by segment, and the legend slides in in sequence

- Component: Shapes · SVG (`shape`)
- Timing: Entrance, Scroll-triggered
- Tech: GSAP
- Uses: Numbers & Data
- Style / keywords: pie chart donut chart donut proportion chart data Donut Pie Chart Segments Data SVG graphic
- Tag: DrawSVG
- Example text: "Traffic Sources" (stage background: dark)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Donut Chart Segments (圓餅圖分段)" motion effect: Donut chart entrance: starting from the very top, the arc segment of the first category is drawn clockwise, then the next segment continues drawing from the previous segment's endpoint, completing the whole circle in sequence, with small gaps kept between segments and each segment in a different category color; the center shows the total and title, and the legend on the right slides in from the right in sequence. (GSAP: each segment is a full circle, drawn to the specified section with DrawSVGPlugin's drawSVG "start% start%" to "start% end%"; the SVG is rotate(-90deg) so the starting point is at the top)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx199">`, preview text "Traffic Sources". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Donut Chart Segments".

### JavaScript — `FX[199]` from `site/fx.js`

```js
199(s,x){const V=[42,28,18,12],Lb=['搜尋','社群','直接','其他'],C=['#ff7a2f','#7c5cff','#00c8ff','#ffd23f'];let acc=0;const seg=V.map((v,i)=>{const a=acc;acc+=v;return [a,acc,C[i]]});
  const w=el('div','dnw');w.innerHTML=`<div class="dn"><svg viewBox="0 0 100 100">${seg.map(([a,b,c])=>`<circle cx="50" cy="50" r="38" stroke="${c}"/>`).join('')}</svg><div class="dnc"><b>100%</b><span></span></div></div><ul>${V.map((v,i)=>`<li><i style="background:${C[i]}"></i>${Lb[i]}<em>${v}%</em></li>`).join('')}</ul>`;w.querySelector('.dnc span').textContent=x;s.append(w);
  const cs=w.querySelectorAll('circle'),tl=gsap.timeline({repeat:-1,repeatDelay:.4}).set(w,{opacity:1},0);seg.forEach(([a,b],i)=>tl.fromTo(cs[i],{drawSVG:`${a}% ${a}%`},{drawSVG:`${a+.6}% ${b-.6}%`,duration:.5+(b-a)/100,ease:'power2.inOut'},i?'-=.15':0));
  tl.fromTo(w.querySelectorAll('li'),{x:10,opacity:0},{x:0,opacity:1,stagger:.1,duration:.4},.4).to(w,{opacity:0,duration:.5},'+=1.8')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx199` rules from `site/fx.css`

_No dedicated `.fx199` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #199
