# 125 · 柔和上浮 — Gentle Fade Up

區塊內元素依閱讀順序由上到下輕輕浮現

- 元件 Component: 版面・頁面 (`layout`)
- 時機 Timing: 進場
- 技術 Tech: GSAP
- 情境 Uses: 標題・Hero
- 風格／關鍵字 Style: 區塊 段落 標題 上浮 淡入 溫和 柔和 輕柔 引導 動線 視線 閱讀順序 低調 Subtle Gentle Soft Entrance Visual Flow Hierarchy Canva 風格 Canva Rise 上升
- 標籤 Tag: Fade up
- 範例文字 Example text: 「讓設計說故事」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「柔和上浮（Gentle Fade Up）」動態效果：一個內容區塊（小標、主標題、兩行內文、按鈕）進場時，依照由上到下的閱讀順序，每個元素從下方約 18px、完全透明的狀態輕輕浮上並淡入，元素之間間隔約 0.14 秒，每個約 0.9 秒、平順減速（power2.out），沒有彈跳也沒有縮放，讓視線自然地從標題被帶到按鈕。（GSAP：fromTo y:18 / opacity:0 → y:0 / opacity:1，stagger 0.14；實際網站搭配 ScrollTrigger 在區塊進入畫面時播放一次即可）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx125">`, preview text 「讓設計說故事」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「柔和上浮」.

### JavaScript — `FX[125]` from `site/fx.js`

```js
125(s,x){const w=el('div','gs');w.innerHTML='<small>NEW · 2026</small><b></b><i class="ln"></i><i class="ln s"></i><span class="bt">了解更多</span>';w.querySelector('b').textContent=x;s.append(w);const it=w.children;
  gsap.timeline({repeat:-1,repeatDelay:.3}).fromTo(it,{y:18,opacity:0},{y:0,opacity:1,duration:.9,ease:'power2.out',stagger:.14}).to(it,{opacity:0,duration:.5,ease:'power1.in'},'+=1.8')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx125` rules from `site/fx.css`

_No dedicated `.fx125` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #125
