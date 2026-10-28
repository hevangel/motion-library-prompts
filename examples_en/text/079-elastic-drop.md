# 079 · Elastic Drop — 彈性落下

Letters fall from the sky and wobble elastically

- Component: Text (`text`)
- Timing: Entrance
- Tech: GSAP
- Uses: Headline · Hero, Emphasis
- Style / keywords: Canva Style Canva Bounce Bounce
- Tag: Stagger·Elastic
- Example text: "Bouncing Drop" (stage background: acc)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Elastic Drop (彈性落下)" motion effect: Each character drops from above the frame in random order, with random rotation, wobbling elastically like jelly as it lands before settling into place; after lingering, they all drop down and fade out together. (GSAP: SplitText chars, ease elastic.out(1,0.35), stagger from random)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage acc fx79">`, preview text "Bouncing Drop". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Elastic Drop".

### JavaScript — `FX[79]` from `site/fx.js`

```js
79(s,x){const t=T(x);s.append(t);const sp=SplitText.create(t,{type:'chars'});
  gsap.timeline({repeat:-1,repeatDelay:.3}).from(sp.chars,{yPercent:-420,rotation:'random(-50,50)',duration:1.3,ease:'elastic.out(1,0.35)',stagger:{each:.07,from:'random'}}).to(sp.chars,{yPercent:420,rotation:'random(-40,40)',opacity:0,duration:.6,ease:'power2.in',stagger:.04},'+=1')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx79` rules from `site/fx.css`

_No dedicated `.fx79` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #79
