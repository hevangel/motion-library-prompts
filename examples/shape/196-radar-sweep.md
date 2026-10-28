# 196 · 雷達掃描 — Radar Sweep

掃描扇形持續繞圈，掃過的位置亮起光點

- 元件 Component: 圖形・SVG (`shape`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 數字資訊、背景裝飾
- 風格／關鍵字 Style: 雷達 掃描 搜尋 定位 科技 地圖 Radar Scan Sweep Ping Search Tech SVG 圖形
- 標籤 Tag: SVG radar
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「雷達掃描（Radar Sweep）」動態效果：雷達畫面：幾圈同心圓與十字準線，一個半透明的扇形掃描區持續順時針繞圈（約 3 秒一圈），掃描線經過的位置會亮起光點並短暫放大，接著逐漸淡出，等下一圈掃過再亮。適合搜尋中、定位、科技風儀表板。（SVG + CSS：扇形 path 放在 g 中以中心旋轉；每個光點的 animation-delay 依照它的角度換算成掃描線抵達的時間）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx196">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「雷達掃描」.

### JavaScript — `FX[196]` from `site/fx.js`

```js
196(s){const B=[[40,.55],[115,.75],[200,.4],[290,.8],[335,.3]];s.insertAdjacentHTML('beforeend',`<svg class="rdr" viewBox="-50 -50 100 100"><circle r="44"/><circle r="30"/><circle r="16"/><path d="M-44,0H44M0,-44V44"/><g class="sw"><path d="M0,0 L0,-44 A44,44 0 0,1 31.1,-31.1 Z"/><path class="ed" d="M0,0 L31.1,-31.1"/><animateTransform attributeName="transform" type="rotate" from="0 0 0" to="360 0 0" dur="3s" repeatCount="indefinite"/></g>${B.map(([a,r])=>{const rad=(a-90)*Math.PI/180;return `<circle class="bp" cx="${(Math.cos(rad)*r*44).toFixed(1)}" cy="${(Math.sin(rad)*r*44).toFixed(1)}" r="2.2" style="animation-delay:${(((a-45+360)%360)/360*3).toFixed(2)}s"/>`}).join('')}</svg>`)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx196` rules from `site/fx.css`

_No dedicated `.fx196` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #196
