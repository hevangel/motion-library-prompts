# 110 · 旋轉光邊按鈕 — Rotating Gradient Border

按鈕外框的漸層光持續繞圈旋轉，帶柔和外光

- 元件 Component: 按鈕 (`button`)
- 時機 Timing: 循環待機、懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動、強調重點
- 風格／關鍵字 Style: 按鈕 邊框 漸層 旋轉 發光 Glow Border Conic Gradient Animated Border Button
- 標籤 Tag: @property
- 範例文字 Example text: 「開始使用」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「旋轉光邊按鈕（Rotating Gradient Border）」動態效果：膠囊按鈕的外框是一圈多色漸層光，漸層持續沿著外框繞圈旋轉（約 3 秒一圈），外框後方帶一層模糊的柔光；按鈕內部是實心底與文字；滑鼠移上去時旋轉加快。（CSS：@property 註冊 --ang 角度變數，背景用 conic-gradient(from var(--ang))，keyframes 把 --ang 轉到 360deg；內層 span 蓋住中間只露出外框；::before 複製背景並 blur 做外光）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx110">`, preview text 「開始使用」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「旋轉光邊按鈕」.

### JavaScript — `FX[110]` from `site/fx.js`

```js
110(s,x){const b=el('button','rgb');const sp=el('span');sp.textContent=x;b.append(sp);b.style.fontSize=Math.min(5,40/chars(x).length)+'cqw';s.append(b)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx110` rules from `site/fx.css`

_No dedicated `.fx110` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #110
