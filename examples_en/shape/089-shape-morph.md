# 089 · Shape Morph — 形狀變形

Circle, star, heart and cloud morph into each other

- Component: Shapes · SVG (`shape`)
- Timing: Switch
- Tech: GSAP
- Uses: Logo · Brand, Transitions
- Style / keywords: 
- Tag: MorphSVG
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Shape Morph (形狀變形)" motion effect: A block of color smoothly morphs between a circle, a star, a heart and a cloud, changing to a different color with each morph, while the whole thing rotates slowly. (GSAP: MorphSVGPlugin, morphSVG switches the paths, ease expo.inOut)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx89">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Shape Morph".

### JavaScript — `FX[89]` from `site/fx.js`

```js
89(s){s.insertAdjacentHTML('beforeend',`<svg class="mo" viewBox="0 0 100 100"><path d="${SH[0]}" fill="${GC[2]}"/></svg>`);const p=s.querySelector('.mo path');const tl=gsap.timeline({repeat:-1});
  [1,2,3,0].forEach(k=>tl.to(p,{morphSVG:SH[k],fill:[GC[1],GC[4],GC[3],GC[2]][k===0?3:k-1],duration:.9,ease:'expo.inOut'},'+=.6'));gsap.to(s.querySelector('.mo'),{rotation:360,duration:14,repeat:-1,ease:'none'})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx89` rules from `site/fx.css`

_No dedicated `.fx89` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #89
