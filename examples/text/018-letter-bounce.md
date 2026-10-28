# 018 · 逐字彈跳 — Letter Bounce

文字逐字彈跳

- 元件 Component: 文字 (`text`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 標題・Hero
- 風格／關鍵字 Style: 逐字律動 Canva 風格 Canva Bounce 彈跳
- 標籤 Tag: 可愛・MV
- 範例文字 Example text: 「はずむ文字」（預覽底色：acc）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「逐字彈跳（Letter Bounce）」動態效果：每個字依序壓扁、彈起、落地再壓扁回彈，像小球一樣有擠壓伸展的彈性，一次只跳一個字。約 2.2 秒一輪，可愛 MV 感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage acc fx18">`, preview text 「はずむ文字」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「逐字彈跳」.

### JavaScript — `FX[18]` from `site/fx.js`

```js
18(s,x){s.append(split(x))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx18` rules from `site/fx.css`

```css
.fx18 .c{transform-origin:50% 100%;animation:bnc 2.2s calc(var(--i)*.18s) infinite}
.fx18 .c:nth-child(n+4){color:#fff}
@keyframes bnc{0%,40%,100%{transform:none}8%{transform:scale(1.2,.8)}18%{transform:translateY(-45%) scale(.9,1.1)}28%{transform:scale(1.15,.85)}34%{transform:scale(.97,1.03)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #18
