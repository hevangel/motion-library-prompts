# 223 · 復古透視網格 — Retro Grid Horizon

地平線上一顆條紋夕陽，透視網格地板不斷往前推進

- 元件 Component: 背景・氛圍 (`bg`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 標題・Hero、背景裝飾
- 風格／關鍵字 Style: 復古 合成波 synthwave vaporwave 透視 網格 地板 地平線 夕陽 80年代 Retro Grid Horizon Perspective 背景 氛圍
- 標籤 Tag: CSS 3D
- 範例文字 Example text: 「RETRO WAVE」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「復古透視網格（Retro Grid Horizon）」動態效果：80 年代合成波風格的背景：畫面中間是一條地平線，上方是一顆下半部被水平條紋切開的圓形夕陽並帶柔光；下方是一片透視傾斜的網格地板，格線持續朝觀者方向推進、遠處漸隱，形成無限往前開的感覺；標題浮在夕陽上方並帶微微發光。（CSS：地板是兩組 linear-gradient 格線，transform:perspective + rotateX(72deg)，keyframes 讓 background-position 前進一格長度無縫循環；遠端用 mask 漸隱；夕陽條紋用 repeating-linear-gradient 的 mask）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx223">`, preview text 「RETRO WAVE」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「復古透視網格」.

### JavaScript — `FX[223]` from `site/fx.js`

```js
223(s,x){const w=el('div','abs bga-hz');w.innerHTML='<i class="bga-sun"></i><div class="bga-floor"></div>';s.append(w);const t=T(x,Math.min(11,52/chars(x).length));t.classList.add('bga-ht');s.append(t)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx223` rules from `site/fx.css`

_No dedicated `.fx223` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #223
