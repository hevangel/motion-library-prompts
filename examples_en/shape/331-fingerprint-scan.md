# 331 · Fingerprint Scan — 指紋掃描解鎖

Fingerprint ridges are drawn ring by ring, a scanning light bar sweeps up and down, and after success the frame glows and a checkmark appears

- Component: Shapes · SVG (`shape`)
- Timing: Entrance, Switch
- Tech: GSAP
- Uses: App Interface, UI Interaction
- Style / keywords: Fingerprint Scan Unlock Biometric Verification Login Fingerprint Scan Biometric Unlock Auth Graphics SVG
- Tag: DrawSVG
- Example text: "Verified" (stage background: dark)
- Added: 2026-10-21

**AI prompt (English copy format):**

```text
"Fingerprint Scan (指紋掃描解鎖)" motion effect: A phone fingerprint-unlock screen: in a rounded-square sensing area, the fingerprint's curved ridges are drawn in sequence ring by ring from the inside out; then a glowing scanning light bar sweeps from top to bottom and back from bottom to top, and the text below shows "Scanning…"; after the scan completes, the fingerprint ridges fade, a thick checkmark is quickly drawn, the sensing area's frame emits a glow, and the text changes to "Verified". (GSAP timeline: the fingerprint arcs are drawn with DrawSVG stagger; the scanning bar top 0% → 100% yoyo; on completion, add a class to make the frame's box-shadow glow, and the checkmark DrawSVG 0% → 100%)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx331">`, preview text "Verified". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Fingerprint Scan".

### JavaScript — `FX[331]` from `site/fx.js`

```js
331(s,x){const arcs=[];for(let i=0;i<7;i++){const rx=6+i*4.2,ry=8+i*5,gap=i%2?.7:.35;arcs.push(`M${(-rx*Math.sin(gap)).toFixed(1)},${(ry*Math.cos(gap)).toFixed(1)} A${rx},${ry} 0 1 1 ${(rx*Math.sin(gap*.6)).toFixed(1)},${(ry*Math.cos(gap*.6)).toFixed(1)}`)}
  s.insertAdjacentHTML('beforeend',`<div class="sv-fp"><div class="sv-fb"><svg viewBox="-40 -42 80 80">${arcs.map(d=>`<path class="ar" d="${d}"/>`).join('')}<path class="ok" d="M-14,0 L-4,10 L16,-12"/></svg><i class="sv-scan"></i></div><b>請輕觸感應區</b></div>`);
  const w=s.querySelector('.sv-fp'),ar=w.querySelectorAll('.ar'),ok=w.querySelector('.ok'),sc=w.querySelector('.sv-scan'),lb=w.querySelector('b');
  gsap.timeline({repeat:-1,repeatDelay:1}).call(()=>{lb.textContent='請輕觸感應區';w.classList.remove('done')}).set(ok,{drawSVG:'0%'}).set(ar,{opacity:1}).fromTo(ar,{drawSVG:'0%'},{drawSVG:'100%',duration:.7,stagger:.07,ease:'power1.inOut'}).call(()=>lb.textContent='掃描中…').fromTo(sc,{top:'0%',opacity:1},{top:'100%',duration:.8,ease:'power1.inOut',yoyo:true,repeat:1}).to(sc,{opacity:0,duration:.1}).call(()=>{w.classList.add('done');lb.textContent=x}).to(ar,{opacity:.15,duration:.3}).to(ok,{drawSVG:'100%',duration:.4,ease:'power2.out'},'<.1').to({},{duration:1.6})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx331` rules from `site/fx.css`

_No dedicated `.fx331` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #331
