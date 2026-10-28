# 277 · Scroll Shape Morph — 捲動形狀變形

A shape morphs in sequence with scrolling into a star, a heart, and a square, rotating as it morphs

- Component: Shapes · SVG (`shape`)
- Timing: Scroll-triggered
- Tech: GSAP
- Uses: Scroll Effects, Emphasis
- Style / keywords: Morph Shape morph Star Heart SVG Scroll Scroll Shape Morph Scroll Trigger ScrollTrigger
- Tag: MorphSVG
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Scroll Shape Morph (捲動形狀變形)" motion effect: In the center of the screen is a solid circular SVG shape, and as the user scrolls down it smoothly morphs in sequence into a five-pointed star, a heart, and a rounded square, rotating 90 degrees with each morph; the morph progress is fully controlled by scrolling, and scrolling back morphs it in reverse. (GSAP MorphSVGPlugin + ScrollTrigger scrub: the timeline in sequence does to(path, {morphSVG: the d of the next shape, rotation: "+=90", transformOrigin: "50% 50%"}))
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx277">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Scroll Shape Morph".

### JavaScript — `FX[277]` from `site/fx.js`

```js
277(s,x){const{sc,wrap,view}=scrollBox(s);view.classList.add('cen');view.innerHTML='<svg class="sx-mo" viewBox="0 0 100 100"><path d="M50 10 A40 40 0 1 1 49.9 10Z"/></svg>';const p=view.querySelector('path');
  const SH=['M50 6 L61 38 L95 38 L67 58 L78 92 L50 71 L22 92 L33 58 L5 38 L39 38Z','M50 88 C20 66 6 50 6 32 C6 18 17 8 30 8 C40 8 46 14 50 22 C54 14 60 8 70 8 C83 8 94 18 94 32 C94 50 80 66 50 88Z','M14 14 H86 V86 H14Z'];
  const tl=gsap.timeline({scrollTrigger:{trigger:wrap,scroller:sc,start:'top top',end:'bottom bottom',scrub:.6}});SH.forEach(d=>tl.to(p,{morphSVG:d,rotation:'+=90',transformOrigin:'50% 50%',ease:'power1.inOut'}));autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx277` rules from `site/fx.css`

_No dedicated `.fx277` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #277
