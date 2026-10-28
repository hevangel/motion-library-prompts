# 123 · Rotating Text Cursor — 旋轉文字環游標

A ring of text keeps rotating around the cursor

- Component: Cursor (`cursor`)
- Timing: Hover · Click, Loop · Idle
- Tech: CSS
- Uses: UI Interaction, Logo · Brand
- Style / keywords: Cursor Text Ring Circular Text Rotation Circular Text Rotating Text Ring Circular Text Cursor Badge SCROLL
- Tag: SVG textPath
- Example text: "SCROLL · EXPLORE" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Rotating Text Cursor (旋轉文字環游標)" motion effect: Hide the system cursor and replace it with a small dot, surrounded by a ring of text arranged along a circle (for example "SCROLL · EXPLORE ·" repeated); the text ring keeps rotating slowly (about 8 seconds per revolution), and the whole assembly follows the cursor with a slight lag; the large background heading stays very faint, making the cursor the focus. (How it works: an SVG circular path + textPath, using textLength so the text exactly fills one revolution; the outer layer's transform follows the cursor, and the inner svg uses a CSS rotation animation)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx123">`, preview text "SCROLL · EXPLORE". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Rotating Text Cursor".

### JavaScript — `FX[123]` from `site/fx.js`

```js
123(s,x,card){const l=el('div','abs gl tcur');l.append(T('探索作品',12));const id='tc'+Math.random().toString(36).slice(2);const u=x+' • ';const c=el('div','tcr');
  c.innerHTML=`<svg viewBox="0 0 100 100"><defs><path id="${id}" d="M50,50 m-38,0 a38,38 0 1,1 76,0 a38,38 0 1,1 -76,0"/></defs><text font-size="10" font-weight="800"><textPath href="#${id}" textLength="236" lengthAdjust="spacing"></textPath></text></svg><i></i>`;
  c.querySelector('textPath').textContent=rep(u,Math.max(1,Math.round(24/chars(u).length)));l.append(c);s.append(l);vpointer(l,card,(px,py)=>c.style.transform=`translate(${px}px,${py}px)`)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx123` rules from `site/fx.css`

_No dedicated `.fx123` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #123
