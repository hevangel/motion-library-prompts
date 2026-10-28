# 131 · Soft Mask Reveal — 柔邊遮罩揭示

An image is revealed from left to right by a soft gradient edge

- Component: Images · Media (`media`)
- Timing: Entrance
- Tech: GSAP
- Uses: Headline · Hero, Transitions
- Style / keywords: Image Photo Mask Soft Edge Gradient Reveal Feather Gentle Soft Light Guidance Flow Gaze Reading Order Low-key Subtle Gentle Soft Entrance Visual Flow Hierarchy
- Tag: Soft mask
- Example text: "" (stage background: cream, fixed text)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Soft Mask Reveal (柔邊遮罩揭示)" motion effect: When an image enters, a gradient mask with a feathered edge slowly sweeps from left to right, softly revealing the image (not a hard straight cut), while the image slowly settles back to its original size and position from 1.08x, slightly left of place, over about 1.9–2.3 seconds, easing out smoothly — quieter and more refined than a hard-edged mask. (CSS + GSAP: the outer frame uses mask:linear-gradient(90deg, #000 var(--p), transparent calc(var(--p) + 25%)); use GSAP to tween --p from -25 to 100; the inner image scale 1.08→1, x -8→0)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage cream fx131">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Soft Mask Reveal".

### JavaScript — `FX[131]` from `site/fx.js`

```js
131(s){const f=el('div','smr');f.innerHTML=scene('#ffd9c2','#c9b6ff','#7b6ca8','#3f3566','#fff6e6');s.append(f);
  gsap.timeline({repeat:-1,repeatDelay:.3}).set(f,{opacity:1},0).fromTo(f,{'--p':-25},{'--p':100,duration:1.9,ease:'power2.out'},0).fromTo(f.querySelector('svg'),{scale:1.08,x:-8},{scale:1,x:0,duration:2.3,ease:'power2.out'},0).to(f,{opacity:0,duration:.6},'+=1.6')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx131` rules from `site/fx.css`

_No dedicated `.fx131` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #131
