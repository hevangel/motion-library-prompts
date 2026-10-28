# 327 · Badge Unlock — 成就徽章解鎖

A hexagonal badge's outline is drawn, a star shrinks from large and stamps onto it, and rays radiate all around

- Component: Shapes · SVG (`shape`)
- Timing: Entrance
- Tech: GSAP
- Uses: Emphasis, App Interface
- Style / keywords: Badge Achievement Unlock Reward Gamification Badge Achievement Unlock Reward Gamification Graphics SVG
- Tag: DrawSVG
- Example text: "7-day login streak" (stage background: dark)
- Added: 2026-10-21

**AI prompt (English copy format):**

```text
"Badge Unlock (成就徽章解鎖)" motion effect: A badge animation for when an achievement is earned: the outline of the hexagonal badge is first drawn in one stroke along its edges, then its interior fades in to fill it; a star quickly shrinks from a very large, rotating, transparent state down to the center of the badge with a bounce-back, like stamping it on; at the same time, a ring of short rays around the badge shoots rapidly outward from the inside and disappears, and the badge as a whole bounces lightly once; the achievement name and the words "Achievement unlocked" below emerge in sequence. (GSAP timeline: DrawSVG draws the outline → fillOpacity → the star fromTo scale 3 → 1, rotation −60 → 0, back.out → the rays DrawSVG "0% 0%" → "0% 100%" → "100% 100%")
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx327">`, preview text "7-day login streak". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Badge Unlock".

### JavaScript — `FX[327]` from `site/fx.js`

```js
327(s,x){const w=el('div','sv-bdg');w.innerHTML='<svg viewBox="-60 -60 120 120"><g class="sv-rays">'+[...Array(12)].map((_,i)=>`<line y1="-40" y2="-52" transform="rotate(${i*30})"/>`).join('')+'</g><path class="sv-hex" d="M0,-36 L31,-18 L31,18 L0,36 L-31,18 L-31,-18Z"/><path class="sv-star" d="M0,-16 L4.7,-6.5 L15.2,-4.9 L7.6,2.5 L9.4,12.9 L0,8 L-9.4,12.9 L-7.6,2.5 L-15.2,-4.9 L-4.7,-6.5Z"/></svg><b></b><small>成就解鎖</small>';w.querySelector('b').textContent=x;s.append(w);
  const hex=w.querySelector('.sv-hex'),st=w.querySelector('.sv-star'),rays=w.querySelectorAll('.sv-rays line');
  gsap.timeline({repeat:-1,repeatDelay:1.4}).set(hex,{fillOpacity:0}).fromTo(hex,{drawSVG:'0%'},{drawSVG:'100%',duration:.8,ease:'power2.inOut'}).to(hex,{fillOpacity:1,duration:.3}).fromTo(st,{scale:3,opacity:0,rotation:-60,transformOrigin:'50% 50%'},{scale:1,opacity:1,rotation:0,duration:.45,ease:'back.out(2.2)'},'-=.1').fromTo(rays,{drawSVG:'0% 0%'},{keyframes:[{drawSVG:'0% 100%',duration:.25},{drawSVG:'100% 100%',duration:.3}],stagger:.015,ease:'power2.out'},'-=.15').from(w.querySelectorAll('b,small'),{y:10,opacity:0,duration:.4,stagger:.08},'<').to(w.querySelector('svg'),{scale:1.06,duration:.15,yoyo:true,repeat:1,transformOrigin:'50% 50%'},'<').to(w,{opacity:0,duration:.4},'+=2.2').set(w,{opacity:1})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx327` rules from `site/fx.css`

_No dedicated `.fx327` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #327
