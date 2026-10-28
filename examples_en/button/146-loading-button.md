# 146 · Loading Button — 按鈕載入成功

On press, the button shrinks into a spinning circle, then a checkmark appears on completion and it restores

- Component: Button (`button`)
- Timing: Hover · Click, Switch
- Tech: GSAP
- Uses: App Interface, UI Interaction
- Style / keywords: Button Loading Submit Spinner Success Checkmark State Loading Button Submit Spinner Success Morph App Mobile Mobile Device Micro-interaction Mobile App Micro-interaction
- Tag: Loading state
- Example text: "Submit Order" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Loading Button (按鈕載入成功)" motion effect: When the 'Submit' button is clicked, the button first presses in gently (scaling to 95%), the text fades out, and the button's width contracts into a circle (about 0.4 seconds) with a spinning loading ring appearing inside it; when done, the loading ring disappears and is replaced by a checkmark being drawn, and the button pops slightly; after holding for about 0.8 seconds, it expands back to its original width and the text fades in. This prevents duplicate clicks and lets the user clearly know the state. (GSAP: a timeline tweens in sequence the width, the spinner rotation, and the DrawSVG checkmark; the width uses fromTo with fixed units)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx146">`, preview text "Submit Order". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Loading Button".

### JavaScript — `FX[146]` from `site/fx.js`

```js
146(s,x){const b=el('button','lb2');b.innerHTML='<span class="t2"></span><i class="spn"></i><svg class="ck" viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7"/></svg>';b.querySelector('.t2').textContent=x;s.append(b);const q=c=>b.querySelector(c);
  gsap.timeline({repeat:-1,repeatDelay:.8}).set(b,{width:'30cqw'},0).set(q('.spn'),{opacity:0},0).set(q('.ck path'),{drawSVG:'0%'},0)
    .to(b,{scale:.95,duration:.1},.3).to(b,{scale:1,duration:.15}).to(q('.t2'),{opacity:0,duration:.15},'<').fromTo(b,{width:'30cqw'},{width:'8cqw',duration:.4,ease:'power3.inOut'},'<')
    .to(q('.spn'),{opacity:1,duration:.15}).fromTo(q('.spn'),{rotation:0},{rotation:720,duration:1.2,ease:'none'},'<').to(q('.spn'),{opacity:0,duration:.15})
    .to(q('.ck path'),{drawSVG:'100%',duration:.35,ease:'power2.out'}).fromTo(b,{scale:1},{scale:1.08,duration:.15,yoyo:true,repeat:1},'<')
    .to(q('.ck path'),{drawSVG:'100% 100%',duration:.25},'+=.8').fromTo(b,{width:'8cqw'},{width:'30cqw',duration:.4,ease:'power3.inOut'}).to(q('.t2'),{opacity:1,duration:.2})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx146` rules from `site/fx.css`

_No dedicated `.fx146` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #146
