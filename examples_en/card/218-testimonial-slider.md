# 218 · Testimonial Slider — 評論輪播

The quote fades out and moves up to switch to the next one, avatars switch along with it, and a progress bar keeps time

- Component: Cards · Groups (`card`)
- Timing: Switch, Loop · Idle
- Tech: GSAP
- Uses: UI Interaction, Numbers & Data
- Style / keywords: Testimonials Recommendations Client Testimonials Carousel Quote Testimonial Review Quote Slider Carousel Cards Group
- Tag: GSAP
- Example text: "Ms. Wang Mr. Chen Designer Lin" (stage background: dark)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Testimonial Slider (評論輪播)" motion effect: A client testimonial carousel: in the center is a large quote and attribution, with a row of circular avatars and a progress bar below; about every 2.6 seconds, the current quote fades out upward and the next one fades in and slides up from below, the corresponding avatar enlarges and gains a ring while the other avatars shrink and fade, and the progress bar restarts filling from 0 to keep time; clicking an avatar switches directly to that testimonial. (GSAP: tween the y and opacity of the old and new quotes separately; the progress bar goes scaleX 0 to 1 with ease none, with a duration equal to the auto-switch interval)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx218">`, preview text "Ms. Wang Mr. Chen Designer Lin". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Testimonial Slider".

### JavaScript — `FX[218]` from `site/fx.js`

```js
218(s,x,card){const Q=['用了之後，整個團隊的溝通效率都提升了。','介面直覺又好看，客戶一看就懂。','終於找到一個不用教就會用的工具！'];const ws=words(x);const w=el('div','kd-ts');w.innerHTML='<div class="kd-q"></div><div class="kd-av"></div><div class="kd-pb"><i></i></div>';const q=w.querySelector('.kd-q'),av=w.querySelector('.kd-av'),pb=w.querySelector('.kd-pb i');
  const as=Q.map((_,i)=>{const a=el('button','kd-a');a.style.background=GC[i+1];a.setAttribute('aria-label',ws[i%ws.length]);av.append(a);return a});s.append(w);let cur=-1,real=0;
  const go=i=>{cur=i;const old=q.firstChild;const n=el('div','kd-qi');n.innerHTML='<p></p><b></b>';n.querySelector('p').textContent='「'+Q[i]+'」';n.querySelector('b').textContent='— '+ws[i%ws.length];q.append(n);if(old)gsap.to(old,{y:-14,opacity:0,duration:.35,onComplete:()=>old.remove()});gsap.fromTo(n,{y:14,opacity:0},{y:0,opacity:1,duration:.5,delay:.15,ease:'power3.out'});as.forEach((a,j)=>a.classList.toggle('on',j===i));gsap.fromTo(pb,{scaleX:0},{scaleX:1,duration:2.6,ease:'none',overwrite:true})};
  as.forEach((a,i)=>a.onclick=()=>{real=Date.now();go(i)});go(0);card._timers.push(setInterval(()=>{if(Date.now()-real>4000)go((cur+1)%Q.length)},2600))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx218` rules from `site/fx.css`

_No dedicated `.fx218` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #218
