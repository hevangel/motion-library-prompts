# 162 · 連結底線滑入 — Underline Slide Link

滑過連結時底線從左長出，離開時往右收走

- 元件 Component: 文字 (`text`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動
- 風格／關鍵字 Style: 連結 底線 選單 導覽 link underline nav menu hover 懸停 滑鼠移入 滑過 互動
- 標籤 Tag: CSS hover
- 範例文字 Example text: 「首頁 作品 關於 聯絡」（預覽底色：dark）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「連結底線滑入（Underline Slide Link）」動態效果：導覽列的文字連結，滑鼠移入時一條細底線從左往右長出，滑鼠移出時底線繼續往右收走（不是原路縮回），像一道光掃過；約 0.45 秒、緩入緩出。（CSS：::after 做底線，transform:scaleX(0)；hover 時 scaleX(1) 且 transform-origin:left，非 hover 時 transform-origin:right，transition cubic-bezier(.7,0,.2,1)）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx162">`, preview text 「首頁 作品 關於 聯絡」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「連結底線滑入」.

### JavaScript — `FX[162]` from `site/fx.js`

```js
162(s,x,card){const n=el('nav','ul2');const its=words(x).slice(0,5).map(v=>{const a=el('span','lk2');a.textContent=v;n.append(a);return a});s.append(n);autoHover(n,its,card)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx162` rules from `site/fx.css`

_No dedicated `.fx162` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #162
