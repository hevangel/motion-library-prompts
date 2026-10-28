# 258 · 放大鏡游標 — Magnifier Lens

游標變成圓形放大鏡，鏡片裡的內容放大顯示

- 元件 Component: 游標 (`cursor`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動
- 風格／關鍵字 Style: 放大鏡 放大 鏡片 細節 商品 Magnifier Lens Zoom Loupe Cursor Product 游標 滑鼠
- 標籤 Tag: JS + CSS
- 範例文字 Example text: 「放大檢視」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「放大鏡游標（Magnifier Lens）」動態效果：游標變成一個帶外框與陰影的圓形放大鏡，鏡片內顯示游標下方內容放大約 2.2 倍的畫面，移動時鏡片內容同步平移，讓小字或商品細節看得清楚。（JS + CSS：在鏡片內放一份內容的複本，設定與原內容同寬高、transform-origin:0 0，transform = translate(半徑 − 游標x × 倍率, 半徑 − 游標y × 倍率) scale(倍率)；鏡片 border-radius:50%、overflow:hidden、pointer-events:none）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx258">`, preview text 「放大檢視」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「放大鏡游標」.

### JavaScript — `FX[258]` from `site/fx.js`

```js
258(s,x,card){const l=el('div','abs cr-mg');const base=el('div','abs gl cr-mb');base.append(T(x,Math.min(9,40/chars(x).length)));const sm=el('small','cr-fine');sm.textContent='細節放大看得更清楚 · Details matter';base.append(sm);
  const lens=el('div','cr-ln');const inner=base.cloneNode(true);inner.classList.add('cr-li');lens.append(inner);l.append(base,lens);s.append(l);const Z=2.2;
  vpointer(l,card,(px,py)=>{const R=lens.offsetWidth/2;lens.style.transform=`translate(${px-R}px,${py-R}px)`;inner.style.width=l.offsetWidth+'px';inner.style.height=l.offsetHeight+'px';inner.style.transform=`translate(${R-px*Z}px,${R-py*Z}px) scale(${Z})`})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx258` rules from `site/fx.css`

_No dedicated `.fx258` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #258
