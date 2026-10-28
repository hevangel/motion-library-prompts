# 012 · Magnifier Lens — 放大鏡

Magnifies text with a magnifying glass

- Component: Text (`text`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Emphasis
- Style / keywords: Textured Fill
- Tag: Explainer · Discovery
- Example text: "Magnified" (stage background: dark)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Magnifier Lens (放大鏡)" motion effect: A circular magnifying glass moves back and forth, left and right, across the text; the text inside the lens is enlarged about 1.5x and switches to an accent color, while the text outside the lens is fainter; the magnifying glass has a handle. About 6 seconds per round trip, with an explanatory / discovery feel.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx12">`, preview text "Magnified". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Magnifier Lens".

### JavaScript — `FX[12]` from `site/fx.js`

```js
12(s,x,card){const w=el('div','w');const b=T(x);b.classList.add('base');const o=T(x);o.classList.add('ov');const l=el('div','lens');w.append(b,o,l);s.append(w);
  ticks.set(card,t=>{const W=w.offsetWidth,H=w.offsetHeight;if(!W)return;const px=W*(.5+.42*Math.sin(t*1.1));const r=H*.62;o.style.transformOrigin=`${px}px 50%`;o.style.transform='scale(1.55)';o.style.clipPath=`circle(${r}px at ${px}px 50%)`;l.style.left=px+'px';l.style.width=l.style.height=(r*2*1.55)+'px'})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx12` rules from `site/fx.css`

```css
.fx12 .w{position:relative}
.fx12 .base{color:#666}
.fx12 .ov{position:absolute;left:0;top:0;color:var(--a);text-shadow:0 0 1px #fff}
.fx12 .lens{position:absolute;top:50%;border:.7cqw solid #fff;border-radius:50%;transform:translate(-50%,-50%);box-shadow:0 0 0 2px #0003,inset 0 0 12px #fff4;pointer-events:none}
.fx12 .lens::after{content:"";position:absolute;width:.9cqw;height:7cqw;background:#fff;border-radius:4px;right:-3.3cqw;bottom:-6.2cqw;transform:rotate(-45deg)}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #12
