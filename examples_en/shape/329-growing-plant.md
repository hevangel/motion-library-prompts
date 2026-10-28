# 329 · Growing Plant — 樹枝生長

The trunk grows first, then branches split off, and finally the leaves emerge one by one

- Component: Shapes · SVG (`shape`)
- Timing: Entrance
- Tech: GSAP
- Uses: Headline · Hero, Logo · Brand
- Style / keywords: Tree Growing Plant Branches Leaves Growth Sustainability Growing Tree Plant Branches Leaves Growth Graphics SVG
- Tag: DrawSVG
- Example text: "Growing Slowly" (stage background: dark)
- Added: 2026-10-21

**AI prompt (English copy format):**

```text
"Growing Plant (樹枝生長)" motion effect: A tree grows from the bottom up: first the ground line and the main trunk are drawn (about 0.8 seconds), then branches to the left and right grow out in sequence, followed by finer twigs; after the branches are drawn, leaves pop out one by one from the ends of the branches in random order (enlarging from 0 to 1, with a bounce-back); finally text emerges below. Suitable for brand stories, growth or sustainability themes. (GSAP timeline: each branch is an SVG path, drawn in sequence with DrawSVG 0% → 100%; the leaves use scale 0 → 1, transform-origin at the leaf stem, stagger from:"random")
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx329">`, preview text "Growing Slowly". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Growing Plant".

### JavaScript — `FX[329]` from `site/fx.js`

```js
329(s,x){const w=el('div','sv-tree');const B=[['M80,118 C80,95 78,80 80,60','t'],['M80,92 C70,86 60,80 54,70',''],['M80,82 C92,76 102,68 108,56',''],['M80,66 C74,58 70,50 70,40',''],['M80,62 C86,54 92,48 96,38',''],['M54,70 C48,66 44,60 42,54','s'],['M108,56 C114,52 118,46 120,40','s']];const LV=[[54,70],[42,54],[108,56],[120,40],[70,40],[96,38],[80,60],[62,78],[100,66]];
  w.innerHTML=`<svg viewBox="0 0 160 125"><path class="gd" d="M30,118 H130"/>${B.map(([d,c])=>`<path class="br ${c}" d="${d}"/>`).join('')}${LV.map(([cx,cy],i)=>`<g class="lf" transform="translate(${cx},${cy}) rotate(${(i*47)%360})"><path d="M0,0 C4,-5 10,-5 13,0 C10,5 4,5 0,0Z"/></g>`).join('')}</svg><b></b>`;w.querySelector('b').textContent=x;s.append(w);
  const br=w.querySelectorAll('.br'),lf=w.querySelectorAll('.lf path');
  gsap.timeline({repeat:-1,repeatDelay:1}).set(lf,{scale:0,transformOrigin:'0% 50%'}).fromTo(br[0],{drawSVG:'0%'},{drawSVG:'100%',duration:.8,ease:'power2.out'}).fromTo([...br].slice(1,5),{drawSVG:'0%'},{drawSVG:'100%',duration:.6,stagger:.12,ease:'power2.out'},'-=.3').fromTo([...br].slice(5),{drawSVG:'0%'},{drawSVG:'100%',duration:.4,stagger:.1},'-=.2').to(lf,{scale:1,duration:.5,ease:'back.out(2.5)',stagger:{each:.07,from:'random'}},'-=.2').from(w.querySelector('b'),{y:8,opacity:0,duration:.4},'-=.2').to(w,{opacity:0,duration:.5},'+=1.6').set(w,{opacity:1})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx329` rules from `site/fx.css`

_No dedicated `.fx329` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #329
