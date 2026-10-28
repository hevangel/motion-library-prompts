# 190 · Skate — 滑行

Text skates in at a tilt like ice skating, then straightens after braking

- Component: Text (`text`)
- Timing: Entrance, Exit
- Tech: CSS
- Uses: Headline · Hero, Transitions
- Style / keywords: skate ice skating tilt brake sense of speed Skate Skew Slide Brake Canva style Canva Skate skate presentation social post animation
- Tag: CSS keyframes
- Example text: "Skating In" (stage background: acc)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Skate (滑行)" motion effect: As the text slides in at high speed from the left, the whole leans forward (skewX about -28 degrees); on arrival it slides slightly too far and tilts in the opposite direction (like a body leaning back while braking), then straightens and stops; on exit it accelerates out to the right and leans forward again. A sense of speed and weight. (CSS: keyframes in sequence translateX(-70%) skewX(-28deg) to translateX(4%) skewX(14deg) to skewX(-4deg) to none, with an accelerating curve for the exit segment)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage acc fx190">`, preview text "Skating In". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Skate".

### JavaScript — `FX[190]` from `site/fx.js`

```js
190(s,x){const t=T(x,Math.min(12,60/chars(x).length));t.classList.add('skt');s.append(t)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx190` rules from `site/fx.css`

_No dedicated `.fx190` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #190
