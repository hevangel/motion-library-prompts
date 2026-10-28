# 312 · Top Loading Bar — 頂部載入進度條

When changing pages, a thin line at the top of the page quickly runs halfway, crawls slowly, then rushes to the end and disappears once loaded, and the content then emerges in sequence

- Component: Layout · Pages (`layout`)
- Timing: Entrance, Switch
- Tech: GSAP
- Uses: Transitions, UI Interaction
- Style / keywords: Loading Progress Bar Top Page Change NProgress YouTube Loading Bar Page Load Progress Layout Page
- Tag: GSAP
- Example text: "Article Title" (stage background: dark)
- Added: 2026-10-21

**AI prompt (English copy format):**

```text
"Top Loading Bar (頂部載入進度條)" motion effect: When the site changes pages or loads content, a thin accent-colored progress bar (with a slight glow) appears at the very top of the page: it first quickly runs to about 30%, then slowly crawls to about 70% (giving the feeling of "loading"), and when loading completes it quickly rushes to 100% and fades out; at the same time the page content (heading, paragraphs, cards) fades in and floats up in sequence from below. (GSAP timeline: the progress bar uses transform-origin:left, scaleX 0 → .3 (power2.out) → .7 (slower) → 1 (fast), then opacity 0; the content fades in with stagger)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx312">`, preview text "Article Title". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Top Loading Bar".

### JavaScript — `FX[312]` from `site/fx.js`

```js
312(s,x,card){const f=lyPage(s);f.insertAdjacentHTML('beforeend','<i class="pg-lb"></i><div class="pg-ct"><b></b><i class="ly-bl"></i><i class="ly-bl s"></i><div class="pg-row"><i></i><i></i><i></i></div></div>');f.querySelector('.pg-ct b').textContent=x;const bar=f.querySelector('.pg-lb'),ct=f.querySelector('.pg-ct');
  gsap.timeline({repeat:-1,repeatDelay:.8}).set(ct.children,{opacity:0,y:10}).set(bar,{scaleX:0,opacity:1}).to(bar,{scaleX:.3,duration:.4,ease:'power2.out'}).to(bar,{scaleX:.7,duration:1.2,ease:'power1.inOut'}).to(bar,{scaleX:1,duration:.25,ease:'power1.in'}).to(bar,{opacity:0,duration:.3}).to(ct.children,{opacity:1,y:0,duration:.5,stagger:.08,ease:'power2.out'},'-=.2').to({},{duration:1.6})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx312` rules from `site/fx.css`

_No dedicated `.fx312` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #312
