# 117 · 導覽列捲動縮小 — Shrinking Sticky Header

往下捲時導覽列變矮、Logo 縮小，並加上毛玻璃底

- 元件 Component: 版面・頁面 (`layout`)
- 時機 Timing: 捲動觸發
- 技術 Tech: CSS
- 情境 Uses: 捲動效果、介面互動
- 風格／關鍵字 Style: 導覽列 頁首 選單 header navbar 捲動 縮小 黏著 毛玻璃 Sticky Shrink Header On Scroll
- 標籤 Tag: Sticky
- 範例文字 Example text: 「LOGO」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「導覽列捲動縮小（Shrinking Sticky Header）」動態效果：頁首導覽列固定在最上方（sticky）。在頁面頂端時導覽列較高、Logo 較大、背景透明；一旦往下捲超過一點距離，導覽列平滑變矮、Logo 縮小，並出現半透明的毛玻璃背景與淡淡的陰影，捲回頂端時恢復原狀。約 0.35 秒過場。（做法：監聽 scroll，scrollY > 某個值時加上 .shrink class；CSS 對 padding、font-size、background、box-shadow 做 transition，背景用 backdrop-filter:blur）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx117">`, preview text 「LOGO」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「導覽列捲動縮小」.

### JavaScript — `FX[117]` from `site/fx.js`

```js
117(s,x,card){const sc=el('div','scr nopad');const h=el('header','shd');h.innerHTML='<b></b><nav><i></i><i></i><i></i></nav>';h.querySelector('b').textContent=x;const c=el('div','shc');for(let i=0;i<8;i++)c.append(el('i'));sc.append(h,c);s.append(sc);
  sc.addEventListener('scroll',()=>h.classList.toggle('sm',sc.scrollTop>12));let idle=0;['wheel','touchstart','pointerdown'].forEach(e=>sc.addEventListener(e,()=>idle=performance.now()+3500,{passive:true}));
  ticks.set(card,t=>{if(performance.now()<idle)return;sc.scrollTop=(.5-.5*Math.cos(t*.9))*(sc.scrollHeight-sc.clientHeight)})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx117` rules from `site/fx.css`

_No dedicated `.fx117` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #117
