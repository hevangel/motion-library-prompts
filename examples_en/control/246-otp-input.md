# 246 · OTP Input — 驗證碼輸入

A four-box verification code; typing one box auto-advances to the next; the boxes jump up in sequence when correct, and the whole row shakes when wrong

- Component: Form · Controls (`control`)
- Timing: Switch
- Tech: CSS
- Uses: UI Interaction, App Interface
- Style / keywords: Verification Code OTP One-Time Password SMS Login PIN Code Input Verification Auto Focus Form Control
- Tag: JS + CSS
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"OTP Input (驗證碼輸入)" motion effect: A four-box verification code input: each box can hold only one digit; after typing, that box gives a light bounce and focus automatically advances to the next box; pressing Backspace in an empty box returns to the previous box and clears it; once all four boxes are filled it automatically verifies: when correct, each box jumps up in sequence and its background fills; when wrong, the whole row shakes left and right and the border changes to a warning style. (JS: each box has maxLength=1 and inputMode="numeric"; the input event focuses the next box, keydown Backspace handles going back; the result triggers CSS keyframes with a class, staggering the jumps with animation-delay; on mobile the font size is at least 16px to avoid auto-zoom)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx246">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "OTP Input".

### JavaScript — `FX[246]` from `site/fx.js`

```js
246(s,x,card){const w=el('div','fm-otp');w.innerHTML='<p>輸入驗證碼</p><div class="fm-ob"></div>';const ob=w.querySelector('.fm-ob');const ins=[...Array(4)].map(()=>{const i=el('input');i.inputMode='numeric';i.maxLength=1;i.autocomplete='one-time-code';ob.append(i);return i});s.append(w);let real=0;
  const check=()=>{const v=ins.map(i=>i.value).join('');w.classList.remove('ok','bad');if(v.length===4){void w.offsetWidth;w.classList.add(v==='2026'?'ok':'bad')}};
  ins.forEach((i,k)=>{i.addEventListener('input',()=>{real=Date.now();i.value=i.value.replace(/\D/g,'').slice(-1);i.classList.toggle('f',!!i.value);if(i.value&&ins[k+1])ins[k+1].focus();check()});
    i.addEventListener('keydown',e=>{if(e.key==='Backspace'&&!i.value&&ins[k-1]){ins[k-1].focus();ins[k-1].value='';ins[k-1].classList.remove('f');check()}});i.addEventListener('focus',()=>{if(Date.now()-real>6000){ins.forEach(x=>{x.value='';x.classList.remove('f')});n=0;check();real=Date.now();if(i!==ins[0])return ins[0].focus()}real=Date.now();i.select()})});
  let n=0;card._timers.push(setInterval(()=>{if(Date.now()-real<6000||ins.includes(document.activeElement))return;if(n<4){ins[n].value='2026'[n];ins[n].classList.add('f')}else if(n===7){ins.forEach(i=>{i.value='';i.classList.remove('f')})}n=(n+1)%9;check()},380))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx246` rules from `site/fx.css`

_No dedicated `.fx246` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #246
