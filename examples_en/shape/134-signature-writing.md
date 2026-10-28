# 134 · Signature Writing — 手寫簽名

A pen tip writes along a signature path, finishing with an underline

- Component: Shapes · SVG (`shape`)
- Timing: Entrance
- Tech: GSAP
- Uses: Logo · Brand, Headline · Hero
- Style / keywords: Signature Handwriting Cursive Writing Pen Tip Signature Handwriting Cursive Pen Write On
- Tag: DrawSVG·MotionPath
- Example text: "" (stage background: cream, fixed text)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Signature Writing (手寫簽名)" motion effect: A cursive signature line path is slowly written out starting from where the pen first touches, with a small round pen tip following at the very front of the path, as if someone is really writing (about 2.6 seconds, ease-in-out); once the signature is finished, the pen tip disappears and a slightly curved underline is quickly drawn underneath to finish. Suited to a portfolio hero or brand signature. (GSAP: DrawSVGPlugin draws the signature path while MotionPathPlugin moves the pen-tip dot along the same path, with identical timing and ease for both; the signature must be a single-stroke outline path, not outlined letterforms)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage cream fx134">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Signature Writing".

### JavaScript — `FX[134]` from `site/fx.js`

```js
134(s){const id='sg'+Math.random().toString(36).slice(2);s.insertAdjacentHTML('beforeend',`<svg class="sig" viewBox="0 0 160 90"><path id="${id}" d="M14,58 C22,30 30,18 34,22 C38,27 30,52 26,64 C34,44 44,36 48,42 C52,48 46,62 52,62 C58,62 60,44 66,42 C72,40 70,58 66,60 C62,62 62,48 70,46 C78,44 76,62 82,60 C88,58 90,40 96,40 C102,40 98,60 104,58 C110,56 112,42 118,42 C124,42 120,60 126,58 C132,56 136,36 142,30"/><path class="sw" d="M20,74 C60,66 110,66 146,72"/><circle class="nib" r="2.4"/></svg>`);
  const sv=s.querySelector('.sig'),p=sv.querySelector('#'+id),sw=sv.querySelector('.sw'),nib=sv.querySelector('.nib');
  gsap.timeline({repeat:-1,repeatDelay:.5}).set(sv,{opacity:1},0).fromTo(p,{drawSVG:'0%'},{drawSVG:'100%',duration:2.6,ease:'power1.inOut'},0).fromTo(nib,{opacity:1},{motionPath:{path:p,align:p,alignOrigin:[.5,.5]},duration:2.6,ease:'power1.inOut'},0)
    .fromTo(sw,{drawSVG:'0%'},{drawSVG:'100%',duration:.7,ease:'power2.out'}).to(nib,{opacity:0,duration:.2},'<').to(sv,{opacity:0,duration:.5},'+=1.4')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx134` rules from `site/fx.css`

_No dedicated `.fx134` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #134
