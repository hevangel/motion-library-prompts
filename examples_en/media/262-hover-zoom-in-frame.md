# 262 · Hover Zoom in Frame — 框內微放大

When hovering over an image, the image slowly zooms in slightly within a fixed frame, and the title floats up from the bottom

- Component: Images · Media (`media`)
- Timing: Hover · Click
- Tech: CSS
- Uses: UI Interaction
- Style / keywords: hover Enlarge Zoom Image Zoom Inside Frame Fixed Frame overflow hidden Portfolio Product Image Image Zoom Hover Scale Thumbnail Gallery Image Media
- Tag: CSS hover
- Example text: "Seaside Forest City" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Hover Zoom in Frame (框內微放大)" motion effect: A row of image cards, each image placed in a fixed-size, rounded frame (overflow: hidden): when the mouse hovers, the frame size does not change, and the image inside slowly enlarges to 1.1 times over about 0.8 seconds with a decelerating curve; the title bar at the bottom of the frame (with a gradient background from transparent to translucent) simultaneously moves up slightly from below and becomes completely clear; when moving away, the image slowly shrinks back. (CSS: container overflow: hidden; img sets transition: transform .8s cubic-bezier(.2,.7,.2,1), and when the container is :hover the img has transform: scale(1.1); the title's translateY and opacity transition together)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx262">`, preview text "Seaside Forest City". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Hover Zoom in Frame".

### JavaScript — `FX[262]` from `site/fx.js`

```js
262(s,x,card){const ws=words(x);const w=el('div','md-zg');const fs=[0,1,2].map(i=>{const f=el('figure','md-z');f.innerHTML=mdImg(i)+'<figcaption></figcaption>';f.querySelector('figcaption').textContent=ws[i%ws.length];w.append(f);return f});s.append(w);autoHover(w,fs,card,1200)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx262` rules from `site/fx.css`

_No dedicated `.fx262` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #262
