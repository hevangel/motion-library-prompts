# 220 · Focus Dim Siblings — 聚焦淡化其他

When hovering over a card it lifts up, while the other cards fade and shrink

- Component: Cards · Groups (`card`)
- Timing: Hover · Click
- Tech: CSS
- Uses: UI Interaction
- Style / keywords: Focus Dim Other Cards hover Highlight Focus Dim Siblings Highlight Spotlight Cards Group
- Tag: :has()
- Example text: "Beginner Advanced Master Team" (stage background: dark)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Focus Dim Siblings (聚焦淡化其他)" motion effect: A row of cards; when the mouse moves over one card, it lifts slightly and enlarges to 1.04x, while the other cards simultaneously fade, blur slightly, desaturate and shrink to 95%, focusing attention on the current card; when the mouse leaves the whole row, everything returns to normal. About 0.45 seconds, decelerating. (CSS: when the container is :hover, .card:not(:hover) gets reduced opacity, filter:blur(1px) saturate(.6) and scale(.95); the hovered card gets translateY + scale; :has() can be used to support keyboard focus)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx220">`, preview text "Beginner Advanced Master Team". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Focus Dim Siblings".

### JavaScript — `FX[220]` from `site/fx.js`

```js
220(s,x,card){const ws=words(x);const w=el('div','kd-fd');const cs=[...Array(4)].map((_,i)=>{const c=el('div','kd-fc');c.innerHTML='<i></i><b></b><em></em>';c.querySelector('i').style.background=`linear-gradient(140deg,${GC[i%5]},${GC[(i+2)%5]})`;c.querySelector('b').textContent=ws[i%ws.length];w.append(c);return c});s.append(w);autoHover(w,cs,card,1300)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx220` rules from `site/fx.css`

_No dedicated `.fx220` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #220
