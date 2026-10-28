# 165 · Circle to Card Image — 圖片圓形展開

A circular thumbnail expands on hover into a tall rounded card and a title fades in

- Component: Images · Media (`media`)
- Timing: Hover · Click
- Tech: CSS
- Uses: UI Interaction, Headline · Hero
- Style / keywords: image circle expand thumbnail avatar team image shape expand circle hover hover hover mouse-enter hover-over interaction
- Tag: CSS hover
- Example text: "Morning Afternoon Night" (stage background: dark)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Circle to Card Image (圖片圓形展開)" motion effect: A row of circular image thumbnails. When the mouse moves over one, the circle smoothly becomes a taller portrait rounded rectangle (growing downward at the same time), the image content scales back from 1.18x to its original size, revealing more of the picture, and the title below fades in; moving away restores the circle. About 0.55 seconds, ease-out. Suitable for team members or work categories. (CSS: outer frame border-radius 50% to a small rounded corner, height transitions in sync; inner image transform: scale 1.18 to 1; title opacity / translateY)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx165">`, preview text "Morning Afternoon Night". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Circle to Card Image".

### JavaScript — `FX[165]` from `site/fx.js`

```js
165(s,x,card){const w=el('div','shw');const ws=words(x);const P=[['#9fd3ff','#ffe1b0','#4f7a6a','#264a3f','#fff6d8'],['#ffd9c2','#c9b6ff','#7b6ca8','#3f3566','#fff6e6'],['#1b1f4a','#4a2a6b','#2c2a55','#14122e','#f4f1d0']];
  const cs=P.map((p,i)=>{const c=el('figure','shp');c.innerHTML=`<div class="im3">${scene(...p)}</div><figcaption></figcaption>`;c.querySelector('figcaption').textContent=ws[i%ws.length];w.append(c);return c});s.append(w);autoHover(w,cs,card,1400)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx165` rules from `site/fx.css`

_No dedicated `.fx165` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #165
