# 121 · 游標拖尾軌跡 — Cursor Trail

游標後面拖著一條漸細漸淡的線條

- 元件 Component: 游標 (`cursor`)
- 時機 Timing: 懸停・點擊、循環待機
- 技術 Tech: Canvas
- 情境 Uses: 介面互動、背景裝飾
- 風格／關鍵字 Style: 游標 拖尾 軌跡 線條 殘影 Cursor Trail Line Comet Canvas
- 標籤 Tag: Canvas trail
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「游標拖尾軌跡（Cursor Trail）」動態效果：游標移動時，後方拖著一條平滑的線條軌跡，越靠近游標越粗越清楚、越尾端越細越透明，像彗星尾巴；游標停下時，尾巴會逐漸收回到游標位置；游標本身是一顆小圓點。（Canvas 2D：每幀把游標座標推入陣列並只保留最近約 28 點，依序畫線段，線寬與透明度隨索引遞增；依 devicePixelRatio 設定畫布；容器 cursor:none）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx121">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「游標拖尾軌跡」.

### JavaScript — `FX[121]` from `site/fx.js`

```js
121(s,x,card){const cv=el('canvas','pnet trail');s.append(cv);const ctx=cv.getContext('2d');const col=getComputedStyle(s).getPropertyValue('--a').trim()||'#ff7a2f';let pts=[],m=null;
  cv.addEventListener('pointermove',e=>{const r=cv.getBoundingClientRect();m=[e.clientX-r.left,e.clientY-r.top]});cv.addEventListener('pointerleave',()=>m=null);
  ticks.set(card,t=>{const dpr=devicePixelRatio||1,W=s.offsetWidth,H=s.offsetHeight;if(!W)return;if(cv.width!==Math.round(W*dpr)){cv.width=Math.round(W*dpr);cv.height=Math.round(H*dpr)}
    const p=m||[W*(.5+.38*Math.sin(t*1.7)),H*(.5+.3*Math.sin(t*2.6+1))];pts.push(p);if(pts.length>28)pts.shift();
    ctx.setTransform(dpr,0,0,dpr,0,0);ctx.clearRect(0,0,W,H);ctx.lineCap='round';ctx.strokeStyle=col;
    for(let i=1;i<pts.length;i++){const k=i/pts.length;ctx.globalAlpha=k;ctx.lineWidth=k*W*.022;ctx.beginPath();ctx.moveTo(...pts[i-1]);ctx.lineTo(...pts[i]);ctx.stroke()}
    ctx.globalAlpha=1;ctx.fillStyle='#fff';ctx.beginPath();ctx.arc(p[0],p[1],W*.012,0,7);ctx.fill()})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx121` rules from `site/fx.css`

_No dedicated `.fx121` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #121
