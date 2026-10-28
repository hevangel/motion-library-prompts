# 202 · Curtain Page Transition — 頁面轉場簾幕

When switching pages, three curtains fall in sequence to cover the screen, then retract downward to reveal the new page

- Component: Layout · Pages (`layout`)
- Timing: Switch
- Tech: GSAP
- Uses: Transitions
- Style / keywords: page transition page change curtain mask SPA routing Page Transition Curtain Wipe Router layout page web structure
- Tag: Timeline
- Example text: "Home Work About" (stage background: dark)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Curtain Page Transition (頁面轉場簾幕)" motion effect: When a navigation click switches the page, three vertical strip curtains fall from the top in sequence (about 0.08 seconds apart) to cover the whole screen — at this moment the page behind is replaced with the new page — then the three curtains retract downward in sequence, and the new page's title and content blocks fade in and float up from top to bottom. The whole sequence takes about 1.4 seconds, giving page changes a complete sense of rhythm. (GSAP: curtains yPercent -101 to 0 to 101, stagger 0.08, ease power3.inOut; switch the content in the callback between the two segments; for an SPA it can be paired with Barba.js or a framework's route transition hooks)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx202">`, preview text "Home Work About". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Curtain Page Transition".

### JavaScript — `FX[202]` from `site/fx.js`

```js
202(s,x){const ws=words(x);const f=lyPage(s);const pg=el('div','ly-pg');f.append(pg);const cur=el('div','ly-cur');for(let i=0;i<3;i++)cur.append(el('i'));f.append(cur);const bars=cur.children;let k=0;
  const paint=()=>{pg.innerHTML='<b></b><i class="ly-bl"></i><i class="ly-bl s"></i><div class="ly-gr"><i></i><i></i><i></i></div>';pg.querySelector('b').textContent=ws[k%ws.length];pg.querySelectorAll('.ly-gr i').forEach((e,i)=>e.style.background=GC[(k+i)%5])};paint();
  gsap.timeline({repeat:-1,repeatDelay:1.2,onRepeat:()=>{}}).fromTo(bars,{yPercent:-101},{yPercent:0,duration:.55,ease:'power3.inOut',stagger:.08},1.2).add(()=>{k++;paint()}).fromTo(bars,{yPercent:0},{yPercent:101,duration:.55,ease:'power3.inOut',stagger:.08},'+=.1').fromTo(pg.children,{y:12,opacity:0},{y:0,opacity:1,duration:.5,stagger:.06,ease:'power2.out'},'-=.3')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx202` rules from `site/fx.css`

_No dedicated `.fx202` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #202
