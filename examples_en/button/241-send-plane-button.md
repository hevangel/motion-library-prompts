# 241 · Send Plane Button — 紙飛機送出

Press send, and the paper plane flies away from the button; the text changes to "Sent" and then recovers

- Component: Button (`button`)
- Timing: Hover · Click, Switch
- Tech: GSAP
- Uses: UI Interaction, App Interface
- Style / keywords: Send Paper Plane Send Out Message Form Success Send Paper Plane Submit Button Success Button
- Tag: GSAP timeline
- Example text: "Send Message" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Send Plane Button (紙飛機送出)" motion effect: A send button with a paper plane icon on its left: when pressed, the button first gives a light press and rebound, the text fades out to the right, and the paper plane first pulls back to build momentum, then accelerates up and to the right, flying out of the button and disappearing; next the text changes to "Sent" and slides in from the left; after about 1 second the text changes back to the original content, and the paper plane flies back to its original position from the lower left. (GSAP timeline: button scale 0.94 to 1, text x and opacity, the paper plane uses keyframes going up and to the right on x/y/rotation accelerating with power2.in, then add() switches the text content; the button's overflow:hidden clips the plane as it flies out)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx241">`, preview text "Send Message". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Send Plane Button".

### JavaScript — `FX[241]` from `site/fx.js`

```js
241(s,x,card){const b=bxBtn('bx-sd',x);b.insertAdjacentHTML('afterbegin','<svg class="bx-pl" viewBox="0 0 24 24"><path d="M3 11l18-8-7 18-3-7z M11 14l10-11"/></svg>');s.append(b);const lb=b.querySelector('span'),pl=b.querySelector('.bx-pl');let busy=false;
  const go=()=>{if(busy)return;busy=true;const tl=gsap.timeline({onComplete:()=>busy=false});
    tl.to(b,{scale:.94,duration:.1}).to(b,{scale:1,duration:.3,ease:'back.out(3)'}).to(lb,{x:'1.2em',opacity:0,duration:.25},'<')
      .to(pl,{x:'-.3em',rotation:-15,duration:.2},'<').to(pl,{keyframes:[{x:'4em',y:'-1.4em',rotation:20,duration:.35,ease:'power2.in'},{opacity:0,duration:.05}]})
      .add(()=>lb.textContent='已送出').fromTo(lb,{x:'-1em',opacity:0},{x:0,opacity:1,duration:.3,ease:'back.out(2)'}).set(pl,{x:'-3em',y:'1em',rotation:0,opacity:0})
      .add(()=>{},'+=1.1').to(lb,{opacity:0,duration:.2}).add(()=>lb.textContent=x).to(lb,{opacity:1,duration:.2}).to(pl,{x:0,y:0,opacity:1,duration:.4,ease:'power3.out'},'<')};
  b.addEventListener('click',go);bxDemo(b,card,go,3600)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx241` rules from `site/fx.css`

_No dedicated `.fx241` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #241
