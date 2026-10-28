# 108 · 粒子連線 — Particle Network

漂浮的粒子靠近時自動連線，游標會吸引附近粒子

- 元件 Component: 背景・氛圍 (`bg`)
- 時機 Timing: 循環待機、懸停・點擊
- 技術 Tech: Canvas
- 情境 Uses: 背景裝飾、標題・Hero
- 風格／關鍵字 Style: 背景 粒子 連線 網路 星座 Particles Network Constellation particles.js Canvas
- 標籤 Tag: Canvas 2D
- 範例文字 Example text: 「Network」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「粒子連線（Particle Network）」動態效果：背景有數十顆小粒子緩慢隨機漂浮、碰到邊界反彈；兩顆粒子距離夠近時自動連一條線，越近線越清楚、越遠越淡；游標移入時，附近粒子會被輕輕吸過去並和游標連線，形成像星座網路的效果。前景標題保持清楚。（Canvas 2D：requestAnimationFrame 每幀更新位置，兩兩計算距離畫線並依距離調整透明度；注意依 devicePixelRatio 設定畫布尺寸）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx108">`, preview text 「Network」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「粒子連線」.

### JavaScript — `FX[108]` from `site/fx.js`

```js
108(s,x,card){const cv=el('canvas','pnet');s.append(cv,T(x,Math.min(13,56/chars(x).length)));const ctx=cv.getContext('2d');const col=getComputedStyle(s).getPropertyValue('--a').trim()||'#3dd9b8';let P=[],m={x:-1e4,y:-1e4};
  cv.addEventListener('pointermove',e=>{const r=cv.getBoundingClientRect();m={x:(e.clientX-r.left)*devicePixelRatio,y:(e.clientY-r.top)*devicePixelRatio}});cv.addEventListener('pointerleave',()=>m={x:-1e4,y:-1e4});
  ticks.set(card,()=>{const dpr=devicePixelRatio||1,W=s.offsetWidth*dpr,H=s.offsetHeight*dpr;if(!W)return;
    if(cv.width!==W){cv.width=W;cv.height=H;P=[...Array(46)].map(()=>({x:Math.random()*W,y:Math.random()*H,vx:(Math.random()-.5)*.6*dpr,vy:(Math.random()-.5)*.6*dpr}))}
    const D=W*.16;ctx.clearRect(0,0,W,H);ctx.fillStyle=ctx.strokeStyle=col;
    P.forEach(p=>{p.x+=p.vx;p.y+=p.vy;if(p.x<0||p.x>W)p.vx*=-1;if(p.y<0||p.y>H)p.vy*=-1;const dm=Math.hypot(p.x-m.x,p.y-m.y);if(dm<D*1.4){p.x+=(m.x-p.x)*.012;p.y+=(m.y-p.y)*.012}});
    for(let i=0;i<P.length;i++){for(let j=i+1;j<P.length;j++){const d=Math.hypot(P[i].x-P[j].x,P[i].y-P[j].y);if(d<D){ctx.globalAlpha=(1-d/D)*.6;ctx.lineWidth=dpr;ctx.beginPath();ctx.moveTo(P[i].x,P[i].y);ctx.lineTo(P[j].x,P[j].y);ctx.stroke()}}
      const dm=Math.hypot(P[i].x-m.x,P[i].y-m.y);if(dm<D*1.4){ctx.globalAlpha=(1-dm/(D*1.4))*.9;ctx.beginPath();ctx.moveTo(P[i].x,P[i].y);ctx.lineTo(m.x,m.y);ctx.stroke()}
      ctx.globalAlpha=.9;ctx.beginPath();ctx.arc(P[i].x,P[i].y,1.8*dpr,0,7);ctx.fill()}ctx.globalAlpha=1})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx108` rules from `site/fx.css`

```css
.fx108 .t{color:#fff;z-index:1;pointer-events:none}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #108
