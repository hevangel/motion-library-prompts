# 026 · 鐘擺搖晃 — Swing Letters

從上方一點如鐘擺搖晃

- 元件 Component: 文字 (`text`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: Logo・品牌
- 風格／關鍵字 Style: 逐字律動
- 標籤 Tag: 可愛・慵懶
- 範例文字 Example text: 「ゆらゆら」（預覽底色：acc）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「鐘擺搖晃（Swing Letters）」動態效果：每個字頂端有一個小圓點，字以這個點為支點像鐘擺一樣左右擺動約 ±14 度，各字擺動錯開。約 1.7 秒一擺，慵懶可愛。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage acc fx26">`, preview text 「ゆらゆら」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「鐘擺搖晃」.

### JavaScript — `FX[26]` from `site/fx.js`

```js
26(s,x){s.append(split(x))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx26` rules from `site/fx.css`

```css
.fx26 .c{transform-origin:50% -18%;animation:sw 1.7s calc(var(--i)*-.27s) ease-in-out infinite;position:relative}
.fx26 .c::before{content:"";position:absolute;left:50%;top:-22%;width:1cqw;height:1cqw;margin-left:-.5cqw;border-radius:50%;background:#111}
.fx26 .c:nth-child(even){color:#fff}
@keyframes sw{0%,100%{transform:rotate(14deg)}50%{transform:rotate(-14deg)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #26
