# 066 · 計數器 — Odometer

數字滾動往上加

- 元件 Component: 文字 (`text`)
- 時機 Timing: 切換
- 技術 Tech: CSS
- 情境 Uses: 數字資訊
- 風格／關鍵字 Style: 文字切換
- 標籤 Tag: 成績・數字
- 範例文字 Example text: 「累計」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「計數器（Odometer）」動態效果：「累計 12,480 人」這類數字，每位數放在小格子中，數字像里程表一樣往上滾動遞增，帶一點回彈。約每 1 秒增加一次。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx66">`, preview text 「累計」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「計數器」.

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
