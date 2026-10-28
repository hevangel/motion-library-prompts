# 286 · Card Info Slide Up — 資訊面板滑上

Image cards normally only show a title; on hover an information panel slides up from the bottom, while the image moves up and enlarges

- Component: Cards · Groups (`card`)
- Timing: Hover · Click
- Tech: CSS
- Uses: UI Interaction
- Style / keywords: Card Information Panel Slide Up Description Work Card Info Slide Up Overlay Details Hover hover Hovering Hover Over
- Tag: CSS hover
- Example text: "Seaside Forest Night Sky" (stage background: dark)
- Added: 2026-10-20

**AI prompt (English copy format):**

```text
"Card Info Slide Up (資訊面板滑上)" motion effect: A row of vertical image cards, normally only a title bar is exposed at the bottom of the card; when the mouse hovers, the translucent frosted information panel at the bottom slides all the way up, displaying the title, a short description, and a “View →” link, while the image behind it moves up slightly and enlarges; when moving away the panel slides back leaving only the title. About 0.5 seconds. (CSS: panel transform: translateY(calc(100% − title bar height)), on :hover translateY(0); the panel uses a translucent background + backdrop-filter: blur; the image scale 1.08 + translateY)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx286">`, preview text "Seaside Forest Night Sky". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Card Info Slide Up".

### JavaScript — `FX[286]` from `site/fx.js`

```js
286(s,x,card){const ws=words(x);const w=el('div','ho-cg');const its=[0,1,2].map(i=>{const c=el('div','ho-cd');c.innerHTML=mdImg(i)+'<div class="ho-in"><b></b><p>滑過時資訊面板從底部滑上來</p><span>查看 →</span></div>';c.querySelector('b').textContent=ws[i%ws.length];w.append(c);return c});s.append(w);autoHover(w,its,card,1300)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx286` rules from `site/fx.css`

_No dedicated `.fx286` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #286
