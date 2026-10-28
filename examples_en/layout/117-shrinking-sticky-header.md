# 117 · Shrinking Sticky Header — 導覽列捲動縮小

When scrolling down, the navigation bar gets shorter, the Logo shrinks, and a frosted-glass background is added

- Component: Layout · Pages (`layout`)
- Timing: Scroll-triggered
- Tech: CSS
- Uses: Scroll Effects, UI Interaction
- Style / keywords: Navigation Bar Header Menu header navbar Scroll Shrink Sticky Frosted Glass Sticky Shrink Header On Scroll
- Tag: Sticky
- Example text: "LOGO" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Shrinking Sticky Header (導覽列捲動縮小)" motion effect: The header navigation bar is fixed at the very top (sticky). At the top of the page the navigation bar is taller, the Logo is larger and the background is transparent; as soon as you scroll down past a certain distance, the navigation bar smoothly becomes shorter, the Logo shrinks, and a translucent frosted-glass background and a faint shadow appear; scrolling back to the top restores the original state. About a 0.35-second transition. (How it works: listen to scroll, and add a .shrink class when scrollY exceeds a certain value; CSS transitions padding, font-size, background and box-shadow, with the background using backdrop-filter:blur)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx117">`, preview text "LOGO". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Shrinking Sticky Header".

### JavaScript — `FX[117]` from `site/fx.js`

```js
117(s,x,card){const sc=el('div','scr nopad');const h=el('header','shd');h.innerHTML='<b></b><nav><i></i><i></i><i></i></nav>';h.querySelector('b').textContent=x;const c=el('div','shc');for(let i=0;i<8;i++)c.append(el('i'));sc.append(h,c);s.append(sc);
  sc.addEventListener('scroll',()=>h.classList.toggle('sm',sc.scrollTop>12));let idle=0;['wheel','touchstart','pointerdown'].forEach(e=>sc.addEventListener(e,()=>idle=performance.now()+3500,{passive:true}));
  ticks.set(card,t=>{if(performance.now()<idle)return;sc.scrollTop=(.5-.5*Math.cos(t*.9))*(sc.scrollHeight-sc.clientHeight)})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx117` rules from `site/fx.css`

_No dedicated `.fx117` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #117
