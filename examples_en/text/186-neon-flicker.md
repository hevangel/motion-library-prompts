# 186 · Neon Flicker — 霓虹閃爍

Text flickers irregularly like a neon tube, then lights up

- Component: Text (`text`)
- Timing: Loop · Idle, Entrance
- Tech: CSS
- Uses: Headline · Hero, Logo · Brand, Emphasis
- Style / keywords: neon tube flicker glow sign nightclub Neon Glow Flicker Sign Canva style Canva Neon neon presentation social post animation
- Tag: CSS keyframes
- Example text: "OPEN" (stage background: dark)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Neon Flicker (霓虹閃爍)" motion effect: Text is like a neon tube that has just been powered: it starts dark, then flickers quickly twice in an irregular pattern, then lights up stably with a multilayer outer glow (brighter inner layer, diffused outer layer); after that it glows stably most of the time, with an occasional brief flicker to add realism. Suitable for signage and nighttime themes. (CSS: keyframes switch opacity and text-shadow at a few percentages for irregular flickering; the glow uses 2–3 layers of text-shadow with different radii; rounded or bold fonts work better)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx186">`, preview text "OPEN". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Neon Flicker".

### JavaScript — `FX[186]` from `site/fx.js`

```js
186(s,x){const t=T(x,Math.min(15,60/chars(x).length));t.classList.add('neo');s.append(t)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx186` rules from `site/fx.css`

_No dedicated `.fx186` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #186
