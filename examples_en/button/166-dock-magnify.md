# 166 · Dock Magnify — Dock 放大選單

As the cursor sweeps over a row of icons, nearby icons magnify and push their neighbors aside

- Component: Button (`button`)
- Timing: Hover · Click
- Tech: CSS
- Uses: UI Interaction, App Interface
- Style / keywords: Dock magnify icons menu macOS toolbar magnify icons toolbar hover hover mouse-enter hover-over interaction
- Tag: CSS + JS
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Dock Magnify (Dock 放大選單)" motion effect: A row of rounded icons like the macOS Dock: when the cursor moves left and right near the icon row, the icon closest to the cursor magnifies to about 1.9x, and the neighboring icons to its left and right magnify in decreasing amounts according to distance, forming a smooth magnification peak and pushing the other icons aside to both sides; when the cursor leaves, all return to their original size. (How to: on mousemove, calculate the horizontal distance between each icon's center and the cursor, scale = 1 + 0.9 × max(0, 1 − distance/influence range), write it into CSS variables controlling width / height so the layout naturally pushes apart; add a short transition to make the change smooth)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx166">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Dock Magnify".

### JavaScript — `FX[166]` from `site/fx.js`

```js
166(s,x,card){const l=el('div','abs dockw');const d=el('div','dock');const ic=[...Array(7)].map((_,i)=>{const e=el('i','dki');e.style.background=`linear-gradient(140deg,${GC[i%5]},${GC[(i+2)%5]})`;d.append(e);return e});l.append(d);s.append(l);
  vpointer(l,card,(px,py)=>{const r=d.getBoundingClientRect(),lr=l.getBoundingClientRect();const cy=r.top-lr.top+r.height/2,near=Math.abs(py-cy)<r.height*1.6;const R=l.offsetWidth*.18;
    ic.forEach(e=>{const cx=e.offsetLeft+e.offsetWidth/2+(d.offsetLeft);const k=near?Math.max(0,1-Math.abs(px-cx)/R):0;e.style.setProperty('--s',1+k*.9)})},(t,W,H)=>[W*(.5+.42*Math.sin(t*.8)),H*.62])}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx166` rules from `site/fx.css`

_No dedicated `.fx166` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #166
