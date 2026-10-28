# 280 · Text Along Path — 沿曲線跑的文字

A line of text moves along a curved line, with scrolling deciding how far it runs

- Component: Text (`text`)
- Timing: Scroll-triggered
- Tech: GSAP
- Uses: Scroll Effects, Background Decoration, Emphasis
- Style / keywords: Curve Path Text Marquee textPath Wave Scroll Text On Path Curve Scroll Scroll Trigger ScrollTrigger
- Tag: SVG textPath
- Example text: "Follow the curve" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Text Along Path (沿曲線跑的文字)" motion effect: In the screen there is a curved wavy line spanning across (a faint thin line), and a line of text is arranged hugging this curve; when the user scrolls down, the text flows along the curve from right to left, the text turns with the curve where it bends, scroll speed determines text movement speed, and scrolling back reverses it. (SVG: <path id> + <text><textPath href="#id">; GSAP ScrollTrigger scrub tweens the textPath's startOffset attribute from 100% → −100%)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx280">`, preview text "Follow the curve". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Text Along Path".

### JavaScript — `FX[280]` from `site/fx.js`

```js
280(s,x){const{sc,wrap,view}=scrollBox(s);const id='tp'+Math.random().toString(36).slice(2);view.innerHTML=`<svg class="sx-tp" viewBox="0 0 400 225"><path id="${id}" d="M-20,170 C80,40 160,40 200,112 S320,190 420,60"/><text><textPath href="#${id}" startOffset="100%"></textPath></text></svg>`;
  const tp=view.querySelector('textPath');tp.textContent=rep(x+' · ',3);gsap.fromTo(tp,{attr:{startOffset:'100%'}},{attr:{startOffset:'-100%'},ease:'none',scrollTrigger:{trigger:wrap,scroller:sc,start:'top top',end:'bottom bottom',scrub:.5}});autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx280` rules from `site/fx.css`

_No dedicated `.fx280` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #280
