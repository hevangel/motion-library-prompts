# 287 · Social Icon Fill — 社群圖示填滿

When hovering over a round social icon, its background fills up from below, the icon swaps upward for another one, and the button floats up slightly

- Component: Button (`button`)
- Timing: Hover · Click
- Tech: CSS
- Uses: UI Interaction
- Style / keywords: Social Icon icon Fill Footer IG Threads Social Icon Fill Hover Footer hover Hovering Hover Over
- Tag: CSS hover
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-20

**AI prompt (English copy format):**

```text
"Social Icon Fill (社群圖示填滿)" motion effect: A row of round social icons in the footer (thin outline border, line icons in the middle): when the mouse hovers over an icon, a solid background rises from the bottom of the circle to fill it, the original icon slides up and out, an inverted-color version of the same icon slides in from below to replace it, and the whole button floats up slightly; when moving away it reverses back. About 0.45 seconds. (CSS: circle overflow: hidden, background layer translateY(101%) → 0; two icons stacked in the same cell, one moving up and out, the other moving in from below)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx287">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Social Icon Fill".

### JavaScript — `FX[287]` from `site/fx.js`

```js
287(s,x,card){const w=el('div','ho-so');const I=[['IG','<rect x="4" y="4" width="16" height="16" rx="5"/><circle cx="12" cy="12" r="3.6"/><circle cx="17" cy="7" r=".6"/>'],['Threads','<path d="M16.5 11.2c-.4-2.6-2-3.9-4.4-3.9-2.6 0-4.3 1.9-4.3 4.7s1.7 4.8 4.3 4.8c2 0 3.4-1 3.4-2.6s-1.3-2.4-3.1-2.4c-1.5 0-2.5.7-2.5 1.8"/><path d="M19 12c0 4.4-2.8 8-7 8s-7-3.6-7-8 2.8-8 7-8c3 0 5.2 1.6 6.3 4.3"/>'],['Mail','<rect x="3" y="6" width="18" height="12" rx="2"/><path d="M3 7l9 6 9-6"/>'],['Link','<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>']];
  const its=I.map(([l,p])=>{const a=el('button','ho-sc');a.setAttribute('aria-label',l);a.innerHTML='<i></i><svg viewBox="0 0 24 24">'+p+'</svg><svg viewBox="0 0 24 24">'+p+'</svg>';w.append(a);return a});s.append(w);autoHover(w,its,card,900)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx287` rules from `site/fx.css`

_No dedicated `.fx287` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #287
