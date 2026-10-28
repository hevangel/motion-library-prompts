# 237 · Icon Slide Button — 箭頭接力按鈕

On hover, the arrow on the right slides out to the right while a new arrow slides in from the left, and the text makes way

- Component: Button (`button`)
- Timing: Hover · Click
- Tech: CSS
- Uses: UI Interaction, Emphasis
- Style / keywords: Arrow Icon Slide In Slide Out Relay Icon Slide Arrow Button Hover CTA Button
- Tag: CSS hover
- Example text: "Learn More" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Icon Slide Button (箭頭接力按鈕)" motion effect: A capsule button with a right-pointing arrow to the right of the text; when the mouse hovers, the right arrow slides out of the button to the right and fades out, while another identical arrow slides in from outside the left of the button to the left of the text, and the text shifts right in sync to make way, like an arrow relay pushing forward; when the mouse leaves, it reverses back. About 0.4 seconds, ease-in-out. (CSS: the button has overflow:hidden; the two arrows and the text each have transform and transition settings, switching displacement on hover)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx237">`, preview text "Learn More". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Icon Slide Button".

### JavaScript — `FX[237]` from `site/fx.js`

```js
237(s,x,card){const b=bxBtn('bx-ic',x);b.insertAdjacentHTML('afterbegin','<svg class="bx-a1" viewBox="0 0 24 24"><path d="M5 12h13M13 6l6 6-6 6"/></svg>');b.insertAdjacentHTML('beforeend','<svg class="bx-a2" viewBox="0 0 24 24"><path d="M5 12h13M13 6l6 6-6 6"/></svg>');s.append(b);autoHover(b,[b],card,1400)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx237` rules from `site/fx.css`

_No dedicated `.fx237` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #237
