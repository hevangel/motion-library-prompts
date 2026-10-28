# 285 · 圖示微動畫 — Icon Micro-animations

滑過圖示時各自做出符合意思的小動作：鈴鐺搖、愛心跳、齒輪轉、垃圾桶掀蓋

- 元件 Component: 圖形・SVG (`shape`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動、App 介面
- 風格／關鍵字 Style: 圖示 icon 微動畫 鈴鐺 愛心 齒輪 垃圾桶 Icon Micro Animation Bell Heart Gear Trash Hover hover 懸停 滑過
- 標籤 Tag: CSS keyframes
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-20

**AI 提示詞（網站複製格式）:**

```text
「圖示微動畫（Icon Micro-animations）」動態效果：一排功能圖示按鈕（通知、收藏、設定、刪除），滑鼠滑過時圖示的底色亮起，並各自做出符合意思的微動畫：鈴鐺以頂端為軸左右搖晃幾下後停住；愛心填滿並跳動一下；齒輪的齒轉 90 度並帶一點回彈；垃圾桶的蓋子以左端為軸掀開一個角度。讓介面更有生命力又不干擾。（CSS：SVG 圖示的特定部位設 transform-origin（SVG 內元素記得 transform-box:fill-box），:hover 時套用各自的 keyframes 或 transform transition）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx285">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「圖示微動畫」.

### JavaScript — `FX[285]` from `site/fx.js`

```js
285(s,x,card){const w=el('div','ho-ic');const I=[['bell','<path d="M6 16V11a6 6 0 0 1 12 0v5l1.5 2h-15z"/><path d="M10 20a2 2 0 0 0 4 0"/>','通知'],['heart','<path d="M12 20s-7-4.5-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.5-7 10-7 10z"/>','收藏'],['gear','<circle cx="12" cy="12" r="3"/><path d="M12 3v3M12 18v3M3 12h3M18 12h3M5.6 5.6l2.1 2.1M16.3 16.3l2.1 2.1M5.6 18.4l2.1-2.1M16.3 7.7l2.1-2.1"/>','設定'],['trash','<g class="lid"><path d="M4 7h16"/><path d="M9 7V4h6v3"/></g><path d="M6 7l1 13h10l1-13"/>','刪除']];
  const its=I.map(([k,p,l])=>{const b=el('button','ho-ib '+k);b.innerHTML='<svg viewBox="0 0 24 24">'+p+'</svg><span>'+l+'</span>';b.setAttribute('aria-label',l);w.append(b);return b});s.append(w);autoHover(w,its,card,900)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx285` rules from `site/fx.css`

_No dedicated `.fx285` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #285
