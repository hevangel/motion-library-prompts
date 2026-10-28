# 113 · 光暈邊框卡片 — Spotlight Card

游標經過時，卡片邊框與內部被一團光照亮

- 元件 Component: 卡片・群組 (`card`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動
- 風格／關鍵字 Style: 卡片 光暈 邊框 聚光 游標 發光 Spotlight Card Glow Border Linear Vercel
- 標籤 Tag: radial-gradient
- 範例文字 Example text: 「設計 開發 行銷」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「光暈邊框卡片（Spotlight Card）」動態效果：一排低調的卡片，游標在卡片附近移動時，靠近游標的那段卡片邊框會被一團光照亮（強調色），卡片內部也有一層很淡的光暈跟著游標；光只照亮游標附近，離越遠越暗，所以同時能看到相鄰卡片的邊緣也被微微點亮。（做法：mousemove 時算出游標相對每張卡片的座標寫入 --x、--y；::before 用 radial-gradient(circle at var(--x) var(--y)) 搭配 mask-composite 只顯示邊框那一圈，::after 做內部柔光）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx113">`, preview text 「設計 開發 行銷」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「光暈邊框卡片」.

### JavaScript — `FX[113]` from `site/fx.js`

```js
113(s,x,card){const l=el('div','abs gl');const w=el('div','spw');const ws=words(x);const cs=[0,1,2].map(i=>{const c=el('div','spc');c.innerHTML='<i></i><b></b><span></span><span class="s"></span>';c.querySelector('b').textContent=ws[i%ws.length];w.append(c);return c});l.append(w);s.append(l);
  vpointer(l,card,(px,py)=>cs.forEach(c=>{c.style.setProperty('--x',px-c.offsetLeft+'px');c.style.setProperty('--y',py-c.offsetTop+'px')}))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx113` rules from `site/fx.css`

_No dedicated `.fx113` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #113
