# 278 · Scroll Fan Out — 捲動扇形展開

Cards stacked together spread out into a fan with scrolling

- Component: Cards · Groups (`card`)
- Timing: Scroll-triggered
- Tech: GSAP
- Uses: Scroll Effects, Headline · Hero
- Style / keywords: Fan Spread Cards Stacked Cards Works Scroll Scroll Fan Out Cards Spread Scroll Trigger ScrollTrigger
- Tag: ScrollTrigger
- Example text: "Seaside Forest Night Sky Afternoon City" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Scroll Fan Out (捲動扇形展開)" motion effect: Five image cards start neatly stacked in a pile; when the user scrolls down, the cards, pivoting on a point below their bottom, spread out to the left and right like opening a fan: the middle card does not move, the outer cards rotate at larger angles (each differing by about 14 degrees), while displacing to both sides and downward; scrolling back retracts them into a stack. (GSAP ScrollTrigger scrub: card transform-origin: 50% 120%, fromTo rotation / x / y calculated with a function according to index (i − middle index))
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx278">`, preview text "Seaside Forest Night Sky Afternoon City". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Scroll Fan Out".

### JavaScript — `FX[278]` from `site/fx.js`

```js
278(s,x){const{sc,wrap,view}=scrollBox(s);view.classList.add('cen');const ws=words(x);const fan=el('div','sx-fn');const cs=[0,1,2,3,4].map(i=>{const c=el('div','sx-fk');c.innerHTML=mdImg(i)+'<b></b>';c.querySelector('b').textContent=ws[i%ws.length];fan.append(c);return c});view.append(fan);
  gsap.timeline({scrollTrigger:{trigger:wrap,scroller:sc,start:'top top',end:'bottom bottom',scrub:.6}}).fromTo(cs,{rotation:0,x:0,y:0},{rotation:i=>(i-2)*14,x:i=>(i-2)*58+'%',y:i=>Math.abs(i-2)*9+'%',ease:'power2.out'});autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx278` rules from `site/fx.css`

_No dedicated `.fx278` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #278
