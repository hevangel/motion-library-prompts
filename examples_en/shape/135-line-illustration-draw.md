# 135 · Line Illustration Draw — 線條插畫逐筆描繪

A line illustration is drawn stroke by stroke, then the main subject softly appears

- Component: Shapes · SVG (`shape`)
- Timing: Entrance
- Tech: GSAP
- Uses: Headline · Hero, Background Decoration
- Style / keywords: Illustration Line Illustration Stroke by Stroke Drawing Hand-drawn Diagram Line Art Illustration Draw Sketch
- Tag: DrawSVG
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Line Illustration Draw (線條插畫逐筆描繪)" motion effect: A line illustration made of multiple lines (for example, a cup of coffee giving off steam: the saucer, cup body, handle, and three wisps of steam) is traced one stroke at a time in order from bottom to top, from the main subject to the details, about 0.9 seconds per stroke with about 0.32 seconds between strokes; once all are drawn, the main subject is softly given a layer of translucent fill, and the steam lines drift gently up and down once. Quiet overall, with a handmade feel. (GSAP: DrawSVGPlugin staggers the drawing across the paths; the fill uses another path of the same shape fading in from opacity 0)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx135">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Line Illustration Draw".

### JavaScript — `FX[135]` from `site/fx.js`

```js
135(s){s.insertAdjacentHTML('beforeend','<svg class="ill" viewBox="0 0 120 90"><path class="fl2" d="M34,40 L38,70 C40,76 80,76 82,70 L86,40 Z"/><path d="M22,78 C40,84 80,84 98,78"/><path d="M34,40 L38,70 C40,76 80,76 82,70 L86,40 Z"/><path d="M86,46 C98,44 100,60 84,62"/><path class="st" d="M48,32 C44,26 52,22 48,14"/><path class="st" d="M60,32 C56,24 64,20 60,10"/><path class="st" d="M72,32 C68,26 76,22 72,14"/></svg>');
  const sv=s.querySelector('.ill'),ps=sv.querySelectorAll('path:not(.fl2)'),st=sv.querySelectorAll('.st');
  gsap.timeline({repeat:-1,repeatDelay:.4}).set(sv,{opacity:1},0).fromTo(ps,{drawSVG:'0%'},{drawSVG:'100%',duration:.9,ease:'power1.inOut',stagger:.32},0).fromTo(sv.querySelector('.fl2'),{opacity:0},{opacity:.28,duration:.8,ease:'power1.out'})
    .to(st,{y:-2,duration:.8,ease:'sine.inOut',yoyo:true,repeat:1,stagger:.15},'<').to(sv,{opacity:0,duration:.5},'+=.6')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx135` rules from `site/fx.css`

_No dedicated `.fx135` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #135
