# 022 · 脈動格子 — Word Pulse Grid

格狀文字隨波膨脹

- 元件 Component: 背景・氛圍 (`bg`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 背景裝飾
- 風格／關鍵字 Style: 流動背景
- 標籤 Tag: 背景・節奏
- 範例文字 Example text: 「脈」（預覽底色：acc，固定文字）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「脈動格子（Word Pulse Grid）」動態效果：同一個字排成 8×4 的格子，從中心往外一圈圈依序放大、變亮再縮小變暗，形成脈動波紋。約 1.8 秒一個波，節奏背景感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage acc fx22">`, preview text 「脈」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「脈動格子」.

### JavaScript — `FX[22]` from `site/fx.js`

```js
22(s,x){const g=el('div','g');for(let r=0;r<4;r++)for(let c=0;c<8;c++){const sp=el('span');sp.textContent=chars(x)[0];sp.style.setProperty('--d',Math.hypot(c-3.5,(r-1.5)*1.6).toFixed(2));g.append(sp)}s.append(g)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx22` rules from `site/fx.css`

```css
.fx22 .g{display:grid;grid-template-columns:repeat(8,1fr);gap:1.4cqw 3cqw}
.fx22 .g span{font-weight:900;font-size:6.5cqw;color:#1b1340;animation:pg 1.8s calc(var(--d)*.13s) ease-in-out infinite}
@keyframes pg{0%,100%{transform:scale(.55);opacity:.35}45%{transform:scale(1.2);opacity:1;color:#fff}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #22
