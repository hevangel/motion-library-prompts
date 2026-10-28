# 209 · Bento Grid Expand — Bento 格局展開

Hover over one cell of the bento grid and that cell grows while the other cells yield space in sync

- Component: Layout · Pages (`layout`)
- Timing: Hover · Click
- Tech: CSS
- Uses: UI Interaction, Headline · Hero
- Style / keywords: Bento Lunch Box Grid Mesh Expand Enlarge Feature Introduction Bento Grid Expand Hover Feature Layout Page Web Structure
- Tag: CSS grid
- Example text: "Design Development Strategy Brand Data Community" (stage background: dark)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Bento Grid Expand (Bento 格局展開)" motion effect: A Bento (lunch-box style) 3x2 grid; when the mouse moves over a cell, the column and row containing that cell enlarge (column width about 2.4x, row height about 1.8x), the other cells shrink in sync to yield space, the whole grid smoothly redistributes, and the title in the enlarged cell also grows in sync; when the mouse leaves, it returns to even sizes. About 0.55 seconds, ease-in-out. (CSS: the container's grid-template-columns / rows use fr values; on hover, JS rewrites the fr values of the target column and row, and a transition is added to grid-template-columns and grid-template-rows)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx209">`, preview text "Design Development Strategy Brand Data Community". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Bento Grid Expand".

### JavaScript — `FX[209]` from `site/fx.js`

```js
209(s,x,card){const w=el('div','ly-bn');const ws=words(x);const L=[[0,0],[1,0],[2,0],[0,1],[1,1],[2,1]];const tiles=L.map(([c,r],i)=>{const t=el('div','ly-bt');t.style.gridArea=`${r+1}/${c+1}`;t.style.background=i%2?'#22242b':`linear-gradient(140deg,${GC[i%5]},${GC[(i+1)%5]})`;t.innerHTML='<b></b>';t.querySelector('b').textContent=ws[i%ws.length];w.append(t);return t});s.append(w);let real=false,k=0;
  const big=i=>{const c=['1fr','1fr','1fr'],r=['1fr','1fr'];if(i!=null){c[L[i][0]]='2.4fr';r[L[i][1]]='1.8fr'}w.style.gridTemplateColumns=c.join(' ');w.style.gridTemplateRows=r.join(' ');tiles.forEach((t,j)=>t.classList.toggle('on',j===i))};
  tiles.forEach((t,i)=>t.addEventListener('pointerenter',()=>{real=true;big(i)}));w.addEventListener('pointerleave',()=>{real=false;big(null)});card._timers.push(setInterval(()=>{if(!real)big(k++%7<6?(k-1)%7:null)},1400))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx209` rules from `site/fx.css`

_No dedicated `.fx209` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #209
