# 244 · Password Strength — 密碼強度條

While typing a password, the strength bar below grows segment by segment, changing with strength and showing a hint

- Component: Form · Controls (`control`)
- Timing: Switch
- Tech: CSS
- Uses: UI Interaction, Numbers & Data
- Style / keywords: Password Strength Signup Validation Form Password Strength Meter Signup Validation Form Control
- Tag: JS + CSS
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Password Strength (密碼強度條)" motion effect: Below a password input field are four strength segments: as the user types, the strength is calculated in real time (whether the length reaches 8 characters, and whether it has uppercase letters, numbers and symbols); the more conditions met, the more segments grow out from left to right; the higher the strength, the stronger the segments' visual, and the text below shows in sequence "Too Weak / Fair / Good / Very Strong"; on the right of the input is an eye button to show/hide the password; when the input is focused its border lights up. (JS: the input event calculates a score of 0-4, sets data-level and each segment's class; newly lit segments grow with a scaleX 0 to 1 keyframes)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx244">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Password Strength".

### JavaScript — `FX[244]` from `site/fx.js`

```js
244(s,x,card){const w=el('div','fm-pw');w.innerHTML='<label>密碼</label><div class="fm-pf"><input type="text" spellcheck="false" autocomplete="off"><button type="button" aria-label="顯示密碼">👁</button></div><div class="fm-bar"><i></i><i></i><i></i><i></i></div><small></small>';s.append(w);
  const inp=w.querySelector('input'),bars=[...w.querySelectorAll('.fm-bar i')],tip=w.querySelector('small'),eye=w.querySelector('button');let show=false;const L=['','太弱','普通','不錯','很強'];
  const score=v=>!v?0:Math.min(4,(v.length>=8)+/[A-Z]/.test(v)+/\d/.test(v)+/[^\w]/.test(v)+(v.length>=4?0:-1)+1);
  const upd=()=>{const n=Math.max(0,score(inp.value));w.dataset.lv=n;bars.forEach((b,i)=>b.classList.toggle('on',i<n));tip.textContent=L[n]};
  const mask=()=>{inp.type=show?'text':'password'};eye.onclick=()=>{show=!show;mask()};show=false;mask();inp.addEventListener('input',()=>{real=Date.now();upd()});inp.addEventListener('focus',()=>real=Date.now());
  let real=0,i=0;const D=['m','mo','mot','moti','motio','motion','Motion','Motion2','Motion26','Motion26!'];upd();
  card._timers.push(setInterval(()=>{if(Date.now()-real<6000||document.activeElement===inp)return;inp.value=i<D.length?D[i]:'';i=(i+1)%(D.length+4);upd()},320))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx244` rules from `site/fx.css`

_No dedicated `.fx244` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #244
