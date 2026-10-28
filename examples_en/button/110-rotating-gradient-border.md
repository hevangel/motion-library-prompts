# 110 · Rotating Gradient Border — 旋轉光邊按鈕

The gradient light on the button's border keeps rotating around it, with a soft outer glow

- Component: Button (`button`)
- Timing: Loop · Idle, Hover · Click
- Tech: CSS
- Uses: UI Interaction, Emphasis
- Style / keywords: Button Border Gradient Rotation Glow Glow Border Conic Gradient Animated Border Button
- Tag: @property
- Example text: "Get Started" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Rotating Gradient Border (旋轉光邊按鈕)" motion effect: The border of a pill button is a ring of multicolored gradient light, and the gradient keeps rotating around the border (about 3 seconds per revolution), with a layer of blurred soft glow behind the border; inside the button are a solid background and text; when the mouse moves over it, the rotation speeds up. (CSS: @property registers the angle variable --ang, the background uses conic-gradient(from var(--ang)), and keyframes rotate --ang to 360deg; an inner span covers the middle so only the border shows; ::before duplicates the background and blurs it for the outer glow)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx110">`, preview text "Get Started". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Rotating Gradient Border".

### JavaScript — `FX[110]` from `site/fx.js`

```js
110(s,x){const b=el('button','rgb');const sp=el('span');sp.textContent=x;b.append(sp);b.style.fontSize=Math.min(5,40/chars(x).length)+'cqw';s.append(b)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx110` rules from `site/fx.css`

_No dedicated `.fx110` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #110
