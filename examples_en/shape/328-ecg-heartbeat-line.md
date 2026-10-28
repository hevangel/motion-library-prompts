# 328 · ECG Heartbeat Line — 心電圖線條

An ECG waveform is drawn from left to right, a glowing cursor dot advances along the line, and the heart-rate figure beside it pulses

- Component: Shapes · SVG (`shape`)
- Timing: Loop · Idle
- Tech: GSAP
- Uses: Numbers & Data, App Interface
- Style / keywords: ECG Heartbeat Waveform Health Medical Monitoring ECG Heartbeat Pulse Monitor Health Graphics SVG
- Tag: DrawSVG
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-21

**AI prompt (English copy format):**

```text
"ECG Heartbeat Line (心電圖線條)" motion effect: An ECG display for a medical or health app: on a dark screen with fine grid lines, a glowing ECG waveform (flat line, small wave, the sharp QRS wave, T wave, repeating) is drawn from left to right, and a glowing cursor dot advances along with the drawing front; after drawing to the end, the line begins disappearing from the left side and is redrawn; the top-right shows a heart-rate figure (occasionally varying slightly) and a heart beating regularly. (GSAP: DrawSVG "0% 0%" → "0% 100%" to draw it out, then to "100% 100%" to make it disappear; the cursor dot uses MotionPathPlugin along the same path; the heart uses scale yoyo)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx328">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "ECG Heartbeat Line".

### JavaScript — `FX[328]` from `site/fx.js`

```js
328(s,x){const id='ecg'+Math.random().toString(36).slice(2);const seg=o=>`L${o+20},50 L${o+26},46 L${o+30},50 L${o+36},50 L${o+39},56 L${o+43},18 L${o+47},68 L${o+51},50 L${o+60},50 L${o+66},43 L${o+74},50 L${o+80},50`;let d='M0,50 ';for(let o=0;o<320;o+=80)d+=seg(o)+' ';
  s.insertAdjacentHTML('beforeend',`<div class="sv-ecg"><svg viewBox="0 0 320 100" preserveAspectRatio="none"><defs><pattern id="${id}g" width="16" height="16" patternUnits="userSpaceOnUse"><path d="M16,0 H0 V16" fill="none"/></pattern></defs><rect width="320" height="100" fill="url(#${id}g)" class="gr"/><path id="${id}" class="tr" d="${d}"/><circle class="hd" r="2.6"/></svg><div class="sv-bpm"><b>72</b><small>BPM</small><span class="hrt">♥</span></div></div>`);
  const w=s.querySelector('.sv-ecg'),tr=w.querySelector('.tr'),hd=w.querySelector('.hd'),bpm=w.querySelector('.sv-bpm b'),hrt=w.querySelector('.hrt');
  gsap.timeline({repeat:-1}).fromTo(tr,{drawSVG:'0% 0%'},{drawSVG:'0% 100%',duration:3,ease:'none'}).to(hd,{motionPath:{path:'#'+id,align:'#'+id,alignOrigin:[.5,.5]},duration:3,ease:'none'},0).to(tr,{drawSVG:'100% 100%',duration:.6,ease:'none'});
  gsap.to(hrt,{scale:1.35,duration:.12,yoyo:true,repeat:-1,repeatDelay:.6,ease:'power2.out'});gsap.to({},{duration:1.5,repeat:-1,onRepeat:()=>bpm.textContent=70+Math.round(Math.random()*6)})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx328` rules from `site/fx.css`

_No dedicated `.fx328` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #328
