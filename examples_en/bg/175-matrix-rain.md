# 175 · Matrix Rain — 數字雨

Columns of characters fall like rain, with afterimage trails

- Component: Background · Ambience (`bg`)
- Timing: Loop · Idle
- Tech: Canvas
- Uses: Background Decoration
- Style / keywords: matrix rain hacker code characters matrix tech Matrix Code Rain Hacker Digital Canvas particles particles requestAnimationFrame interactive background
- Tag: Canvas text
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Matrix Rain (數字雨)" motion effect: The whole section is filled with columns of characters falling down (katakana, numbers, English), each column at a consistent speed with a different starting point. The frontmost character is brightest, and the characters behind it gradually dim, pulling out a trail; after falling to the bottom, it randomly returns to the top and starts again. Tech, hacker feel. (Canvas 2D: number of columns = width / font size, each column records its current y; about every 55ms cover the whole screen once with a translucent background color, then draw a random character at each column's current position, y moves down one cell, and resets randomly after exceeding the screen)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx175">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Matrix Rain".

### JavaScript — `FX[175]` from `site/fx.js`

```js
175(s,x,card){const CH='アイウエオカキクケコサシスセソタチツテト0123456789ABCDEF';cfx(s,card,{init:(c,W,H)=>{c.fillStyle=`rgb(${BGD})`;c.fillRect(0,0,W,H);const fs=W/38;return{fs,D:[...Array(Math.ceil(W/fs))].map(()=>rnd(-H/fs,0)),acc:0,c:accRGB(s)}},
  frame:(c,W,H,t,dt,m,o)=>{o.acc+=dt;if(o.acc<.055)return;o.acc=0;c.fillStyle=`rgba(${BGD},.12)`;c.fillRect(0,0,W,H);c.font=`700 ${o.fs}px ui-monospace,monospace`;c.textAlign='center';
    o.D.forEach((y,i)=>{const ch=CH[Math.floor(Math.random()*CH.length)],px=i*o.fs+o.fs/2,py=y*o.fs;c.fillStyle=`rgba(${o.c},.85)`;c.fillText(ch,px,py-o.fs);c.fillStyle='#fff';c.fillText(CH[Math.floor(Math.random()*CH.length)],px,py);
      o.D[i]=py>H&&Math.random()>.96?0:y+1})}})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx175` rules from `site/fx.css`

_No dedicated `.fx175` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #175
