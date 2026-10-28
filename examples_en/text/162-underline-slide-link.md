# 162 · Underline Slide Link — 連結底線滑入

Hovering over a link grows an underline from the left, and leaving retracts it to the right

- Component: Text (`text`)
- Timing: Hover · Click
- Tech: CSS
- Uses: UI Interaction
- Style / keywords: Link Underline Menu Navigation link underline nav menu hover Hover Mouse Enter Hover Interaction
- Tag: CSS hover
- Example text: "Home Work About Contact" (stage background: dark)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Underline Slide Link (連結底線滑入)" motion effect: Text links in a navigation bar: when the mouse moves in, a thin underline grows from left to right; when the mouse moves out, the underline continues retracting to the right (instead of shrinking back the way it came), like a sweep of light passing through; about 0.45 seconds, ease-in-out. (CSS: ::after makes the underline, transform:scaleX(0); on hover, scaleX(1) with transform-origin:left; when not hovering, transform-origin:right, transition cubic-bezier(.7,0,.2,1))
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx162">`, preview text "Home Work About Contact". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Underline Slide Link".

### JavaScript — `FX[162]` from `site/fx.js`

```js
162(s,x,card){const n=el('nav','ul2');const its=words(x).slice(0,5).map(v=>{const a=el('span','lk2');a.textContent=v;n.append(a);return a});s.append(n);autoHover(n,its,card)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx162` rules from `site/fx.css`

_No dedicated `.fx162` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #162
