# 256 · Crosshair Cursor — 十字準星座標

Two thin lines, horizontal and vertical, follow the cursor, with coordinate numbers displayed in real time beside it

- Component: Cursor (`cursor`)
- Timing: Hover · Click
- Tech: CSS
- Uses: UI Interaction, Numbers & Data, Headline · Hero
- Style / keywords: Cross Crosshair Coordinates Aiming Technology Blueprint Crosshair Coordinates Cursor Blueprint Tech Cursor Mouse
- Tag: JS + CSS
- Example text: "Precision" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Crosshair Cursor (十字準星座標)" motion effect: On a background with faint grid lines, a horizontal line and a vertical line span the whole area and intersect at the cursor position, with a small circle at the intersection; at the lower right of the cursor there is a small label that displays the current X and Y coordinate numbers in real time in a monospace font (converted to 1920 × 1080), and near the edges the label automatically tucks inward so it does not go off screen. Suitable for technology, design tools, or portfolio homepages. (JS: on mousemove, transform moves the two lines and the label, coordinates = cursor position / container width and height × 1920, 1080, padded with zeros using padStart)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx256">`, preview text "Precision". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Crosshair Cursor".

### JavaScript — `FX[256]` from `site/fx.js`

```js
256(s,x,card){const l=el('div','abs cr-xh');l.innerHTML='<i class="h"></i><i class="v"></i><b></b><em></em>';const t=T(x,Math.min(12,52/chars(x).length));l.append(t);s.append(l);const [h,v]=l.querySelectorAll('i'),rd=l.querySelector('b'),dot=l.querySelector('em');
  vpointer(l,card,(px,py)=>{const W=l.offsetWidth,H=l.offsetHeight;h.style.transform=`translateY(${py}px)`;v.style.transform=`translateX(${px}px)`;dot.style.transform=`translate(${px}px,${py}px)`;rd.textContent=`X ${String(Math.round(px/W*1920)).padStart(4,'0')}  Y ${String(Math.round(py/H*1080)).padStart(4,'0')}`;rd.style.transform=`translate(${Math.min(px+10,W-rd.offsetWidth-6)}px,${Math.min(py+10,H-rd.offsetHeight-6)}px)`})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx256` rules from `site/fx.css`

_No dedicated `.fx256` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #256
