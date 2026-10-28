# 201 · SVG 濾鏡水波扭曲 — Turbulence Distortion

文字像隔著水面一樣持續波動扭曲

- 元件 Component: 圖形・SVG (`shape`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 標題・Hero、背景裝飾
- 風格／關鍵字 Style: 濾鏡 扭曲 水波 液態 熱浪 迷幻 SVG Filter Turbulence Displacement Distortion Liquid SVG 圖形
- 標籤 Tag: feTurbulence
- 範例文字 Example text: 「水波扭曲」（預覽底色：dark）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「SVG 濾鏡水波扭曲（Turbulence Distortion）」動態效果：大標題像隔著水面或熱浪一樣持續波動扭曲，扭曲的紋理與強度緩慢變化，文字仍可辨識但帶有液態、迷幻的感覺。（SVG filter：feTurbulence 產生雜訊、feDisplacementMap 依雜訊位移原圖，用 animate 讓 baseFrequency 與 scale 在數值間循環；在 HTML 元素上以 CSS filter:url(#id) 套用；注意效能，避免套在大面積或大量元素上）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx201">`, preview text 「水波扭曲」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「SVG 濾鏡水波扭曲」.

### JavaScript — `FX[201]` from `site/fx.js`

```js
201(s,x){const id='tb'+Math.random().toString(36).slice(2);s.insertAdjacentHTML('beforeend',`<svg width="0" height="0" style="position:absolute"><filter id="${id}" x="-10%" y="-10%" width="120%" height="120%"><feTurbulence type="fractalNoise" baseFrequency="0.012 0.04" numOctaves="2" seed="3"><animate attributeName="baseFrequency" dur="6s" values="0.012 0.045;0.025 0.08;0.012 0.045" repeatCount="indefinite"/></feTurbulence><feDisplacementMap in="SourceGraphic" scale="20"><animate attributeName="scale" dur="3s" values="8;22;8" repeatCount="indefinite"/></feDisplacementMap></filter></svg>`);
  const t=T(x,Math.min(15,64/chars(x).length));t.classList.add('tbt');t.style.filter=`url(#${id})`;s.append(t)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx201` rules from `site/fx.css`

_No dedicated `.fx201` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #201
