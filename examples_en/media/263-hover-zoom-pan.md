# 263 · Hover Zoom & Pan — 滑過放大檢視

Hover over an image to zoom in two times, with the enlarged position following the cursor to view product details

- Component: Images · Media (`media`)
- Timing: Hover · Click
- Tech: CSS
- Uses: UI Interaction
- Style / keywords: Zoom View Details Product Image Ecommerce Follow Cursor Pan Zoom Pan Hover Product Detail Ecommerce Image Media
- Tag: transform-origin
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Hover Zoom & Pan (滑過放大檢視)" motion effect: A large product image: when the mouse moves into the image, the image smoothly enlarges to about 2.2 times within the original frame, and the center point of enlargement follows the cursor position — moving the cursor to the upper left shows the upper-left details, and moving it to the lower right shows the lower-right details; when the mouse leaves it shrinks back to the original size. There is a small hint “Hover to see details” in the lower right corner, which fades out when zoomed. (JS + CSS: on mousemove, set transform-origin to the cursor's percentage position in the image, the container scales to scale(2.2) on :hover with a 0.5 second transition; container overflow: hidden, cursor: zoom-in)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx263">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Hover Zoom & Pan".

### JavaScript — `FX[263]` from `site/fx.js`

```js
263(s,x,card){const f=el('div','md-zp');f.innerHTML=mdImg(1)+'<span class="md-zh">滑過看細節</span>';s.append(f);const im=f.querySelector('.md-im');let on=false;
  f.addEventListener('pointerenter',()=>on=true);f.addEventListener('pointerleave',()=>{on=false;f.classList.remove('on')});
  vpointer(f,card,(px,py)=>{const W=f.offsetWidth,H=f.offsetHeight;f.classList.add('on');im.style.transformOrigin=`${px/W*100}% ${py/H*100}%`},(t,W,H)=>{const k=Math.sin(t*.5);if(k<-.6)f.classList.remove('on');return[W*(.5+.4*Math.sin(t*1.1)),H*(.5+.35*Math.cos(t*.8))]})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx263` rules from `site/fx.css`

_No dedicated `.fx263` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #263
