# 124 · 手電筒探照 — Flashlight Reveal

畫面一片暗，只有游標附近像手電筒一樣照出隱藏內容

- 元件 Component: 游標 (`cursor`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動、標題・Hero
- 風格／關鍵字 Style: 游標 手電筒 探照 聚光燈 揭示 遮罩 Flashlight Spotlight Reveal Mask Cursor Hidden
- 標籤 Tag: CSS mask
- 範例文字 Example text: 「找到我了」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「手電筒探照（Flashlight Reveal）」動態效果：整個區塊幾乎是暗的，大標題只隱約可見；游標所在位置像手電筒一樣照出一個邊緣柔和的圓形範圍，範圍內顯示出藏在下面、更鮮明的版本（清楚的標題與漸層背景），手電筒跟著游標移動，探照到哪就揭示到哪。（做法：上下兩層相同版面，上層是鮮明版本，用 mask:radial-gradient(circle at var(--mx) var(--my), #000 55%, transparent) 只露出游標附近；mousemove 時更新 --mx、--my）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx124">`, preview text 「找到我了」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「手電筒探照」.

### JavaScript — `FX[124]` from `site/fx.js`

```js
124(s,x,card){const l=el('div','abs fl1');l.innerHTML='<div class="b"></div><div class="r"></div>';l.querySelectorAll('div').forEach(d=>d.append(T(x,Math.min(16,64/chars(x).length))));s.append(l);
  vpointer(l,card,(px,py)=>{l.style.setProperty('--mx',px+'px');l.style.setProperty('--my',py+'px')})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx124` rules from `site/fx.css`

_No dedicated `.fx124` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #124
