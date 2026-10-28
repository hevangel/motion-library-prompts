# 071 · 圖案遮罩 — Text Mask Pattern

文字變成窗，條紋從裡面流過

- 元件 Component: 文字 (`text`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 標題・Hero
- 風格／關鍵字 Style: 質感填色
- 標籤 Tag: 俏皮・祭典
- 範例文字 Example text: 「祭典」（預覽底色：cream）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「圖案遮罩（Text Mask Pattern）」動態效果：文字像一扇窗，字裡填滿兩色交錯的斜條紋，條紋持續往側邊流動。粗體字，約 1 秒流動一個條紋週期，俏皮祭典感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage cream fx71">`, preview text 「祭典」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「圖案遮罩」.

### JavaScript — `FX[71]` from `site/fx.js`

```js
71(s,x){s.append(T(x,22))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx71` rules from `site/fx.css`

```css
.fx71 .t{background:repeating-linear-gradient(45deg,var(--a) 0 1.2cqw,#222 1.2cqw 2.4cqw);background-size:3.394cqw 3.394cqw;-webkit-background-clip:text;background-clip:text;color:transparent;animation:mp 1s linear infinite}
@keyframes mp{to{background-position:3.394cqw 0}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #71
