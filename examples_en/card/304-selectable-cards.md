# 304 · Selectable Cards — 多選卡片

When you click a card to select it, an outline and a checkmark appear, and an action bar reading "N selected" pops up at the bottom

- Component: Cards · Groups (`card`)
- Timing: Switch
- Tech: CSS
- Uses: UI Interaction, App Interface
- Style / keywords: Select Multi-select Check Cards Action Bar Selectable Cards Multi Select Checkbox Action Bar Cards Group
- Tag: JS + CSS
- Example text: "Seaside Mountains Night Sky Afternoon" (stage background: dark)
- Added: 2026-10-20

**AI prompt (English copy format):**

```text
"Selectable Cards (多選卡片)" motion effect: A row of multi-selectable image cards: when you click a card, an accent-colored outline appears around the card and it shrinks slightly, the image enlarges slightly inside the frame, and the circular checkbox in the top-right corner fills in and draws a checkmark (with a bounce-back); as long as anything is selected, a capsule-shaped action bar pops up from the bottom of the screen, showing "N selected" (the number rolls up and down when it changes) and a "Next →" button; when everything is deselected, the action bar slides back and hides. (JS toggles aria-pressed, CSS changes the outline, scale and the checkmark's stroke-dashoffset based on [aria-pressed=true]; the action bar uses translateY and opacity transitions)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx304">`, preview text "Seaside Mountains Night Sky Afternoon". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Selectable Cards".

### JavaScript — `FX[304]` from `site/fx.js`

```js
304(s,x,card){const ws=words(x);const w=el('div','cg-sw');w.innerHTML='<div class="cg-sg"></div><div class="cg-bar"><b>已選 <span>0</span> 項</b><button>下一步 →</button></div>';const sg=w.querySelector('.cg-sg'),bar=w.querySelector('.cg-bar'),cnt=bar.querySelector('span');
  const cs=[0,1,2,3].map(i=>{const c=el('button','cg-sc');c.setAttribute('aria-pressed','false');c.innerHTML=mdImg(i)+'<i class="cg-ck"><svg viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7"/></svg></i><b></b>';c.querySelector('b').textContent=ws[i%ws.length];c.onclick=()=>{real=Date.now();tog(c)};sg.append(c);return c});s.append(w);let real=0;
  const tog=c=>{const on=c.getAttribute('aria-pressed')!=='true';c.setAttribute('aria-pressed',on);const n=cs.filter(x=>x.getAttribute('aria-pressed')==='true').length;cnt.textContent=n;bar.classList.toggle('on',n>0);gsap.fromTo(cnt,{y:on?'-60%':'60%',opacity:0},{y:0,opacity:1,duration:.3,ease:'back.out(3)'})};
  card._timers.push(setInterval(()=>{if(Date.now()-real<5000)return;tog(cs[Math.floor(Math.random()*4)])},1100))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx304` rules from `site/fx.css`

_No dedicated `.fx304` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #304
