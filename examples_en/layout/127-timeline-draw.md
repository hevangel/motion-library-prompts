# 127 · Timeline Draw — 時間軸延伸

A line extends downward, and each step appears as the line reaches it

- Component: Layout · Pages (`layout`)
- Timing: Entrance, Scroll-triggered
- Tech: GSAP
- Uses: UI Interaction, Numbers & Data
- Style / keywords: Timeline Process Steps Journey Line Extend Gentle Soft Light Guidance Flow Gaze Reading Order Low-key Subtle Gentle Soft Entrance Visual Flow Hierarchy
- Tag: Timeline
- Example text: "Discovery Concepts Design Launch" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Timeline Draw (時間軸延伸)" motion effect: A vertical timeline: a thin line on the left slowly extends downward from the top (about 2.4 seconds, ease-in-out); whenever the line extends to a node, that node's dot, heading, and description row gently slide in and fade in from about 10px to the left, letting the eye follow the line all the way down through the process. (GSAP: the line scaleY 0→1, with transform-origin at the top; each node does fromTo x:-10 / opacity:0 at its corresponding time point; on a real site, ScrollTrigger scrub can be used so the line's length follows scroll progress)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx127">`, preview text "Discovery Concepts Design Launch". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Timeline Draw".

### JavaScript — `FX[127]` from `site/fx.js`

```js
127(s,x){const w=el('div','vt');w.innerHTML='<i class="rail"></i>';const its=words(x).slice(0,4).map(v=>{const r=el('div','vi2');r.innerHTML='<i class="dot"></i><b></b><span></span>';r.querySelector('b').textContent=v;w.append(r);return r});s.append(w);
  const tl=gsap.timeline({repeat:-1,repeatDelay:.3}).set(w,{opacity:1},0).fromTo(w.querySelector('.rail'),{scaleY:0},{scaleY:1,duration:2.4,ease:'power1.inOut'},0);
  its.forEach((r,i)=>tl.fromTo(r.children,{x:-10,opacity:0},{x:0,opacity:1,duration:.7,ease:'power2.out',stagger:.08},.2+i*.6));tl.to(w,{opacity:0,duration:.5},'+=1.6')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx127` rules from `site/fx.css`

_No dedicated `.fx127` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #127
