# 109 · Shine Sweep Button — 光澤掃過按鈕

A diagonal sheen sweeps across the button on a timer; on hover it speeds up and the button lifts

- Component: Button (`button`)
- Timing: Hover · Click, Loop · Idle
- Tech: CSS
- Uses: UI Interaction, Emphasis
- Style / keywords: Button Sheen Reflection Light Sweep Flash Shine Sweep Glint Shimmer Button CTA
- Tag: CSS hover
- Example text: "Buy Now" (stage background: cream)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Shine Sweep Button (光澤掃過按鈕)" motion effect: On a solid button there is a diagonal translucent highlight that quickly sweeps from left to right about every 2.4 seconds, like a reflection on metal or glass; when the mouse moves over it, the sheen sweeps faster, and the button lifts slightly while its shadow deepens at the same time. (CSS: the button has overflow:hidden, ::after creates a gradient highlight band with skewX(-20deg), and keyframes change its left position; :hover shortens the animation-duration and adds translateY)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage cream fx109">`, preview text "Buy Now". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Shine Sweep Button".

### JavaScript — `FX[109]` from `site/fx.js`

```js
109(s,x){const b=el('button','shb');b.textContent=x;b.style.fontSize=Math.min(5,40/chars(x).length)+'cqw';s.append(b)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx109` rules from `site/fx.css`

_No dedicated `.fx109` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #109
