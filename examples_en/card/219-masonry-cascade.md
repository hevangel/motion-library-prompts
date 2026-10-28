# 219 · Masonry Cascade — 瀑布流依序落下

Masonry cards of varying heights fall into place row by row with a slight rotation

- Component: Cards · Groups (`card`)
- Timing: Entrance
- Tech: GSAP
- Uses: UI Interaction, Headline · Hero
- Style / keywords: Masonry masonry Pinterest Gallery Entrance Fall Masonry Grid Cascade Gallery Cards Group
- Tag: Stagger
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Masonry Cascade (瀑布流依序落下)" motion effect: A Masonry gallery entrance: cards in three columns of varying heights, in reading order from top to bottom and left to right, fall one by one from about 30px above with a slight random rotation and fade in, with a slight rebound as they settle (interval about 0.09 seconds), so the whole gallery looks as if it is being placed piece by piece. (GSAP: after sorting by each card's row and column index, stagger 0.09, fromTo y:-30 / opacity:0 / rotation:random(-6,6) back to zero, ease back.out(1.4); on a real site, layout can be done with CSS columns or a masonry library)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx219">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Masonry Cascade".

### JavaScript — `FX[219]` from `site/fx.js`

```js
219(s){const H=[[14,9,12],[10,13,8],[12,8,11]];const w=el('div','kd-ms');const items=[];H.forEach((col,ci)=>{const c=el('div','kd-mc');col.forEach((h,ri)=>{const it=el('i');it.style.height=h+'cqw';it.style.background=`linear-gradient(150deg,${GC[(ci+ri)%5]},${GC[(ci+ri+2)%5]})`;c.append(it);items.push([it,ri,ci])});w.append(c)});s.append(w);
  const ord=items.sort((a,b)=>a[1]-b[1]||a[2]-b[2]).map(a=>a[0]);gsap.timeline({repeat:-1,repeatDelay:.4}).fromTo(ord,{y:-30,opacity:0,rotation:()=>gsap.utils.random(-6,6)},{y:0,opacity:1,rotation:0,duration:.6,ease:'back.out(1.4)',stagger:.09}).to(ord,{opacity:0,y:10,duration:.4,stagger:.03},'+=1.6')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx219` rules from `site/fx.css`

_No dedicated `.fx219` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #219
