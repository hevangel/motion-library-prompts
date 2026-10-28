# 099 · Confetti Burst — 彩紙爆發

A burst of confetti affected by gravity

- Component: Background · Ambience (`bg`)
- Timing: Entrance
- Tech: GSAP
- Uses: Emphasis
- Style / keywords: 
- Tag: Physics2D
- Example text: "Congrats" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Confetti Burst (彩紙爆發)" motion effect: As the text elastically scales up, a large handful of paper pieces bursts out from below; the pieces fall in gravity-driven parabolas, rotating and fading out toward the end, once every 2 seconds. (GSAP: Physics2DPlugin velocity / angle / gravity, randomized with random)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx99">`, preview text "Congrats". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Confetti Burst".

### JavaScript — `FX[99]` from `site/fx.js`

```js
99(s,x,card){const t=T(x,Math.min(16,64/chars(x).length));s.append(t);const R=gsap.utils.random;const burst=()=>{const W=s.offsetWidth,H=s.offsetHeight;if(!W)return;gsap.fromTo(t,{scale:.6},{scale:1,duration:.8,ease:'elastic.out(1,.4)'});
  for(let i=0;i<36;i++){const p=el('i','cf');p.style.background=GC[i%5];s.append(p);gsap.set(p,{x:W/2,y:H*.62,rotation:R(0,360)});gsap.to(p,{physics2D:{velocity:R(H*.9,H*1.8),angle:R(215,325),gravity:H*1.9},rotation:'+='+R(-540,540),duration:2,ease:'none',onComplete:()=>p.remove()});gsap.to(p,{opacity:0,duration:.5,delay:1.5})}};
  burst();card._timers.push(setInterval(burst,2300))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx99` rules from `site/fx.css`

_No dedicated `.fx99` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #99
