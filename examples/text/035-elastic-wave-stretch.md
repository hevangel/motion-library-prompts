# 035 · 彈性拉伸 — Elastic Wave Stretch

文字縱向拉伸成波浪

- 元件 Component: 文字 (`text`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 標題・Hero
- 風格／關鍵字 Style: 逐字律動
- 標籤 Tag: 流行・音樂
- 範例文字 Example text: 「のびる波」（預覽底色：cream）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「彈性拉伸（Elastic Wave Stretch）」動態效果：每個字以底部為基準，依序縱向拉長到約 1.7 倍再縮回，同時橫向變窄，形成彈性波浪，最後一個字用強調色。約 1.3 秒一個波，流行音樂感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage cream fx35">`, preview text 「のびる波」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「彈性拉伸」.

### JavaScript — `FX[35]` from `site/fx.js`

```js
35(s,x){s.append(split(x))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx35` rules from `site/fx.css`

```css
.fx35 .c{transform-origin:50% 100%;animation:str 1.3s calc(var(--i)*-.16s) ease-in-out infinite}
.fx35 .c:last-child{color:#c08a00}
@keyframes str{0%,100%{transform:scale(1.05,.85)}50%{transform:scale(.85,1.75)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #35
