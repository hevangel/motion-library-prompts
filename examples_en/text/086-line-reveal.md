# 086 · Line Reveal — 逐行揭示

Lines flip up one by one from beneath a mask

- Component: Text (`text`)
- Timing: Entrance
- Tech: GSAP
- Uses: Headline · Hero
- Style / keywords: 
- Tag: Mask·Stagger
- Example text: "Animation Brings Interfaces to Life" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Line Reveal (逐行揭示)" motion effect: Multiple lines of text flip up one by one from beneath their own masks, with a slight rotation, the last line in the accent color; a thin line below is drawn from left to right, and after a pause the whole block sweeps upward and away. (GSAP: each line wrapped in overflow hidden, from yPercent:115, stagger 0.14)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx86">`, preview text "Animation Brings Interfaces to Life". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Line Reveal".

### JavaScript — `FX[86]` from `site/fx.js`

```js
86(s,x){const ws=words(x);const w=el('div','ln');w.style.fontSize=Math.min(10,62/Math.max(...ws.map(v=>chars(v).length)))+'cqw';const inn=ws.map((v,i)=>{const m=el('div','m');const e=el('div','i');e.textContent=v;if(i===ws.length-1)e.style.color='var(--a)';m.append(e);w.append(m);return e});const rule=el('div','rule');w.append(rule);s.append(w);
  gsap.timeline({repeat:-1,repeatDelay:.3}).from(inn,{yPercent:115,rotation:4,duration:.9,ease:'power4.out',stagger:.14}).fromTo(rule,{scaleX:0,transformOrigin:'0% 50%'},{scaleX:1,duration:.8,ease:'power3.inOut'},'-=.5').to(inn,{yPercent:-115,duration:.5,ease:'power3.in',stagger:.08},'+=1.4').to(rule,{scaleX:0,transformOrigin:'100% 50%',duration:.5,ease:'power3.in'},'<')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx86` rules from `site/fx.css`

_No dedicated `.fx86` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #86
