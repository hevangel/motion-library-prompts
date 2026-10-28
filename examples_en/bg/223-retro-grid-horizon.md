# 223 · Retro Grid Horizon — 復古透視網格

A striped sunset above the horizon, and a perspective grid floor continuously advancing forward

- Component: Background · Ambience (`bg`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Headline · Hero, Background Decoration
- Style / keywords: Retro Synthwave synthwave vaporwave Perspective Grid Floor Horizon Sunset 80s Retro Grid Horizon Perspective Background Atmosphere
- Tag: CSS 3D
- Example text: "RETRO WAVE" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Retro Grid Horizon (復古透視網格)" motion effect: An 80s synthwave-style background: in the middle of the screen is a horizon line; above it is a circular sunset whose lower half is cut by horizontal stripes, with a soft glow; below is a perspective-tilted grid floor whose grid lines continuously advance toward the viewer and fade out in the distance, creating a feeling of endlessly driving forward; the title floats above the sunset with a slight glow. (CSS: the floor is two sets of linear-gradient grid lines, with transform:perspective + rotateX(72deg), and keyframes advancing background-position by one grid length for a seamless loop; the far end fades out with a mask; the sunset stripes use a repeating-linear-gradient mask)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx223">`, preview text "RETRO WAVE". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Retro Grid Horizon".

### JavaScript — `FX[223]` from `site/fx.js`

```js
223(s,x){const w=el('div','abs bga-hz');w.innerHTML='<i class="bga-sun"></i><div class="bga-floor"></div>';s.append(w);const t=T(x,Math.min(11,52/chars(x).length));t.classList.add('bga-ht');s.append(t)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx223` rules from `site/fx.css`

_No dedicated `.fx223` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #223
