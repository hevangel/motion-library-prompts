# 132 · 左右交錯淡入 — Zigzag Cascade

圖文列表左右交錯出現，視線呈 Z 字往下走

- 元件 Component: 卡片・群組 (`card`)
- 時機 Timing: 進場、捲動觸發
- 技術 Tech: GSAP
- 情境 Uses: 介面互動
- 風格／關鍵字 Style: 圖文 列表 左右 交錯 Z 字 往下 介紹 特色 溫和 柔和 輕柔 引導 動線 視線 閱讀順序 低調 Subtle Gentle Soft Entrance Visual Flow Hierarchy
- 標籤 Tag: Zigzag
- 範例文字 Example text: 「關於 作品 服務 聯絡」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「左右交錯淡入（Zigzag Cascade）」動態效果：上下排列的圖文列，左右交錯配置（第一列圖左文右、第二列圖右文左，以此類推），進場時由上到下依序出現，每一列從它所在的那一側往內輕輕滑入約 20px 並淡入，間隔約 0.35 秒、每列約 0.9 秒、平順減速，視線因此呈 Z 字一路往下閱讀。（GSAP：fromTo x 依索引正負交替 ±20 / opacity:0，stagger 0.35，ease power2.out；實際網站可用 ScrollTrigger.batch 讓每列捲到時才出現）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx132">`, preview text 「關於 作品 服務 聯絡」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「左右交錯淡入」.

### JavaScript — `FX[132]` from `site/fx.js`

```js
132(s,x){const w=el('div','zz');const ws=words(x);for(let i=0;i<4;i++){const r=el('div','zr'+(i%2?' rt':''));r.innerHTML='<i></i><span><b></b><em></em></span>';r.querySelector('i').style.background=`linear-gradient(135deg,${GC[i]},${GC[i+1]})`;r.querySelector('b').textContent=ws[i%ws.length];w.append(r)}s.append(w);const rs=[...w.children];
  gsap.timeline({repeat:-1,repeatDelay:.3}).fromTo(rs,{x:i=>i%2?20:-20,opacity:0},{x:0,opacity:1,duration:.9,ease:'power2.out',stagger:.35}).to(rs,{opacity:0,duration:.5},'+=1.6')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx132` rules from `site/fx.css`

_No dedicated `.fx132` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #132
