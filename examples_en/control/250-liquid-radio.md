# 250 · Liquid Radio — 水滴單選

When switching radio options, the selected dot stretches into a droplet, slides to the new option, then bounces back into a circle

- Component: Form · Controls (`control`)
- Timing: Switch
- Tech: GSAP
- Uses: UI Interaction
- Style / keywords: Radio radio Options Droplet Liquid Stretch Liquid Radio Button Gooey Morph Form Control
- Tag: GSAP elastic
- Example text: "Standard Shipping Express Delivery Store Pickup" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Liquid Radio (水滴單選)" motion effect: A set of vertically arranged radio options, where the selected dot is a separate solid small circle: when switching options, the small circle is first stretched into a vertically elongated droplet shape, slides in a straight line to the center of the new option's circle, and on arrival recovers into a circle with an elastic wobble, flowing over like a liquid; the selected outer ring changes style at the same time. (GSAP timeline: first scaleY 2.2 / scaleX 0.7, while tweening y to the new position with power3.inOut, finally scaleX/scaleY back to 1 using elastic.out(1.2,0.5); the native radio is hidden but keyboard operation is retained)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx250">`, preview text "Standard Shipping Express Delivery Store Pickup". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Liquid Radio".

### JavaScript — `FX[250]` from `site/fx.js`

```js
250(s,x,card){const ws=words(x).slice(0,3);const w=el('div','fm-rd');w.innerHTML='<i class="fm-dot"></i>';const ls=ws.map((t,i)=>{const l=el('label');l.innerHTML='<input type="radio" name="r'+Math.random().toString(36).slice(2)+'"><i></i><span></span>';l.querySelector('span').textContent=t;w.append(l);return l});
  const nm='fm'+Math.random().toString(36).slice(2);ls.forEach(l=>l.querySelector('input').name=nm);s.append(w);const dot=w.querySelector('.fm-dot');let cur=-1,real=0;
  const go=(i,instant)=>{if(i===cur)return;const r=ls[i].querySelector('i'),wr=w.getBoundingClientRect(),rr=r.getBoundingClientRect(),y=rr.top-wr.top+rr.height/2;ls[i].querySelector('input').checked=true;
    if(instant||cur<0)gsap.set(dot,{y,x:rr.left-wr.left+rr.width/2});else gsap.timeline().to(dot,{scaleY:2.2,scaleX:.7,duration:.15,ease:'power1.in'}).to(dot,{y,duration:.35,ease:'power3.inOut'},0).to(dot,{scaleY:1,scaleX:1,duration:.4,ease:'elastic.out(1.2,.5)'},.3);cur=i};
  ls.forEach((l,i)=>l.querySelector('input').addEventListener('change',()=>{real=Date.now();go(i)}));requestAnimationFrame(()=>go(0,true));
  card._timers.push(setInterval(()=>{if(Date.now()-real>5000)go((cur+1)%ls.length)},1400))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx250` rules from `site/fx.css`

_No dedicated `.fx250` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #250
