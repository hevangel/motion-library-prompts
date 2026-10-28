# 267 · Lightbox Zoom — 點圖放大燈箱

Click a thumbnail and it smoothly enlarges from its original position to the center of the screen, with the background darkening; click again and it shrinks back

- Component: Images · Media (`media`)
- Timing: Switch
- Tech: GSAP
- Uses: UI Interaction, Transitions
- Style / keywords: Lightbox lightbox Zoom Image View Album Modal Zoom Gallery Photo Viewer Flip Image Media
- Tag: Flip
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Lightbox Zoom (點圖放大燈箱)" motion effect: A row of square thumbnails; when clicking any one, that image smoothly enlarges from its original position and size to a large size in the center of the screen (about 0.55 seconds, easing in and out), while a translucent overlay is laid behind it darkening the other content; clicking the large image or the overlay makes the image smoothly shrink back to its original position in the thumbnail row and the overlay fade out. (GSAP Flip: Flip.getState records the thumbnail → add the “enlarged” class (changed to absolute positioning centered, larger size) → Flip.from tweens it; reverse when collapsing; the overlay uses an opacity transition)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx267">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Lightbox Zoom".

### JavaScript — `FX[267]` from `site/fx.js`

```js
267(s,x,card){const w=el('div','md-lb');const ths=[0,1,2,3].map(i=>{const t=el('button','md-th');t.setAttribute('aria-label','放大圖片 '+(i+1));t.innerHTML=mdImg(i);w.append(t);return t});const bd=el('div','md-bd');w.append(bd);s.append(w);let open=null,real=0;
  const close=()=>{if(!open)return;const t=open;open=null;const st=Flip.getState(t);t.classList.remove('big');Flip.from(st,{duration:.5,ease:'power3.inOut',zIndex:5});bd.classList.remove('on')};
  const show=t=>{if(open)return close();open=t;const st=Flip.getState(t);t.classList.add('big');Flip.from(st,{duration:.55,ease:'power3.inOut',zIndex:5});bd.classList.add('on')};
  ths.forEach(t=>t.onclick=()=>{real=Date.now();open===t?close():show(t)});bd.onclick=()=>{real=Date.now();close()};let k=0;
  card._timers.push(setInterval(()=>{if(Date.now()-real<5000)return;open?close():show(ths[k++%4])},1700))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx267` rules from `site/fx.css`

_No dedicated `.fx267` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #267
