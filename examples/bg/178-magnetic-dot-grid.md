# 178 · 磁力點陣 — Magnetic Dot Grid

滿版小圓點，游標經過時被推開並放大

- 元件 Component: 背景・氛圍 (`bg`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: Canvas
- 情境 Uses: 背景裝飾、介面互動
- 風格／關鍵字 Style: 點陣 圓點 網格 磁力 排斥 互動背景 Dot Grid Repel Magnetic Interactive Background Canvas 粒子 particles requestAnimationFrame 互動背景
- 標籤 Tag: Canvas spring
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「磁力點陣（Magnetic Dot Grid）」動態效果：背景是整齊排列的細小圓點，游標移動時，附近的圓點被往外推開並變大、改用強調色，距離越近推得越遠，離開後以彈簧般的動作回到原位，形成跟著游標流動的凹陷。低調但很有互動感的背景。（Canvas 2D：每個點記錄原始位置，目標位置 = 原位 + 遠離游標方向 × 影響係數，用速度 + 阻尼做彈簧回彈；大小與透明度依距離插值）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx178">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「磁力點陣」.

### JavaScript — `FX[178]` from `site/fx.js`

```js
178(s,x,card){cfx(s,card,{init:(c,W,H)=>{const g=W/34,D=[];for(let y=g/2;y<H;y+=g)for(let xx=g/2;xx<W;xx+=g)D.push({ox:xx,oy:y,x:xx,y,vx:0,vy:0});return{D,g,c:accRGB(s)}},
  frame:(c,W,H,t,dt,m,o)=>{c.clearRect(0,0,W,H);const [mx,my]=demoPt(t,W,H,m),R=W*.14;
    o.D.forEach(p=>{const dx=p.ox-mx,dy=p.oy-my,d=Math.hypot(dx,dy)||1,k=Math.max(0,1-d/R);const tx=p.ox+dx/d*k*R*.45,ty=p.oy+dy/d*k*R*.45;p.vx+=(tx-p.x)*.15;p.vy+=(ty-p.y)*.15;p.vx*=.75;p.vy*=.75;p.x+=p.vx;p.y+=p.vy;
      c.fillStyle=k>.02?`rgba(${o.c},${.4+k*.6})`:'rgba(255,255,255,.22)';c.beginPath();c.arc(p.x,p.y,o.g*(.12+k*.22),0,7);c.fill()})}})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx178` rules from `site/fx.css`

_No dedicated `.fx178` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #178
