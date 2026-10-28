# 214 · Stack Fan Out — 疊卡散開

A stack of slightly skewed cards fans out into a row to both sides on hover

- Component: Cards · Groups (`card`)
- Timing: Hover · Click
- Tech: CSS
- Uses: UI Interaction, Headline · Hero
- Style / keywords: Stacked Cards Fan Out Fan Shape Expand Portfolio Stack Spread Fan Cards Hover Cards Group
- Tag: CSS hover
- Example text: "Planning Design Development Testing Launch" (stage background: dark)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Stack Fan Out (疊卡散開)" motion effect: Five cards stacked in a pile, each skewed at a slightly different angle; when the mouse moves over the stack, the cards fan out to the left and right around the middle card into a fan-shaped row (the further out, the larger the angle and the more they droop slightly downward), with a slight elastic rebound; when the mouse leaves, they gather back into a stack. About 0.6 seconds. (CSS: each card uses the CSS variable --i (-2 to 2) to calculate translateX, rotate and translateY; on hover larger coefficients are used, with transition cubic-bezier(.3,1.3,.5,1))
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx214">`, preview text "Planning Design Development Testing Launch". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Stack Fan Out".

### JavaScript — `FX[214]` from `site/fx.js`

```js
214(s,x,card){const ws=words(x);const w=el('div','kd-st');const cs=[...Array(5)].map((_,i)=>{const c=el('div','kd-sk');c.style.setProperty('--i',i-2);c.style.background=`linear-gradient(160deg,${GC[i%5]},${GC[(i+2)%5]})`;c.innerHTML='<b></b>';c.querySelector('b').textContent=ws[i%ws.length];w.append(c);return c});s.append(w);autoHover(w,[w],card,1500)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx214` rules from `site/fx.css`

_No dedicated `.fx214` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #214
