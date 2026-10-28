# 036 · 墨水暈開 — Ink Bleed

墨水暈開成形

- 元件 Component: 文字 (`text`)
- 時機 Timing: 進場
- 技術 Tech: CSS
- 情境 Uses: 標題・Hero
- 風格／關鍵字 Style: 質感填色
- 標籤 Tag: 和風・手寫感
- 範例文字 Example text: 「にじむ墨」（預覽底色：dark）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「墨水暈開（Ink Bleed）」動態效果：文字像墨水滴在紙上：一開始是模糊暈開的墨團，逐漸收斂成清晰銳利的字形，停留後再暈開消失，各字依序錯開。約 3.4 秒一輪，和風手寫感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx36">`, preview text 「にじむ墨」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「墨水暈開」.

### JavaScript — `FX[36]` from `site/fx.js`

```js
36(s,x){const g=el('div','goo');g.append(split(x));s.append(g)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx36` rules from `site/fx.css`

```css
.fx36{background:#000!important}
.fx36 .goo{filter:contrast(16);background:#000;padding:4cqw 6cqw}
.fx36 .c{color:#fff;animation:ink 3.4s calc(var(--i)*.22s) infinite}
@keyframes ink{0%{filter:blur(16px);opacity:0;transform:scale(1.3)}15%{opacity:1}55%,80%{filter:blur(0);transform:none;opacity:1}100%{filter:blur(16px);opacity:0;transform:scale(1.2)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #36
