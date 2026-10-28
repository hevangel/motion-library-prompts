# 148 · Floating Label Input — 輸入框浮動標籤

When you tap into an input, the hint text shrinks and floats up, and the underline expands from the center

- Component: Form · Controls (`control`)
- Timing: Hover · Click, Entrance
- Tech: CSS
- Uses: App Interface, UI Interaction
- Style / keywords: Input Form Label Floating Focus Floating Label Input Focus Form Material App Mobile Mobile Device Micro-interaction Mobile App Micro-interaction
- Tag: Floating label
- Example text: "Email" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Floating Label Input (輸入框浮動標籤)" motion effect: A form input normally shows only a hint label like a placeholder; when you tap in (focus), the label shrinks and floats up above the input, while the underline expands from the center out to both sides in the accent color and the cursor starts blinking; after entering content and leaving, the label stays in the small-text state above, returning to its original position only when the field is cleared. About 0.3–0.4 seconds, decelerating. (CSS: the label is absolutely positioned, using :focus-within or :not(:placeholder-shown) to change top and font-size; the underline uses transform:scaleX(0→1))
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx148">`, preview text "Email". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Floating Label Input".

### JavaScript — `FX[148]` from `site/fx.js`

```js
148(s,x,card){const f=el('div','fli');f.innerHTML='<label></label><div class="val"><span class="tx"></span><i class="caret"></i></div><i class="ul"></i>';f.querySelector('label').textContent=x;s.append(f);const tx=f.querySelector('.tx');const word='hello@example.com';
  const cycle=()=>{f.classList.remove('fo','filled');tx.textContent='';setTimeout(()=>{f.classList.add('fo');[...word].forEach((c,i)=>setTimeout(()=>tx.textContent=word.slice(0,i+1),400+i*70))},500);setTimeout(()=>{f.classList.remove('fo');f.classList.add('filled')},500+400+word.length*70+900)};
  cycle();card._timers.push(setInterval(cycle,4600))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx148` rules from `site/fx.css`

_No dedicated `.fx148` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #148
