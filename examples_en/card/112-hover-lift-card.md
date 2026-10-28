# 112 · Hover Lift Card — 卡片浮起

On hover the card lifts and its shadow deepens, and the thumbnail zooms inside its frame

- Component: Cards · Groups (`card`)
- Timing: Hover · Click
- Tech: CSS
- Uses: UI Interaction
- Style / keywords: Card hover Lift Shadow Thumbnail Zoom Hover Lift Card Shadow Zoom Portfolio Product
- Tag: CSS hover
- Example text: "Brand Website Illustration" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Hover Lift Card (卡片浮起)" motion effect: A row of work cards (a thumbnail on top, a title and a line of text below). When the mouse moves over a card, the card lifts up a little and a deeper, larger shadow appears, and the thumbnail slowly zooms to about 1.15× inside its original frame (the frame stays the same, the image is cropped); when the mouse leaves, it smoothly returns to its original position. About 0.45–0.6 seconds, ease-out. (CSS: the card transitions transform and box-shadow, on :hover translateY(-8px); the thumbnail's frame has overflow:hidden, and the inner image uses transform:scale(1.14))
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx112">`, preview text "Brand Website Illustration". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Hover Lift Card".

### JavaScript — `FX[112]` from `site/fx.js`

```js
112(s,x,card){const w=el('div','lift');const ws=words(x);const cs=[0,1,2].map(i=>{const c=el('div','lc');c.innerHTML='<div class="im"><i></i></div><b></b><span></span>';c.querySelector('b').textContent=ws[i%ws.length];c.querySelector('.im i').style.background=`linear-gradient(135deg,${GC[i]},${GC[(i+1)%5]})`;w.append(c);return c});s.append(w);
  let k=0,real=false;w.addEventListener('pointerenter',()=>{real=true;cs.forEach(c=>c.classList.remove('hv'))});w.addEventListener('pointerleave',()=>real=false);
  card._timers.push(setInterval(()=>{if(real)return;cs.forEach((c,i)=>c.classList.toggle('hv',i===k%3));k++},1300))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx112` rules from `site/fx.css`

_No dedicated `.fx112` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #112
