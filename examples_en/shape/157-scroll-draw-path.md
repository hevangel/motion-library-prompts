# 157 · Scroll Draw Path — 捲動繪製路徑

A curve draws its way down with scrolling, connecting each section

- Component: Shapes · SVG (`shape`)
- Timing: Scroll-triggered
- Tech: GSAP
- Uses: Scroll Effects, Numbers & Data
- Style / keywords: Path Curve Line Drawing Timeline Journey Story Scroll Path Draw SVG Line Journey Story Scroll Scroll scroll ScrollTrigger scrub Scroll-triggered
- Tag: DrawSVG scrub
- Example text: "Start Explore Grow Arrive" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Scroll Draw Path (捲動繪製路徑)" motion effect: In the page background there is a curve winding left and right through the whole stretch of content, with a very faint track underneath it first; as you scroll down, the accent-colored line draws along the track, drawing as far as you have scrolled, and retracts when you scroll back; several nodes along the line (dots + headings) fade in alternately from both sides as the line approaches. Suited to brand stories, journeys, and history introductions. (GSAP: DrawSVGPlugin drawSVG 0%→100% bound to ScrollTrigger scrub; the SVG is the same height as the content, preserveAspectRatio:none; each node fades in with its own toggleActions)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx157">`, preview text "Start Explore Grow Arrive". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Scroll Draw Path".

### JavaScript — `FX[157]` from `site/fx.js`

```js
157(s,x){const{sc,wrap}=scrollBox(s);wrap.classList.add('dpw');wrap.insertAdjacentHTML('afterbegin','<svg class="dpath" viewBox="0 0 100 400" preserveAspectRatio="none"><path class="bg2" d="M50,0 C92,40 92,60 50,100 C8,140 8,160 50,200 C92,240 92,260 50,300 C8,340 8,360 50,400"/><path class="fg2" d="M50,0 C92,40 92,60 50,100 C8,140 8,160 50,200 C92,240 92,260 50,300 C8,340 8,360 50,400"/></svg>');
  words(x).slice(0,4).forEach((v,i)=>{const m=el('div','dms'+(i%2?' r':''));m.style.top=(12+i*25)+'%';m.innerHTML='<i></i><b></b>';m.querySelector('b').textContent=v;wrap.append(m);
    gsap.fromTo(m,{opacity:0,x:i%2?16:-16},{opacity:1,x:0,duration:.5,ease:'power2.out',scrollTrigger:{trigger:m,scroller:sc,start:'top 65%',toggleActions:'play none none reverse'}})});
  gsap.fromTo(wrap.querySelector('.fg2'),{drawSVG:'0%'},{drawSVG:'100%',ease:'none',scrollTrigger:{trigger:wrap,scroller:sc,start:'top top',end:'bottom bottom',scrub:.5}});autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx157` rules from `site/fx.css`

_No dedicated `.fx157` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #157
