# 159 · Scroll Marquee Text — 捲動橫移大字

Three lines of large text move left and right in opposite directions with scrolling, the middle one hollow

- Component: Text (`text`)
- Timing: Scroll-triggered
- Tech: GSAP
- Uses: Background Decoration, Scroll Effects, Headline · Hero
- Style / keywords: Big Type Horizontal Shift Marquee Reverse Heading Scroll Marquee Big Type Horizontal Text Kinetic Scroll Scroll scroll ScrollTrigger scrub Scroll-triggered
- Tag: ScrollTrigger scrub
- Example text: "MOTION LIBRARY" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Scroll Marquee Text (捲動橫移大字)" motion effect: There are three lines of extra-large repeated text on screen (the middle line is hollow outline), and when scrolling, the first and third lines move left while the second line moves right, with the distance moved entirely following scroll progress (stopping when scrolling stops), creating a tense layout rhythm. (GSAP: a timeline bound to ScrollTrigger scrub:0.6, each line fromTo xPercent 0↔-40; the section is pinned or sticky)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx159">`, preview text "MOTION LIBRARY". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Scroll Marquee Text".

### JavaScript — `FX[159]` from `site/fx.js`

```js
159(s,x){const{sc,wrap,view}=scrollBox(s);view.classList.add('smq');const U=rep(x+' ',5);const rows=[0,1,2].map(i=>{const r=el('div','smr2'+(i===1?' o':''));r.textContent=U;view.append(r);return r});
  const tl=gsap.timeline({scrollTrigger:{trigger:wrap,scroller:sc,start:'top top',end:'bottom bottom',scrub:.6}});rows.forEach((r,i)=>tl.fromTo(r,{xPercent:i%2?-40:0},{xPercent:i%2?0:-40,ease:'none'},0));autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx159` rules from `site/fx.css`

_No dedicated `.fx159` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #159
