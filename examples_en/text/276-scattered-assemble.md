# 276 · Scattered Assemble — 散落文字聚合

Letters scattered around, flipped and scaled, fly back into place with scrolling to form a title

- Component: Text (`text`)
- Timing: Scroll-triggered
- Tech: GSAP
- Uses: Scroll Effects, Headline · Hero, Logo · Brand
- Style / keywords: Scattered Assemble Combine Letters Fly Back Piece Together Scattered Letters Assemble Scroll Scroll Trigger ScrollTrigger
- Tag: ScrollTrigger
- Example text: "ASSEMBLE" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Scattered Assemble (散落文字聚合)" motion effect: Each letter of a title starts randomly scattered around the screen, each with a different rotation angle, scale size, and transparency; when the user scrolls down, the letters in random order fly back in sequence to their original positions, straighten, and recover their size and opacity, assembling into the complete title; scrolling back scatters them again. (GSAP ScrollTrigger scrub: SplitText splits the characters, timeline.from(letters, { x/y/rotation/scale use functions returning random values, opacity: 0, stagger: {each: .02, from: "random"} }))
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx276">`, preview text "ASSEMBLE". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Scattered Assemble".

### JavaScript — `FX[276]` from `site/fx.js`

```js
276(s,x){const{sc,wrap,view}=scrollBox(s);view.classList.add('cen');const t=el('div','sx-as');const ch=chars(x).map(c=>{const sp=el('span');sp.textContent=c===' '?' ':c;t.append(sp);return sp});t.style.fontSize=Math.min(14,64/ch.length)+'cqw';view.append(t);
  gsap.timeline({scrollTrigger:{trigger:wrap,scroller:sc,start:'top top',end:'bottom bottom',scrub:.6}}).from(ch,{x:()=>gsap.utils.random(-160,160),y:()=>gsap.utils.random(-90,90),rotation:()=>gsap.utils.random(-180,180),scale:()=>gsap.utils.random(.3,2),opacity:0,ease:'power2.out',stagger:{each:.02,from:'random'}});autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx276` rules from `site/fx.css`

_No dedicated `.fx276` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #276
