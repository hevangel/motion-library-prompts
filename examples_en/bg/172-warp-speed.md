# 172 · Warp Speed — 星空穿越

Stars fly outward from the center into streaks of light; hovering speeds them up

- Component: Background · Ambience (`bg`)
- Timing: Loop · Idle, Hover · Click
- Tech: Canvas
- Uses: Headline · Hero, Background Decoration
- Style / keywords: starfield stars warp space light speed tunnel Starfield Warp Hyperspace Space Canvas particles particles requestAnimationFrame interactive background
- Tag: Canvas 3D
- Example text: "Warp Ahead" (stage background: dark)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Warp Speed (星空穿越)" motion effect: The Hero background is a field of stars flying toward the camera: each star starts near the center of the screen, gets brighter and larger as it approaches the viewer, and pulls out short radial streaks of light, like a spaceship accelerating through space; when the cursor moves into the section, the speed smoothly increases, and the vanishing point shifts slightly toward the cursor direction, returning slowly to cruising speed after it leaves. The foreground title stays clear. (Canvas 2D: each star has x, y, z, z decreases each frame, projected coordinates = center + x/z × focal length, draw a line from the previous frame's projected position to this frame's; cover the screen with a translucent background color to create afterimages)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx172">`, preview text "Warp Ahead". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Warp Speed".

### JavaScript — `FX[172]` from `site/fx.js`

```js
172(s,x,card){cfx(s,card,{init:()=>({S:[...Array(320)].map(()=>({x:rnd(-1,1),y:rnd(-1,1),z:rnd(.05,1),pz:0})),v:.25,c:accRGB(s)}),
  frame:(c,W,H,t,dt,m,o)=>{o.v+=((m.in?1.4:.25)-o.v)*.05;c.fillStyle=`rgba(${BGD},.55)`;c.fillRect(0,0,W,H);const cx=W/2+(m.in?(m.x-W/2)*.25:0),cy=H/2+(m.in?(m.y-H/2)*.25:0),F=W*.45;
    o.S.forEach((p,i)=>{p.pz=p.z;p.z-=o.v*dt;if(p.z<=.02){p.x=rnd(-1,1);p.y=rnd(-1,1);p.z=1;p.pz=1}const sx=cx+p.x/p.z*F,sy=cy+p.y/p.z*F,px=cx+p.x/p.pz*F,py=cy+p.y/p.pz*F;
      c.strokeStyle=i%5?`rgba(255,255,255,${1-p.z})`:`rgba(${o.c},${1-p.z})`;c.lineWidth=(1-p.z)*2.2;c.beginPath();c.moveTo(px,py);c.lineTo(sx,sy);c.stroke()})}});
  const tx=T(x,Math.min(11,56/chars(x).length));tx.classList.add('cvt');s.append(tx)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx172` rules from `site/fx.css`

_No dedicated `.fx172` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #172
