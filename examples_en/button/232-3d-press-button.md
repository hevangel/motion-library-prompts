# 232 · 3D Press Button — 立體按壓按鈕

There is a layer of thickness beneath the button; when pressed, the whole button presses down and the thickness disappears, like a physical key

- Component: Button (`button`)
- Timing: Hover · Click
- Tech: CSS
- Uses: UI Interaction, App Interface
- Style / keywords: Three-Dimensional Press Physical Key 3D Pressable Button Push Tactile Game Button
- Tag: CSS :active
- Example text: "Get Started Now" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"3D Press Button (立體按壓按鈕)" motion effect: A button with the feel of a physical key: below the button body is a layer of "thickness" in the same color family but darker (made with an unblurred shadow below), with another layer of soft shadow around the outside; when the mouse hovers, the button lifts slightly and the thickness increases; when pressed, the whole button presses down until almost flat, the thickness and shadow shrink, and it springs back on release. About 0.12 seconds, crisp and responsive. (CSS: box-shadow: 0 6px 0 darker color, 0 10px 20px semi-transparent; on :active, translateY(5px) and shrink the first shadow layer to 1px)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx232">`, preview text "Get Started Now". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "3D Press Button".

### JavaScript — `FX[232]` from `site/fx.js`

```js
232(s,x,card){const b=bxBtn('bx-3d',x);s.append(b);bxDemo(b,card,()=>{b.classList.add('dn');setTimeout(()=>b.classList.remove('dn'),180)},1600)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx232` rules from `site/fx.css`

_No dedicated `.fx232` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #232
