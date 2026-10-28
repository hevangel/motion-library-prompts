# 132 · Zigzag Cascade — 左右交錯淡入

Figure-and-text rows appear alternating left and right, the gaze moving down in a Z pattern

- Component: Cards · Groups (`card`)
- Timing: Entrance, Scroll-triggered
- Tech: GSAP
- Uses: UI Interaction
- Style / keywords: Image and Text List Left and Right Alternating Z Shape Downward Intro Features Gentle Soft Light Guidance Flow Gaze Reading Order Low-key Subtle Gentle Soft Entrance Visual Flow Hierarchy
- Tag: Zigzag
- Example text: "About Work Services Contact" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Zigzag Cascade (左右交錯淡入)" motion effect: Figure-and-text rows stacked vertically, alternating left and right (first row image left / text right, second row image right / text left, and so on). On entry they appear top to bottom in sequence, each row gently sliding in about 20px inward from its own side and fading in, spaced about 0.35 seconds apart, about 0.9 seconds per row, easing out smoothly, so the gaze reads downward in a Z pattern. (GSAP: fromTo x alternating ±20 by index / opacity:0, stagger 0.35, ease power2.out; on a real site, ScrollTrigger.batch can be used so each row appears only when scrolled to)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx132">`, preview text "About Work Services Contact". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Zigzag Cascade".

### JavaScript — `FX[132]` from `site/fx.js`

```js
132(s,x){const w=el('div','zz');const ws=words(x);for(let i=0;i<4;i++){const r=el('div','zr'+(i%2?' rt':''));r.innerHTML='<i></i><span><b></b><em></em></span>';r.querySelector('i').style.background=`linear-gradient(135deg,${GC[i]},${GC[i+1]})`;r.querySelector('b').textContent=ws[i%ws.length];w.append(r)}s.append(w);const rs=[...w.children];
  gsap.timeline({repeat:-1,repeatDelay:.3}).fromTo(rs,{x:i=>i%2?20:-20,opacity:0},{x:0,opacity:1,duration:.9,ease:'power2.out',stagger:.35}).to(rs,{opacity:0,duration:.5},'+=1.6')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx132` rules from `site/fx.css`

_No dedicated `.fx132` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #132
