# 287 · 社群圖示填滿 — Social Icon Fill

圓形社群圖示滑過時底色從下往上填滿，圖示往上換成另一個、按鈕微微浮起

- 元件 Component: 按鈕 (`button`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動
- 風格／關鍵字 Style: 社群 圖示 icon 填滿 頁尾 IG Threads Social Icon Fill Hover Footer hover 懸停 滑過
- 標籤 Tag: CSS hover
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-20

**AI 提示詞（網站複製格式）:**

```text
「社群圖示填滿（Social Icon Fill）」動態效果：頁尾的一排圓形社群圖示（外框細線、中間是線條圖示）：滑鼠滑過某個圖示時，實心底色從圓形底部往上升起填滿，原本的圖示往上滑出，同一個圖示的反色版本從下方滑入取代，整顆按鈕微微往上浮起；滑開時反向回復。約 0.45 秒。（CSS：圓形 overflow:hidden，底色層 translateY(101%) → 0；兩個圖示疊在同一格，一個往上移出、一個從下方移入）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx287">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「社群圖示填滿」.

### JavaScript — `FX[287]` from `site/fx.js`

```js
287(s,x,card){const w=el('div','ho-so');const I=[['IG','<rect x="4" y="4" width="16" height="16" rx="5"/><circle cx="12" cy="12" r="3.6"/><circle cx="17" cy="7" r=".6"/>'],['Threads','<path d="M16.5 11.2c-.4-2.6-2-3.9-4.4-3.9-2.6 0-4.3 1.9-4.3 4.7s1.7 4.8 4.3 4.8c2 0 3.4-1 3.4-2.6s-1.3-2.4-3.1-2.4c-1.5 0-2.5.7-2.5 1.8"/><path d="M19 12c0 4.4-2.8 8-7 8s-7-3.6-7-8 2.8-8 7-8c3 0 5.2 1.6 6.3 4.3"/>'],['Mail','<rect x="3" y="6" width="18" height="12" rx="2"/><path d="M3 7l9 6 9-6"/>'],['Link','<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>']];
  const its=I.map(([l,p])=>{const a=el('button','ho-sc');a.setAttribute('aria-label',l);a.innerHTML='<i></i><svg viewBox="0 0 24 24">'+p+'</svg><svg viewBox="0 0 24 24">'+p+'</svg>';w.append(a);return a});s.append(w);autoHover(w,its,card,900)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx287` rules from `site/fx.css`

_No dedicated `.fx287` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #287
