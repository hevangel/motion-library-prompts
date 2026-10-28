# 070 · 故障切片 — Glitch Slices

大字被切成好幾條錯開

- 元件 Component: 文字 (`text`)
- 時機 Timing: 退場
- 技術 Tech: CSS
- 情境 Uses: 強調重點、轉場切換
- 風格／關鍵字 Style: 消散退場
- 標籤 Tag: 衝擊・MV
- 範例文字 Example text: 「故障」（預覽底色：acc）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「故障切片（Glitch Slices）」動態效果：大字平時靜止，偶爾突然被切成 6 條橫向切片，各條左右隨機錯開並帶色差錯位（RGB split），閃一下又恢復，頻率不規則。故障約每 0.1 秒閃動，衝擊 MV 感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage acc fx70">`, preview text 「故障」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「故障切片」.

### JavaScript — `FX[70]` from `site/fx.js`

```js
70(s,x,card){const w=el('div','w');const base=T(x,22);w.append(base);const sl=[];for(let i=0;i<6;i++){const e=T(x,22);e.classList.add('sl');e.style.clipPath=`inset(${i*100/6}% 0 ${100-(i+1)*100/6}% 0)`;w.append(e);sl.push(e)}s.append(w);
  card._timers.push(setInterval(()=>{const g=Math.random()<.32;base.style.opacity=g?0:1;sl.forEach(e=>{e.style.transform=g?`translateX(${rnd(-9,9)}cqw)`:'none';e.style.color=g&&Math.random()<.4?'#fff':'#111';e.style.textShadow=g?'.8cqw 0 #3cf,-.8cqw 0 #f24':'none';e.style.opacity=g?1:0})},110))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx70` rules from `site/fx.css`

```css
.fx70 .w{position:relative}
.fx70 .t{color:#111}
.fx70 .sl{position:absolute;left:0;top:0;transition:none}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #70
