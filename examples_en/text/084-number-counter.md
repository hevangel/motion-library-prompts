# 084 · Number Counter — 數字累加

Numbers count up in a rolling fashion while a progress bar fills in sync

- Component: Text (`text`)
- Timing: Entrance
- Tech: GSAP
- Uses: Numbers & Data
- Style / keywords: 
- Tag: Tween Value
- Example text: "Downloads" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Number Counter (數字累加)" motion effect: The large number below the label quickly counts up from 0 to 128,450, slowing down as it gets closer to the end, while the progress bar below fills in sync; after a pause it fades out and starts over, with the number in tabular figures. (GSAP: tween an object's value + onUpdate writes it with toLocaleString, ease power3.out)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx84">`, preview text "Downloads". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Number Counter".

### JavaScript — `FX[84]` from `site/fx.js`

```js
84(s,x){const w=el('div','ctr');w.innerHTML='<div class="lb"></div><div class="num">0</div><div class="bar"><i></i></div>';w.querySelector('.lb').textContent=x;s.append(w);const n=w.querySelector('.num'),b=w.querySelector('.bar i'),o={v:0};
  gsap.timeline({repeat:-1,repeatDelay:.3}).fromTo(w,{opacity:0},{opacity:1,duration:.3}).fromTo(o,{v:0},{v:128450,duration:2.4,ease:'power3.out',onUpdate:()=>n.textContent=Math.round(o.v).toLocaleString()},0).fromTo(b,{scaleX:0},{scaleX:1,duration:2.4,ease:'power3.out'},0).to(w,{opacity:0,duration:.4},'+=1.4')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx84` rules from `site/fx.css`

_No dedicated `.fx84` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #84
