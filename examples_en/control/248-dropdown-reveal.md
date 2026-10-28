# 248 · Dropdown Reveal — 下拉選單展開

When a dropdown is opened, the panel pops out from the top, options slide in one after another, and the arrow flips

- Component: Form · Controls (`control`)
- Timing: Switch
- Tech: CSS
- Uses: UI Interaction
- Style / keywords: Dropdown Menu Expand Options Sequential Dropdown Select Menu Stagger Reveal Form Control
- Tag: transition-delay
- Example text: "Taipei Taichung Kaohsiung Hualien Tainan" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Dropdown Reveal (下拉選單展開)" motion effect: Dropdown menu: when the menu button is clicked, the arrow on the right flips 180 degrees, and the options panel below expands from its top edge with a slight bounce (scaleY 0.6 → 1, fading in), with the options inside sliding down and fading in one after another (each spaced about 0.05 seconds apart); when hovering over an option, its background lights up faintly; after a selection, the panel collapses and the button displays the selected value. (CSS: panel transform-origin: top, transition using cubic-bezier(.3,1.3,.5,1); each option sets --i, and on expansion transition-delay: calc(var(--i) × 0.05s))
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx248">`, preview text "Taipei Taichung Kaohsiung Hualien Tainan". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Dropdown Reveal".

### JavaScript — `FX[248]` from `site/fx.js`

```js
248(s,x,card){const ws=words(x);const w=el('div','fm-dd');w.innerHTML='<button type="button" class="fm-dh"><span></span><svg viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg></button><ul></ul>';const sp=w.querySelector('.fm-dh span'),ul=w.querySelector('ul');sp.textContent=ws[0];
  ws.slice(0,4).forEach((t,i)=>{const li=el('li');li.style.setProperty('--i',i);li.textContent=t;li.onclick=()=>{real=Date.now();sp.textContent=t;w.classList.remove('open')};ul.append(li)});s.append(w);let real=0;
  w.querySelector('.fm-dh').onclick=()=>{real=Date.now();w.classList.toggle('open')};card._timers.push(setInterval(()=>{if(Date.now()-real<5000)return;w.classList.toggle('open')},1600))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx248` rules from `site/fx.css`

_No dedicated `.fx248` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #248
