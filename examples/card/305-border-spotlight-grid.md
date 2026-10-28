# 305 · 邊框聚光網格 — Border Spotlight Grid

游標在卡片群之間移動時，靠近的卡片邊框和內部被一團光照亮

- 元件 Component: 卡片・群組 (`card`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動、標題・Hero
- 風格／關鍵字 Style: 邊框 聚光 光暈 網格 功能介紹 SaaS Linear Border Spotlight Glow Grid Feature Cards 卡片 群組
- 標籤 Tag: radial-gradient
- 範例文字 Example text: 「速度 安全 協作 整合 分析 支援」（預覽底色：dark）
- 收錄日期 Added: 2026-10-20

**AI 提示詞（網站複製格式）:**

```text
「邊框聚光網格（Border Spotlight Grid）」動態效果：功能介紹區的一組卡片排成網格，每張卡片的邊框是細細的一圈：游標在整個區塊內移動時，每張卡片都在「游標相對於自己的位置」畫一團柔和的光，所以靠近游標的卡片邊框被照亮成強調色、內部也帶淡淡光暈，遠離的卡片幾乎不亮；游標在卡片之間移動，光會自然地跨越相鄰卡片的邊框。（CSS：卡片外層 padding 1px 當邊框，背景 radial-gradient(circle at var(--x) var(--y), 強調色, 透明)；內層用另一個較淡的 radial-gradient；JS 在容器 mousemove 時為每張卡片計算相對座標寫入 --x、--y）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx305">`, preview text 「速度 安全 協作 整合 分析 支援」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「邊框聚光網格」.

### JavaScript — `FX[305]` from `site/fx.js`

```js
305(s,x,card){const ws=words(x);const g=el('div','abs gl cg-bs');const gr=el('div','cg-bg');const cs=[0,1,2,3,4,5].map(i=>{const c=el('div','cg-bc');c.innerHTML='<div class="cg-bi"><i></i><b></b><small>滑過看看邊框光</small></div>';c.querySelector('b').textContent=ws[i%ws.length];gr.append(c);return c});g.append(gr);s.append(g);
  vpointer(g,card,(px,py)=>{const q=g.getBoundingClientRect();cs.forEach(c=>{const r=c.getBoundingClientRect();c.style.setProperty('--x',(px-(r.left-q.left))+'px');c.style.setProperty('--y',(py-(r.top-q.top))+'px')})})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx305` rules from `site/fx.css`

_No dedicated `.fx305` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #305
