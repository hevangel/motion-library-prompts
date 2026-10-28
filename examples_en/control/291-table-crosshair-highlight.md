# 291 · Table Crosshair Highlight — 表格十字高亮

When you hover over a cell in a table, its entire row and column light up faintly, and that cell enlarges to stand out

- Component: Form · Controls (`control`)
- Timing: Hover · Click
- Tech: CSS
- Uses: Numbers & Data, UI Interaction
- Style / keywords: Table Data Row Column Highlight Crosshair Table Row Column Highlight Crosshair Hover Data hover Hover Mouseover
- Tag: JS + CSS
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-20

**AI prompt (English copy format):**

```text
"Table Crosshair Highlight (表格十字高亮)" motion effect: A data table: when the mouse hovers over a cell, the entire row and column containing that cell light up faintly to form a cross, and the cell being pointed at fills with an accent background color, its text becomes bold and it enlarges slightly, so you can quickly cross-check the row heading and column heading; as you move to other cells the cross moves with it, and when you leave the table everything resets. (JS: on pointerover, find the td's cellIndex and its containing tr, and add a class to each; CSS: .row and .col use a very faint translucent background color, the pointed-at cell uses the accent background color + scale(1.12), transition 0.25 seconds)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx291">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Table Crosshair Highlight".

### JavaScript — `FX[291]` from `site/fx.js`

```js
291(s,x,card){const t=el('table','ho-tb');const H=['','一月','二月','三月','四月'],R=[['網站',42,58,61,77],['App',31,36,52,49],['商店',18,24,29,41]];t.innerHTML='<thead><tr>'+H.map(h=>`<th>${h}</th>`).join('')+'</tr></thead><tbody>'+R.map(r=>'<tr>'+r.map((v,i)=>i?`<td>${v}</td>`:`<th>${v}</th>`).join('')+'</tr>').join('')+'</tbody>';s.append(t);
  const cells=[...t.querySelectorAll('td')];const set=td=>{t.querySelectorAll('.r,.c,.x').forEach(e=>e.classList.remove('r','c','x'));if(!td)return;const ci=td.cellIndex;td.parentElement.classList.add('r');t.querySelectorAll('tr').forEach(tr=>tr.children[ci]&&tr.children[ci].classList.add('c'));td.classList.add('x')};
  let real=false,k=0;t.addEventListener('pointerover',e=>{real=true;set(e.target.closest('td'))});t.addEventListener('pointerleave',()=>{real=false;set(null)});card._timers.push(setInterval(()=>{if(!real)set(cells[(k=(k+5)%cells.length)])},900))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx291` rules from `site/fx.css`

_No dedicated `.fx291` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #291
