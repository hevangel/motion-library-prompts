# 019 · 文字旗幟 — Text Flag

文字像旗子般飄揚

- 元件 Component: 文字 (`text`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 強調重點
- 風格／關鍵字 Style: 逐字律動
- 標籤 Tag: 氣勢・應援
- 範例文字 Example text: 「はためく旗」（預覽底色：cream）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「文字旗幟（Text Flag）」動態效果：文字左側有一根旗桿，每個字依序做 3D 翻轉與傾斜，形成旗子迎風飄揚的波浪。約 1.3 秒一個波，有氣勢的應援感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage cream fx19">`, preview text 「はためく旗」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「文字旗幟」.

### JavaScript — `FX[19]` from `site/fx.js`

```js
19(s,x){const w=el('div','w');w.append(el('div','pole'),split(x));s.append(w)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx19` rules from `site/fx.css`

```css
.fx19 .w{display:flex;align-items:center;gap:2cqw}
.fx19 .pole{width:1cqw;height:34cqw;background:#333;border-radius:2px;align-self:center}
.fx19 .c{animation:flag 1.3s calc(var(--i)*-.17s) ease-in-out infinite;transform-origin:0 50%}
.fx19 .c:nth-child(even){color:var(--a)}
@keyframes flag{0%,100%{transform:rotateY(0) skewY(0) translateY(0)}50%{transform:rotateY(38deg) skewY(-9deg) translateY(-7%)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #19
