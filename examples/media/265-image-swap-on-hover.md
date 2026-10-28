# 265 · 商品圖切換 — Image Swap on Hover

電商商品卡片滑過時，換成第二張角度的照片，下方圓點跟著切換

- 元件 Component: 圖片・媒體 (`media`)
- 時機 Timing: 懸停・點擊、切換
- 技術 Tech: CSS
- 情境 Uses: 介面互動
- 風格／關鍵字 Style: 商品 電商 第二張圖 換圖 切換 Image Swap Hover Product Card Ecommerce Second Image 圖片 媒體
- 標籤 Tag: CSS hover
- 範例文字 Example text: 「亞麻襯衫」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「商品圖切換（Image Swap on Hover）」動態效果：電商商品卡片：上方是商品主圖，滑鼠滑過卡片時，第二張（例如穿搭或背面角度）的照片淡入並從 1.08 倍縮回原尺寸，主圖同時淡出並微微放大，形成柔和的換圖；圖片下方的兩個小圓點指示器跟著切換目前是第幾張；卡片下方顯示商品名稱與價格。（CSS：兩張圖疊在同一個框內絕對定位，:hover 時交換 opacity 與 scale，transition 約 0.5–0.7 秒）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx265">`, preview text 「亞麻襯衫」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「商品圖切換」.

### JavaScript — `FX[265]` from `site/fx.js`

```js
265(s,x,card){const f=el('div','md-sw');f.innerHTML=mdImg(0,'a')+mdImg(2,'b')+'<div class="md-sp"><b></b><span>NT$ 1,280</span></div><i class="md-dt"><em></em><em></em></i>';f.querySelector('b').textContent=x;s.append(f);autoHover(f,[f],card,1600)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx265` rules from `site/fx.css`

_No dedicated `.fx265` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #265
