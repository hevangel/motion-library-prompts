# 200 · 幾何載入動畫 — Geometric Loader

圓形、方形、三角形依序彈跳翻轉，作為載入中提示

- 元件 Component: 圖形・SVG (`shape`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 介面互動、App 介面
- 風格／關鍵字 Style: 載入 讀取 loading 等待 幾何 彈跳 Loader Spinner Geometric Shapes Bounce SVG 圖形
- 標籤 Tag: CSS keyframes
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「幾何載入動畫（Geometric Loader）」動態效果：載入中提示：三個描邊的幾何圖形（圓形、方形、三角形）排成一列，依序像波浪一樣先壓扁蓄力、跳起並翻轉 360 度、落地時再壓扁回彈，循環播放，比一般轉圈圖示更有個性。（CSS：同一組 keyframes 包含 scale 壓扁、translateY 跳起、rotate 翻轉，三個圖形用 animation-delay 錯開 0.18 秒）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx200">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「幾何載入動畫」.

### JavaScript — `FX[200]` from `site/fx.js`

```js
200(s){s.insertAdjacentHTML('beforeend','<div class="geo"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/></svg><svg viewBox="0 0 24 24"><rect x="3.5" y="3.5" width="17" height="17" rx="2"/></svg><svg viewBox="0 0 24 24"><path d="M12 3 L21.5 20 H2.5 Z"/></svg></div>')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx200` rules from `site/fx.css`

_No dedicated `.fx200` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #200
