# 227 · 旋轉光芒 — Sunburst Rays

放射狀光芒在標題後方緩緩旋轉，中心最亮往外淡出

- 元件 Component: 背景・氛圍 (`bg`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 標題・Hero、強調重點、背景裝飾
- 風格／關鍵字 Style: 光芒 放射 太陽光 旋轉 慶祝 得獎 抽獎 Sunburst Rays Rotating God Rays Conic 背景 氛圍
- 標籤 Tag: conic-gradient
- 範例文字 Example text: 「WINNER」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「旋轉光芒（Sunburst Rays）」動態效果：標題後方有一圈從中心向外放射的光芒條紋，整圈以約 30 秒一圈的速度緩慢旋轉，中心最亮、往外漸漸融入背景，像得獎、抽獎或慶祝畫面的聚光效果。（CSS：repeating-conic-gradient 畫出放射條紋並放大超出容器，keyframes rotate 360deg linear infinite；上方疊一層 radial-gradient 讓中心亮、邊緣暗）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx227">`, preview text 「WINNER」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「旋轉光芒」.

### JavaScript — `FX[227]` from `site/fx.js`

```js
227(s,x){s.append(el('div','abs bga-ray'),el('div','abs bga-rg'),T(x,Math.min(12,56/chars(x).length)))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx227` rules from `site/fx.css`

```css
.fx222 .t,.fx224 .t,.fx227 .t,.fx231 .t{color:#fff;z-index:1;text-shadow:0 .4cqw 2cqw #0006}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #227
