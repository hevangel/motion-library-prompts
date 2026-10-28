# 194 · 漸層光流線條 — Flowing Gradient Stroke

線條上的漸層持續流動，一道光點沿線繞行

- 元件 Component: 圖形・SVG (`shape`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 背景裝飾、Logo・品牌
- 風格／關鍵字 Style: 漸層 線條 流動 光點 彗星 無限符號 Gradient Stroke Flow Comet Infinity Loop SVG 圖形
- 標籤 Tag: SVG gradient
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「漸層光流線條（Flowing Gradient Stroke）」動態效果：一條封閉的無限符號形曲線，線條本身是多色漸層，漸層沿著線條方向持續流動；同時有一小段明亮的光點像彗星一樣沿著線條繞行並帶微微發光。適合品牌裝飾或科技感背景。（SVG：linearGradient 設 gradientUnits="userSpaceOnUse"、spreadMethod="repeat"，用 animateTransform 平移 gradientTransform；光點用第二條相同路徑，stroke-dasharray 一短段實線、keyframes 改 stroke-dashoffset）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx194">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「漸層光流線條」.

### JavaScript — `FX[194]` from `site/fx.js`

```js
194(s){const id='gs'+Math.random().toString(36).slice(2),P='M20,45 C20,10 70,10 80,45 S140,80 140,45 S100,10 80,45 S20,80 20,45 Z';
  s.insertAdjacentHTML('beforeend',`<svg class="gfl" viewBox="0 0 160 90"><defs><linearGradient id="${id}" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="160" y2="0" spreadMethod="repeat"><stop offset="0" stop-color="#7c5cff"/><stop offset=".33" stop-color="#00c8ff"/><stop offset=".66" stop-color="#ff4fd8"/><stop offset="1" stop-color="#7c5cff"/><animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="160 0" dur="2.4s" repeatCount="indefinite"/></linearGradient></defs><path class="base" d="${P}" stroke="url(#${id})"/><path class="cmt" d="${P}"/></svg>`)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx194` rules from `site/fx.css`

_No dedicated `.fx194` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #194
