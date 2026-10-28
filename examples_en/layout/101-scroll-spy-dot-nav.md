# 101 · Scroll Spy Dot Nav — 捲動導覽點

Side navigation dots light up with scrolling; click one to jump to that section

- Component: Layout · Pages (`layout`)
- Timing: Scroll-triggered, Hover · Click
- Tech: GSAP
- Uses: UI Interaction, Scroll Effects
- Style / keywords: Scroll Navigation Side Navigation Dots Anchor Navigation Page Progress Navigation Scroll Spy Navigation Dot Navigation
- Tag: ScrollTrigger
- Example text: "About Works Services Contact" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Scroll Spy Dot Nav (捲動導覽點)" motion effect: Scroll navigation / side navigation dots (Scroll Spy / Dot Navigation, also called anchor navigation or page progress navigation): a row of small dots is fixed on the right side of the page, each dot corresponding to one section; whichever section is scrolled to, its corresponding dot enlarges and fills with the accent color, with a pill label showing that section's name floating out beside it; between the dots there is a thin track, and the progress bar inside the track grows downward in proportion to the whole page's scrolling; clicking any dot smoothly scrolls to that section, and hovering the mouse over a dot also shows its name. The sections alternate between light and dark background shades. (GSAP: one ScrollTrigger per section, start "top center", end "bottom center", onToggle toggles active; the progress bar uses scaleY with scrub:true; clicking uses gsap.to(scroller,{scrollTop}) or ScrollToPlugin)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx101">`, preview text "About Works Services Contact". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Scroll Spy Dot Nav".

### JavaScript — `FX[101]` from `site/fx.js`

```js
101(s,x){const sc=el('div','scr nopad');const nav=el('nav','dnav');const fill=el('i');const track=el('div','dtrack');track.append(fill);nav.append(track);s.append(sc,nav);
  const dots=[];words(x).slice(0,6).forEach((n,i)=>{const sec=el('section','dsec');sec.innerHTML=`<small>0${i+1}</small><b></b>`;sec.querySelector('b').textContent=n;sc.append(sec);
    const d=el('button','dd');d.setAttribute('aria-label',n);const lab=el('span');lab.textContent=n;d.append(lab);nav.append(d);dots.push(d);
    d.onclick=()=>gsap.to(sc,{scrollTop:sec.offsetTop,duration:.8,ease:'power3.inOut',overwrite:true});
    ScrollTrigger.create({trigger:sec,scroller:sc,start:'top center',end:'bottom center',onToggle:t=>{if(t.isActive)dots.forEach((o,k)=>o.classList.toggle('on',k===i))}})});
  gsap.fromTo(fill,{scaleY:0},{scaleY:1,ease:'none',scrollTrigger:{scroller:sc,start:0,end:'max',scrub:true}});autoScroll(sc,nav)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx101` rules from `site/fx.css`

_No dedicated `.fx101` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #101
