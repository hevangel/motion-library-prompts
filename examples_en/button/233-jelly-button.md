# 233 · Jelly Button — 果凍彈跳按鈕

On hover or click, the button is squashed flat like jelly, stretched long, then bounces back

- Component: Button (`button`)
- Timing: Hover · Click
- Tech: CSS
- Uses: UI Interaction, Emphasis, App Interface
- Style / keywords: Jelly Bounce Bouncy Squash Stretch Jelly Rubber Squash Stretch Bounce Button Button
- Tag: CSS keyframes
- Example text: "Try Clicking Me" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Jelly Button (果凍彈跳按鈕)" motion effect: When the mouse hovers over or clicks it, the button, like jelly, is first squashed horizontally flat (width 1.18, height 0.82), then stretched vertically long (width 0.85, height 1.15), then wobbles back and forth a few times with decreasing amplitude until it returns to its original shape; the whole sequence is about 0.7 seconds, bouncy and cute. (CSS keyframes: in sequence scale(1.18,.82) then (.85,1.15) then (1.08,.92) then (.97,1.03) then (1,1); when triggered by a click, first remove the class, force a reflow, then add it back so it can replay)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx233">`, preview text "Try Clicking Me". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Jelly Button".

### JavaScript — `FX[233]` from `site/fx.js`

```js
233(s,x,card){const b=bxBtn('bx-jl',x);s.append(b);const go=()=>{b.classList.remove('go');void b.offsetWidth;b.classList.add('go')};b.addEventListener('click',go);b.addEventListener('animationend',()=>b.classList.remove('go'));bxDemo(b,card,go,1800)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx233` rules from `site/fx.css`

_No dedicated `.fx233` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #233
