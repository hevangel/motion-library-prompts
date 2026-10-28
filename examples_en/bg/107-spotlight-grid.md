# 107 · Spotlight Grid — 聚光網格

A fine grid-line background, with the grid lines near the cursor lit up with a soft glow

- Component: Background · Ambience (`bg`)
- Timing: Hover · Click
- Tech: CSS
- Uses: Background Decoration, UI Interaction
- Style / keywords: Background Grid Grid Lines Spotlight Cursor Glow Spotlight Grid Pattern Cursor Glow SaaS
- Tag: CSS mask
- Example text: "Spotlight" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Spotlight Grid (聚光網格)" motion effect: The background of the whole section is a faint fine grid; the ring of grid lines around the cursor's position lights up in the accent color, with a soft glow, the lit area following the cursor and fading out naturally at the edges; when the cursor leaves, the lit area disappears. (How it works: two identical grid-line background layers, the upper layer in the accent color, then mask:radial-gradient(circle at var(--mx) var(--my)) reveals only the area near the cursor; --mx and --my are updated on mousemove)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx107">`, preview text "Spotlight". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Spotlight Grid".

### JavaScript — `FX[107]` from `site/fx.js`

```js
107(s,x,card){const l=el('div','abs gl sgrid');l.append(el('div','spot'),T(x,Math.min(12,56/chars(x).length)));s.append(l);vpointer(l,card,(px,py)=>{l.style.setProperty('--mx',px+'px');l.style.setProperty('--my',py+'px')})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx107` rules from `site/fx.css`

_No dedicated `.fx107` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #107
