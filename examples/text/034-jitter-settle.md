# 034 · 顫抖穩定 — Jitter Settle

顫抖後慢慢穩定

- 元件 Component: 文字 (`text`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 強調重點
- 風格／關鍵字 Style: 逐字律動
- 標籤 Tag: 驚嚇・緊張
- 範例文字 Example text: 「ブルブル」（預覽底色：acc）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「顫抖穩定（Jitter Settle）」動態效果：文字一開始劇烈地左右上下抖動並旋轉，抖動幅度逐漸變小，最後穩定停住，停一會兒再重新顫抖。約 2.4 秒一輪，驚嚇緊張感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage acc fx34">`, preview text 「ブルブル」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「顫抖穩定」.

### JavaScript — `FX[34]` from `site/fx.js`

```js
34(s,x){s.append(split(x))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx34` rules from `site/fx.css`

```css
.fx34 .c{animation:jit 2.4s calc(var(--i)*.09s) infinite linear}
.fx34 .c:nth-child(even){color:#7a5500}
@keyframes jit{0%{transform:translate(9%,-7%) rotate(7deg)}4%{transform:translate(-9%,6%) rotate(-7deg)}8%{transform:translate(8%,5%) rotate(6deg)}12%{transform:translate(-7%,-6%) rotate(-5deg)}16%{transform:translate(6%,4%) rotate(4deg)}21%{transform:translate(-4%,-3%) rotate(-3deg)}26%{transform:translate(3%,2%) rotate(2deg)}32%{transform:translate(-2%,-1%) rotate(-1deg)}38%{transform:translate(1%,1%) rotate(.5deg)}44%,86%{transform:none}100%{transform:translate(9%,-7%) rotate(7deg)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #34
