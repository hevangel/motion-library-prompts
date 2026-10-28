# 030 · 棋盤翻轉 — Checker Words

棋盤格文字依波浪翻轉

- 元件 Component: 背景・氛圍 (`bg`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 背景裝飾
- 風格／關鍵字 Style: 流動背景
- 標籤 Tag: 花紋・背景
- 範例文字 Example text: 「文」（預覽底色：acc，固定文字）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「棋盤翻轉（Checker Words）」動態效果：同一個字排成 10×4 的棋盤格，深淺方塊交錯，從左上到右下依序以 Y 軸翻轉，形成斜向的翻牌波浪。約 2.6 秒一輪，花紋背景感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage acc fx30">`, preview text 「文」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「棋盤翻轉」.

### JavaScript — `FX[30]` from `site/fx.js`

```js
30(s,x){const g=el('div','g');for(let r=0;r<4;r++)for(let c=0;c<10;c++){const sp=el('span',(r+c)%2?'d':'l');sp.textContent=chars(x)[0];sp.style.setProperty('--d',c+r);g.append(sp)}s.append(g)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx30` rules from `site/fx.css`

```css
.fx30 .g{display:grid;grid-template-columns:repeat(10,1fr);gap:1cqw;padding:0 3cqw}
.fx30 .g span{font-weight:900;font-size:5.6cqw;line-height:1.4;text-align:center;border-radius:1cqw;animation:chk 2.6s calc(var(--d)*.07s) infinite}
.fx30 .g span.l{background:#111;color:var(--a)}
.fx30 .g span.d{background:#0002;color:#111}
@keyframes chk{0%,15%{transform:rotateY(0)}35%,65%{transform:rotateY(180deg)}85%,100%{transform:rotateY(360deg)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #30
