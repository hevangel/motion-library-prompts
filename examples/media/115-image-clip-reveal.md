# 115 · 圖片遮罩揭示 — Image Clip Reveal

圖片從下往上被揭開，同時由放大慢慢縮回原尺寸

- 元件 Component: 圖片・媒體 (`media`)
- 時機 Timing: 進場、退場
- 技術 Tech: CSS
- 情境 Uses: 轉場切換、標題・Hero
- 風格／關鍵字 Style: 圖片 照片 遮罩 揭示 進場 clip-path Image Reveal Mask Wipe Zoom
- 標籤 Tag: clip-path
- 範例文字 Example text: 「」（預覽底色：cream，固定文字）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「圖片遮罩揭示（Image Clip Reveal）」動態效果：圖片進場時，外框像窗簾一樣由下往上被揭開，框內的圖片同時從約 1.35 倍慢慢縮回原尺寸，形成「揭開＋鏡頭拉遠」的層次；停留後再由下往上收起消失。揭開約 1.2 秒，緩入緩出（cubic-bezier(.7,0,.2,1)）。（CSS：外框用 clip-path:inset() 的 keyframes 從 inset(100% 0 0 0) 到 inset(0)；內層圖片 transform:scale 1.35→1；實際網站可配合捲動進入畫面時才播放）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage cream fx115">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「圖片遮罩揭示」.

### JavaScript — `FX[115]` from `site/fx.js`

```js
115(s){const f=el('div','rv');f.innerHTML=scene('#9fd3ff','#ffe1b0','#4f7a6a','#264a3f','#fff6d8');s.append(f)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx115` rules from `site/fx.css`

_No dedicated `.fx115` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #115
