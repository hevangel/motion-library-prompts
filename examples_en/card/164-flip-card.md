# 164 · Flip Card — 卡片 3D 翻面

Hovering over a card flips it in 3D to its back, showing more information

- Component: Cards · Groups (`card`)
- Timing: Hover · Click
- Tech: CSS
- Uses: UI Interaction
- Style / keywords: Card Flip Turnover Front and Back 3D flip card hover Back Side Hover Mouse Enter Hover Interaction
- Tag: CSS 3D
- Example text: "Brand Website Illustration" (stage background: dark)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Flip Card (卡片 3D 翻面)" motion effect: A row of project cards, with the hero visual and heading on the front; when the mouse moves in, the card flips 180 degrees in 3D around the vertical axis to the back, which shows action text such as 'View Project →', with a slight overshoot bounce to the flip; moving out flips it back to the front. About 0.7 seconds. (CSS: the outer layer has perspective, the inner layer transform-style:preserve-3d + a transition on transform, rotateY(180deg) on hover; both faces have backface-visibility:hidden, and the back face is pre-rotated rotateY(180deg))
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx164">`, preview text "Brand Website Illustration". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Flip Card".

### JavaScript — `FX[164]` from `site/fx.js`

```js
164(s,x,card){const w=el('div','flp');const ws=words(x);const cs=[0,1,2].map(i=>{const c=el('div','fc2');c.innerHTML='<div class="in"><div class="f"><b></b><small>PROJECT 0'+(i+1)+'</small></div><div class="b">查看專案 →</div></div>';c.querySelector('.f').style.background=`linear-gradient(160deg,${GC[i]},${GC[(i+2)%5]})`;c.querySelector('b').textContent=ws[i%ws.length];w.append(c);return c});s.append(w);autoHover(w,cs,card,1400)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx164` rules from `site/fx.css`

_No dedicated `.fx164` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #164
