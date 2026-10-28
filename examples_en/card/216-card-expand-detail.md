# 216 · Card Expand Detail — 卡片展開詳情

Clicking a card smoothly enlarges it into a detail panel while the other cards fade out

- Component: Cards · Groups (`card`)
- Timing: Switch
- Tech: GSAP
- Uses: UI Interaction, Transitions
- Style / keywords: Cards Expand Details Enlarge Shared Element shared element transition Expand Detail Flip Cards Group
- Tag: Flip
- Example text: "Work 1 Work 2 Work 3 Work 4" (stage background: dark)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Card Expand Detail (卡片展開詳情)" motion effect: A row of work cards; when one is clicked, it smoothly enlarges from its original position and size into a detail panel that fills the whole area (large image on the left, title and description on the right), while the other cards fade out at the same time; the text inside the detail fades in in sequence around the completion of the enlargement; clicking again shrinks it back to its original position and the other cards fade back in. About 0.6 seconds, ease-in-out. (GSAP Flip: use Flip.getState to record all cards, then toggle the enlarged card's class (changing it to absolute positioning that fills the container with a new layout), then Flip.from to tween, with nested:true so inner elements transform along with it)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx216">`, preview text "Work 1 Work 2 Work 3 Work 4". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Card Expand Detail".

### JavaScript — `FX[216]` from `site/fx.js`

```js
216(s,x,card){const ws=words(x);const g=el('div','kd-xg');const cs=[...Array(4)].map((_,i)=>{const c=el('div','kd-xc');c.innerHTML='<i class="kd-xi"></i><b></b><div class="kd-xd"><em></em><em></em><em class="s"></em></div>';c.querySelector('.kd-xi').style.background=`linear-gradient(140deg,${GC[i%5]},${GC[(i+2)%5]})`;c.querySelector('b').textContent=ws[i%ws.length];g.append(c);return c});s.append(g);let open=null,real=0,k=0;
  const tog=c=>{const st=Flip.getState(cs);if(open){open.classList.remove('big');g.classList.remove('has');open=open===c?null:c}else open=c;if(open){open.classList.add('big');g.classList.add('has')}Flip.from(st,{duration:.6,ease:'power3.inOut',absolute:true,nested:true});if(open)gsap.fromTo(open.querySelectorAll('.kd-xd em'),{opacity:0,y:8},{opacity:1,y:0,stagger:.06,delay:.35,duration:.35})};
  cs.forEach(c=>c.onclick=()=>{real=Date.now();tog(c)});card._timers.push(setInterval(()=>{if(Date.now()-real<4000)return;tog(open?open:cs[k++%4])},1600))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx216` rules from `site/fx.css`

_No dedicated `.fx216` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #216
