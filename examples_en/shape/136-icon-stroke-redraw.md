# 136 · Icon Stroke Redraw — 圖示描邊 hover

Hovering over a line icon redraws its strokes and lifts it slightly

- Component: Shapes · SVG (`shape`)
- Timing: Hover · Click
- Tech: GSAP
- Uses: UI Interaction
- Style / keywords: Icon icon Line Icon hover Redraw Stroke Menu Navigation Icon Stroke Draw Hover Menu
- Tag: DrawSVG hover
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Icon Stroke Redraw (圖示描邊 hover)" motion effect: A row of line icons (home, search, heart, notifications), each placed inside a rounded-corner square frame; when the mouse moves over an icon, that icon's lines are redrawn from the beginning (about 0.7 seconds, multiple strokes staggered by 0.12 seconds), the frame border and the lines simultaneously switch to the accent color, and the icon lifts slightly by 6px and returns. (GSAP: on pointerenter, for that icon's path / circle elements, fromTo drawSVG "0%"→"100%", with overwrite:true to avoid conflicts when hovering across quickly)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx136">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Icon Stroke Redraw".

### JavaScript — `FX[136]` from `site/fx.js`

```js
136(s,x,card){const IC=['<path d="M3 11l9-8 9 8"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/>','<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/>','<path d="M12 20s-7-4.5-9-9a5 5 0 0 1 9-3 5 5 0 0 1 9 3c-2 4.5-9 9-9 9z"/>','<path d="M6 16v-5a6 6 0 0 1 12 0v5l2 2H4z"/><path d="M10 20a2 2 0 0 0 4 0"/>'];
  const w=el('div','icr');const tiles=IC.map(d=>{const t=el('div','ict');t.innerHTML=`<svg viewBox="0 0 24 24">${d}</svg>`;w.append(t);return t});s.append(w);
  const run=t=>{gsap.fromTo(t.querySelectorAll('path,circle'),{drawSVG:'0%'},{drawSVG:'100%',duration:.7,ease:'power2.inOut',stagger:.12,overwrite:true});gsap.fromTo(t,{y:0},{y:-6,duration:.3,yoyo:true,repeat:1,ease:'power2.out',overwrite:true});tiles.forEach(o=>o.classList.toggle('on',o===t))};
  let real=false,k=0;tiles.forEach(t=>t.addEventListener('pointerenter',()=>{real=true;run(t)}));w.addEventListener('pointerleave',()=>real=false);card._timers.push(setInterval(()=>{if(!real)run(tiles[k++%4])},1200))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx136` rules from `site/fx.css`

_No dedicated `.fx136` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #136
