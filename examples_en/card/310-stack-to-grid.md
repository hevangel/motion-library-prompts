# 310 · Stack to Grid — 照片堆展開

A scattered stack of photos smoothly arranges into a tidy grid with one click, and stacks back up with another click

- Component: Cards · Groups (`card`)
- Timing: Switch
- Tech: GSAP
- Uses: UI Interaction, Headline · Hero
- Style / keywords: Photos Stack Spread Out Grid Album Organize Photo Pile Stack To Grid Spread Flip Cards Group
- Tag: Flip
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-20

**AI prompt (English copy format):**

```text
"Stack to Grid (照片堆展開)" motion effect: A scattered stack of photos (each with a wide border, randomly tilted at different angles, stacked in the center): when clicked, the photos fly one after another (about 0.04 seconds apart) smoothly into a tidy 3 × 2 grid position and straighten up; click again and they fly from the grid back into a scattered stack. About 0.7 seconds, ease-in-out. (GSAP Flip: Flip.getState(photos) → switch the container's class (from absolutely-positioned stacking to a grid layout, rotate reset to zero) → Flip.from(state, {absolute:true, stagger:.04}))
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx310">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Stack to Grid".

### JavaScript — `FX[310]` from `site/fx.js`

```js
310(s,x,card){const w=el('div','cg-sg2');const cs=[0,1,2,3,4,5].map(i=>{const c=el('div','cg-ph');c.innerHTML=mdImg(i);c.style.setProperty('--r',((i*37)%25-12)+'deg');w.append(c);return c});const lb=el('div','cg-lb','點一下展開');s.append(w,lb);let open=false,real=0;
  const tog=()=>{const st=Flip.getState(cs);open=!open;w.classList.toggle('open',open);lb.textContent=open?'點一下收起':'點一下展開';Flip.from(st,{duration:.7,ease:'power3.inOut',stagger:.04,absolute:true})};
  w.onclick=()=>{real=Date.now();tog()};card._timers.push(setInterval(()=>{if(Date.now()-real>5000)tog()},2400))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx310` rules from `site/fx.css`

_No dedicated `.fx310` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #310
