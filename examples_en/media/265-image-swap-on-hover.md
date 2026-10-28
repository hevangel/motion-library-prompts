# 265 · Image Swap on Hover — 商品圖切換

When hovering over an e-commerce product card, it switches to a second-angle photo, and the dots below switch along with it

- Component: Images · Media (`media`)
- Timing: Hover · Click, Switch
- Tech: CSS
- Uses: UI Interaction
- Style / keywords: Product Ecommerce Second Image Image Swap Switch Image Swap Hover Product Card Ecommerce Second Image Image Media
- Tag: CSS hover
- Example text: "Linen Shirt" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Image Swap on Hover (商品圖切換)" motion effect: E-commerce product card: above is the main product image, and when the mouse hovers over the card, a second photo (for example a worn or back-angle view) fades in and shrinks back from 1.08 times to the original size, while the main image simultaneously fades out and enlarges slightly, forming a soft image swap; the two small dot indicators below the image switch along to show which image is current; the product name and price are displayed below the card. (CSS: the two images are stacked absolutely positioned in the same frame, on :hover their opacity and scale are exchanged, transition about 0.5–0.7 seconds)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx265">`, preview text "Linen Shirt". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Image Swap on Hover".

### JavaScript — `FX[265]` from `site/fx.js`

```js
265(s,x,card){const f=el('div','md-sw');f.innerHTML=mdImg(0,'a')+mdImg(2,'b')+'<div class="md-sp"><b></b><span>NT$ 1,280</span></div><i class="md-dt"><em></em><em></em></i>';f.querySelector('b').textContent=x;s.append(f);autoHover(f,[f],card,1600)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx265` rules from `site/fx.css`

_No dedicated `.fx265` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #265
