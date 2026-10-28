# 183 · Drift — 漂移

Text fades in from the side, keeps drifting slowly, then fades out

- Component: Text (`text`)
- Timing: Entrance, Exit
- Tech: CSS
- Uses: Headline · Hero, Transitions
- Style / keywords: drift slow pan fade in and out presentation Drift Slow Slide Fade Canva style Canva Drift drift presentation social post animation
- Tag: CSS keyframes
- Example text: "Drifting Slowly" (stage background: dark)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Drift (漂移)" motion effect: Text fades in from a position about 12% in from the right and decelerates quickly, then instead of stopping it keeps drifting to the left at a very slow constant speed, and at the end fades out while still drifting; the whole sequence takes about 4 seconds, giving a quiet, flowing feeling. Suitable for titles in presentations or social posts. (CSS: in the keyframes, the first 20% fades in with an ease-out curve, 20%–80% is a small linear displacement, then it fades out at the end)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx183">`, preview text "Drifting Slowly". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Drift".

### JavaScript — `FX[183]` from `site/fx.js`

```js
183(s,x){s.append(T(x,Math.min(12,60/chars(x).length)))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx183` rules from `site/fx.css`

```css
.fx183 .t{animation:drift 4.2s linear infinite}
@keyframes drift{0%{transform:translateX(12%);opacity:0;animation-timing-function:cubic-bezier(.2,.6,.3,1)}20%{transform:translateX(3%);opacity:1;animation-timing-function:linear}80%{transform:translateX(-3%);opacity:1}100%{transform:translateX(-6%);opacity:0}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #183
