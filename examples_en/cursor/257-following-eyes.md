# 257 · Following Eyes — 眼睛跟隨

A pair of large eyes whose pupils keep staring and turning toward the cursor, blinking occasionally

- Component: Cursor (`cursor`)
- Timing: Hover · Click, Loop · Idle
- Tech: CSS
- Uses: UI Interaction, Logo · Brand
- Style / keywords: Eyes Pupils Following Staring Cute Mascot 404 Googly Eyes Follow Cursor Mascot Cursor Mouse
- Tag: JS atan2
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Following Eyes (眼睛跟隨)" motion effect: A pair of large eyes (eye whites + pupils, with a small highlight dot on each pupil), whose pupils keep turning toward the cursor direction: the farther the cursor, the closer the pupils get to the edge of the eye socket, and when the cursor is directly in front of the eyes the pupils return to the center; every few seconds both eyes blink quickly together once (the eyes flatten vertically and recover, about 0.15 seconds). Suitable for a mascot, a 404 page, or playful interaction. (JS: each eye calculates the atan2 angle from its center point, the distance is min(1, distance / range) × maximum offset, and the pupils are moved with transform; blinking toggles a class on scaleY)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx257">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Following Eyes".

### JavaScript — `FX[257]` from `site/fx.js`

```js
257(s,x,card){const l=el('div','abs gl cr-ey');const f=el('div','cr-ef');f.innerHTML='<div class="cr-e"><i></i></div><div class="cr-e"><i></i></div><span class="cr-m"></span>';l.append(f);s.append(l);const es=[...f.querySelectorAll('.cr-e')];let blink=0;
  vpointer(l,card,(px,py)=>{const r=l.getBoundingClientRect();es.forEach(e=>{const q=e.getBoundingClientRect(),cx=q.left-r.left+q.width/2,cy=q.top-r.top+q.height/2,a=Math.atan2(py-cy,px-cx),d=Math.min(1,Math.hypot(px-cx,py-cy)/(q.width*1.5))*q.width*.26;e.firstChild.style.transform=`translate(${Math.cos(a)*d}px,${Math.sin(a)*d}px)`})});
  card._timers.push(setInterval(()=>{f.classList.add('bk');setTimeout(()=>f.classList.remove('bk'),160)},2600))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx257` rules from `site/fx.css`

_No dedicated `.fx257` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #257
