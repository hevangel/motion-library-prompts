# 295 · 圖片填字 — Image Filled Text

大字裡面填的是一張風景圖片，圖片在字裡緩慢平移縮放

- 元件 Component: 文字 (`text`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 標題・Hero
- 風格／關鍵字 Style: 圖片 填字 鏤空 背景 文字遮罩 Image Text Background Clip Knockout Mask 文字 標題 動態文字
- 標籤 Tag: background-clip
- 範例文字 Example text: 「WILD」（預覽底色：dark）
- 收錄日期 Added: 2026-10-20

**AI 提示詞（網站複製格式）:**

```text
「圖片填字（Image Filled Text）」動態效果：一個超大、超粗的英文標題，字的內部填滿一張風景照片（字以外的地方看不到圖片），照片在字裡面緩慢地平移並微微放大，約 9 秒來回一次，像透過文字形狀的窗戶看風景；字外緣有一條極淡的細描邊。（CSS：color:transparent + background-image + background-clip:text，keyframes 改變 background-position 與 background-size）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx295">`, preview text 「WILD」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「圖片填字」.

### JavaScript — `FX[295]` from `site/fx.js`

```js
295(s,x){const t=el('div','tx-if');t.style.fontSize=Math.min(19,80/chars(x).length)+'cqw';t.textContent=x;s.append(t);t.style.backgroundImage=`url("data:image/svg+xml,${encodeURIComponent(scene(...MD_P[3]).replace('<svg ','<svg xmlns="http://www.w3.org/2000/svg" '))}")`}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx295` rules from `site/fx.css`

_No dedicated `.fx295` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #295
