# 092 · Scroll Reveal — 捲動揭示

Fades in when scrolled to, with the progress bar in sync

- Component: Layout · Pages (`layout`)
- Timing: Scroll-triggered
- Tech: GSAP
- Uses: Scroll Effects
- Style / keywords: 
- Tag: ScrollTrigger
- Example text: "Scroll Reveal" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Scroll Reveal (捲動揭示)" motion effect: In a scrollable region, the progress bar at the top fills in proportion to scrolling; each paragraph of text fades in from the left when it is scrolled to 85% of the viewport, and fades out again when scrolling back up. (GSAP: ScrollTrigger toggleActions "play none none reverse", the progress bar uses scrub:true)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx92">`, preview text "Scroll Reveal". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Scroll Reveal".

### JavaScript — `FX[92]` from `site/fx.js`

```js
92(s,x){const sc=el('div','scr');const bar=el('div','pbar');const bi=el('i');bar.append(bi);sc.append(bar);s.append(sc);
  [x,'元素依序淡入','進度條跟著捲動','到底了 ✓'].forEach(v=>{const b=el('div','blk');b.textContent=v;sc.append(b);gsap.from(b,{opacity:0,x:-40,duration:.6,ease:'power3.out',scrollTrigger:{trigger:b,scroller:sc,start:'top 85%',toggleActions:'play none none reverse'}})});
  gsap.fromTo(bi,{scaleX:0},{scaleX:1,ease:'none',scrollTrigger:{scroller:sc,start:0,end:'max',scrub:true}});autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx92` rules from `site/fx.css`

_No dedicated `.fx92` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #92
