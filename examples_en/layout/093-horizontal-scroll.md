# 093 · Horizontal Scroll — 橫向捲動

Scroll down, and the content slides left

- Component: Layout · Pages (`layout`)
- Timing: Scroll-triggered
- Tech: GSAP
- Uses: Scroll Effects
- Style / keywords: 
- Tag: ScrollTrigger scrub
- Example text: "Horizontal Scroll Showcase Works" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Horizontal Scroll (橫向捲動)" motion effect: When scrolling down, a whole row of work cards instead slides horizontally to the left, so that scrolling to the very bottom lands exactly on the last card, like a horizontal portfolio showcase. (GSAP: ScrollTrigger pin (or sticky) + scrub, the x travel distance = track width − viewport width)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx93">`, preview text "Horizontal Scroll Showcase Works". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Horizontal Scroll".

### JavaScript — `FX[93]` from `site/fx.js`

```js
93(s,x){const{sc,wrap,view}=scrollBox(s);const tr=el('div','htrack');words(x).forEach((v,i)=>{const p=el('div','hp');p.innerHTML=`<small>0${i+1}</small><b></b>`;p.querySelector('b').textContent=v;p.style.background=GC[i%4];tr.append(p)});view.append(tr);
  gsap.to(tr,{x:()=>-(tr.scrollWidth-view.clientWidth),ease:'none',scrollTrigger:{trigger:wrap,scroller:sc,start:'top top',end:'bottom bottom',scrub:.5,invalidateOnRefresh:true}});autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx93` rules from `site/fx.css`

_No dedicated `.fx93` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #93
