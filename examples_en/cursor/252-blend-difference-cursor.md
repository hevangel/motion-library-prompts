# 252 · Blend Difference Cursor — 反色混合游標

A circular cursor that enlarges when passing over text, with colors inverting where it overlaps

- Component: Cursor (`cursor`)
- Timing: Hover · Click
- Tech: CSS
- Uses: Headline · Hero, Emphasis
- Style / keywords: Inverted Colors Inversion Blend Mode difference Cursor Circle Blend Mode Invert Cursor Hero Cursor Mouse
- Tag: mix-blend-mode
- Example text: "INVERT" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Blend Difference Cursor (反色混合游標)" motion effect: The cursor is replaced with a solid circle that follows the mouse with a smooth delay; the circle uses the “difference” blend mode, and when it overlaps the text below, the colors of the text and background invert each other; when the cursor moves onto a large heading, the circle smoothly enlarges about three times so the inverted area covers more text, and shrinks back after leaving the heading. (CSS: the circle element has mix-blend-mode: difference, pointer-events: none; JS lerps toward the mouse coordinates every frame and detects whether it is within a heading's range to interpolate the scale; the container uses cursor: none to hide the native cursor)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx252">`, preview text "INVERT". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Blend Difference Cursor".

### JavaScript — `FX[252]` from `site/fx.js`

```js
252(s,x,card){const l=el('div','abs gl cr-bl');l.append(T(x,Math.min(15,64/chars(x).length)));const c=el('i','cr-bc');l.append(c);s.append(l);let cx=0,cy=0,tx=0,ty=0,big=false,sc=.35;
  vpointer(l,card,(px,py)=>{tx=px;ty=py;const t=l.querySelector('.t').getBoundingClientRect(),r=l.getBoundingClientRect();big=px>t.left-r.left&&px<t.right-r.left&&py>t.top-r.top&&py<t.bottom-r.top});
  const loop=()=>{cx+=(tx-cx)*.2;cy+=(ty-cy)*.2;sc+=((big?1:.3)-sc)*.12;c.style.transform=`translate(${cx}px,${cy}px) translate(-50%,-50%) scale(${sc})`};const prev=ticks.get(card);ticks.set(card,t=>{prev&&prev(t);loop()})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx252` rules from `site/fx.css`

_No dedicated `.fx252` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #252
