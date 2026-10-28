# 238 · 霓虹呼吸按鈕 — Neon Glow Button

外框與光暈像呼吸般忽明忽暗，滑過時填滿並大量發光

- 元件 Component: 按鈕 (`button`)
- 時機 Timing: 循環待機、懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動、強調重點、標題・Hero
- 風格／關鍵字 Style: 霓虹 發光 光暈 呼吸 Neon Glow Pulse Button Cyberpunk 按鈕
- 標籤 Tag: box-shadow
- 範例文字 Example text: 「加入我們」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「霓虹呼吸按鈕（Neon Glow Button）」動態效果：霓虹風格按鈕：外框細線與文字使用強調色，周圍有一圈柔和的外發光與內發光，光暈以約 2.4 秒的週期像呼吸般變亮又變暗；滑鼠滑過時整顆填滿、文字反白，並散發出多層大範圍的強烈光暈。（CSS：多層 box-shadow（含 inset）做發光，keyframes 改變光暈大小與透明度；hover 時停止呼吸動畫、改成更大的多層 box-shadow，transition 0.35 秒）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx238">`, preview text 「加入我們」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「霓虹呼吸按鈕」.

### JavaScript — `FX[238]` from `site/fx.js`

```js
238(s,x,card){const b=bxBtn('bx-gl',x);s.append(b);autoHover(b,[b],card,1600)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx238` rules from `site/fx.css`

_No dedicated `.fx238` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #238
