# 087 · Squash Bounce — 壓扁彈跳

Squashes flat on landing, stretches on rebound

- Component: Text (`text`)
- Timing: Entrance
- Tech: GSAP
- Uses: Emphasis
- Style / keywords: 
- Tag: CustomBounce
- Example text: "Bounce Bounce Bounce" (stage background: acc)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Squash Bounce (壓扁彈跳)" motion effect: The text drops from above, squashing flat like rubber when it lands and stretching out as it rebounds, bouncing a few times before coming to rest, while the ground shadow scales with its height. (GSAP: CustomBounce.create generates two eases, bounce and squash, applied to y and to scaleX/scaleY respectively)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage acc fx87">`, preview text "Bounce Bounce Bounce". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Squash Bounce".

### JavaScript — `FX[87]` from `site/fx.js`

```js
87(s,x){const w=el('div','bn');const t=T(x);const sh=el('div','sh');w.append(t,sh);s.append(w);
  gsap.timeline({repeat:-1,repeatDelay:.3}).fromTo(w,{opacity:0},{opacity:1,duration:.2}).fromTo(t,{yPercent:-260},{yPercent:0,duration:1.8,ease:'tmBounce'},0).fromTo(t,{scaleX:1,scaleY:1},{scaleX:1.35,scaleY:.7,duration:1.8,ease:'tmBounce-squash',transformOrigin:'50% 100%'},0).fromTo(sh,{scaleX:.2,opacity:.1},{scaleX:1,opacity:.45,duration:1.8,ease:'tmBounce'},0).to(w,{opacity:0,duration:.3},'+=.8')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx87` rules from `site/fx.css`

_No dedicated `.fx87` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #87
