# 129 · Connected Steps — 步驟依序連接

After the connector line between step cards draws across, the next step appears

- Component: Cards · Groups (`card`)
- Timing: Entrance
- Tech: GSAP
- Uses: UI Interaction, Numbers & Data
- Style / keywords: Steps Process 1 2 3 Connector Line Tutorial Checkout Onboarding Gentle Soft Light Guidance Flow Gaze Reading Order Low-key Subtle Gentle Soft Entrance Visual Flow Hierarchy
- Tag: Steps
- Example text: "Choose a Plan Enter Details Complete Payment" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Connected Steps (步驟依序連接)" motion effect: Three step cards arranged horizontally (numbers 01, 02, 03 + a heading + one line of description). On entry, the first card fades in from about 14px below, then a thin connector line draws from left to right to the second card, which only then fades in, then the line draws to the third card, which fades in; the rhythm is steady, so users clearly understand 'what to do first, then what.' (GSAP: a timeline chained in sequence; cards fromTo y:14 / opacity:0, connector lines scaleX 0→1 with transform-origin on the left, ease power1.inOut / power2.out)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx129">`, preview text "Choose a Plan Enter Details Complete Payment". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Connected Steps".

### JavaScript — `FX[129]` from `site/fx.js`

```js
129(s,x){const w=el('div','stp');const parts=[];words(x).slice(0,3).forEach((v,i)=>{if(i){const c=el('i','cn');w.append(c);parts.push(['c',c])}const c=el('div','sc');c.innerHTML=`<em>0${i+1}</em><b></b><span></span>`;c.querySelector('b').textContent=v;w.append(c);parts.push(['s',c])});s.append(w);
  const tl=gsap.timeline({repeat:-1,repeatDelay:.3}).set(w,{opacity:1},0);let t=0;
  parts.forEach(([k,e])=>{if(k==='s'){tl.fromTo(e,{opacity:0,y:14},{opacity:1,y:0,duration:.8,ease:'power2.out'},t);t+=.45}else{tl.fromTo(e,{scaleX:0},{scaleX:1,duration:.6,ease:'power1.inOut'},t);t+=.55}});tl.to(w,{opacity:0,duration:.5},'+=1.6')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx129` rules from `site/fx.css`

_No dedicated `.fx129` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #129
