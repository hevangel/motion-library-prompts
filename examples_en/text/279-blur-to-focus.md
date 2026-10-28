# 279 · Blur to Focus — 模糊對焦

Section headings go from blurred to clear as they scroll into view, and blur again as they scroll out

- Component: Text (`text`)
- Timing: Scroll-triggered
- Tech: GSAP
- Uses: Scroll Effects, Headline · Hero
- Style / keywords: Blur Focus Clear blur Depth of Field Scroll Blur To Focus Scroll Depth Scroll Trigger ScrollTrigger
- Tag: ScrollTrigger
- Example text: "Slowly See Clearly Then Leave" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Blur to Focus (模糊對焦)" motion effect: Several large headings in a long page: each heading is blurred, transparent, and slightly smaller when it scrolls in from below the screen, becomes clearer the closer it gets to the center of the screen, and is completely clear at the center; continuing to scroll up out of the screen it gradually blurs, fades out, and enlarges slightly, like a camera focusing as it sweeps past, guiding the gaze to stay on the current section. (GSAP ScrollTrigger scrub: each heading start "top bottom", end "bottom top", the timeline first fromTo filter blur(12px) → blur(0), opacity 0 → 1, scale .92 → 1, then to blur(12px), opacity 0, scale 1.06)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx279">`, preview text "Slowly See Clearly Then Leave". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Blur to Focus".

### JavaScript — `FX[279]` from `site/fx.js`

```js
279(s,x){const sc=el('div','scr');const box=el('div','sx-bf');box.innerHTML='<div class="sx-sp"></div>';words(x).slice(0,3).forEach(t=>{const h=T(t,Math.min(12,52/chars(t).length));h.classList.add('sx-bl');box.append(h)});box.insertAdjacentHTML('beforeend','<div class="sx-sp"></div>');sc.append(box);s.append(sc);
  box.querySelectorAll('.sx-bl').forEach(h=>gsap.timeline({scrollTrigger:{trigger:h,scroller:sc,start:'top bottom',end:'bottom top',scrub:true}}).fromTo(h,{filter:'blur(12px)',opacity:0,scale:.92},{filter:'blur(0px)',opacity:1,scale:1,ease:'power1.out'}).to(h,{filter:'blur(12px)',opacity:0,scale:1.06,ease:'power1.in'}));autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx279` rules from `site/fx.css`

_No dedicated `.fx279` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #279
