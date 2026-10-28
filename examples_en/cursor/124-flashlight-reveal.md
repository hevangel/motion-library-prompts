# 124 · Flashlight Reveal — 手電筒探照

The screen is dark, with hidden content lit up only near the cursor, like a flashlight

- Component: Cursor (`cursor`)
- Timing: Hover · Click
- Tech: CSS
- Uses: UI Interaction, Headline · Hero
- Style / keywords: Cursor Flashlight Searchlight Spotlight Reveal Mask Flashlight Spotlight Reveal Mask Cursor Hidden
- Tag: CSS mask
- Example text: "You found me" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Flashlight Reveal (手電筒探照)" motion effect: The whole section is almost dark, with the big headline only faintly visible; wherever the cursor is, it lights up a soft-edged circular area like a flashlight, and inside that area a brighter version hidden underneath is revealed (a clear headline and gradient background). The flashlight follows the cursor, revealing wherever it shines. (How to: two stacked layers with the same layout; the top layer is the vivid version, using mask: radial-gradient(circle at var(--mx) var(--my), #000 55%, transparent) to show only the area near the cursor; update --mx and --my on mousemove)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx124">`, preview text "You found me". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Flashlight Reveal".

### JavaScript — `FX[124]` from `site/fx.js`

```js
124(s,x,card){const l=el('div','abs fl1');l.innerHTML='<div class="b"></div><div class="r"></div>';l.querySelectorAll('div').forEach(d=>d.append(T(x,Math.min(16,64/chars(x).length))));s.append(l);
  vpointer(l,card,(px,py)=>{l.style.setProperty('--mx',px+'px');l.style.setProperty('--my',py+'px')})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx124` rules from `site/fx.css`

_No dedicated `.fx124` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #124
