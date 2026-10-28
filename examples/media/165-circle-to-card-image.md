# 165 · 圖片圓形展開 — Circle to Card Image

圓形縮圖在滑過時展開成直式圓角卡片並浮出標題

- 元件 Component: 圖片・媒體 (`media`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動、標題・Hero
- 風格／關鍵字 Style: 圖片 圓形 展開 縮圖 頭像 團隊 image shape expand circle hover hover 懸停 滑鼠移入 滑過 互動
- 標籤 Tag: CSS hover
- 範例文字 Example text: 「清晨 午後 夜晚」（預覽底色：dark）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「圖片圓形展開（Circle to Card Image）」動態效果：一排圓形的圖片縮圖，滑鼠移到其中一張時，圓形平滑變成較高的直式圓角矩形（同時往下長高），圖片內容從 1.18 倍縮回原尺寸、看到更多畫面，下方標題淡入；移開時恢復圓形。約 0.55 秒、減速。適合團隊成員或作品分類。（CSS：外框 border-radius 50%→小圓角、height 同步 transition；內層圖片 transform:scale 1.18→1；標題 opacity / translateY）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx165">`, preview text 「清晨 午後 夜晚」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「圖片圓形展開」.

### JavaScript — `FX[165]` from `site/fx.js`

```js
165(s,x,card){const w=el('div','shw');const ws=words(x);const P=[['#9fd3ff','#ffe1b0','#4f7a6a','#264a3f','#fff6d8'],['#ffd9c2','#c9b6ff','#7b6ca8','#3f3566','#fff6e6'],['#1b1f4a','#4a2a6b','#2c2a55','#14122e','#f4f1d0']];
  const cs=P.map((p,i)=>{const c=el('figure','shp');c.innerHTML=`<div class="im3">${scene(...p)}</div><figcaption></figcaption>`;c.querySelector('figcaption').textContent=ws[i%ws.length];w.append(c);return c});s.append(w);autoHover(w,cs,card,1400)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx165` rules from `site/fx.css`

_No dedicated `.fx165` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #165
