# 125 · Gentle Fade Up — 柔和上浮

Elements in a section gently appear from top to bottom in reading order

- Component: Layout · Pages (`layout`)
- Timing: Entrance
- Tech: GSAP
- Uses: Headline · Hero
- Style / keywords: Section Paragraph Heading Rise Fade In Gentle Soft Light Guidance Flow Gaze Reading Order Low-key Subtle Gentle Soft Entrance Visual Flow Hierarchy Canva Style Canva Rise Rise
- Tag: Fade up
- Example text: "Let design tell the story" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Gentle Fade Up (柔和上浮)" motion effect: When a content section (kicker, main heading, two lines of body copy, and a button) enters, each element gently rises from about 18px below and fully transparent and fades in, following top-to-bottom reading order, with about 0.14 seconds between elements, about 0.9 seconds each, easing out smoothly (power2.out), with no bounce and no scaling, so the eye is naturally led from the heading to the button. (GSAP: fromTo y:18 / opacity:0 → y:0 / opacity:1, stagger 0.14; on a real site, pair it with ScrollTrigger to play once when the section enters the viewport)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx125">`, preview text "Let design tell the story". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Gentle Fade Up".

### JavaScript — `FX[125]` from `site/fx.js`

```js
125(s,x){const w=el('div','gs');w.innerHTML='<small>NEW · 2026</small><b></b><i class="ln"></i><i class="ln s"></i><span class="bt">了解更多</span>';w.querySelector('b').textContent=x;s.append(w);const it=w.children;
  gsap.timeline({repeat:-1,repeatDelay:.3}).fromTo(it,{y:18,opacity:0},{y:0,opacity:1,duration:.9,ease:'power2.out',stagger:.14}).to(it,{opacity:0,duration:.5,ease:'power1.in'},'+=1.8')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx125` rules from `site/fx.css`

_No dedicated `.fx125` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #125
