# 065 · 拉霸 — Slot Text

滾輪轉一轉停下來

- 元件 Component: 文字 (`text`)
- 時機 Timing: 切換
- 技術 Tech: CSS
- 情境 Uses: 數字資訊
- 風格／關鍵字 Style: 文字切換
- 標籤 Tag: 結果揭曉
- 範例文字 Example text: 「大吉利」（預覽底色：dark）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「拉霸（Slot Text）」動態效果：每個字放在拉霸滾輪窗格裡（窗格上下有內陰影），滾輪快速往上捲動許多隨機字，再由左到右依序減速停在結果字上（略帶回彈），停留後重轉。約 4 秒一輪。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx65">`, preview text 「大吉利」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「拉霸」.

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
