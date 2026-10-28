# 228 · Twinkling Sky — 閃爍星空

Stars all over the sky twinkle individually, a meteor occasionally streaks past, and the starry sky shifts with slight parallax as the cursor moves

- Component: Background · Ambience (`bg`)
- Timing: Loop · Idle, Hover · Click
- Tech: Canvas
- Uses: Headline · Hero, Background Decoration
- Style / keywords: Starry Sky Stars Twinkle Meteor Night Sky Universe Parallax Twinkling Stars Night Sky Shooting Star Canvas particles requestAnimationFrame Interactive Background Background Atmosphere
- Tag: Canvas 2D
- Example text: "Good Night" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Twinkling Sky (閃爍星空)" motion effect: A night-sky background: darker at the top with a soft glow lower down, filled with more than two hundred stars of different sizes and brightness, each twinkling slowly at its own speed and phase; when the brightest few reach peak brightness, fine cross-shaped sparkles appear; every few seconds a meteor streaks from the upper right diagonally down to the lower left, trailing a fading tail; when the cursor moves, the starry sky makes reverse parallax shifts of different magnitudes depending on the stars' depths. (Canvas 2D: each star records its position, radius, depth, twinkle frequency and phase, with brightness = sin(time x frequency + phase); meteors are line segments drawn with createLinearGradient; parallax displacement is smoothed with lerp)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx228">`, preview text "Good Night". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Twinkling Sky".

### JavaScript — `FX[228]` from `site/fx.js`

```js
228(s,x,card){cfx(s,card,{init:(c,W,H)=>({S:[...Array(220)].map(()=>({x:rnd(0,W),y:rnd(0,H),r:rnd(.3,1.5),z:rnd(.2,1),p:rnd(0,6.3),f:rnd(.6,2.4)})),sh:null,next:1,c:accRGB(s),ox:0,oy:0}),
  frame:(c,W,H,t,dt,m,o)=>{const g=c.createLinearGradient(0,0,0,H);g.addColorStop(0,`rgb(${BGD})`);g.addColorStop(1,`rgba(${o.c},.18)`);c.fillStyle=`rgb(${BGD})`;c.fillRect(0,0,W,H);c.fillStyle=g;c.fillRect(0,0,W,H);
    const tx=m.in?(m.x/W-.5)*-W*.04:0,ty=m.in?(m.y/H-.5)*-H*.04:0;o.ox+=(tx-o.ox)*.06;o.oy+=(ty-o.oy)*.06;
    o.S.forEach(p=>{const a=.35+.65*(.5+.5*Math.sin(t*p.f+p.p));const X=(p.x+o.ox*p.z+W)%W,Y=(p.y+o.oy*p.z+H)%H;c.fillStyle=`rgba(255,255,255,${a*p.z})`;c.beginPath();c.arc(X,Y,p.r*(.7+p.z*.6),0,7);c.fill();
      if(p.r>1.35&&a>.9){c.strokeStyle=`rgba(255,255,255,${(a-.9)*4*p.z})`;c.lineWidth=.6;c.beginPath();c.moveTo(X-p.r*4,Y);c.lineTo(X+p.r*4,Y);c.moveTo(X,Y-p.r*4);c.lineTo(X,Y+p.r*4);c.stroke()}});
    o.next-=dt;if(!o.sh&&o.next<0)o.sh={x:rnd(W*.2,W),y:rnd(0,H*.4),l:0};
    if(o.sh){const q=o.sh;q.l+=dt*1.6;const L=W*.22,px=q.x-q.l*W*.5,py=q.y+q.l*W*.25;const gr=c.createLinearGradient(px,py,px+L,py-L/2);gr.addColorStop(0,`rgba(${o.c},${Math.max(0,1-q.l)})`);gr.addColorStop(1,'rgba(255,255,255,0)');c.strokeStyle=gr;c.lineWidth=1.6;c.beginPath();c.moveTo(px,py);c.lineTo(px+L,py-L/2);c.stroke();if(q.l>1){o.sh=null;o.next=rnd(1.5,3.5)}}}});
  const tx=T(x,Math.min(11,52/chars(x).length));tx.classList.add('cvt');s.append(tx)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx228` rules from `site/fx.css`

_No dedicated `.fx228` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #228
