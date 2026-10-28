# 307 · Memory Match — 翻牌配對遊戲

Click two cards to flip them over; if they match they stay and bounce, if not they flip back

- Component: Cards · Groups (`card`)
- Timing: Switch
- Tech: CSS
- Uses: UI Interaction, App Interface
- Style / keywords: Card Flip Matching Memory Game Mini-game Interactive Memory Match Card Game Flip Pairs Cards Group
- Tag: JS + CSS
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-20

**AI prompt (English copy format):**

```text
"Memory Match (翻牌配對遊戲)" motion effect: A 4 × 2 card-flipping memory mini-game: all the cards start face down, and clicking one flips it in 3D to show the pattern on its front; after two cards are flipped, if the patterns are the same, both stay face up, their background turns into the accent color and they bounce; if they differ, after lingering about 0.8 seconds both flip back face down together; text below shows the matching progress, and after all pairs are matched successfully it shows celebratory text, shuffles and starts again. (CSS: cards use transform-style:preserve-3d, front and back faces use backface-visibility:hidden, and .on applies rotateY(180deg); JS manages the flipped cards and the match checking)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx307">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Memory Match".

### JavaScript — `FX[307]` from `site/fx.js`

```js
307(s,x,card){const E=['🌙','⭐','🍀','🌸'];const deck=[...E,...E].sort(()=>Math.random()-.5);const g=el('div','cg-mm');const cs=deck.map(e=>{const c=el('button','cg-mc');c.innerHTML='<i class="f">?</i><i class="b">'+e+'</i>';c.dataset.e=e;g.append(c);return c});const st=el('div','cg-ms');st.textContent='翻兩張找出一樣的';s.append(g,st);let open=[],lock=false,real=0,done=0;
  const flip=c=>{if(lock||c.classList.contains('on'))return;c.classList.add('on');open.push(c);if(open.length<2)return;lock=true;const [a,b]=open;open=[];
    if(a.dataset.e===b.dataset.e){done++;setTimeout(()=>{[a,b].forEach(z=>{z.classList.add('ok')});lock=false;st.textContent=done===4?'全部配對成功！🎉':'配對成功 '+done+' / 4';if(done===4)setTimeout(reset,1600)},400)}
    else setTimeout(()=>{a.classList.remove('on');b.classList.remove('on');lock=false},800)};
  const reset=()=>{done=0;st.textContent='翻兩張找出一樣的';cs.forEach(c=>c.classList.remove('on','ok'));setTimeout(()=>{const d=[...E,...E].sort(()=>Math.random()-.5);cs.forEach((c,i)=>{c.dataset.e=d[i];c.querySelector('.b').textContent=d[i]})},500)};
  cs.forEach(c=>c.onclick=()=>{real=Date.now();flip(c)});
  card._timers.push(setInterval(()=>{if(Date.now()-real<6000||lock)return;const cl=cs.filter(c=>!c.classList.contains('on'));if(!cl.length)return;if(open.length===1){const m=cl.find(c=>c.dataset.e===open[0].dataset.e);flip(Math.random()<.6&&m?m:cl[Math.floor(Math.random()*cl.length)])}else flip(cl[Math.floor(Math.random()*cl.length)])},700))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx307` rules from `site/fx.css`

_No dedicated `.fx307` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #307
