# 254 · Velocity Stretch Cursor — 速度拉伸游標

A circular cursor stretches along its direction according to movement speed, and returns to a circle when it stops

- Component: Cursor (`cursor`)
- Timing: Hover · Click
- Tech: CSS
- Uses: UI Interaction, Headline · Hero
- Style / keywords: Velocity Stretch Elongation Elastic Direction Velocity Stretch Squash Cursor Elastic Cursor Mouse
- Tag: JS rAF
- Example text: "Stretch" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Velocity Stretch Cursor (速度拉伸游標)" motion effect: A circular cursor follows the mouse with a smooth delay, calculating movement speed every frame: the faster it moves, the more the circle is stretched along the movement direction and flattened vertically, like elastic jelly; when the mouse stops, it slowly recovers into a perfect circle. (JS requestAnimationFrame: position lerps toward the target; speed = the length of this frame's displacement, angle = atan2(dy,dx); transform = translate → rotate(angle) → scale(1 + speed coefficient, 1 − speed coefficient × 0.45), and the speed coefficient itself is also lerped to avoid jitter)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx254">`, preview text "Stretch". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Velocity Stretch Cursor".

### JavaScript — `FX[254]` from `site/fx.js`

```js
254(s,x,card){const l=el('div','abs gl cr-vs');l.append(T(x,Math.min(13,56/chars(x).length)));const c=el('i','cr-vc');l.append(c);s.append(l);let px0=0,py0=0,tx=0,ty=0,cx=0,cy=0,sc=0,ang=0;
  vpointer(l,card,(px,py)=>{tx=px;ty=py});const prev=ticks.get(card);
  ticks.set(card,t=>{prev&&prev(t);const nx=cx+(tx-cx)*.22,ny=cy+(ty-cy)*.22,vx=nx-cx,vy=ny-cy,v=Math.hypot(vx,vy);cx=nx;cy=ny;sc+=(Math.min(v/14,1)-sc)*.25;if(v>.4)ang=Math.atan2(vy,vx)*180/Math.PI;
    c.style.transform=`translate(${cx}px,${cy}px) translate(-50%,-50%) rotate(${ang}deg) scale(${1+sc*1.3},${1-sc*.45})`})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx254` rules from `site/fx.css`

_No dedicated `.fx254` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #254
