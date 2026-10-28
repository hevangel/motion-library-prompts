# 137 · 流程連線流動 — Flowing Connectors

節點之間的虛線持續流動，小圓點沿線傳遞

- 元件 Component: 圖形・SVG (`shape`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 數字資訊、背景裝飾
- 風格／關鍵字 Style: 流程圖 架構圖 節點 連線 虛線 流動 資料流 Flow Diagram Connector Dashed Line Data Flow
- 標籤 Tag: stroke-dashoffset
- 範例文字 Example text: 「使用者 前端 後端 資料庫」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「流程連線流動（Flowing Connectors）」動態效果：流程圖或系統架構圖中，各節點（圓形＋下方標籤）之間用平滑曲線連接，連線是虛線且虛線持續朝資料流動的方向移動，另外有小圓點沿著每條連線來回傳遞，表達資料正在流動；速度平穩、循環不停。（CSS：path 設 stroke-dasharray，用 keyframes 持續改變 stroke-dashoffset；小圓點用 SVG animateMotion 或 CSS offset-path 沿同一條路徑移動，各條錯開起始時間）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx137">`, preview text 「使用者 前端 後端 資料庫」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「流程連線流動」.

### JavaScript — `FX[137]` from `site/fx.js`

```js
137(s,x){const ws=words(x);const N=[[25,45],[80,20],[80,70],[135,45]];const P=['M34,45 C52,45 56,20 71,20','M34,45 C52,45 56,70 71,70','M89,20 C104,20 108,45 126,45','M89,70 C104,70 108,45 126,45'];
  s.insertAdjacentHTML('beforeend',`<svg class="flow" viewBox="0 0 160 90">${P.map((d,i)=>`<path d="${d}"/><circle class="mv" r="1.8"><animateMotion dur="2.2s" begin="${-i*.55}s" repeatCount="indefinite" path="${d}"/></circle>`).join('')}${N.map(([cx,cy])=>`<circle class="nd" cx="${cx}" cy="${cy}" r="9"/>`).join('')}${N.map(([cx,cy],i)=>`<text x="${cx}" y="${cy+17}"></text>`).join('')}</svg>`);
  s.querySelectorAll('.flow text').forEach((t,i)=>t.textContent=ws[i%ws.length])}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx137` rules from `site/fx.css`

_No dedicated `.fx137` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #137
