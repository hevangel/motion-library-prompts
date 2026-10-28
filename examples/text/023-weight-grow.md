# 023 · 字重變粗 — Weight Grow

細字逐漸變粗

- 元件 Component: 文字 (`text`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 強調重點
- 風格／關鍵字 Style: 質感填色
- 標籤 Tag: 強調・變化
- 範例文字 Example text: 「太くなる」（預覽底色：cream）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「字重變粗（Weight Grow）」動態效果：文字從極細的字重慢慢變成最粗的字重，停留後再變回細字（需使用可變字重字體）。約 3 秒一輪，強調變化感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage cream fx23">`, preview text 「太くなる」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「字重變粗」.

### JavaScript — `FX[23]` from `site/fx.js`

```js
23(s,x){s.append(T(x))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx23` rules from `site/fx.css`

```css
.fx23 .t{font-weight:100;animation:wg 3s ease-in-out infinite}
@keyframes wg{0%,12%{font-weight:100}55%,82%{font-weight:900}100%{font-weight:100}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #23
