# 100 · Velocity Marquee — 滾輪加速跑馬燈

The wheel or dragging speeds up the marquee and tilts it

- Component: Background · Ambience (`bg`)
- Timing: Scroll-triggered, Drag Gesture
- Tech: GSAP
- Uses: Background Decoration, UI Interaction
- Style / keywords: 
- Tag: Observer
- Example text: "Scroll to Speed Up" (stage background: acc)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Velocity Marquee (滾輪加速跑馬燈)" motion effect: Two lines of infinite marquee (one solid, one hollow outline, running in opposite directions); when the user scrolls the wheel or drags, they speed up and tilt according to the direction, and after stopping they slowly return to their original speed. (GSAP: Observer obtains velocityY, adjusting tween.timeScale and skewX)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage acc fx100">`, preview text "Scroll to Speed Up". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Velocity Marquee".

### JavaScript — `FX[100]` from `site/fx.js`

```js
100(s,x,card){const l=layer(s);l.classList.add('vm');const U=rep(x+' ✦ ',6);const inns=[0,1].map(()=>{const r=el('div','vr');const i=el('div','vi');i.textContent=U+U;r.append(i);l.append(r);return i});
  const tws=inns.map((e,i)=>gsap.fromTo(e,{xPercent:i?-50:0},{xPercent:i?0:-50,duration:16,ease:'none',repeat:-1}));let st,busy=0;
  const boost=v=>{v=gsap.utils.clamp(-8,8,v);tws.forEach(tw=>gsap.to(tw,{timeScale:Math.max(1,Math.abs(v)),duration:.25,overwrite:true}));gsap.to(inns,{skewX:-v*2,duration:.25,overwrite:true});clearTimeout(st);
    st=setTimeout(()=>{tws.forEach(tw=>gsap.to(tw,{timeScale:1,duration:1.4,overwrite:true}));gsap.to(inns,{skewX:0,duration:1.2,ease:'elastic.out(1,.5)',overwrite:true})},180)};
  const ob=Observer.create({target:l,type:'wheel,touch,pointer',onChangeY:self=>{busy=Date.now();boost(self.velocityY/150)}});card._kill.push(()=>ob.kill());
  card._timers.push(setInterval(()=>{if(Date.now()-busy>3000)boost(gsap.utils.random([7,-6,8]))},3200))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx100` rules from `site/fx.css`

_No dedicated `.fx100` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #100
