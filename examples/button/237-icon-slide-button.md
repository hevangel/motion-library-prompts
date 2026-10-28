# 237 · 箭頭接力按鈕 — Icon Slide Button

滑過時右側箭頭往右滑出，同時新箭頭從左側滑入、文字讓位

- 元件 Component: 按鈕 (`button`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動、強調重點
- 風格／關鍵字 Style: 箭頭 圖示 滑入 滑出 接力 Icon Slide Arrow Button Hover CTA 按鈕
- 標籤 Tag: CSS hover
- 範例文字 Example text: 「了解更多」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「箭頭接力按鈕（Icon Slide Button）」動態效果：膠囊按鈕，文字右側有一個向右箭頭；滑鼠滑過時，右側箭頭往右滑出按鈕並淡出，同時另一個相同的箭頭從按鈕左側外滑入到文字左邊，文字同步往右讓出位置，像箭頭接力往前推；滑開時反向回復。約 0.4 秒、緩入緩出。（CSS：按鈕 overflow:hidden，兩個箭頭與文字各自設定 transform 與 transition，hover 時切換位移）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx237">`, preview text 「了解更多」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「箭頭接力按鈕」.

### JavaScript — `FX[237]` from `site/fx.js`

```js
237(s,x,card){const b=bxBtn('bx-ic',x);b.insertAdjacentHTML('afterbegin','<svg class="bx-a1" viewBox="0 0 24 24"><path d="M5 12h13M13 6l6 6-6 6"/></svg>');b.insertAdjacentHTML('beforeend','<svg class="bx-a2" viewBox="0 0 24 24"><path d="M5 12h13M13 6l6 6-6 6"/></svg>');s.append(b);autoHover(b,[b],card,1400)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx237` rules from `site/fx.css`

_No dedicated `.fx237` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #237
