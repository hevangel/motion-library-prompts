# 261 · Click Confetti Pop — 點擊噴出小物

Click anywhere on the screen and small patterns such as hearts and stars spray out from there and fall down

- Component: Cursor (`cursor`)
- Timing: Hover · Click
- Tech: GSAP
- Uses: Emphasis, UI Interaction
- Style / keywords: Click Spray Hearts Stars Confetti Feedback Cute Click Burst Hearts Confetti Pop Particles Cursor Mouse
- Tag: GSAP keyframes
- Example text: "Click!" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Click Confetti Pop (點擊噴出小物)" motion effect: When clicking anywhere inside the area, about 7 small patterns (hearts, stars, small flowers) spray out from the click position, each flying out into a fan-shaped range above with random size and angle, and after reaching the highest point they fall while fading out; at the same time there is a thin ring at the click point that expands and disappears. Suitable for cute-style websites or like feedback. (GSAP: each small pattern uses fromTo starting at scale 0 at the click point, the first keyframe segment flies out to a random angle and distance with power3.out, the second segment goes down and opacity 0; the element is removed when the animation ends)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx261">`, preview text "Click!". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Click Confetti Pop".

### JavaScript — `FX[261]` from `site/fx.js`

```js
261(s,x,card){const l=el('div','abs gl cr-ck');const t=T(x,Math.min(12,52/chars(x).length));l.append(t,el('div','cr-hint','點一下試試'));s.append(l);const E=['❤','✦','★','✿','♥'];let real=0;
  const pop=(px,py)=>{for(let i=0;i<7;i++){const p=el('span','cr-pp');p.textContent=E[i%E.length];p.style.color=i%2?'var(--a)':GC[i%5];l.append(p);const a=rnd(-Math.PI*.95,-Math.PI*.05),d=rnd(30,70);
    gsap.fromTo(p,{x:px,y:py,xPercent:-50,yPercent:-50,scale:0,rotation:rnd(-40,40)},{keyframes:[{x:px+Math.cos(a)*d,y:py+Math.sin(a)*d,scale:rnd(.8,1.3),duration:.45,ease:'power3.out'},{y:`+=${rnd(20,40)}`,opacity:0,duration:.6,ease:'power1.in'}],onComplete:()=>p.remove()})}
    const r=el('i','cr-cr');r.style.transform=`translate(${px}px,${py}px)`;l.append(r);r.addEventListener('animationend',()=>r.remove())};
  l.addEventListener('pointerdown',e=>{real=Date.now();const q=l.getBoundingClientRect();pop(e.clientX-q.left,e.clientY-q.top)});
  card._timers.push(setInterval(()=>{if(Date.now()-real<5000)return;pop(rnd(.2,.8)*l.offsetWidth,rnd(.3,.75)*l.offsetHeight)},1300))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx261` rules from `site/fx.css`

_No dedicated `.fx261` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #261
