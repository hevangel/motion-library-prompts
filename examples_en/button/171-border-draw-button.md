# 171 · Border Draw Button — 邊框描繪按鈕

When you hover over a button, its four borders are drawn in sequence to enclose it

- Component: Button (`button`)
- Timing: Hover · Click
- Tech: CSS
- Uses: UI Interaction, Emphasis
- Style / keywords: button border stroke line draw border draw outline button hover hover hover mouse-enter hover-over interaction
- Tag: CSS transition
- Example text: "Learn More" (stage background: dark)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Border Draw Button (邊框描繪按鈕)" motion effect: A button with only a very faint thin frame normally. On mouse-enter, an accent-colored border is drawn in sequence starting from the top-left corner: top edge to the right, then right edge downward, then bottom edge to the left, then left edge upward, each segment about 0.18 seconds, joining up to enclose the button, and when the drawing finishes the text also changes to the accent color; on mouse-leave it retracts in the reverse order. (CSS: four absolutely positioned line elements, each using scaleX / scaleY with a different transform-origin; use transition-delay to arrange the order, with opposite delays for the hover and non-hover states)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx171">`, preview text "Learn More". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Border Draw Button".

### JavaScript — `FX[171]` from `site/fx.js`

```js
171(s,x,card){const b=el('button','bdr');b.innerHTML='<i class="t"></i><i class="r"></i><i class="b"></i><i class="l"></i><span></span>';b.querySelector('span').textContent=x;s.append(b);autoHover(b,[b],card,1600)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx171` rules from `site/fx.css`

_No dedicated `.fx171` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #171
