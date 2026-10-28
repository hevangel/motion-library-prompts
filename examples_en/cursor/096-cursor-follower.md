# 096 · Cursor Follower — 游標跟隨

Trailing dots and an inverted-color circle

- Component: Cursor (`cursor`)
- Timing: Hover · Click
- Tech: GSAP
- Uses: UI Interaction
- Style / keywords: 
- Tag: quickTo
- Example text: "Follow the Cursor" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Cursor Follower (游標跟隨)" motion effect: Behind the cursor follows a string of trailing dots, from fast to slow, plus a larger circle laid over the text in an inverted-color blend mode, so the text turns inverted in color as it passes over. (GSAP: multiple gsap.quickTo with different durations, the large circle uses mix-blend-mode:difference)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx96">`, preview text "Follow the Cursor". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Cursor Follower".

### JavaScript — `FX[96]` from `site/fx.js`

```js
96(s,x){const l=layer(s);l.append(T(x,Math.min(14,60/chars(x).length)));const big=el('div','fbig');const ds=[...Array(5)].map((_,i)=>{const d=el('div','fdot');d.style.opacity=1-i*.17;l.append(d);return d});l.append(big);gsap.set([big,...ds],{xPercent:-50,yPercent:-50});
  const qs=[big,...ds].map((d,i)=>[gsap.quickTo(d,'x',{duration:i?.12+i*.1:.5,ease:'power3'}),gsap.quickTo(d,'y',{duration:i?.12+i*.1:.5,ease:'power3'})]);
  pointer(l,(px,py)=>qs.forEach(([a,b])=>{a(px);b(py)}),null,false)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx96` rules from `site/fx.css`

_No dedicated `.fx96` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #96
