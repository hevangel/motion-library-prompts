# 240 · 展開文字按鈕 — Expanding Button

平常只有圓形「+」圖示，滑過時向右展開出文字、加號旋轉

- 元件 Component: 按鈕 (`button`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動、App 介面
- 風格／關鍵字 Style: 展開 浮動按鈕 FAB 加號 圖示按鈕 Expanding Icon Button Floating Action Reveal Label 按鈕
- 標籤 Tag: CSS max-width
- 範例文字 Example text: 「新增專案」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「展開文字按鈕（Expanding Button）」動態效果：浮動操作按鈕平常是一顆只有「+」的圓形，滑鼠滑過時按鈕向右平滑展開成膠囊形，露出文字標籤（例如「新增專案」），加號同時旋轉 90 度；文字在展開一半後才淡入；滑開時收回成圓形。約 0.5 秒。（CSS：按鈕 overflow:hidden，用 max-width 從圓的寬度過渡到較大值，文字 opacity 加 transition-delay；加號 rotate(90deg)）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx240">`, preview text 「新增專案」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「展開文字按鈕」.

### JavaScript — `FX[240]` from `site/fx.js`

```js
240(s,x,card){const b=el('button','bx-ex');b.innerHTML='<b>+</b><span></span>';b.querySelector('span').textContent=x;b.style.fontSize=Math.min(5,40/chars(x).length)+'cqw';b.setAttribute('aria-label',x);s.append(b);autoHover(b,[b],card,1500)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx240` rules from `site/fx.css`

_No dedicated `.fx240` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #240
