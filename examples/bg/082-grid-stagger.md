# 082 · 格狀擴散 — Grid Stagger

格子從中心向外一波波縮放

- 元件 Component: 背景・氛圍 (`bg`)
- 時機 Timing: 循環待機
- 技術 Tech: GSAP
- 情境 Uses: 背景裝飾
- 風格／關鍵字 Style: 
- 標籤 Tag: Grid stagger
- 範例文字 Example text: 「動」（預覽底色：acc）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「格狀擴散（Grid Stagger）」動態效果：同一個字排成 10×5 的格子，從中心向外一波波縮小旋轉變淡，再從邊緣往內放大轉回，形成波紋。（GSAP：stagger { grid:[5,10], from:"center" / "edges", amount:1 }）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage acc fx82">`, preview text 「動」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「格狀擴散」.

### JavaScript — `FX[82]` from `site/fx.js`

```js
82(s,x){const g=el('div','gg');const ch=chars(x)[0];for(let i=0;i<50;i++){const e=el('span');e.textContent=ch;g.append(e)}s.append(g);const c=g.children;
  gsap.timeline({repeat:-1}).to(c,{scale:.2,rotation:180,opacity:.3,duration:.7,ease:'power2.inOut',stagger:{grid:[5,10],from:'center',amount:1}}).to(c,{scale:1,rotation:360,opacity:1,duration:.7,ease:'power2.inOut',stagger:{grid:[5,10],from:'edges',amount:1}}).set(c,{rotation:0})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx82` rules from `site/fx.css`

_No dedicated `.fx82` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #82
