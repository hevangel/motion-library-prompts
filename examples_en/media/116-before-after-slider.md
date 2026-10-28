# 116 · Before / After Slider — 前後對比滑桿

Drag the handle in the middle to compare the difference between two images, left and right

- Component: Images · Media (`media`)
- Timing: Drag Gesture, Hover · Click
- Tech: CSS
- Uses: UI Interaction
- Style / keywords: Image Comparison Contrast Before and After Slider Drag Before After Compare Slider Image Comparison
- Tag: clip-path·Drag
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Before / After Slider (前後對比滑桿)" motion effect: Two images of the same size overlap, with a straight line and a circular handle (with left and right arrows) in the middle, BEFORE marked in the top-left corner and AFTER in the top-right; when the handle is dragged, the dividing line moves left and right with it, the left side showing the original image and the right side the edited image, making the differences easy to compare; when not operated, it can sway slowly left and right to hint that it is draggable. (How it works: the upper image uses clip-path:inset(0 0 0 var(--p)), on pointerdown/pointermove the cursor's proportion inside the frame is calculated and written into --p; the handle uses setPointerCapture to ensure dragging continues even when dragged outside the frame; on mobile, set touch-action:pan-y)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx116">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Before / After Slider".

### JavaScript — `FX[116]` from `site/fx.js`

```js
116(s,x,card){const w=el('div','ba');w.innerHTML=`<div class="b1">${scene('#9fd3ff','#ffe1b0','#4f7a6a','#264a3f','#fff6d8')}</div><div class="b2">${scene('#1b1f4a','#4a2a6b','#2c2a55','#14122e','#f4f1d0')}</div><div class="hd"><i></i></div><span class="lb l">BEFORE</span><span class="lb r">AFTER</span>`;s.append(w);
  let drag=false,idle=0;const set=v=>w.style.setProperty('--p',v*100+'%');set(.5);const move=e=>{const r=w.getBoundingClientRect();set(Math.min(1,Math.max(0,(e.clientX-r.left)/r.width)))};
  w.addEventListener('pointerdown',e=>{drag=true;idle=Infinity;w.setPointerCapture(e.pointerId);move(e)});w.addEventListener('pointermove',e=>{if(drag)move(e)});w.addEventListener('pointerup',()=>{drag=false;idle=performance.now()+3000});
  ticks.set(card,t=>{if(!drag&&performance.now()>idle)set(.5+.38*Math.sin(t*1.2))})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx116` rules from `site/fx.css`

_No dedicated `.fx116` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #116
