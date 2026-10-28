# 268 · Thumbnail Gallery — 縮圖列相簿

Click a thumbnail below and the large image pushes in from the side to change, shrinking back slightly, while the indicator bar slides to the current thumbnail

- Component: Images · Media (`media`)
- Timing: Switch, Loop · Idle
- Tech: GSAP
- Uses: UI Interaction
- Style / keywords: Album Thumbnails Large Image Product Images Carousel Gallery Thumbnails Slider Product Images Carousel Image Media
- Tag: GSAP
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Thumbnail Gallery (縮圖列相簿)" motion effect: Product album: one large image above and a row of thumbnails below; when clicking a thumbnail, the new large image pushes in from the corresponding direction (from the right when clicking forward, from the left when clicking backward), the old image moves out slightly in the opposite direction, and inside the new image it simultaneously shrinks slowly back from 1.25 times to the original size, adding a sense of depth; in the thumbnail row the current one becomes fully opaque and the others translucent, and an indicator bar below slides and aligns to the current thumbnail; it can also auto-play as a carousel. (GSAP: the new image fromTo xPercent ±100 → 0, the old image to xPercent ∓30, power3.inOut 0.6 seconds; the indicator bar transitions with CSS transform and width)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx268">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Thumbnail Gallery".

### JavaScript — `FX[268]` from `site/fx.js`

```js
268(s,x,card){const w=el('div','md-gl');w.innerHTML='<div class="md-gm"></div><div class="md-gs"><i class="md-gi"></i></div>';const gm=w.querySelector('.md-gm'),gs=w.querySelector('.md-gs'),gi=w.querySelector('.md-gi');
  const big=[0,1,2,3].map(i=>{const d=el('div','md-gb');d.innerHTML=mdImg(i);gm.append(d);return d});const th=[0,1,2,3].map(i=>{const b=el('button','md-gt');b.setAttribute('aria-label','第 '+(i+1)+' 張');b.innerHTML=mdImg(i);b.onclick=()=>{real=Date.now();go(i)};gs.append(b);return b});s.append(w);let cur=-1,real=0;
  const go=i=>{if(i===cur)return;const dir=i>cur?1:-1;big.forEach((d,j)=>{d.style.zIndex=j===i?2:j===cur?1:0});if(cur>=0)gsap.to(big[cur],{xPercent:-30*dir,duration:.6,ease:'power3.inOut'});gsap.fromTo(big[i],{xPercent:100*dir,scale:1},{xPercent:0,duration:.6,ease:'power3.inOut'});gsap.fromTo(big[i].firstChild,{scale:1.25},{scale:1,duration:.9,ease:'power2.out'});
    cur=i;th.forEach((b,j)=>b.classList.toggle('on',j===i));gi.style.transform=`translateX(${th[i].offsetLeft}px)`;gi.style.width=th[i].offsetWidth+'px'};requestAnimationFrame(()=>{go(0)});
  card._timers.push(setInterval(()=>{if(Date.now()-real>5000)go((cur+1)%4)},2000))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx268` rules from `site/fx.css`

_No dedicated `.fx268` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #268
