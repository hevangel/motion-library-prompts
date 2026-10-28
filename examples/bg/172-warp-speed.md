# 172 · 星空穿越 — Warp Speed

星星從中心往外飛成光線，游標移入時加速

- 元件 Component: 背景・氛圍 (`bg`)
- 時機 Timing: 循環待機、懸停・點擊
- 技術 Tech: Canvas
- 情境 Uses: 標題・Hero、背景裝飾
- 風格／關鍵字 Style: 星空 星星 穿越 太空 光速 隧道 Starfield Warp Hyperspace Space Canvas 粒子 particles requestAnimationFrame 互動背景
- 標籤 Tag: Canvas 3D
- 範例文字 Example text: 「加速前進」（預覽底色：dark）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「星空穿越（Warp Speed）」動態效果：Hero 背景是一片往鏡頭飛來的星星：每顆星星從畫面中心附近出發，越靠近觀者越亮、越大，並拉出放射狀的短光線，像太空船加速穿越；游標移入區塊時速度平滑加快，而且消失點會微微往游標方向偏移，移開後緩緩回到巡航速度。前景標題保持清楚。（Canvas 2D：每顆星有 x、y、z，每幀 z 遞減，投影座標 = 中心 + x/z × 焦距，從上一幀投影位置畫線到這一幀；畫面用半透明底色覆蓋做出殘影）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx172">`, preview text 「加速前進」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「星空穿越」.

### JavaScript — `FX[172]` from `site/fx.js`

```js
172(s,x,card){cfx(s,card,{init:()=>({S:[...Array(320)].map(()=>({x:rnd(-1,1),y:rnd(-1,1),z:rnd(.05,1),pz:0})),v:.25,c:accRGB(s)}),
  frame:(c,W,H,t,dt,m,o)=>{o.v+=((m.in?1.4:.25)-o.v)*.05;c.fillStyle=`rgba(${BGD},.55)`;c.fillRect(0,0,W,H);const cx=W/2+(m.in?(m.x-W/2)*.25:0),cy=H/2+(m.in?(m.y-H/2)*.25:0),F=W*.45;
    o.S.forEach((p,i)=>{p.pz=p.z;p.z-=o.v*dt;if(p.z<=.02){p.x=rnd(-1,1);p.y=rnd(-1,1);p.z=1;p.pz=1}const sx=cx+p.x/p.z*F,sy=cy+p.y/p.z*F,px=cx+p.x/p.pz*F,py=cy+p.y/p.pz*F;
      c.strokeStyle=i%5?`rgba(255,255,255,${1-p.z})`:`rgba(${o.c},${1-p.z})`;c.lineWidth=(1-p.z)*2.2;c.beginPath();c.moveTo(px,py);c.lineTo(sx,sy);c.stroke()})}});
  const tx=T(x,Math.min(11,56/chars(x).length));tx.classList.add('cvt');s.append(tx)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx172` rules from `site/fx.css`

_No dedicated `.fx172` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #172
