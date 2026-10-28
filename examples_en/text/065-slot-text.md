# 065 · Slot Text — 拉霸

Reels spin and come to a stop

- Component: Text (`text`)
- Timing: Switch
- Tech: CSS
- Uses: Numbers & Data
- Style / keywords: Text Switching
- Tag: Result Reveal
- Example text: "Great Fortune" (stage background: dark)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Slot Text (拉霸)" motion effect: Each character sits in a slot-machine reel window (the windows have inner shadows at the top and bottom); the reels rapidly scroll upward through many random characters, then slow down and stop in sequence from left to right on the result characters (with a slight rebound); after lingering, they spin again. About 4 seconds per cycle.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx65">`, preview text "Great Fortune". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Slot Text".

### JavaScript — `FX[65]` from `site/fx.js`

```js
65(s,x,card){const w=el('div','w');s.append(w);const tg=chars(x).slice(0,4);const pool=[...'大吉利福壽財中凶7★♥'];const spin=()=>{w.innerHTML='';tg.forEach((t,i)=>{const r=el('div','reel');const st=el('div','strip');const n=18+i*6;for(let k=0;k<n;k++){const e=el('span');e.textContent=k===n-1?t:pool[Math.floor(Math.random()*pool.length)];st.append(e)}r.append(st);w.append(r);st.animate([{transform:'translateY(0)'},{transform:`translateY(calc(${-(n-1)} * 20cqw))`}],{duration:1400+i*500,easing:'cubic-bezier(.2,.75,.25,1.04)',fill:'forwards'})})};spin();card._timers.push(setInterval(spin,4200))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx65` rules from `site/fx.css`

```css
.fx65 .w{display:flex;gap:2cqw}
.fx65 .reel{width:17cqw;height:20cqw;overflow:hidden;background:#2b2b2b;border-radius:1.6cqw;box-shadow:inset 0 2cqw 2cqw -1cqw #000a,inset 0 -2cqw 2cqw -1cqw #000a}
.fx65 .strip{display:flex;flex-direction:column}
.fx65 .strip span{height:20cqw;display:grid;place-items:center;font-weight:900;font-size:13cqw;color:var(--a)}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #65
