# 191 · 緩慢推鏡 — Ken Burns

圖片持續緩慢放大並微微平移，像紀錄片的推鏡

- 元件 Component: 圖片・媒體 (`media`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 標題・Hero、背景裝飾
- 風格／關鍵字 Style: 推鏡 慢速 放大 平移 相片 紀錄片 Ken Burns Slow Zoom Pan Photo Canva 風格 Canva Photo Zoom 相片放大 簡報 社群貼文 動畫
- 標籤 Tag: CSS keyframes
- 範例文字 Example text: 「海岸線」（預覽底色：dark）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「緩慢推鏡（Ken Burns）」動態效果：照片在固定的外框內非常緩慢地放大（約 9 秒放大到 1.22 倍）並同時往一側輕微平移，然後再慢慢退回，來回循環，像紀錄片中對靜態照片的推鏡，讓靜態圖片產生生命感；圖片上的標題保持不動。（CSS：外框 overflow:hidden，內層圖片 keyframes scale(1)→scale(1.22) translate(-4%, 2%)，ease-in-out，alternate infinite，transform-origin 設在主體附近）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx191">`, preview text 「海岸線」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「緩慢推鏡」.

### JavaScript — `FX[191]` from `site/fx.js`

```js
191(s,x){const w=el('div','kbw');w.innerHTML=scene('#ffb36b','#ff6b8b','#8a3f6e','#3b1f45','#fff3d6');const t=T(x,Math.min(6,36/chars(x).length));t.classList.add('kbt');w.append(t);s.append(w)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx191` rules from `site/fx.css`

_No dedicated `.fx191` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #191
