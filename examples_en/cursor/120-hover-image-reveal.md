# 120 · Hover Image Reveal — 清單懸停預覽圖

When skimming a work list, a preview image floats out following the cursor and tilts as it moves

- Component: Cursor (`cursor`)
- Timing: Hover · Click
- Tech: CSS
- Uses: UI Interaction, Headline · Hero
- Style / keywords: Cursor List List Preview Image Emerge Follow Hover Image Reveal List Preview Follow Cursor Portfolio
- Tag: Hover preview
- Example text: "Brand Identity Website Design Packaging Illustration" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Hover Image Reveal (清單懸停預覽圖)" motion effect: A large-text work list (each row has the work's name on the left and its number on the right, with thin divider lines between rows), with unselected rows in fainter text; when the cursor slides onto a row, that row's text becomes clear and pushes slightly to the right, while a preview image of that work scales up from small and floats beside the cursor, following its movement — the faster it moves left or right, the more the image tilts in the direction of movement; when moving to another row, the preview image changes to another one, and when leaving the list, the image shrinks and fades out. (How it works: the preview image uses position:absolute + pointer-events:none, on mousemove it is translated to the cursor position, its rotate is calculated from the horizontal velocity with an upper limit; image switching uses opacity / scale transitions)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx120">`, preview text "Brand Identity Website Design Packaging Illustration". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Hover Image Reveal".

### JavaScript — `FX[120]` from `site/fx.js`

```js
120(s,x,card){const l=el('div','abs hl');const rows=words(x).slice(0,4).map((w,i)=>{const r=el('div','hr');r.innerHTML=`<b></b><span>0${i+1}</span>`;r.querySelector('b').textContent=w;l.append(r);return r});const im=el('div','himg');l.append(im);s.append(l);let lx=0;
  vpointer(l,card,(px,py)=>{const i=rows.findIndex(r=>py>=r.offsetTop&&py<r.offsetTop+r.offsetHeight);rows.forEach((r,k)=>r.classList.toggle('on',k===i));im.classList.toggle('on',i>=0);if(i>=0)im.style.background=`linear-gradient(135deg,${GC[i%5]},${GC[(i+2)%5]})`;
    const vx=px-lx;lx=px;im.style.transform=`translate(${px}px,${py}px) rotate(${Math.max(-12,Math.min(12,vx*.8))}deg)`})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx120` rules from `site/fx.css`

_No dedicated `.fx120` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #120
