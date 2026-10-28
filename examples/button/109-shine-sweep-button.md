# 109 · 光澤掃過按鈕 — Shine Sweep Button

一道斜向光澤定時掃過按鈕，hover 時加快並浮起

- 元件 Component: 按鈕 (`button`)
- 時機 Timing: 懸停・點擊、循環待機
- 技術 Tech: CSS
- 情境 Uses: 介面互動、強調重點
- 風格／關鍵字 Style: 按鈕 光澤 反光 掃光 閃光 Shine Sweep Glint Shimmer Button CTA
- 標籤 Tag: CSS hover
- 範例文字 Example text: 「立即購買」（預覽底色：cream）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「光澤掃過按鈕（Shine Sweep Button）」動態效果：實心按鈕上有一道斜向的半透明亮光，每隔約 2.4 秒從左往右快速掃過一次，像金屬或玻璃的反光；滑鼠移上去時光澤掃得更快，按鈕同時微微上浮、陰影加深。（CSS：按鈕 overflow:hidden，::after 做一條 skewX(-20deg) 的漸層亮帶，用 keyframes 改變 left 位置；:hover 縮短 animation-duration 並加 translateY）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage cream fx109">`, preview text 「立即購買」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「光澤掃過按鈕」.

### JavaScript — `FX[109]` from `site/fx.js`

```js
109(s,x){const b=el('button','shb');b.textContent=x;b.style.fontSize=Math.min(5,40/chars(x).length)+'cqw';s.append(b)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx109` rules from `site/fx.css`

_No dedicated `.fx109` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #109
