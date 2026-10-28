# 243 · Segmented Control — 分段控制器

A row of options has a slider block underneath; clicking one slides it over with a slight elasticity and changes its width

- Component: Form · Controls (`control`)
- Timing: Switch
- Tech: CSS
- Uses: UI Interaction, App Interface
- Style / keywords: Segmented Control Switch Tabs tabs Slider Segmented Control Tabs Pill Switcher iOS Form Control
- Tag: CSS transition
- Example text: "Day Week Month Year" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Segmented Control (分段控制器)" motion effect: A capsule-shaped segmented control, for example "Day / Week / Month / Year"; beneath the current option is a solid slider block; when another option is clicked, the slider slides to the new position with a slight rebound and changes its width at the same time to fit the new option's text length; the selected text becomes a color that contrasts with the slider. About 0.45 seconds. (CSS: the slider is absolutely positioned; JS reads the clicked button's offsetLeft and offsetWidth into CSS variables, and transform:translateX(var(--x)) and width transition with cubic-bezier(.5,1.5,.5,1))
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx243">`, preview text "Day Week Month Year". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Segmented Control".

### JavaScript — `FX[243]` from `site/fx.js`

```js
243(s,x,card){const ws=words(x).slice(0,4);const w=el('div','fm-seg');w.innerHTML='<i class="fm-ind"></i>';const bs=ws.map((t,i)=>{const b=el('button');b.textContent=t;b.onclick=()=>{real=Date.now();go(i)};w.append(b);return b});s.append(w);let cur=0,real=0;
  const go=i=>{cur=i;const b=bs[i];w.style.setProperty('--x',b.offsetLeft+'px');w.style.setProperty('--w',b.offsetWidth+'px');bs.forEach((o,j)=>o.classList.toggle('on',j===i))};requestAnimationFrame(()=>go(0));
  card._timers.push(setInterval(()=>{if(Date.now()-real>5000)go((cur+1)%bs.length)},1500))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx243` rules from `site/fx.css`

_No dedicated `.fx243` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #243
