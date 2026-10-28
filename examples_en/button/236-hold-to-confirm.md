# 236 · Hold to Confirm — 長按確認

Holding it down slowly fills the progress, releasing rolls it back, and only a full fill executes it, suitable for dangerous actions like deletion

- Component: Button (`button`)
- Timing: Hover · Click
- Tech: CSS
- Uses: UI Interaction, App Interface
- Style / keywords: Long Press Hold Confirm Delete Dangerous Action Progress Hold To Confirm Long Press Delete Destructive Button
- Tag: CSS transition
- Example text: "Hold to Delete" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Hold to Confirm (長按確認)" motion effect: A button for dangerous actions (such as deletion): an outline style; when the user holds it down, a fill layer fills the whole button from left to right at a constant speed over about 1.2 seconds, and the button shrinks slightly; if released midway, the fill quickly rolls back and nothing is executed; once fully filled, the button gives a slight bounce and the text becomes "Deleted ✓". This prevents accidental taps. (CSS: the fill layer has transform:scaleX(0); while held, a class changes it to scaleX(1) with a 1.2s linear transition; on release the class is removed and it rolls back with a shorter transition; JS starts a 1.2-second timer on pointerdown and cancels it on pointerup / pointerleave)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx236">`, preview text "Hold to Delete". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Hold to Confirm".

### JavaScript — `FX[236]` from `site/fx.js`

```js
236(s,x,card){const b=bxBtn('bx-hd',x);b.insertAdjacentHTML('afterbegin','<i class="bx-hf"></i>');const lb=b.querySelector('span');s.append(b);const hint=el('div','bx-hint','按住不放');s.append(hint);let tm=0,real=0;
  const down=()=>{if(b.classList.contains('ok'))return;b.classList.add('hold');tm=setTimeout(()=>{b.classList.remove('hold');b.classList.add('ok');lb.textContent='已刪除 ✓';setTimeout(()=>{b.classList.remove('ok');lb.textContent=x},1500)},1200)};
  const up=()=>{clearTimeout(tm);b.classList.remove('hold')};
  b.addEventListener('pointerdown',()=>{real=Date.now();down()});['pointerup','pointerleave'].forEach(ev=>b.addEventListener(ev,up));card._kill.push(()=>clearTimeout(tm));
  let k=0;card._timers.push(setInterval(()=>{if(Date.now()-real<5000)return;k++;down();setTimeout(()=>{if(Date.now()-real>5000&&k%2)up()},500)},3200))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx236` rules from `site/fx.css`

_No dedicated `.fx236` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #236
