# 189 · Spread — 展開

Characters stacked together spread out from a blur into normal letter spacing

- Component: Text (`text`)
- Timing: Entrance
- Tech: CSS
- Uses: Headline · Hero, Emphasis
- Style / keywords: spread letter spacing expand blur focus Spread Letter Spacing Tracking Expand Canva style Canva Spread spread presentation social post animation
- Tag: letter-spacing
- Example text: "Spread Out" (stage background: cream)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Spread (展開)" motion effect: The text starts with extremely tight letter spacing, all characters stacked together and blurred and transparent. Then the letter spacing smoothly expands to normal width while it becomes clear and fades in (about 1.1 seconds, ease-out), as if spreading out and taking shape from the center; it fades out after a pause. (CSS: keyframes letter-spacing:-0.55em to 0.06em, with filter:blur(6px) to 0 and opacity)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage cream fx189">`, preview text "Spread Out". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Spread".

### JavaScript — `FX[189]` from `site/fx.js`

```js
189(s,x){const t=T(x,Math.min(12,48/chars(x).length));t.classList.add('spr');s.append(t)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx189` rules from `site/fx.css`

_No dedicated `.fx189` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #189
