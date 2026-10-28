# 123 · 旋轉文字環游標 — Rotating Text Cursor

一圈環狀文字繞著游標持續旋轉

- 元件 Component: 游標 (`cursor`)
- 時機 Timing: 懸停・點擊、循環待機
- 技術 Tech: CSS
- 情境 Uses: 介面互動、Logo・品牌
- 風格／關鍵字 Style: 游標 文字環 環狀文字 旋轉 圓形文字 Rotating Text Ring Circular Text Cursor Badge SCROLL
- 標籤 Tag: SVG textPath
- 範例文字 Example text: 「SCROLL · EXPLORE」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「旋轉文字環游標（Rotating Text Cursor）」動態效果：隱藏系統游標，改成一個小圓點，外圍是一圈沿圓形排列的文字（例如「SCROLL · EXPLORE ·」重複），文字環持續慢慢旋轉（約 8 秒一圈），整組帶一點延遲感地跟著游標移動；背景的大標題保持很淡，讓游標成為焦點。（做法：SVG 圓形 path + textPath，用 textLength 讓文字剛好繞滿一圈；外層 transform 跟隨游標，內層 svg 用 CSS 旋轉動畫）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx123">`, preview text 「SCROLL · EXPLORE」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「旋轉文字環游標」.

### JavaScript — `FX[123]` from `site/fx.js`

```js
123(s,x,card){const l=el('div','abs gl tcur');l.append(T('探索作品',12));const id='tc'+Math.random().toString(36).slice(2);const u=x+' • ';const c=el('div','tcr');
  c.innerHTML=`<svg viewBox="0 0 100 100"><defs><path id="${id}" d="M50,50 m-38,0 a38,38 0 1,1 76,0 a38,38 0 1,1 -76,0"/></defs><text font-size="10" font-weight="800"><textPath href="#${id}" textLength="236" lengthAdjust="spacing"></textPath></text></svg><i></i>`;
  c.querySelector('textPath').textContent=rep(u,Math.max(1,Math.round(24/chars(u).length)));l.append(c);s.append(l);vpointer(l,card,(px,py)=>c.style.transform=`translate(${px}px,${py}px)`)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx123` rules from `site/fx.css`

_No dedicated `.fx123` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #123
