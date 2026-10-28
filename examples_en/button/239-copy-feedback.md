# 239 · Copy Feedback — 複製成功回饋

After pressing copy, the icon rotates into a checkmark, and a small "Copied" hint pops up above

- Component: Button (`button`)
- Timing: Switch
- Tech: CSS
- Uses: UI Interaction, App Interface
- Style / keywords: Copy Clipboard Check Hint tooltip Feedback Copy To Clipboard Feedback Check Code Button
- Tag: CSS transition
- Example text: "npm i gsap" (stage background: dark, fixed text)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Copy Feedback (複製成功回饋)" motion effect: A copy button beside a line of code (or text): when pressed, the copy icon rotates, shrinks and disappears, a check icon appears with an elastic scale-up, and the button background becomes the accent color; at the same time a small "Copied" hint box pops up above the button, and after about 1.5 seconds everything returns to its original state. (CSS: the two SVG icons are stacked in the same cell, using a class to switch transform and opacity, with a transition using a bouncy cubic-bezier(.3,1.5,.5,1); the hint box is absolutely positioned above the button; JS calls navigator.clipboard.writeText, then adds the class and removes it with setTimeout)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx239">`, preview text "npm i gsap". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Copy Feedback".

### JavaScript — `FX[239]` from `site/fx.js`

```js
239(s,x,card){const w=el('div','bx-cpw');w.innerHTML='<code></code><button class="bx-cp" aria-label="複製"><svg class="i1" viewBox="0 0 24 24"><rect x="8" y="8" width="12" height="12" rx="2"/><path d="M16 8V5a1 1 0 0 0-1-1H5a1 1 0 0 0-1 1v10a1 1 0 0 0 1 1h3"/></svg><svg class="i2" viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7"/></svg><em>已複製</em></button>';w.querySelector('code').textContent=x;w.style.fontSize=Math.min(4,34/chars(x).length)+'cqw';s.append(w);const b=w.querySelector('button');let tm;
  const go=()=>{b.classList.add('ok');clearTimeout(tm);tm=setTimeout(()=>b.classList.remove('ok'),1500)};b.addEventListener('click',go);card._kill.push(()=>clearTimeout(tm));bxDemo(b,card,go,2800)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx239` rules from `site/fx.css`

_No dedicated `.fx239` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #239
