# 311 · Folding Card — 對折邀請卡

Like a physical card, the cover opens in 3D around its left edge as its axis, revealing the image and text inside

- Component: Cards · Groups (`card`)
- Timing: Switch
- Tech: GSAP
- Uses: UI Interaction, Headline · Hero
- Style / keywords: Card Folded Invitation Card Greeting Card Open 3D Folding Greeting Invitation Card Open Cards Group
- Tag: GSAP 3D
- Example text: "YOU ARE INVITED" (stage background: dark)
- Added: 2026-10-20

**AI prompt (English copy format):**

```text
"Folding Card (對折邀請卡)" motion effect: A folded invitation card: at first you only see the cover (accent-colored background, a large heading and "Click to open"); when clicked, the cover flips open 180 degrees to the left in 3D space around its left side as its axis (about 0.9 seconds); the back of the cover is an image, and the right side reveals the invitation text and date on the card's inner page; at the same time the whole card shifts to the right so the opened whole stays centered; click again to close it. (CSS 3D: perspective on the container; the cover uses transform-origin:left, preserve-3d, front and back faces use backface-visibility:hidden, and the back uses rotateY(180deg); a GSAP timeline simultaneously tweens the cover's rotationY 0 → −180 and the card's xPercent 0 → 50, toggling play / reverse)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx311">`, preview text "YOU ARE INVITED". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Folding Card".

### JavaScript — `FX[311]` from `site/fx.js`

```js
311(s,x,card){const w=el('div','cg-fo');w.innerHTML='<div class="cg-ins"><p>邀請你參加<br>我們的週年派對 🎉</p><small>11 / 08 · 19:00</small></div><div class="cg-cv"><div class="fr"><b></b><small>點一下打開</small></div><div class="bk">'+mdImg(1)+'</div></div>';w.querySelector('.fr b').textContent=x;s.append(w);
  const cv=w.querySelector('.cg-cv');let open=false,real=0;const tl=gsap.timeline({paused:true}).to(cv,{rotationY:-180,duration:.9,ease:'power2.inOut'}).to(w,{xPercent:50,duration:.9,ease:'power2.inOut'},0);
  const tog=()=>{open=!open;open?tl.play():tl.reverse()};w.onclick=()=>{real=Date.now();tog()};card._timers.push(setInterval(()=>{if(Date.now()-real>5000)tog()},2600))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx311` rules from `site/fx.css`

_No dedicated `.fx311` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #311
