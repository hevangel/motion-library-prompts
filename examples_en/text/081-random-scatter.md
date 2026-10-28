# 081 · Random Scatter — 隨機散聚

Letters fly in from everywhere, then scatter apart

- Component: Text (`text`)
- Timing: Entrance, Exit
- Tech: GSAP
- Uses: Headline · Hero
- Style / keywords: 
- Tag: Stagger random
- Example text: "Scatter and Gather" (stage background: cream)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Random Scatter (隨機散聚)" motion effect: Each character flies in from random positions all over the frame, with random rotation and size, decelerating strongly to assemble into the text; after lingering, it bursts apart to random positions. (GSAP: SplitText chars, "random(-400,400)" function-based values, ease expo, stagger from random)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage cream fx81">`, preview text "Scatter and Gather". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Random Scatter".

### JavaScript — `FX[81]` from `site/fx.js`

```js
81(s,x){const t=T(x);s.append(t);const sp=SplitText.create(t,{type:'chars'});const v={xPercent:'random(-400,400)',yPercent:'random(-300,300)',rotation:'random(-200,200)',scale:'random(0,2)',opacity:0};
  gsap.timeline({repeat:-1,repeatDelay:.2}).from(sp.chars,{...v,duration:1.3,ease:'expo.out',stagger:{each:.05,from:'random'}}).to(sp.chars,{...v,duration:.9,ease:'expo.in',stagger:{each:.03,from:'random'}},'+=1.1')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx81` rules from `site/fx.css`

_No dedicated `.fx81` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #81
