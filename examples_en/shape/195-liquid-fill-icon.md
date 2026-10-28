# 195 · Liquid Fill Icon — 液體填充圖示

The liquid surface inside an icon rises slowly with waves, and the percentage increases in sync

- Component: Shapes · SVG (`shape`)
- Timing: Loop · Idle
- Tech: GSAP
- Uses: Numbers & Data, UI Interaction, App Interface
- Style / keywords: liquid fill wave progress percentage loading Liquid Fill Wave Progress Loading Icon SVG graphic
- Tag: SVG clipPath
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Liquid Fill Icon (液體填充圖示)" motion effect: A heart-shaped icon. The liquid inside flows with two layers of waves crossing each other, and the liquid surface slowly rises from the bottom until it fills up, while the percentage number in the center increases in sync from 0% to 100%; outside the liquid surface, the icon's outline is retained. Can be used for upload progress or a goal completion rate. (SVG: use clipPath to constrain the waves inside the icon shape; the wave path is two wavelengths wide, CSS translateX loops seamlessly; the liquid surface height is controlled by a GSAP tween of the outer g's y, and the number tweens in sync)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx195">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Liquid Fill Icon".

### JavaScript — `FX[195]` from `site/fx.js`

```js
195(s){const id='lq'+Math.random().toString(36).slice(2),H='M50,88 C20,68 6,50 6,32 C6,18 17,8 30,8 C40,8 47,14 50,22 C53,14 60,8 70,8 C83,8 94,18 94,32 C94,50 80,68 50,88 Z',W='M0,10 C12.5,0 37.5,0 50,10 C62.5,20 87.5,20 100,10 C112.5,0 137.5,0 150,10 C162.5,20 187.5,20 200,10 L200,120 L0,120 Z';
  const w=el('div','lqw');w.innerHTML=`<svg viewBox="0 0 100 100"><defs><clipPath id="${id}"><path d="${H}"/></clipPath></defs><g clip-path="url(#${id})"><g class="lv"><path class="w1" d="${W}"/><path class="w2" d="${W}"/></g></g><path class="ol" d="${H}"/></svg><b>0%</b>`;s.append(w);const b=w.querySelector('b'),o={v:0};
  gsap.timeline({repeat:-1,repeatDelay:.5}).fromTo(w.querySelector('.lv'),{y:92},{y:12,duration:3,ease:'power1.inOut'},0).fromTo(o,{v:0},{v:100,duration:3,ease:'power1.inOut',onUpdate:()=>b.textContent=Math.round(o.v)+'%'},0).to({},{duration:.8})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx195` rules from `site/fx.css`

_No dedicated `.fx195` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #195
