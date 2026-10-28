# 141 · Toggle Switch — 開關切換

As the round knob slides to the other side it stretches slightly, and the track switches state along with it

- Component: Form · Controls (`control`)
- Timing: Hover · Click, Switch
- Tech: CSS
- Uses: UI Interaction, App Interface
- Style / keywords: Toggle Switch switch toggle Settings iOS Round Knob App Mobile Mobile Device Micro-interaction Mobile App Micro-interaction
- Tag: CSS switch
- Example text: "Notifications" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Toggle Switch (開關切換)" motion effect: A toggle switch on an app settings page: when clicked, the round knob slides from one side to the other; during the slide, the knob first stretches horizontally and then shrinks back (like elastic jelly), overshooting slightly on arrival before settling into place; the track simultaneously switches to the accent color of the on state, and returns to a low-contrast state when off. About 0.35 seconds. (CSS: a button with role="switch"; the knob uses a left transition with cubic-bezier(.5,1.4,.5,1) for the overshoot, plus keyframes that widen it at 50%; remember to update aria-checked)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx141">`, preview text "Notifications". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Toggle Switch".

### JavaScript — `FX[141]` from `site/fx.js`

```js
141(s,x,card){const w=el('div','tgw');w.innerHTML='<span class="tgl"></span><button class="tg" role="switch" aria-checked="false"><i></i></button>';w.querySelector('.tgl').textContent=x;s.append(w);const b=w.querySelector('.tg');let real=0;
  const tog=()=>{const on=!b.classList.contains('on');b.classList.toggle('on',on);b.setAttribute('aria-checked',on)};b.onclick=()=>{real=Date.now();tog()};card._timers.push(setInterval(()=>{if(Date.now()-real>3000)tog()},1400))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx141` rules from `site/fx.css`

_No dedicated `.fx141` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #141
