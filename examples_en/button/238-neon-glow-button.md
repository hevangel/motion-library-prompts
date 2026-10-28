# 238 · Neon Glow Button — 霓虹呼吸按鈕

The border and glow brighten and dim like breathing; on hover it fills and glows strongly

- Component: Button (`button`)
- Timing: Loop · Idle, Hover · Click
- Tech: CSS
- Uses: UI Interaction, Emphasis, Headline · Hero
- Style / keywords: Neon Glow Halo Breathing Neon Glow Pulse Button Cyberpunk Button
- Tag: box-shadow
- Example text: "Join Us" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Neon Glow Button (霓虹呼吸按鈕)" motion effect: A neon-style button: the thin border and text use an accent color, surrounded by a ring of soft outer glow and inner glow, with the halo brightening and dimming like breathing on a cycle of about 2.4 seconds; when the mouse hovers, the whole button fills, the text inverts to white, and it emits multiple layers of strong, wide-range glow. (CSS: multiple layers of box-shadow (including inset) create the glow, and keyframes change the halo size and opacity; on hover, the breathing animation stops and changes to a larger multi-layer box-shadow, with a 0.35 second transition)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx238">`, preview text "Join Us". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Neon Glow Button".

### JavaScript — `FX[238]` from `site/fx.js`

```js
238(s,x,card){const b=bxBtn('bx-gl',x);s.append(b);autoHover(b,[b],card,1600)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx238` rules from `site/fx.css`

_No dedicated `.fx238` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #238
