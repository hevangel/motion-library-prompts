# 066 · Odometer — 計數器

Numbers scroll upward and increase

- Component: Text (`text`)
- Timing: Switch
- Tech: CSS
- Uses: Numbers & Data
- Style / keywords: Text Switching
- Tag: Results·Numbers
- Example text: "Total" (stage background: dark, fixed text)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Odometer (計數器)" motion effect: For numbers such as 'Cumulative total: 12,480 people', each digit sits in a small cell, the numbers scrolling upward and incrementing like an odometer, with a slight rebound. It increases about once every 1 second.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx66">`, preview text "Total". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Odometer".

### JavaScript — `FX[66]` from `site/fx.js`

```js
66(s,x,card){const w=el('div','w');w.innerHTML=`<span class="lab">${x}</span>`;const reels=[];const N=5;for(let i=0;i<N;i++){if(i===2)w.insertAdjacentHTML('beforeend','<span class="cm">,</span>');const d=el('div','dg');const inner=el('div');inner.innerHTML=Array.from({length:10},(_,k)=>`<span>${k}</span>`).join('');d.append(inner);w.append(d);reels.push(inner)}w.insertAdjacentHTML('beforeend','<span class="lab" style="margin:0 0 0 1cqw">人</span>');s.append(w);let v=12400;
  const set=()=>{const str=String(v).padStart(N,'0');reels.forEach((r,i)=>r.style.transform=`translateY(${-+str[i]*11}cqw)`)};set();card._timers.push(setInterval(()=>{v+=Math.floor(rnd(3,40));if(v>99000)v=12400;set()},1100))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx66` rules from `site/fx.css`

```css
.fx66 .w{display:flex;align-items:center;gap:.8cqw;font-weight:900}
.fx66 .lab{font-size:6cqw;margin-right:1cqw}
.fx66 .dg{width:7.4cqw;height:11cqw;overflow:hidden;background:#2b2b2b;border-radius:.8cqw}
.fx66 .dg div{transition:transform .7s cubic-bezier(.3,1.3,.5,1)}
.fx66 .dg span{display:grid;place-items:center;height:11cqw;color:#fff;font-size:8.5cqw}
.fx66 .cm{font-size:8cqw}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #66
