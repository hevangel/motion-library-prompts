# 105 · Tilt Parallax Image — 3D 傾斜視差圖片

On hover the image tilts in 3D following the cursor, with layered parallax scenery, a glare, and a caption sliding out

- Component: Images · Media (`media`)
- Timing: Hover · Click
- Tech: GSAP
- Uses: UI Interaction, Emphasis
- Style / keywords: Image Photo hover Hover 3D Tilt Parallax Glare Tilt Parallax Glare Image Hover Card
- Tag: quickTo·3D
- Example text: "Mountain Mist Sunset" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Tilt Parallax Image (3D 傾斜視差圖片)" motion effect: An image card: when the mouse moves over the image, the whole image tilts in 3D in the direction of the cursor position (up to about ±10 degrees) and scales up slightly; the far, middle and near scenery inside the image shift in the opposite direction at different rates, forming parallax depth; a soft glare follows the cursor; at the same time, the caption text at the bottom (a small label + a title) slides up from below. When the mouse leaves, everything smoothly returns upright and the caption retracts. (GSAP: gsap.quickTo controls rotationX / rotationY / scale, the parent layer has perspective set; each layer is displaced with quickTo at a different coefficient; the glare uses a radial-gradient positioned with the CSS variables --gx and --gy; the caption uses a transform transition)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx105">`, preview text "Mountain Mist Sunset". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Tilt Parallax Image".

### JavaScript — `FX[105]` from `site/fx.js`

```js
105(s,x){const l=layer(s);l.style.perspective='700px';const id='tg'+Math.random().toString(36).slice(2);const f=el('div','tilt');
  f.innerHTML=`<svg viewBox="0 0 160 120" preserveAspectRatio="xMidYMid slice"><defs><linearGradient id="${id}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffb36b"/><stop offset="1" stop-color="#ff6b8b"/></linearGradient></defs><rect x="-20" y="-20" width="200" height="160" fill="url(#${id})"/><g class="l1"><circle cx="108" cy="42" r="15" fill="#fff3d6"/></g><g class="l2"><path d="M-30,92 L28,48 L60,72 L96,36 L140,80 L190,56 L190,140 L-30,140Z" fill="#8a3f6e"/></g><g class="l3"><path d="M-30,110 L18,82 L54,102 L92,78 L132,104 L190,84 L190,140 L-30,140Z" fill="#3b1f45"/></g></svg><div class="glare"></div><div class="cap"><small>PHOTO</small><b></b></div>`;
  f.querySelector('.cap b').textContent=x;l.append(f);
  const q=(e,k,d=.5)=>gsap.quickTo(e,k,{duration:d,ease:'power3.out'});const rx=q(f,'rotationX'),ry=q(f,'rotationY'),sc=q(f,'scale');
  const ls=[...f.querySelectorAll('.l1,.l2,.l3')].map((g,i)=>[q(g,'x',.6),q(g,'y',.6),[4,8,13][i]]);
  pointer(l,(px,py)=>{const nx=(px-f.offsetLeft)/f.offsetWidth,ny=(py-f.offsetTop)/f.offsetHeight,inside=nx>=0&&nx<=1&&ny>=0&&ny<=1;f.classList.toggle('on',inside);
    const dx=inside?nx-.5:0,dy=inside?ny-.5:0;rx(-dy*18);ry(dx*22);sc(inside?1.05:1);ls.forEach(([a,b,k])=>{a(-dx*k);b(-dy*k*.6)});f.style.setProperty('--gx',nx*100+'%');f.style.setProperty('--gy',ny*100+'%')},
    [[.5,.5],[.36,.34],[.64,.38],[.6,.66],[.38,.64],[.08,.2],[.92,.85]])}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx105` rules from `site/fx.css`

_No dedicated `.fx105` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #105
