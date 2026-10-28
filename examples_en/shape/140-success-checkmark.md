# 140 · Success Checkmark — 打勾完成

A circle is drawn first, then a checkmark pops, and finally a success message appears

- Component: Shapes · SVG (`shape`)
- Timing: Entrance
- Tech: GSAP
- Uses: UI Interaction, Numbers & Data
- Style / keywords: Success Complete Checkmark Tick Confirm Submit Payment State Success Check Done Confirm Tick
- Tag: DrawSVG
- Example text: "Payment Successful" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Success Checkmark (打勾完成)" motion effect: The success state after submitting or completing payment: first a circle is drawn (about 0.8 seconds), then a checkmark is quickly drawn inside the circle (about 0.45 seconds); the instant the check finishes, the whole icon pops slightly bigger by 8% and back, while the 'Payment Successful' text below fades in from 8px below. Clean, clear, and reassuring. (GSAP: DrawSVGPlugin draws the circle and the check path in sequence; the icon scale 1→1.08 yoyo; the text fromTo y:8 / opacity:0)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx140">`, preview text "Payment Successful". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Success Checkmark".

### JavaScript — `FX[140]` from `site/fx.js`

```js
140(s,x){const w=el('div','okw');w.innerHTML='<svg viewBox="0 0 52 52"><circle class="oc" cx="26" cy="26" r="23"/><path class="ok" d="M15 27l7 7 15-16"/></svg><b></b>';w.querySelector('b').textContent=x;s.append(w);const sv=w.querySelector('svg');
  gsap.timeline({repeat:-1,repeatDelay:.4}).set(w,{opacity:1},0).fromTo(w.querySelector('.oc'),{drawSVG:'0%'},{drawSVG:'100%',duration:.8,ease:'power2.inOut'}).fromTo(w.querySelector('.ok'),{drawSVG:'0%'},{drawSVG:'100%',duration:.45,ease:'power2.out'})
    .fromTo(sv,{scale:1},{scale:1.08,duration:.18,yoyo:true,repeat:1,ease:'power2.out'},'<.3').fromTo(w.querySelector('b'),{opacity:0,y:8},{opacity:1,y:0,duration:.5,ease:'power2.out'},'<').to(w,{opacity:0,duration:.5},'+=1.6')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx140` rules from `site/fx.css`

_No dedicated `.fx140` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #140
