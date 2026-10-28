# 150 · Splash to Home — 啟動頁轉場

The launch logo pops out and breathes, then zooms through the screen into the home page

- Component: Layout · Pages (`layout`)
- Timing: Entrance
- Tech: GSAP
- Uses: App Interface, Transitions, Logo · Brand
- Style / keywords: Splash Screen Opening splash Loading Logo Home Transition Launch Screen Intro Zoom Through App Mobile Mobile Device Micro-interaction Mobile App Micro-interaction
- Tag: Splash
- Example text: "M" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Splash to Home (啟動頁轉場)" motion effect: When the app opens, the logo in the center of the screen pops out from small (back.out) and breathes gently once; then the logo accelerates and zooms until it fills the whole screen and fades out, as if passing through the logo into the app, while the home content underneath (hero card, list) fades in and rises in sequence from top to bottom. The whole sequence is about 2 seconds, ending on the home screen. (GSAP: timeline: logo scale 0.6→1 → yoyo 1.06 → scale 14 (power3.in) + the splash layer opacity 0 → home elements stagger fromTo y:10 / opacity:0)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx150">`, preview text "M". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Splash to Home".

### JavaScript — `FX[150]` from `site/fx.js`

```js
150(s,x){const ph=phone(s);const home=el('div','home');home.innerHTML='<i class="hb"></i>';for(let i=0;i<4;i++)home.append(mrow(i));const sp=el('div','spl');const lg=el('i');lg.textContent=chars(x)[0]||'M';sp.append(lg);ph.append(home,sp);
  gsap.timeline({repeat:-1,repeatDelay:.6}).set(sp,{opacity:1},0).fromTo(lg,{scale:.6,opacity:0},{scale:1,opacity:1,duration:.6,ease:'back.out(1.7)'},.2).to(lg,{scale:1.06,duration:.35,yoyo:true,repeat:1,ease:'sine.inOut'})
    .to(lg,{scale:14,duration:.6,ease:'power3.in'},'+=.2').to(sp,{opacity:0,duration:.3},'-=.25').fromTo(home.children,{y:10,opacity:0},{y:0,opacity:1,duration:.5,stagger:.07,ease:'power2.out'},'-=.15').to({},{duration:1.6})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx150` rules from `site/fx.css`

_No dedicated `.fx150` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #150
