# 106 · 流動光暈漸層 — Aurora Gradient

幾團模糊光暈緩慢漂移交融，像極光一樣流動

- 元件 Component: 背景・氛圍 (`bg`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 背景裝飾、標題・Hero
- 風格／關鍵字 Style: 背景 極光 漸層 光暈 Aurora Mesh Gradient Blob Glow Hero 背景
- 標籤 Tag: CSS blur
- 範例文字 Example text: 「Aurora」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「流動光暈漸層（Aurora Gradient）」動態效果：Hero 區塊背景放 3–4 團大型圓形光暈，經過強烈模糊後互相重疊交融，各自以不同速度（約 9–16 秒）緩慢漂移、放大縮小、來回擺盪，形成像極光一樣持續流動的漸層；前景標題保持清楚可讀。（CSS：每團用大尺寸圓形 + filter:blur + mix-blend-mode:screen，各自設不同 animation-duration 與負的 animation-delay，animation-direction:alternate）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx106">`, preview text 「Aurora」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「流動光暈漸層」.

### JavaScript — `FX[106]` from `site/fx.js`

```js
106(s,x){const a=el('div','aur');for(let i=0;i<4;i++)a.append(el('i'));s.append(a,T(x,Math.min(14,60/chars(x).length)))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx106` rules from `site/fx.css`

```css
.fx106 .t{color:#fff;mix-blend-mode:overlay;z-index:1}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #106
