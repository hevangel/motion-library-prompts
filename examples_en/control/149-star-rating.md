# 149 · Star Rating — 星星評分

When a rating is selected, the stars light up in sequence from left to right and pop

- Component: Form · Controls (`control`)
- Timing: Hover · Click
- Tech: CSS
- Uses: App Interface, UI Interaction
- Style / keywords: Rating Stars Review Feedback Rating Stars Review Feedback App Mobile Mobile Device Micro-interaction Mobile App Micro-interaction
- Tag: Rating
- Example text: "Rate this experience" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Star Rating (星星評分)" motion effect: Five hollow stars: when the user taps star N, stars 1 through N fill in from left to right in sequence and each pops larger from small (about 0.08 seconds between each), while the rest stay hollow; matching text feedback appears below in sync (for example 'Very good' or 'Amazing!'). When fewer stars are selected, the extra stars turn hollow again. (CSS: toggle .on for the fill color and .pop for the pop keyframes, staggered by index using setTimeout or transition-delay; each star is a button with an aria-label)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx149">`, preview text "Rate this experience". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Star Rating".

### JavaScript — `FX[149]` from `site/fx.js`

```js
149(s,x,card){const c=el('div','rtc');const w=el('div','rtw');const lb=el('div','rtl');lb.textContent=x;const rs=el('div','rts');c.append(w,lb,rs);s.append(c);let real=0;const T2=['','很差','普通','不錯','很好','超讚！'];
  const st=[...Array(5)].map((_,i)=>{const b=el('button','star');b.setAttribute('aria-label',(i+1)+' 顆星');b.innerHTML='<svg viewBox="0 0 24 24"><path d="M12 2.8l2.8 5.8 6.3.9-4.6 4.4 1.1 6.3L12 17.3l-5.6 2.9 1.1-6.3L2.9 9.5l6.3-.9z"/></svg>';b.onclick=()=>{real=Date.now();rate(i+1)};w.append(b);return b});
  let gen=0;const rate=n=>{const g=++gen;st.forEach((b,k)=>{b.classList.remove('pop');if(k<n)setTimeout(()=>{if(g===gen)b.classList.add('on','pop')},k*80);else b.classList.remove('on')});rs.textContent=T2[n]};
  const demo=()=>{if(Date.now()-real<4000)return;rate(0);setTimeout(()=>{if(Date.now()-real>=4000)rate(3+Math.floor(Math.random()*3))},500)};demo();card._timers.push(setInterval(demo,2600))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx149` rules from `site/fx.css`

_No dedicated `.fx149` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #149
