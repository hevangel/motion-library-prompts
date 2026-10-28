# 285 · Icon Micro-animations — 圖示微動畫

On hovering over icons, each performs a small action matching its meaning: a bell shakes, a heart jumps, a gear turns, a trash can lifts its lid

- Component: Shapes · SVG (`shape`)
- Timing: Hover · Click
- Tech: CSS
- Uses: UI Interaction, App Interface
- Style / keywords: Icon icon Micro-animation Bell Heart Gear Trash Can Icon Micro Animation Bell Heart Gear Trash Hover hover Hovering Hover Over
- Tag: CSS keyframes
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-20

**AI prompt (English copy format):**

```text
"Icon Micro-animations (圖示微動畫)" motion effect: A row of function icon buttons (notifications, favorites, settings, delete); when the mouse hovers, the icon's background lights up, and each performs a micro-animation matching its meaning: the bell shakes left and right a few times pivoting on its top, then stops; the heart fills and jumps once; the gear's teeth rotate 90 degrees with a little bounce; the trash can's lid lifts open at an angle pivoting on its left end. It makes the interface livelier without being distracting. (CSS: specific parts of the SVG icons set transform-origin (remember transform-box: fill-box for elements inside SVG), on :hover apply each one's keyframes or transform transition)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx285">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Icon Micro-animations".

### JavaScript — `FX[285]` from `site/fx.js`

```js
285(s,x,card){const w=el('div','ho-ic');const I=[['bell','<path d="M6 16V11a6 6 0 0 1 12 0v5l1.5 2h-15z"/><path d="M10 20a2 2 0 0 0 4 0"/>','通知'],['heart','<path d="M12 20s-7-4.5-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.5-7 10-7 10z"/>','收藏'],['gear','<circle cx="12" cy="12" r="3"/><path d="M12 3v3M12 18v3M3 12h3M18 12h3M5.6 5.6l2.1 2.1M16.3 16.3l2.1 2.1M5.6 18.4l2.1-2.1M16.3 7.7l2.1-2.1"/>','設定'],['trash','<g class="lid"><path d="M4 7h16"/><path d="M9 7V4h6v3"/></g><path d="M6 7l1 13h10l1-13"/>','刪除']];
  const its=I.map(([k,p,l])=>{const b=el('button','ho-ib '+k);b.innerHTML='<svg viewBox="0 0 24 24">'+p+'</svg><span>'+l+'</span>';b.setAttribute('aria-label',l);w.append(b);return b});s.append(w);autoHover(w,its,card,900)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx285` rules from `site/fx.css`

_No dedicated `.fx285` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #285
