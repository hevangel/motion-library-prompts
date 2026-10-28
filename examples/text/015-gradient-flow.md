# 015 · 漸層流動 — Gradient Flow

漸層在文字中流動

- 元件 Component: 文字 (`text`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 標題・Hero、Logo・品牌
- 風格／關鍵字 Style: 質感填色
- 標籤 Tag: 標題・潮流
- 範例文字 Example text: 「流れる色」（預覽底色：cream）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「漸層流動（Gradient Flow）」動態效果：文字內填充多色漸層，漸層持續由左往右在字裡流動。粗體大字，約 3 秒流動一輪，時尚標題感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage cream fx15">`, preview text 「流れる色」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「漸層流動」.

### JavaScript — `FX[15]` from `site/fx.js`

```js
15(s,x){s.append(T(x))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx15` rules from `site/fx.css`

```css
.fx15 .t{background:linear-gradient(90deg,#c22,#ff6b4a,#ffcf3c,#ff6b4a,#7a1a1a,#c22);background-size:300% 100%;-webkit-background-clip:text;background-clip:text;color:transparent;animation:gf 3s linear infinite}
@keyframes gf{to{background-position:300% 0}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #15
