# 309 · Page Flip Book — 翻頁書

Click a page and it flips in 3D to the left around the spine as its axis; after flipping through them all, they flip back together to the first page

- Component: Cards · Groups (`card`)
- Timing: Switch
- Tech: GSAP
- Uses: UI Interaction, Headline · Hero
- Style / keywords: Page Flip Book Pages Magazine Catalog E-book Page Flip Book Magazine Catalog 3D Cards Group
- Tag: GSAP 3D
- Example text: "Prologue Journey Encounter Epilogue" (stage background: dark)
- Added: 2026-10-20

**AI prompt (English copy format):**

```text
"Page Flip Book (翻頁書)" motion effect: Like a book: on the right is a stack of pages, each page's front has an image and a page number; when clicked, the topmost page flips to the left in 3D space around the spine on its left side as its axis (about 0.9 seconds, ease-in-out), and halfway through the flip you can see the page's 3D angle; after flipping over, it shows that page's back; after flipping through them page by page, all the pages quickly flip back in sequence to the first page. (CSS 3D: each page uses transform-origin:left, transform-style:preserve-3d, front and back faces use backface-visibility:hidden, and the back uses rotateY(180deg); GSAP tweens rotationY 0 → −180, and adjusts the z-index during the flip so flipped pages stack on top)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx309">`, preview text "Prologue Journey Encounter Epilogue". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Page Flip Book".

### JavaScript — `FX[309]` from `site/fx.js`

```js
309(s,x,card){const ws=words(x);const bk=el('div','cg-bk');const P=4;bk.innerHTML='<div class="cg-pg base"></div>';const pgs=[];for(let i=P-1;i>=0;i--){const p=el('div','cg-pg');p.innerHTML='<div class="fr">'+mdImg(i)+'<b></b></div><div class="bk">'+mdImg(i+1)+'</div>';p.querySelector('b').textContent=ws[i%ws.length]+'　'+(i+1)+' / '+P;p.style.zIndex=P-i;bk.append(p);pgs.unshift(p)}s.append(bk);let k=0,real=0,busy=false;
  bk.querySelector('.base').innerHTML=mdImg(P)+'<b>THE END</b>';
  const next=()=>{if(busy)return;busy=true;if(k<P){const p=pgs[k++];gsap.to(p,{rotationY:-180,duration:.9,ease:'power2.inOut',onStart:()=>{p.style.zIndex=10+k},onComplete:()=>busy=false})}else{gsap.to(pgs.slice().reverse(),{rotationY:0,duration:.6,stagger:.1,ease:'power2.inOut',onComplete:()=>{pgs.forEach((p,i)=>p.style.zIndex=P-i);k=0;busy=false}})}};
  bk.onclick=()=>{real=Date.now();next()};card._timers.push(setInterval(()=>{if(Date.now()-real>5000)next()},1700))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx309` rules from `site/fx.css`

_No dedicated `.fx309` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #309
