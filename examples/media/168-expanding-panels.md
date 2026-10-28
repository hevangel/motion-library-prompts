# 168 · 展開式圖片面板 — Expanding Panels

一排窄圖片面板，滑過的那一片展開變寬並顯示標題

- 元件 Component: 圖片・媒體 (`media`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動、標題・Hero
- 風格／關鍵字 Style: 圖片 面板 展開 手風琴 相簿 gallery accordion expanding panels flex hover 懸停 滑鼠移入 滑過 互動
- 標籤 Tag: CSS flex
- 範例文字 Example text: 「山林 花海 夜空 夕照 海岸」（預覽底色：dark）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「展開式圖片面板（Expanding Panels）」動態效果：一排等寬的直條圖片面板，滑鼠移到某一片時，它平滑展開成約其他片 4 倍寬，其他面板同步縮窄，展開完成後該片左下角的標題淡入；移到另一片時順暢地交棒。約 0.6 秒、減速。適合作品分類或圖庫入口。（CSS：容器 display:flex，每片 flex:1，hover 時 flex:4，transition flex；圖片用 object-fit:cover 避免變形；標題加 transition-delay）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx168">`, preview text 「山林 花海 夜空 夕照 海岸」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「展開式圖片面板」.

### JavaScript — `FX[168]` from `site/fx.js`

```js
168(s,x,card){const w=el('div','exp');const ws=words(x);const P=[['#9fd3ff','#ffe1b0','#4f7a6a','#264a3f','#fff6d8'],['#ffd9c2','#c9b6ff','#7b6ca8','#3f3566','#fff6e6'],['#1b1f4a','#4a2a6b','#2c2a55','#14122e','#f4f1d0'],['#ffb36b','#ff6b8b','#8a3f6e','#3b1f45','#fff3d6'],['#c9f0e6','#7fd1c7','#2f7d74','#16433f','#ffffff']];
  const ps=P.map((p,i)=>{const e=el('div','ep');e.innerHTML=scene(...p)+'<b></b>';e.querySelector('b').textContent=ws[i%ws.length];w.append(e);return e});s.append(w);autoHover(w,ps,card,1300)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx168` rules from `site/fx.css`

_No dedicated `.fx168` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #168
