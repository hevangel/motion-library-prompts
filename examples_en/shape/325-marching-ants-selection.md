# 325 · Marching Ants Selection — 選取框螞蟻線

The lines of a dashed selection box flow continuously, there are handles at its four corners, and the size figures update in real time as the box changes size

- Component: Shapes · SVG (`shape`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: UI Interaction, Emphasis
- Style / keywords: Selection Box Dashed Line Marching Ants Handles Design Tool Figma Marching Ants Selection Box Handles Graphics SVG
- Tag: stroke-dashoffset
- Example text: "Design Tool" (stage background: dark)
- Added: 2026-10-21

**AI prompt (English copy format):**

```text
"Marching Ants Selection (選取框螞蟻線)" motion effect: A selection box like those in design tools: a dashed rectangle frames the content, the dashes flow continuously in the same direction (commonly called marching ants), and there are square handles at the four corners; the selection box's size changes smoothly between two sizes, and the size label below it (width × height) updates its figures in real time along with it. (SVG rect: stroke-dasharray 6 5, with keyframes looping stroke-dashoffset from 0 to −11 infinitely; the box's width/height are changed with CSS keyframes; JS periodically reads the size and updates the label)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx325">`, preview text "Design Tool". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Marching Ants Selection".

### JavaScript — `FX[325]` from `site/fx.js`

```js
325(s,x,card){const w=el('div','sv-mq');w.innerHTML='<div class="sv-sel"><svg><rect x="1" y="1" width="100%" height="100%" rx="2"/></svg>'+['tl','tr','bl','br'].map(k=>`<i class="${k}"></i>`).join('')+'<span class="sv-dim"></span></div><b class="sv-mt"></b>';w.querySelector('.sv-mt').textContent=x;s.append(w);
  const sel=w.querySelector('.sv-sel'),dim=w.querySelector('.sv-dim');const upd=()=>{dim.textContent=Math.round(sel.offsetWidth*3)+' × '+Math.round(sel.offsetHeight*3)};card._timers.push(setInterval(upd,90));upd()}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx325` rules from `site/fx.css`

_No dedicated `.fx325` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #325
