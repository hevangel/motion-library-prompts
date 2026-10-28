# 151 · Shake on Error — 錯誤震動提示

On an input error, the field shakes left and right and an error message slides out below

- Component: Form · Controls (`control`)
- Timing: Hover · Click
- Tech: CSS
- Uses: App Interface, UI Interaction
- Style / keywords: Error Shake Shaking Validation Password Login Form Shake Error Validation Wrong Password Login App Mobile Mobile Device Micro-interaction Mobile App Micro-interaction
- Tag: CSS keyframes
- Example text: "Incorrect password, please try again" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Shake on Error (錯誤震動提示)" motion effect: When the password is wrong at login, the input field shakes rapidly left and right a few times (like shaking its head no, about 0.45 seconds, with the amplitude growing then shrinking), the border simultaneously switches to the error color, and the error message below fades and slides in from 4px above; after the input is corrected, the border and message return to normal. (CSS: keyframes use translateX to move left and right across 10%–90%, cubic-bezier(.36,.07,.19,.97); before replaying, remove the class and trigger a reflow; it can be paired with phone vibration via navigator.vibrate)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx151">`, preview text "Incorrect password, please try again". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Shake on Error".

### JavaScript — `FX[151]` from `site/fx.js`

```js
151(s,x,card){const f=el('div','shk');f.innerHTML='<div class="pw"><span>••••••</span></div><div class="er"></div>';f.querySelector('.er').textContent=x;s.append(f);
  const run=()=>{f.classList.remove('err');void f.offsetWidth;f.classList.add('err');setTimeout(()=>f.classList.remove('err'),2200)};run();card._timers.push(setInterval(run,3000))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx151` rules from `site/fx.css`

_No dedicated `.fx151` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #151
