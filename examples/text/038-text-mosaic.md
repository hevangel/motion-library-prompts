# 038 · 字體樣本 — Text Mosaic

不同字體依序發光

- 元件 Component: 文字 (`text`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 背景裝飾
- 風格／關鍵字 Style: 質感填色
- 標籤 Tag: 字體樣本・設計
- 範例文字 Example text: 「愛夢光風花月海空」（預覽底色：acc，固定文字）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「字體樣本（Text Mosaic）」動態效果：8 個字排成 4×2 格，每格使用不同字體（黑體、明體、點陣、圓體、毛筆等），依序一格一格反白亮起並微微放大，再暗回去。約 3.2 秒一輪。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage acc fx38">`, preview text 「愛夢光風花月海空」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「字體樣本」.

### JavaScript — `FX[38]` from `site/fx.js`

```js
38(s,x){const F=['"Noto Sans JP";font-weight:900','"Noto Serif JP";font-weight:900','"DotGothic16"','"Zen Maru Gothic";font-weight:700','"Yuji Syuku"','"Rampart One"','"Reggae One"','"Kaisei Decol";font-weight:700'];const g=el('div','g');chars(x).slice(0,8).forEach((c,i)=>{const e=el('span');e.textContent=c;e.style.cssText+=`;font-family:${F[i%8]}`;e.style.setProperty('--i',i);g.append(e)});s.append(g)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx38` rules from `site/fx.css`

```css
.fx38 .g{display:grid;grid-template-columns:repeat(4,1fr);gap:1.6cqw;width:88%}
.fx38 .g span{font-size:11cqw;line-height:1.5;text-align:center;border-radius:1.4cqw;background:#0000000f;color:#6b4a00;animation:lit 3.2s calc(var(--i)*.4s) infinite}
@keyframes lit{0%,6%{background:#fff;color:#111;transform:scale(1.08)}22%,100%{background:#0000000f;color:#6b4a00;transform:none}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #38
