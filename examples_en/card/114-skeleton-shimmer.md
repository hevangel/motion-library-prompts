# 114 · Skeleton Shimmer — 骨架載入

A skeleton is shown before the content loads; after a sheen sweeps across, the real content fades in

- Component: Cards · Groups (`card`)
- Timing: Loop · Idle, Entrance
- Tech: CSS
- Uses: UI Interaction, Numbers & Data
- Style / keywords: Skeleton Loading Reading Placeholder Skeleton Loading Shimmer Placeholder Loader
- Tag: Skeleton
- Example text: "Let's Design Motion Together" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Skeleton Shimmer (骨架載入)" motion effect: While the data is loading, the card first shows a low-contrast skeleton: a circular avatar, two text bars of different lengths, and a large image area, with a soft highlight continuously sweeping across the skeleton from left to right; when loading completes, the skeleton fades out, and the real avatar, title, time and image fade in while sliding slightly upward into place. (CSS: the skeleton elements use a linear-gradient highlight band + background-size:300%, with keyframes moving the background-position; when loading completes, a class is switched so the skeleton goes to opacity 0 and the content to opacity 1 + a translateY transition)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx114">`, preview text "Let's Design Motion Together". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Skeleton Shimmer".

### JavaScript — `FX[114]` from `site/fx.js`

```js
114(s,x,card){const c=el('div','skc');c.innerHTML='<div class="sk"><i class="av"></i><i class="l1"></i><i class="l2"></i><i class="im"></i></div><div class="rl"><i class="av"></i><b></b><span>剛剛 · 3 分鐘閱讀</span><i class="im"></i></div>';c.querySelector('.rl b').textContent=x;s.append(c);card._timers.push(setInterval(()=>c.classList.toggle('ld'),2200))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx114` rules from `site/fx.css`

_No dedicated `.fx114` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #114
