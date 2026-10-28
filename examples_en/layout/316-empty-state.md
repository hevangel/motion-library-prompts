# 316 · Empty State — 空狀態插畫

When there are no search results, an empty box bounces down, its lid flips open and a question mark pops out, and the text and button appear in sequence

- Component: Layout · Pages (`layout`)
- Timing: Entrance
- Tech: GSAP
- Uses: UI Interaction, App Interface
- Style / keywords: Empty State No Results Not Found 404 Illustration Empty State No Results Illustration Layout Page
- Tag: GSAP timeline
- Example text: "No matching effects found" (stage background: dark)
- Added: 2026-10-21

**AI prompt (English copy format):**

```text
"Empty State (空狀態插畫)" motion effect: An empty state for when a search has no results or a list is empty: a simple box illustration drops from above and bounces to a stop, then the box's lid flips open around one corner as its axis, and a question mark emerges from inside and floats gently up and down; the heading, description text and "Browse all" button below fade in and move up in sequence; afterwards the lid closes and the question mark disappears. It keeps the blank screen from feeling cold and guides the next step. (GSAP timeline: the illustration from y:-20 with ease bounce.out → the lid rotation −28 with back.out → the question mark from scale 0 → the text fades in with stagger → the question mark floats with yoyo)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx316">`, preview text "No matching effects found". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Empty State".

### JavaScript — `FX[316]` from `site/fx.js`

```js
316(s,x,card){const w=el('div','pg-em');w.innerHTML='<div class="pg-il"><i class="pg-box"></i><i class="pg-lid"></i><i class="pg-q">?</i><i class="pg-sh"></i></div><b></b><p>試試換個關鍵字，或看看熱門效果</p><button>瀏覽全部</button>';w.querySelector('b').textContent=x;s.append(w);
  gsap.timeline({repeat:-1,repeatDelay:1.2}).from(w.querySelector('.pg-il'),{y:-20,opacity:0,duration:.6,ease:'bounce.out'}).to(w.querySelector('.pg-lid'),{rotation:-28,y:-6,duration:.35,ease:'back.out(3)'}).from(w.querySelector('.pg-q'),{y:14,scale:0,opacity:0,duration:.45,ease:'back.out(3)'},'-=.1').from(w.querySelectorAll('b,p,button'),{y:12,opacity:0,duration:.4,stagger:.08},'-=.2').to(w.querySelector('.pg-q'),{y:-4,duration:.6,yoyo:true,repeat:3,ease:'sine.inOut'}).to(w.querySelector('.pg-lid'),{rotation:0,y:0,duration:.3},'+=.2').to(w.querySelector('.pg-q'),{opacity:0,duration:.2},'<')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx316` rules from `site/fx.css`

_No dedicated `.fx316` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #316
