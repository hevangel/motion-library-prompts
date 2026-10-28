# 192 · Logo Build Reveal — Logo 組合登場

The logo's circle, square and dot are drawn and assembled in sequence, then the brand name slides out

- Component: Shapes · SVG (`shape`)
- Timing: Entrance
- Tech: GSAP
- Uses: Logo · Brand, Headline · Hero
- Style / keywords: Logo logo brand opening assemble draw Logo Reveal Brand Intro Build SVG graphic
- Tag: DrawSVG
- Example text: "STUDIO" (stage background: dark)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Logo Build Reveal (Logo 組合登場)" motion effect: A brand logo assembles and enters in sequence: the outer circle is drawn first (about 0.9 seconds), then the square in the middle, rotated 45 degrees, is stroked and filled with an accent color, the center dot pops out from 0 and scales up, and finally the brand name slides in from 12px to the left and fades in; after a pause the whole fades out. Suitable for a website opening or a video intro. (GSAP: DrawSVGPlugin draws the circle and rect in sequence, fill-opacity 0 to 1; the dot's scale uses back.out(3); text fromTo x:-12 / opacity:0)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx192">`, preview text "STUDIO". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Logo Build Reveal".

### JavaScript — `FX[192]` from `site/fx.js`

```js
192(s,x){const w=el('div','lgw');w.innerHTML='<svg viewBox="0 0 60 60" class="lgm"><circle class="o" cx="30" cy="30" r="26"/><rect class="q" x="19" y="19" width="22" height="22" rx="3" transform="rotate(45 30 30)"/><circle class="d" cx="30" cy="30" r="4"/></svg>';const t=T(x,Math.min(8,44/chars(x).length));t.classList.add('lgt');w.append(t);s.append(w);const q=c=>w.querySelector(c);
  gsap.timeline({repeat:-1,repeatDelay:.4}).set(w,{opacity:1},0).fromTo(q('.o'),{drawSVG:'0%'},{drawSVG:'100%',duration:.9,ease:'power2.inOut'},0).fromTo(q('.q'),{drawSVG:'0%',fillOpacity:0},{drawSVG:'100%',duration:.7,ease:'power2.inOut'},.35)
    .fromTo(q('.d'),{scale:0,transformOrigin:'50% 50%'},{scale:1,duration:.5,ease:'back.out(3)'},'-=.1').to(q('.q'),{fillOpacity:1,duration:.4},'<').fromTo(t,{x:-12,opacity:0},{x:0,opacity:1,duration:.6,ease:'power3.out'},'-=.2').to(w,{opacity:0,duration:.5},'+=1.6')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx192` rules from `site/fx.css`

_No dedicated `.fx192` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #192
