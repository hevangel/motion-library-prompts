# 073 · 液體填滿 — Liquid Fill

空心字被液體慢慢裝滿

- 元件 Component: 文字 (`text`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 強調重點
- 風格／關鍵字 Style: 質感填色
- 標籤 Tag: 清爽・MV
- 範例文字 Example text: 「滿」（預覽底色：dark）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「液體填滿（Liquid Fill）」動態效果：一開始只有描邊的空心字，液體由下往上慢慢把字填滿，填滿後停留，再清空重來。約 3.4 秒一輪，清爽 MV 感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx73">`, preview text 「滿」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「液體填滿」.

### JavaScript — `FX[73]` from `site/fx.js`

```js
73(s,x){s.append(T(x,chars(x).length<2?30:undefined))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx73` rules from `site/fx.css`

```css
.fx73 .t{-webkit-text-stroke:.35cqw var(--a);color:transparent;background:linear-gradient(to top,var(--a) var(--lv),transparent calc(var(--lv) + .1%));-webkit-background-clip:text;background-clip:text;animation:lq 3.4s ease-in-out infinite}
@keyframes lq{0%,6%{--lv:0%}70%,90%{--lv:100%}100%{--lv:0%}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #73
