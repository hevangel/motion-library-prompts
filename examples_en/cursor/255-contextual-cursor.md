# 255 · Contextual Cursor — 情境標籤游標

When the cursor moves onto different content, it becomes a large circle with text for the corresponding action, such as play, view, or drag

- Component: Cursor (`cursor`)
- Timing: Hover · Click
- Tech: CSS
- Uses: UI Interaction, Headline · Hero
- Style / keywords: Context Label Cursor Play View Drag Portfolio Contextual Label Cursor View Play Drag Portfolio Cursor Mouse
- Tag: JS + CSS
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Contextual Cursor (情境標籤游標)" motion effect: A card area in a portfolio, where the cursor is normally a small dot; when moving onto different types of content, the small dot elastically enlarges into a solid large circle, displaying the corresponding icon in the middle, with action text floating out below, for example a video shows “▶ Play”, a work shows “↗ View”, and a carousel shows “⇆ Drag”; when leaving the content it shrinks back to a small dot. (JS: each area sets its text and icon with a data-cursor attribute, mousemove detects the current area and updates the cursor content; CSS: the large circle scale 0 → 1 uses cubic-bezier(.3,1.5,.5,1), and the text fades in and moves up)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx255">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Contextual Cursor".

### JavaScript — `FX[255]` from `site/fx.js`

```js
255(s,x,card){const l=el('div','abs gl cr-ct');const g=el('div','cr-cg');const K=[['播放','▶'],['查看','↗'],['拖曳','⇆']];const it=K.map(([lb,ic],i)=>{const d=el('div','cr-ci');d.dataset.lb=lb;d.dataset.ic=ic;d.style.background=`linear-gradient(135deg,${GC[i]},${GC[(i+2)%5]})`;g.append(d);return d});
  const c=el('div','cr-cc');c.innerHTML='<b></b><span></span>';l.append(g,c);s.append(l);const [ib,sp]=[c.querySelector('b'),c.querySelector('span')];
  vpointer(l,card,(px,py)=>{const r=l.getBoundingClientRect();c.style.transform=`translate(${px}px,${py}px)`;let hit=null;it.forEach(d=>{const q=d.getBoundingClientRect();if(px>q.left-r.left&&px<q.right-r.left&&py>q.top-r.top&&py<q.bottom-r.top)hit=d});
    c.classList.toggle('on',!!hit);if(hit&&sp.textContent!==hit.dataset.lb){sp.textContent=hit.dataset.lb;ib.textContent=hit.dataset.ic}})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx255` rules from `site/fx.css`

_No dedicated `.fx255` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #255
