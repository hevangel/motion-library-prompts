# 059 · Text Orbit — 軌道

A single word orbits with depth of field

- Component: Text (`text`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Logo · Brand
- Style / keywords: 3D Spatial Rotation
- Tag: Logo·Title
- Example text: "Orbit" (stage background: acc)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Text Orbit (軌道)" motion effect: Text circles along an elliptical dashed orbit, growing larger and sharper as it comes to the front and smaller and fainter as it goes to the back, creating depth of field. About 5 seconds per orbit, with a logo title feel.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage acc fx59">`, preview text "Orbit". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Text Orbit".

### JavaScript — `FX[59]` from `site/fx.js`

```js
59(s,x,card){s.append(el('div','ell'));const o=el('div','ob');o.textContent=x;s.append(o);ticks.set(card,t=>{const W=s.offsetWidth;const a=t*1.3;const sc=.55+.45*(1+Math.sin(a))/2;o.style.transform=`translate(-50%,-50%) translate(${Math.cos(a)*W*.31}px,${Math.sin(a)*W*.08}px) scale(${sc})`;o.style.opacity=.45+.55*(1+Math.sin(a))/2;o.style.zIndex=Math.sin(a)>0?3:0})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx59` rules from `site/fx.css`

```css
.fx59 .ell{position:absolute;left:50%;top:50%;width:62cqw;height:16cqw;margin:-8cqw 0 0 -31cqw;border:.3cqw dashed #1115;border-radius:50%}
.fx59 .ob{position:absolute;left:50%;top:50%;font-weight:900;font-size:13cqw;color:#111;white-space:nowrap}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #59
