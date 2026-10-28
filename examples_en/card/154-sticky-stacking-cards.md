# 154 · Sticky Stacking Cards — 黏著堆疊卡片

Cards scroll up one by one and stack over each other, while the one below shrinks and darkens

- Component: Cards · Groups (`card`)
- Timing: Scroll-triggered
- Tech: GSAP
- Uses: UI Interaction, Scroll Effects
- Style / keywords: Cards Stacking Sticky sticky Stacked Service Intro Stacking Cards Sticky Stack Deck Scroll Scroll scroll ScrollTrigger scrub Scroll-triggered
- Tag: Sticky·scrub
- Example text: "Research Design Develop Launch" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Sticky Stacking Cards (黏著堆疊卡片)" motion effect: A set of large cards arranged in sequence; when each card scrolls to near the top of the screen it sticks (each card's resting position is offset slightly further down, so the edge of the previous card is visible); when the next card scrolls up and stacks on top of it, the covered card simultaneously shrinks to about 90% and darkens, creating the depth of a stack of cards; scrolling back restores it. (CSS position:sticky + top increasing by index; with GSAP, each card gets a ScrollTrigger that scrubs its scale and brightness over the range 'from the next card entering the viewport to its reaching the top')
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx154">`, preview text "Research Design Develop Launch". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Sticky Stacking Cards".

### JavaScript — `FX[154]` from `site/fx.js`

```js
154(s,x){const sc=el('div','scr nopad');const c=el('div','stk');const ws=words(x);const cs=ws.slice(0,4).map((v,i)=>{const k=el('div','skc2');k.style.setProperty('--i',i);k.style.background=GC[i%5];k.innerHTML=`<small>0${i+1}</small><b></b>`;k.querySelector('b').textContent=v;c.append(k);return k});sc.append(c);s.append(sc);
  cs.forEach((k,i)=>{if(i<cs.length-1)gsap.to(k,{scale:.9,filter:'brightness(.55)',ease:'none',scrollTrigger:{trigger:cs[i+1],scroller:sc,start:'top bottom',end:'top top+=8%',scrub:true}})});autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx154` rules from `site/fx.css`

_No dedicated `.fx154` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #154
