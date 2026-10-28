# 098 · Card Deal — 發牌展開

Cards are dealt from the bottom and unfold into a fan

- Component: Cards · Groups (`card`)
- Timing: Entrance, Exit
- Tech: GSAP
- Uses: Transitions, UI Interaction
- Style / keywords: 
- Tag: Timeline·Stagger
- Example text: "Spring Summer Autumn Winter Snow" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Card Deal (發牌展開)" motion effect: 5 cards are dealt in sequence from the bottom of the screen, unfolding into an angled fan with a slight rebound, and after a pause they are gathered back to the bottom, starting from the last card. (GSAP: timeline + stagger, xPercent / rotation use function values (i)=>(i-2)*115)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx98">`, preview text "Spring Summer Autumn Winter Snow". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Card Deal".

### JavaScript — `FX[98]` from `site/fx.js`

```js
98(s,x){const w=el('div','deal');const cs=chars(x);const cds=[...Array(5)].map((_,i)=>{const c=el('div','dc');c.textContent=cs[i%cs.length];w.append(c);return c});s.append(w);
  gsap.timeline({repeat:-1,repeatDelay:.2}).fromTo(cds,{xPercent:0,yPercent:170,rotation:0},{xPercent:i=>(i-2)*115,yPercent:0,rotation:i=>(i-2)*6,duration:.7,ease:'back.out(1.4)',stagger:.1}).to(cds,{xPercent:0,yPercent:170,rotation:0,duration:.5,ease:'power3.in',stagger:{each:.06,from:'end'}},'+=1.3')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx98` rules from `site/fx.css`

_No dedicated `.fx98` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #98
