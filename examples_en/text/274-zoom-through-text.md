# 274 · Zoom Through Text — 穿越大字轉場

A huge title keeps enlarging with scrolling, as if the camera passes through a letter into the next screen

- Component: Text (`text`)
- Timing: Scroll-triggered
- Tech: GSAP
- Uses: Scroll Effects, Transitions, Headline · Hero
- Style / keywords: Enlarge Pass Through Large Text Camera Transition Zoom Through Text Scale Scroll Transition Scroll Trigger ScrollTrigger
- Tag: ScrollTrigger
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Zoom Through Text (穿越大字轉場)" motion effect: A huge English title (for example ZOOM) is in the center of the screen, and when the user scrolls down the title starts enlarging, enlarging faster the more they scroll (an accelerating curve), finally enlarging to several tens of times, as if the camera passes through the gap in the middle of a letter, and after the screen is filled by the letter it transitions to the next section of content (the next section fades in from behind and enlarges from 0.8 times to 1 times). (GSAP ScrollTrigger scrub: inside a sticky area, fromTo scale 1 → 38, ease power2.in, transform-origin aligned to the letter gap to pass through; the next section fades in after 70% progress)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx274">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Zoom Through Text".

### JavaScript — `FX[274]` from `site/fx.js`

```js
274(s,x){const{sc,wrap,view}=scrollBox(s);view.classList.add('cen');const nx=el('div','abs gl sx-nx');nx.append(T('WELCOME',9));const big=el('div','sx-zt');big.textContent='ZOOM';view.append(big,nx);
  // 放大中心對準第一個 O 的中空處，穿過去後下一段淡入
  gsap.timeline({scrollTrigger:{trigger:wrap,scroller:sc,start:'top top',end:'bottom bottom',scrub:.5}}).fromTo(big,{scale:1},{scale:40,ease:'power2.in',duration:.8},0).fromTo(nx,{opacity:0,scale:.85},{opacity:1,scale:1,ease:'power1.out',duration:.25},.65).to({},{duration:.2});autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx274` rules from `site/fx.css`

_No dedicated `.fx274` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #274
