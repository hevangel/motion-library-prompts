# 212 · Focus Carousel — 焦點卡片輪播

The middle card is enlarged and clear, the sides are smaller and faded, switch left and right

- Component: Cards · Groups (`card`)
- Timing: Switch, Loop · Idle
- Tech: CSS
- Uses: UI Interaction, Headline · Hero
- Style / keywords: Carousel carousel slider Focus Center Enlarge coverflow Works Carousel Image Cards Group
- Tag: CSS transition
- Example text: "Brand Website Illustration Packaging Photography" (stage background: dark)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Focus Carousel (焦點卡片輪播)" motion effect: A set of cards arranged horizontally as a carousel; the current card is centered, largest, and fully clear, the adjacent cards on the left and right shrink to about 82% and become semi-transparent, and cards further out are smaller and fainter still; when switching, all cards slide smoothly together to their new positions and change size (about 0.6 seconds, ease-in-out); below are left and right arrows and dot indicators (the current dot is elongated); it can autoplay, and clicking a side card can switch directly to it. (CSS: each card sets translateX, scale, opacity and z-index according to its distance from the current index, with a transition; when out of range, take the nearest looping direction)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx212">`, preview text "Brand Website Illustration Packaging Photography". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Focus Carousel".

### JavaScript — `FX[212]` from `site/fx.js`

```js
212(s,x,card){const ws=words(x);const w=el('div','kd-car');const cs=[...Array(5)].map((_,i)=>{const c=el('div','kd-cc');c.style.background=`linear-gradient(150deg,${GC[i%5]},${GC[(i+2)%5]})`;c.innerHTML='<small>0'+(i+1)+'</small><b></b>';c.querySelector('b').textContent=ws[i%ws.length];w.append(c);return c});
  const nav=el('div','kd-nav');nav.innerHTML='<button aria-label="上一張">‹</button><span></span><button aria-label="下一張">›</button>';const dots=nav.querySelector('span');cs.forEach(()=>dots.append(el('i')));s.append(w,nav);let cur=0,real=0;
  const lay=()=>cs.forEach((c,i)=>{let o=i-cur;if(o>2)o-=5;if(o<-2)o+=5;c.style.transform=`translateX(${o*58}%) scale(${1-Math.abs(o)*.18})`;c.style.zIndex=10-Math.abs(o);c.style.opacity=Math.abs(o)>1?.25:Math.abs(o)?.6:1;dots.children[i].classList.toggle('on',i===cur)});
  const go=d=>{cur=(cur+d+5)%5;lay()};const [pv,nx]=nav.querySelectorAll('button');pv.onclick=()=>{real=Date.now();go(-1)};nx.onclick=()=>{real=Date.now();go(1)};cs.forEach((c,i)=>c.onclick=()=>{real=Date.now();cur=i;lay()});lay();
  card._timers.push(setInterval(()=>{if(Date.now()-real>4000)go(1)},1700))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx212` rules from `site/fx.css`

_No dedicated `.fx212` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #212
