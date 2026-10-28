# 042 · 逐字敲擊 — Letter Sequence

一個字一個字砸上來

- 元件 Component: 文字 (`text`)
- 時機 Timing: 進場
- 技術 Tech: CSS
- 情境 Uses: 標題・Hero
- 風格／關鍵字 Style: 衝擊登場
- 標籤 Tag: 節奏・歌詞
- 範例文字 Example text: 「砸上來吧」（預覽底色：acc）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「逐字敲擊（Letter Sequence）」動態效果：文字一個字一個字從上方大尺寸砸下來定位，每個字落下時略微壓縮再回彈，依序間隔約 0.2 秒，全部出現後一起淡出。約 3 秒一輪。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage acc fx42">`, preview text 「砸上來吧」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「逐字敲擊」.

### JavaScript — `FX[42]` from `site/fx.js`

```js
42(s,x){s.append(split(x))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx42` rules from `site/fx.css`

```css
.fx42 .c{animation:seq 3s calc(var(--i)*.22s) infinite both}
.fx42 .c:nth-child(odd){color:#fff}
@keyframes seq{0%{opacity:0;transform:scale(2.6) translateY(-20%)}7%{opacity:1;transform:scale(.88)}11%{transform:scale(1.06)}14%,78%{transform:none;opacity:1}90%,100%{opacity:0}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #42
