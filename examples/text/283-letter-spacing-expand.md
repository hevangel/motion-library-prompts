# 283 · 字距展開 — Letter Spacing Expand

滑過時字母間距慢慢拉開、字重變粗，像深呼吸一樣

- 元件 Component: 文字 (`text`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動、強調重點
- 風格／關鍵字 Style: 字距 拉開 字重 呼吸 選單 導覽 Letter Spacing Tracking Expand Weight Hover Menu hover 懸停 滑過
- 標籤 Tag: letter-spacing
- 範例文字 Example text: 「ABOUT WORK CONTACT」（預覽底色：dark）
- 收錄日期 Added: 2026-10-20

**AI 提示詞（網站複製格式）:**

```text
「字距展開（Letter Spacing Expand）」動態效果：導覽列或大型選單的文字：滑鼠滑過某個項目時，字母間距平滑地從 0 拉開到約 0.35em，字重從細變粗、文字變得更清楚，像深呼吸一樣展開；滑開時收回。約 0.5 秒、減速曲線。（CSS：transition letter-spacing 與 font-weight（使用可變字體效果最平順），:hover 改變數值）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx283">`, preview text 「ABOUT WORK CONTACT」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「字距展開」.

### JavaScript — `FX[283]` from `site/fx.js`

```js
283(s,x,card){const ws=words(x).slice(0,3);const w=el('div','ho-ls');const its=ws.map(t=>{const d=el('div','ho-li');d.textContent=t;w.append(d);return d});s.append(w);autoHover(w,its,card,1100)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx283` rules from `site/fx.css`

_No dedicated `.fx283` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #283
