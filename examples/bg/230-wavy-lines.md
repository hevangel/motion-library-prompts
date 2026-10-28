# 230 · 起伏線條 — Wavy Lines

一整片細線像布料般起伏，游標經過的地方被輕輕拱起

- 元件 Component: 背景・氛圍 (`bg`)
- 時機 Timing: 循環待機、懸停・點擊
- 技術 Tech: Canvas
- 情境 Uses: 標題・Hero、背景裝飾
- 風格／關鍵字 Style: 線條 波浪 起伏 布料 地形 等高線 Wavy Lines Wave Field Terrain Canvas 互動背景 requestAnimationFrame 背景 氛圍
- 標籤 Tag: Canvas 2D
- 範例文字 Example text: 「Flow」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「起伏線條（Wavy Lines）」動態效果：整個背景是約 26 條水平細線，每條線由兩組不同頻率的正弦波疊加而起伏，並隨時間緩慢流動，相鄰的線相位略錯開，整片看起來像飄動的布料或地形線；其中每隔幾條用較粗、較亮的線點綴；游標經過的地方，附近的線條會被平滑地往上拱起，離開後恢復。（Canvas 2D：每條線取 80 個點，y = 基準 + sin(x×f1 + t + j×相位) × A1 + sin(x×f2 − t + j×相位) × A2，再減去以游標為中心的高斯函數 × 高度）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx230">`, preview text 「Flow」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「起伏線條」.

### JavaScript — `FX[230]` from `site/fx.js`

```js
230(s,x,card){cfx(s,card,{init:()=>({c:accRGB(s)}),
  frame:(c,W,H,t,dt,m,o)=>{c.fillStyle=`rgb(${BGD})`;c.fillRect(0,0,W,H);const N=26,[mx,my]=demoPt(t,W,H,m),R=W*.16;
    for(let j=0;j<N;j++){const by=H*(.08+j/N*.9),k=j/N;c.strokeStyle=j%6===3?`rgba(${o.c},.9)`:`rgba(255,255,255,${.12+k*.3})`;c.lineWidth=j%6===3?1.6:1;c.beginPath();
      for(let i=0;i<=80;i++){const X=i/80*W;let y=by+Math.sin(X*.011+t*.7+j*.35)*H*.025+Math.sin(X*.004-t*.4+j*.2)*H*.04;const d=X-mx,dy=by-my,g=Math.exp(-(d*d+dy*dy)/(2*R*R));y-=g*H*.09;i?c.lineTo(X,y):c.moveTo(X,y)}c.stroke()}}});
  const tx=T(x,Math.min(11,52/chars(x).length));tx.classList.add('cvt');s.append(tx)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx230` rules from `site/fx.css`

_No dedicated `.fx230` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #230
