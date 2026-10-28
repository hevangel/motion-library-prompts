# 104 · 卡片依序浮現 — Staggered Card Reveal

一組卡片從左上往右下依序浮上、由模糊變清楚

- 元件 Component: 卡片・群組 (`card`)
- 時機 Timing: 進場、退場
- 技術 Tech: GSAP
- 情境 Uses: 介面互動、轉場切換
- 風格／關鍵字 Style: 卡片 群組 列表 進場 依序 錯開 浮現 淡入 Stagger Fade Up Grid Reveal List Entrance
- 標籤 Tag: Grid stagger
- 範例文字 Example text: 「品牌 網站 App 海報 包裝 插畫」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「卡片依序浮現（Staggered Card Reveal）」動態效果：3 欄 × 2 列的作品卡片（上方縮圖、下方標題與兩條文字列），進場時每張卡片從下方 30px、95% 大小、模糊且透明的狀態浮上來變清楚，順序從左上往右下斜向依序錯開（總共約 0.6 秒）；卡片內的縮圖、標題、文字列再稍微延遲逐一補上；停留後從最後一張開始反向往上淡出。緩出（power3.out）。（GSAP：stagger { grid:[2,3], from:"start", amount:0.6 }，fromTo y / opacity / scale / filter:blur；實際網站可搭配 ScrollTrigger 在捲到時才播放、或用 ScrollTrigger.batch 讓列表分批進場）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx104">`, preview text 「品牌 網站 App 海報 包裝 插畫」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「卡片依序浮現」.

### JavaScript — `FX[104]` from `site/fx.js`

```js
104(s,x){const g=el('div','cg');const ws=words(x);for(let i=0;i<6;i++){const c=el('div','cgc');c.innerHTML='<i class="th"></i><b></b><span class="ln"></span><span class="ln s"></span>';c.querySelector('b').textContent=ws[i%ws.length];c.querySelector('.th').style.background=GC[i%5];g.append(c)}s.append(g);
  const cs=g.children,inner=g.querySelectorAll('.th,b,.ln'),grid={grid:[2,3]};
  gsap.timeline({repeat:-1,repeatDelay:.4})
    .fromTo(cs,{y:30,opacity:0,scale:.94,filter:'blur(6px)'},{y:0,opacity:1,scale:1,filter:'blur(0px)',duration:.7,ease:'power3.out',stagger:{...grid,from:'start',amount:.6}})
    .fromTo(inner,{y:8,opacity:0},{y:0,opacity:1,duration:.4,ease:'power2.out',stagger:.02},'-=.65')
    .to(cs,{y:-16,opacity:0,duration:.4,ease:'power2.in',stagger:{...grid,from:'end',amount:.3}},'+=1.6')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx104` rules from `site/fx.css`

_No dedicated `.fx104` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #104
