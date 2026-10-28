# 075 · 斜線反轉 — Split Invert

斜線掃過，兩區互換

- 元件 Component: 文字 (`text`)
- 時機 Timing: 切換
- 技術 Tech: CSS
- 情境 Uses: 轉場切換
- 風格／關鍵字 Style: 文字切換 Canva 風格 Canva Block 區塊
- 標籤 Tag: 切換・標題
- 範例文字 Example text: 「反轉」（預覽底色：cream）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「斜線反轉（Split Invert）」動態效果：畫面被一條斜線分成兩區，兩區的底色與文字色互為反差，斜線由左往右掃過畫面，讓文字的兩種配色互換。約 3.4 秒掃一輪，切換標題感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage cream fx75">`, preview text 「反轉」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「斜線反轉」.

### JavaScript — `FX[75]` from `site/fx.js`

```js
75(s,x){const a=el('div','lay');a.append(T(x,24));const b=el('div','lay b');b.append(T(x,24));s.append(a,b)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx75` rules from `site/fx.css`

```css
.fx75 .lay{position:absolute;inset:0;display:grid;place-items:center;background:#fff;color:#111}
.fx75 .lay.b{background:#2b2b2b;color:var(--a);animation:si 3.4s infinite cubic-bezier(.7,0,.3,1)}
@keyframes si{0%{clip-path:polygon(0 0,0% 0,-25% 100%,0 100%)}40%,60%{clip-path:polygon(0 0,62% 0,38% 100%,0 100%)}100%{clip-path:polygon(0 0,130% 0,105% 100%,0 100%)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #75
