# 289 · Holographic Card — 全息閃卡

A collectible card tilts in 3D following the cursor, and the iridescent foil shine and reflections on its surface flow with the angle

- Component: Cards · Groups (`card`)
- Timing: Hover · Click
- Tech: CSS
- Uses: Headline · Hero, UI Interaction
- Style / keywords: Holographic Foil Card Iridescent Foil Card Game Pokemon Tilt Reflection Holographic Foil Card Tilt Glare Shiny Trading Card hover Hovering Hover Over
- Tag: mix-blend-mode
- Example text: "HOLO" (stage background: dark)
- Added: 2026-10-20

**AI prompt (English copy format):**

```text
"Holographic Card (全息閃卡)" motion effect: A collectible card (an image above, a title and number below) tilts in 3D space following the cursor (up to about 13 degrees); the card's surface has a layer of iridescent holographic foil shine, the foil shine position follows the cursor movement, the more it tilts the more obvious the foil shine, and there is also a soft reflection following the cursor position; when the cursor leaves the card straightens and the foil shine fades. (CSS + JS: mousemove calculates the cursor's relative position on the card 0~1, sets rotateX/rotateY and CSS variables --px, --py; the foil layer is iridescent stripes of repeating-linear-gradient, mix-blend-mode: color-dodge, background-position using --px/--py; the reflection layer is a radial-gradient overlaid with overlay; the parent sets perspective)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx289">`, preview text "HOLO". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Holographic Card".

### JavaScript — `FX[289]` from `site/fx.js`

```js
289(s,x,card){const l=el('div','abs gl ho-hw');const c=el('div','ho-ho');c.innerHTML='<div class="ho-hi">'+mdImg(2)+'</div><b></b><small>No. 289 · HOLO</small><i class="ho-foil"></i><i class="ho-gl"></i>';c.querySelector('b').textContent=x;l.append(c);s.append(l);
  vpointer(l,card,(px,py)=>{const r=c.getBoundingClientRect(),q=l.getBoundingClientRect(),cx=(px-(r.left-q.left))/r.width,cy=(py-(r.top-q.top))/r.height,X=Math.max(0,Math.min(1,cx)),Y=Math.max(0,Math.min(1,cy));
    c.style.transform=`rotateY(${(X-.5)*26}deg) rotateX(${(.5-Y)*26}deg)`;c.style.setProperty('--px',X*100+'%');c.style.setProperty('--py',Y*100+'%');c.style.setProperty('--d',Math.hypot(X-.5,Y-.5)*1.6)})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx289` rules from `site/fx.css`

_No dedicated `.fx289` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #289
