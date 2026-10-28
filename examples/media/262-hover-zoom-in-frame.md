# 262 · 框內微放大 — Hover Zoom in Frame

滑過圖片時，圖片在固定的框內慢慢微放大，標題從底部浮上來

- 元件 Component: 圖片・媒體 (`media`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動
- 風格／關鍵字 Style: hover 放大 縮放 圖片放大 框內 固定框 overflow hidden 作品集 商品圖 Image Zoom Hover Scale Thumbnail Gallery 圖片 媒體
- 標籤 Tag: CSS hover
- 範例文字 Example text: 「海邊 山林 城市」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「框內微放大（Hover Zoom in Frame）」動態效果：一排圖片卡片，每張圖片放在固定尺寸、圓角的框裡（overflow:hidden）：滑鼠滑過時，框的大小不變，裡面的圖片以約 0.8 秒、減速的曲線慢慢放大到 1.1 倍；框底部的標題列（帶由透明到半透明的漸層底）同時從下方略微上移並變得完全清楚；滑開時圖片緩緩縮回。（CSS：容器 overflow:hidden；img 設 transition: transform .8s cubic-bezier(.2,.7,.2,1)，容器 :hover 時 img transform:scale(1.1)；標題 translateY 與 opacity 一起過渡）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx262">`, preview text 「海邊 山林 城市」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「框內微放大」.

### JavaScript — `FX[262]` from `site/fx.js`

```js
262(s,x,card){const ws=words(x);const w=el('div','md-zg');const fs=[0,1,2].map(i=>{const f=el('figure','md-z');f.innerHTML=mdImg(i)+'<figcaption></figcaption>';f.querySelector('figcaption').textContent=ws[i%ws.length];w.append(f);return f});s.append(w);autoHover(w,fs,card,1200)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx262` rules from `site/fx.css`

_No dedicated `.fx262` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #262
