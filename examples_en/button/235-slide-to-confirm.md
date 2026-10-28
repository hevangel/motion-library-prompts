# 235 · Slide to Confirm — 滑動確認

Drag the round knob all the way to the end to confirm; if it does not reach the end it springs back, and the text has a shimmer hint

- Component: Button (`button`)
- Timing: Drag Gesture
- Tech: GSAP
- Uses: UI Interaction, App Interface
- Style / keywords: Slide Confirm Unlock Payment Drag Slide To Unlock Confirm Swipe Button Payment Button
- Tag: Draggable
- Example text: "Slide to Pay" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Slide to Confirm (滑動確認)" motion effect: A capsule-shaped slide track, with a round handle on the left (with a right arrow inside), and a beam of light sweeps across the hint text in the middle from left to right; when the user drags the handle, the track the handle has passed is filled and the hint text gradually fades out; only releasing near the far right counts as confirmation - the whole track fills and the text becomes "Done ✓"; if released before reaching the end, the handle springs back to the start with elasticity. (GSAP Draggable type:"x", with bounds limiting it to the track, onDrag updates the filled width, onRelease checks whether it exceeds 85%; the shimmer uses background-clip:text with a moving gradient)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx235">`, preview text "Slide to Pay". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Slide to Confirm".

### JavaScript — `FX[235]` from `site/fx.js`

```js
235(s,x,card){const w=el('div','bx-sl');w.innerHTML='<span class="bx-st"></span><i class="bx-sf"></i><b class="bx-kn">'+'<svg viewBox="0 0 24 24"><path d="M5 12h13M13 6l6 6-6 6"/></svg></b>';w.querySelector('.bx-st').textContent=x;w.style.fontSize=Math.min(4.2,36/chars(x).length)+'cqw';s.append(w);
  const kn=w.querySelector('.bx-kn'),fill=w.querySelector('.bx-sf'),st=w.querySelector('.bx-st');let idle=0,done=false;const max=()=>w.offsetWidth-kn.offsetWidth-w.offsetHeight*.16;
  const upd=v=>{fill.style.width=v+kn.offsetWidth+'px';st.style.opacity=1-v/max()*1.4};
  const finish=()=>{done=true;w.classList.add('ok');st.textContent='完成 ✓';st.style.opacity=1;setTimeout(()=>{w.classList.remove('ok');st.textContent=x;gsap.to(kn,{x:0,duration:.5,ease:'power3.out',onUpdate:()=>upd(gsap.getProperty(kn,'x')),onComplete:()=>done=false})},1400)};
  const dr=Draggable.create(kn,{type:'x',bounds:{minX:0,maxX:max()},onPress(){idle=Date.now()+5000;if(!done)gsap.killTweensOf(kn);this.applyBounds({minX:0,maxX:max()})},onDrag(){upd(this.x)},onRelease(){if(this.x>max()*.85){gsap.to(kn,{x:max(),duration:.15,onUpdate:()=>upd(gsap.getProperty(kn,'x')),onComplete:finish})}else gsap.to(kn,{x:0,duration:.45,ease:'back.out(2)',onUpdate:()=>upd(gsap.getProperty(kn,'x'))})}})[0];card._kill.push(()=>dr.kill());
  card._timers.push(setInterval(()=>{if(done||Date.now()<idle)return;gsap.to(kn,{x:max(),duration:.9,ease:'power2.inOut',onUpdate:()=>upd(gsap.getProperty(kn,'x')),onComplete:finish})},3600))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx235` rules from `site/fx.css`

_No dedicated `.fx235` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #235
