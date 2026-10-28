# 153 · Scroll Zoom to Full — 捲動放大全幅圖片

A small image zooms with scrolling until it fills the screen, then a heading appears

- Component: Images · Media (`media`)
- Timing: Scroll-triggered
- Tech: GSAP
- Uses: Headline · Hero, Scroll Effects, Transitions
- Style / keywords: Image Zoom Full-bleed Full Screen Expand Zoom Image Expand Full Screen Fullbleed Scroll Scroll scroll ScrollTrigger scrub Scroll-triggered
- Tag: ScrollTrigger scrub
- Example text: "Into the Scenery" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Scroll Zoom to Full (捲動放大全幅圖片)" motion effect: A small image with rounded corners at the center of the screen (about 40% wide) gradually enlarges as you scroll down until it fills the whole screen; its corners simultaneously shrink to square corners, and the image content slowly scales back from 1.3x to its original size (so it does not look blurry when enlarged); late in the enlargement, a heading fades in from below, overlaid on the image; scrolling back reverses everything. (GSAP: a timeline bound to ScrollTrigger scrub:true, with the section pinned or sticky; tween width / height / borderRadius and the inner layer's scale; clip-path inset can also be used)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx153">`, preview text "Into the Scenery". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Scroll Zoom to Full".

### JavaScript — `FX[153]` from `site/fx.js`

```js
153(s,x){const{sc,wrap,view}=scrollBox(s);view.classList.add('cen');const f=el('div','zim');f.innerHTML=scene('#9fd3ff','#ffe1b0','#4f7a6a','#264a3f','#fff6d8');const cap=T(x,Math.min(10,50/chars(x).length));cap.classList.add('zcap');f.append(cap);view.append(f);
  gsap.timeline({scrollTrigger:{trigger:wrap,scroller:sc,start:'top top',end:'bottom bottom',scrub:true}}).fromTo(f,{width:'38%',height:'46%',borderRadius:'2cqw'},{width:'100%',height:'100%',borderRadius:'0cqw',ease:'none'},0)
    .fromTo(f.querySelector('svg'),{scale:1.3},{scale:1,ease:'none'},0).fromTo(cap,{opacity:0,y:20},{opacity:1,y:0,ease:'none',duration:.3},.7);autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx153` rules from `site/fx.css`

_No dedicated `.fx153` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #153
