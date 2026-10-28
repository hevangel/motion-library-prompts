# 080 · 3D Char Flip — 3D 翻字

Each character enters flipping around the X axis

- Component: Text (`text`)
- Timing: Entrance
- Tech: GSAP
- Uses: Transitions, Headline · Hero
- Style / keywords: 
- Tag: SplitText·3D
- Example text: "Flipping In" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"3D Char Flip (3D 翻字)" motion effect: Each character enters with a 3D flip around the X axis (flipping from the back to the front, with a slight rebound), spaced 0.07 seconds apart in sequence; after lingering, it flips forward and disappears. (GSAP: SplitText chars, rotationX, transformOrigin with Z depth, ease back.out)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx80">`, preview text "Flipping In". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "3D Char Flip".

### JavaScript — `FX[80]` from `site/fx.js`

```js
80(s,x){const t=T(x);s.append(t);const sp=SplitText.create(t,{type:'chars'});const o={transformOrigin:'50% 50% -30'};
  gsap.timeline({repeat:-1,repeatDelay:.3}).from(sp.chars,{...o,rotationX:-95,opacity:0,duration:.9,ease:'back.out(1.8)',stagger:.07}).to(sp.chars,{...o,rotationX:95,opacity:0,duration:.6,ease:'power2.in',stagger:.05},'+=1.2')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx80` rules from `site/fx.css`

_No dedicated `.fx80` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #80
