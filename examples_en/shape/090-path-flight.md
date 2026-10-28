# 090 · Path Flight — 路徑飛行

A paper plane flies along a curve, turning as it goes

- Component: Shapes · SVG (`shape`)
- Timing: Loop · Idle
- Tech: GSAP
- Uses: Background Decoration
- Style / keywords: 
- Tag: MotionPath
- Example text: "" (stage background: acc, fixed text)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Path Flight (路徑飛行)" motion effect: A paper plane flies across the screen along a dashed curve with a loop, its nose turning to follow the path's direction, and starts over after it flies off-screen. (GSAP: MotionPathPlugin, path/align specify the SVG path, autoRotate:true)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage acc fx90">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Path Flight".

### JavaScript — `FX[90]` from `site/fx.js`

```js
90(s){const id='mp'+Math.random().toString(36).slice(2);s.insertAdjacentHTML('beforeend',`<svg class="mpth" viewBox="0 0 320 180"><path id="${id}" d="M-30,130 C40,130 60,40 115,58 C160,74 130,132 100,112 C72,92 112,36 175,58 C235,80 255,135 350,95" fill="none" stroke="#111" stroke-opacity=".35" stroke-width="2" stroke-dasharray="4 7" stroke-linecap="round"/><g class="pl"><path d="M-11,-9 L13,0 L-11,9 L-6,0 Z" fill="#111"/></g></svg>`);
  gsap.to(s.querySelector('.pl'),{motionPath:{path:'#'+id,align:'#'+id,alignOrigin:[.5,.5],autoRotate:true},duration:4.2,repeat:-1,repeatDelay:.3,ease:'power1.inOut'})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx90` rules from `site/fx.css`

_No dedicated `.fx90` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #90
