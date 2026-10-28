# 245 · Range Slider Bubble — 滑桿數值氣泡

While dragging the slider, a value bubble pops up above, moves with the handle, and shrinks back on release

- Component: Form · Controls (`control`)
- Timing: Drag Gesture
- Tech: CSS
- Uses: UI Interaction, Numbers & Data
- Style / keywords: Slider Lever Value Bubble Range Volume Range Slider Tooltip Bubble Value Input Form Control
- Tag: input range
- Example text: "Volume" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Range Slider Bubble (滑桿數值氣泡)" motion effect: A range slider: the portion of the track already dragged over is filled; when the handle is held or dragged, it enlarges slightly, and a value bubble with a small triangle pops up directly above it; the bubble moves horizontally with the handle and displays the number in real time; on release the bubble shrinks and fades out. (CSS: customize the track of input[type=range] and its ::-webkit-slider-thumb; the track fill uses a background linear-gradient with a CSS variable percentage; the bubble is an absolutely positioned output, with left = handle width / 2 + (track width - handle width) x percentage, popping with scale and opacity)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx245">`, preview text "Volume". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Range Slider Bubble".

### JavaScript — `FX[245]` from `site/fx.js`

```js
245(s,x,card){const w=el('div','fm-rg');w.innerHTML='<label></label><div class="fm-rt"><input type="range" min="0" max="100" value="40"><output></output></div>';w.querySelector('label').textContent=x;s.append(w);const r=w.querySelector('input'),o=w.querySelector('output');
  const upd=()=>{const v=+r.value;w.style.setProperty('--p',v);o.textContent=v};r.addEventListener('input',upd);upd();let real=0;['pointerdown','focus'].forEach(e=>r.addEventListener(e,()=>{real=Date.now();w.classList.add('drag')}));['pointerup','blur'].forEach(e=>r.addEventListener(e,()=>w.classList.remove('drag')));
  let t=0;card._kill.push(()=>{});ticks.set(card,tm=>{if(Date.now()-real<5000)return;r.value=Math.round(50+42*Math.sin(tm*.9));upd();w.classList.toggle('drag',Math.cos(tm*.9)>-.3)})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx245` rules from `site/fx.css`

_No dedicated `.fx245` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #245
