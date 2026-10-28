# 211 · Back to Top Progress — 回到頂部進度環

After scrolling, a button floats in at the bottom right, its outer ring shows reading progress, and clicking it returns to the top

- Component: Layout · Pages (`layout`)
- Timing: Scroll-triggered, Hover · Click
- Tech: GSAP
- Uses: UI Interaction, Scroll Effects
- Style / keywords: Back To Top Top Progress Ring Reading Progress Scroll Progress Back To Top Scroll Progress Ring Button Layout Page Web Structure
- Tag: DrawSVG scrub
- Example text: "Reading Progress" (stage background: dark)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Back to Top Progress (回到頂部進度環)" motion effect: On a long article page, after scrolling down past a short distance, a circular button at the bottom right elastically scales in from 0; around the button is a progress ring that is drawn full according to the scroll proportion of the whole page (clockwise from the very top), with an upward arrow in the middle; when clicked, the page smoothly scrolls back to the top, and near the top the button shrinks and disappears. (GSAP: DrawSVGPlugin bound to a ScrollTrigger with scrub draws the progress ring, onUpdate toggles visibility based on progress; on click use gsap.to(window, {scrollTo:0}) or window.scrollTo({top:0, behavior:"smooth"}))
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx211">`, preview text "Reading Progress". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Back to Top Progress".

### JavaScript — `FX[211]` from `site/fx.js`

```js
211(s,x){const sc=el('div','scr nopad');const c=el('div','ly-art');c.innerHTML='<b></b>'+[...Array(14)].map((_,i)=>`<i class="ly-bl${i%3===2?' s':''}"></i>`).join('');c.querySelector('b').textContent=x;sc.append(c);s.append(sc);
  const btn=el('button','ly-top');btn.setAttribute('aria-label','回到頂部');btn.innerHTML='<svg viewBox="0 0 40 40"><circle class="tr" cx="20" cy="20" r="17"/><circle class="pr" cx="20" cy="20" r="17"/></svg><span>↑</span>';s.append(btn);
  gsap.fromTo(btn.querySelector('.pr'),{drawSVG:'0%'},{drawSVG:'100%',ease:'none',scrollTrigger:{scroller:sc,start:0,end:'max',scrub:true,onUpdate:t=>btn.classList.toggle('on',t.progress>.12)}});
  btn.onclick=()=>gsap.to(sc,{scrollTop:0,duration:.8,ease:'power3.inOut'});autoScroll(sc,btn)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx211` rules from `site/fx.css`

_No dedicated `.fx211` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #211
