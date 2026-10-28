# 169 · Tooltip Pop — 提示框彈出

When you hover over an icon, a tooltip pops up elastically from below

- Component: Form · Controls (`control`)
- Timing: Hover · Click
- Tech: CSS
- Uses: UI Interaction, App Interface
- Style / keywords: tooltip tooltip explanation hint bubble popover hover hint hover hover mouse-enter hover-over interaction
- Tag: CSS hover
- Example text: "Help Info Share" (stage background: dark)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Tooltip Pop (提示框彈出)" motion effect: A row of circular icon buttons. When the mouse moves over an icon, a tooltip with a small triangular arrow pops up above it, elastically scaling up from about 60% size and a slightly lower position, using the arrow as the origin, and moving up into place (about 0.3 seconds, with a slight overshoot); moving away fades it out and shrinks it back. (CSS: tooltip position:absolute, transform-origin set at the arrow, on hover scale(0.6) to 1 + translateY + opacity, transition cubic-bezier(.3,1.5,.5,1); remember pointer-events:none to avoid flickering)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx169">`, preview text "Help Info Share". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Tooltip Pop".

### JavaScript — `FX[169]` from `site/fx.js`

```js
169(s,x,card){const w=el('div','ttw');const ws=words(x);const its=['?','i','↗'].map((g,i)=>{const b=el('span','tti');b.textContent=g;const t=el('span','tip');t.textContent=ws[i%ws.length];b.append(t);w.append(b);return b});s.append(w);autoHover(w,its,card,1200)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx169` rules from `site/fx.css`

_No dedicated `.fx169` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #169
