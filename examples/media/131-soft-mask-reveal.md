# 131 · 柔邊遮罩揭示 — Soft Mask Reveal

圖片由左到右被一道柔和的漸層邊緣揭開

- 元件 Component: 圖片・媒體 (`media`)
- 時機 Timing: 進場
- 技術 Tech: GSAP
- 情境 Uses: 標題・Hero、轉場切換
- 風格／關鍵字 Style: 圖片 照片 遮罩 柔邊 漸層 揭示 羽化 溫和 柔和 輕柔 引導 動線 視線 閱讀順序 低調 Subtle Gentle Soft Entrance Visual Flow Hierarchy
- 標籤 Tag: Soft mask
- 範例文字 Example text: 「」（預覽底色：cream，固定文字）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「柔邊遮罩揭示（Soft Mask Reveal）」動態效果：圖片進場時，一道帶羽化邊緣的漸層遮罩由左往右慢慢掃過，把圖片柔和地揭開（不是硬切的直線），同時圖片從 1.08 倍、稍微偏左的位置慢慢縮回原尺寸定位，約 1.9–2.3 秒、平順減速，比硬邊遮罩更安靜、更有質感。（CSS + GSAP：外框 mask:linear-gradient(90deg, #000 var(--p), transparent calc(var(--p) + 25%))，用 GSAP tween --p 從 -25 到 100；內層圖片 scale 1.08→1、x -8→0）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage cream fx131">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「柔邊遮罩揭示」.

### JavaScript — `FX[131]` from `site/fx.js`

```js
131(s){const f=el('div','smr');f.innerHTML=scene('#ffd9c2','#c9b6ff','#7b6ca8','#3f3566','#fff6e6');s.append(f);
  gsap.timeline({repeat:-1,repeatDelay:.3}).set(f,{opacity:1},0).fromTo(f,{'--p':-25},{'--p':100,duration:1.9,ease:'power2.out'},0).fromTo(f.querySelector('svg'),{scale:1.08,x:-8},{scale:1,x:0,duration:2.3,ease:'power2.out'},0).to(f,{opacity:0,duration:.6},'+=1.6')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx131` rules from `site/fx.css`

_No dedicated `.fx131` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #131
