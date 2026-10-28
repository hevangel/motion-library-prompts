# 040 · 漂浮 — Float Drift

輕飄飄地浮動

- 元件 Component: 文字 (`text`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 背景裝飾、Logo・品牌
- 風格／關鍵字 Style: 逐字律動
- 標籤 Tag: 療癒・夢幻
- 範例文字 Example text: 「ふわふわ」（預覽底色：dark）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「漂浮（Float Drift）」動態效果：每個字以不同速度緩慢上下左右漂浮並輕微旋轉，帶柔和光暈，像羽毛輕飄飄。每字約 3–4.5 秒一輪，療癒夢幻感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx40">`, preview text 「ふわふわ」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「漂浮」.

### JavaScript — `FX[40]` from `site/fx.js`

```js
40(s,x){const t=split(x);t.querySelectorAll('.c').forEach(c=>c.style.setProperty('--dur',rnd(2.8,4.4).toFixed(2)+'s'));s.append(t)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx40` rules from `site/fx.css`

```css
.fx40 .c{animation:flo var(--dur) calc(var(--i)*-.7s) ease-in-out infinite;text-shadow:0 0 12px #fff6}
.fx40 .c:nth-child(even){color:var(--a)}
@keyframes flo{0%,100%{transform:translate(0,0) rotate(-4deg)}33%{transform:translate(4%,-14%) rotate(4deg)}66%{transform:translate(-3%,-5%) rotate(-1deg)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #40
