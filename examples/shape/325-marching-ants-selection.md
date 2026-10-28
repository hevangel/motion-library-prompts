# 325 · 選取框螞蟻線 — Marching Ants Selection

虛線選取框的線條持續流動，四角有控制點，框的大小改變時尺寸數字即時更新

- 元件 Component: 圖形・SVG (`shape`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 介面互動、強調重點
- 風格／關鍵字 Style: 選取框 虛線 螞蟻線 控制點 設計工具 Figma Marching Ants Selection Box Handles 圖形 SVG
- 標籤 Tag: stroke-dashoffset
- 範例文字 Example text: 「設計工具」（預覽底色：dark）
- 收錄日期 Added: 2026-10-21

**AI 提示詞（網站複製格式）:**

```text
「選取框螞蟻線（Marching Ants Selection）」動態效果：像設計工具裡的選取框：一個虛線矩形框住內容，虛線持續往同一個方向流動（俗稱螞蟻線），四個角落有方形控制點；選取框的大小在兩種尺寸之間平滑變化，下方的尺寸標籤（寬 × 高）跟著即時更新數字。（SVG rect：stroke-dasharray 6 5，keyframes 讓 stroke-dashoffset 從 0 到 −11 無限循環；框的 width/height 用 CSS keyframes 改變；JS 定時讀取尺寸更新標籤）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx325">`, preview text 「設計工具」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「選取框螞蟻線」.

### JavaScript — `FX[325]` from `site/fx.js`

```js
325(s,x,card){const w=el('div','sv-mq');w.innerHTML='<div class="sv-sel"><svg><rect x="1" y="1" width="100%" height="100%" rx="2"/></svg>'+['tl','tr','bl','br'].map(k=>`<i class="${k}"></i>`).join('')+'<span class="sv-dim"></span></div><b class="sv-mt"></b>';w.querySelector('.sv-mt').textContent=x;s.append(w);
  const sel=w.querySelector('.sv-sel'),dim=w.querySelector('.sv-dim');const upd=()=>{dim.textContent=Math.round(sel.offsetWidth*3)+' × '+Math.round(sel.offsetHeight*3)};card._timers.push(setInterval(upd,90));upd()}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx325` rules from `site/fx.css`

_No dedicated `.fx325` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #325
