# 168 · Expanding Panels — 展開式圖片面板

A row of narrow image panels; the hovered panel expands wider and shows its title

- Component: Images · Media (`media`)
- Timing: Hover · Click
- Tech: CSS
- Uses: UI Interaction, Headline · Hero
- Style / keywords: image panel expand accordion album gallery accordion expanding panels flex hover hover mouse-enter hover-over interaction
- Tag: CSS flex
- Example text: "Mountains Flowers Night Sky Sunset Coast" (stage background: dark)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Expanding Panels (展開式圖片面板)" motion effect: A row of equally wide vertical-strip image panels. When the mouse moves over one panel, it smoothly expands to about 4 times the width of the others, the other panels narrow in sync, and after the expansion completes the title at the bottom-left of that panel fades in; moving to another panel hands off smoothly. About 0.6 seconds, ease-out. Suitable for work categories or gallery entrances. (CSS: container display:flex, each panel flex:1, on hover flex:4, transition flex; images use object-fit:cover to avoid distortion; title gets a transition-delay)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx168">`, preview text "Mountains Flowers Night Sky Sunset Coast". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Expanding Panels".

### JavaScript — `FX[168]` from `site/fx.js`

```js
168(s,x,card){const w=el('div','exp');const ws=words(x);const P=[['#9fd3ff','#ffe1b0','#4f7a6a','#264a3f','#fff6d8'],['#ffd9c2','#c9b6ff','#7b6ca8','#3f3566','#fff6e6'],['#1b1f4a','#4a2a6b','#2c2a55','#14122e','#f4f1d0'],['#ffb36b','#ff6b8b','#8a3f6e','#3b1f45','#fff3d6'],['#c9f0e6','#7fd1c7','#2f7d74','#16433f','#ffffff']];
  const ps=P.map((p,i)=>{const e=el('div','ep');e.innerHTML=scene(...p)+'<b></b>';e.querySelector('b').textContent=ws[i%ws.length];w.append(e);return e});s.append(w);autoHover(w,ps,card,1300)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx168` rules from `site/fx.css`

_No dedicated `.fx168` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #168
