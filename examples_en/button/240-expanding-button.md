# 240 · Expanding Button — 展開文字按鈕

Usually only a round "+" icon; on hover it expands to the right to reveal text, and the plus rotates

- Component: Button (`button`)
- Timing: Hover · Click
- Tech: CSS
- Uses: UI Interaction, App Interface
- Style / keywords: Expand Floating Button FAB Plus Icon Button Expanding Icon Button Floating Action Reveal Label Button
- Tag: CSS max-width
- Example text: "New Project" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Expanding Button (展開文字按鈕)" motion effect: A floating action button that is usually a circle with only a "+"; when the mouse hovers, the button smoothly expands to the right into a capsule shape, revealing a text label (for example "New Project"), while the plus rotates 90 degrees at the same time; the text fades in only after the expansion is halfway; when the mouse leaves, it retracts into a circle. About 0.5 seconds. (CSS: the button has overflow:hidden, using max-width to transition from the circle's width to a larger value, the text opacity is paired with a transition-delay; the plus uses rotate(90deg))
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx240">`, preview text "New Project". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Expanding Button".

### JavaScript — `FX[240]` from `site/fx.js`

```js
240(s,x,card){const b=el('button','bx-ex');b.innerHTML='<b>+</b><span></span>';b.querySelector('span').textContent=x;b.style.fontSize=Math.min(5,40/chars(x).length)+'cqw';b.setAttribute('aria-label',x);s.append(b);autoHover(b,[b],card,1500)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx240` rules from `site/fx.css`

_No dedicated `.fx240` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #240
