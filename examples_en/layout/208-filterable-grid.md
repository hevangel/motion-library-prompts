# 208 · Filterable Grid — 作品篩選重排

When switching categories, works that do not match shrink away and disappear, while the other works smoothly move to fill the gaps

- Component: Layout · Pages (`layout`)
- Timing: Switch
- Tech: GSAP
- Uses: UI Interaction
- Style / keywords: Filter Category Portfolio Grid Rearrange Fill Filter Grid Portfolio Isotope Reflow Flip Layout Page Web Structure
- Tag: Flip
- Example text: "Brand Website Illustration" (stage background: dark)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Filterable Grid (作品篩選重排)" motion effect: A portfolio with category labels at the top (All / Brand / Website / Illustration); when a category is clicked, works that do not match shrink and fade out, works that match smoothly move from their original positions to new layout positions to fill the gaps, and works that reappear scale up from small and fade in; the selected category label switches to an emphasized state. About 0.6 seconds. (GSAP: use Flip.getState to record all cards, then switch display, then Flip.from, with absolute:true and onEnter / onLeave handling the scale and fade in/out for entering and leaving items)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx208">`, preview text "Brand Website Illustration". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Filterable Grid".

### JavaScript — `FX[208]` from `site/fx.js`

```js
208(s,x,card){const cats=words(x).slice(0,3);const w=el('div','ly-fw');w.innerHTML='<div class="ly-fc"></div><div class="ly-fg"></div>';const fc=w.firstChild,fg=w.lastChild;const all=['全部',...cats];const chs=all.map(v=>{const b=el('button');b.textContent=v;fc.append(b);return b});
  const tiles=[...Array(9)].map((_,i)=>{const t=el('div','ly-ft');t.dataset.c=cats[i%cats.length];t.style.background=`linear-gradient(140deg,${GC[i%3]},${GC[(i%3)+2]})`;t.innerHTML='<span></span>';t.querySelector('span').textContent=cats[i%cats.length];fg.append(t);return t});s.append(w);let k=0,real=0;
  const go=i=>{chs.forEach((b,j)=>b.classList.toggle('on',j===i));const st=Flip.getState(tiles);tiles.forEach(t=>t.style.display=(i===0||t.dataset.c===all[i])?'':'none');Flip.from(st,{duration:.6,ease:'power2.inOut',scale:true,absolute:true,onEnter:e=>gsap.fromTo(e,{opacity:0,scale:.6},{opacity:1,scale:1,duration:.5}),onLeave:e=>gsap.to(e,{opacity:0,scale:.6,duration:.4})})};
  chs.forEach((b,i)=>b.onclick=()=>{real=Date.now();go(i)});go(0);card._timers.push(setInterval(()=>{if(Date.now()-real>4000)go(++k%all.length)},1900))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx208` rules from `site/fx.css`

_No dedicated `.fx208` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #208
