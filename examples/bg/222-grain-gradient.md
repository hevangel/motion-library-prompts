# 222 · 顆粒漸層 — Grain Gradient

柔和的大片漸層緩慢流動，上面疊一層細微跳動的底片顆粒

- 元件 Component: 背景・氛圍 (`bg`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 標題・Hero、背景裝飾
- 風格／關鍵字 Style: 顆粒 雜訊 底片 噪點 漸層 質感 Grain Noise Film Gradient Texture 網格漸層 mesh gradient 背景 氛圍
- 標籤 Tag: SVG noise
- 範例文字 Example text: 「Grain」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「顆粒漸層（Grain Gradient）」動態效果：Hero 背景是三團大面積、邊緣柔和的漸層光暈，以約 12 秒的週期緩慢交錯移動、來回飄移；上方再疊一層非常細的底片顆粒（雜訊）紋理，顆粒每秒跳動數次，讓畫面有類比印刷般的質感，前景標題保持清楚。（CSS：多個 radial-gradient 疊在同一背景，以 keyframes 動畫 background-position；顆粒層用 SVG feTurbulence 產生的雜訊當 background-image，mix-blend-mode:overlay、低透明度，用 steps() 的 keyframes 隨機位移製造跳動）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx222">`, preview text 「Grain」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「顆粒漸層」.

### JavaScript — `FX[222]` from `site/fx.js`

```js
222(s,x){s.append(el('div','abs bga-grd'),el('div','abs bga-grain'),T(x,Math.min(12,56/chars(x).length)))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx222` rules from `site/fx.css`

```css
.fx222 .t,.fx224 .t,.fx227 .t,.fx231 .t{color:#fff;z-index:1;text-shadow:0 .4cqw 2cqw #0006}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #222
