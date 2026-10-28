# 200 · Geometric Loader — 幾何載入動畫

A circle, square and triangle bounce and flip in sequence as a loading indicator

- Component: Shapes · SVG (`shape`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: UI Interaction, App Interface
- Style / keywords: loading reading loading waiting geometric bounce Loader Spinner Geometric Shapes Bounce SVG graphic
- Tag: CSS keyframes
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Geometric Loader (幾何載入動畫)" motion effect: A loading indicator: three outlined geometric shapes (circle, square, triangle) in a row. In sequence, like a wave, they first squash down to build up energy, jump up and flip 360 degrees, then squash and rebound when they land, playing in a loop — more characterful than an ordinary spinner icon. (CSS: a single set of keyframes includes scale squashing, translateY jumping, and rotate flipping, with the three shapes staggered by 0.18 seconds using animation-delay)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx200">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Geometric Loader".

### JavaScript — `FX[200]` from `site/fx.js`

```js
200(s){s.insertAdjacentHTML('beforeend','<div class="geo"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/></svg><svg viewBox="0 0 24 24"><rect x="3.5" y="3.5" width="17" height="17" rx="2"/></svg><svg viewBox="0 0 24 24"><path d="M12 3 L21.5 20 H2.5 Z"/></svg></div>')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx200` rules from `site/fx.css`

_No dedicated `.fx200` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #200
