# 169 · 提示框彈出 — Tooltip Pop

滑過圖示時，提示框從下方帶彈性彈出

- 元件 Component: 表單・控制項 (`control`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動、App 介面
- 風格／關鍵字 Style: 提示框 tooltip 說明 小提示 氣泡 popover hover hint hover 懸停 滑鼠移入 滑過 互動
- 標籤 Tag: CSS hover
- 範例文字 Example text: 「說明 資訊 分享」（預覽底色：dark）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「提示框彈出（Tooltip Pop）」動態效果：一排圓形圖示按鈕，滑鼠移到某個圖示時，上方彈出一個帶小三角箭頭的提示框，從約 60% 大小、略低的位置以箭頭為原點彈性放大並上移到定位（約 0.3 秒，帶一點過衝），移開時淡出縮回。（CSS：提示框 position:absolute，transform-origin 設在箭頭處，hover 時 scale(0.6)→1 + translateY + opacity，transition cubic-bezier(.3,1.5,.5,1)；記得 pointer-events:none 避免閃爍）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx169">`, preview text 「說明 資訊 分享」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「提示框彈出」.

### JavaScript — `FX[169]` from `site/fx.js`

```js
169(s,x,card){const w=el('div','ttw');const ws=words(x);const its=['?','i','↗'].map((g,i)=>{const b=el('span','tti');b.textContent=g;const t=el('span','tip');t.textContent=ws[i%ws.length];b.append(t);w.append(b);return b});s.append(w);autoHover(w,its,card,1200)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx169` rules from `site/fx.css`

_No dedicated `.fx169` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #169
