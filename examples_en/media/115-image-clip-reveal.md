# 115 · Image Clip Reveal — 圖片遮罩揭示

The image is uncovered from bottom to top, while scaling down from enlarged to its original size

- Component: Images · Media (`media`)
- Timing: Entrance, Exit
- Tech: CSS
- Uses: Transitions, Headline · Hero
- Style / keywords: Image Photo Mask Reveal Entrance clip-path Image Reveal Mask Wipe Zoom
- Tag: clip-path
- Example text: "" (stage background: cream, fixed text)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Image Clip Reveal (圖片遮罩揭示)" motion effect: When the image enters, its frame is uncovered from bottom to top like a curtain, while the picture inside the frame slowly scales down from about 1.35× to its original size, creating the layers of "uncovering + camera pulling back"; after a pause, it is then gathered up and disappears from bottom to top. The uncovering takes about 1.2 seconds, ease-in-out (cubic-bezier(.7,0,.2,1)). (CSS: the frame uses clip-path:inset() keyframes from inset(100% 0 0 0) to inset(0); the inner image uses transform:scale 1.35→1; on a real site, this can be played only when scrolled into view)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage cream fx115">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Image Clip Reveal".

### JavaScript — `FX[115]` from `site/fx.js`

```js
115(s){const f=el('div','rv');f.innerHTML=scene('#9fd3ff','#ffe1b0','#4f7a6a','#264a3f','#fff6d8');s.append(f)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx115` rules from `site/fx.css`

_No dedicated `.fx115` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #115
