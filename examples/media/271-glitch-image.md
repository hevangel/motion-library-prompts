# 271 · 故障錯位圖片 — Glitch Image

滑過時圖片分出兩層色版左右錯位、一段段閃爍，像訊號不良

- 元件 Component: 圖片・媒體 (`media`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動、強調重點
- 風格／關鍵字 Style: 故障 glitch 錯位 色版 訊號 賽博 Glitch Image RGB Split Distortion Cyberpunk 圖片 媒體
- 標籤 Tag: CSS clip-path
- 範例文字 Example text: 「SIGNAL」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「故障錯位圖片（Glitch Image）」動態效果：滑鼠滑過圖片時觸發故障效果：圖片疊出兩個不同色版的複本，以「濾色」混合模式疊在原圖上，各自左右錯開幾個百分比，並用 clip-path 只顯示隨機的水平條帶，快速跳動閃爍；原圖本身也小幅左右抖動；中間的標題文字出現左右錯開的兩道色邊；滑開後恢復正常。（CSS：兩個複本用 filter:sepia + saturate + hue-rotate 做成不同色版、mix-blend-mode:screen；keyframes 搭配 steps() 改變 transform 與 clip-path: inset(...)）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx271">`, preview text 「SIGNAL」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「故障錯位圖片」.

### JavaScript — `FX[271]` from `site/fx.js`

```js
271(s,x,card){const f=el('div','md-gc');f.innerHTML=mdImg(2,'o')+mdImg(2,'c1')+mdImg(2,'c2')+'<b class="md-gx"></b>';f.querySelector('.md-gx').textContent=x;s.append(f);autoHover(f,[f],card,1700)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx271` rules from `site/fx.css`

_No dedicated `.fx271` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #271
