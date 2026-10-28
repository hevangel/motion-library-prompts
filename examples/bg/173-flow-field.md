# 173 · 流場線條 — Flow Field

上千條細線順著看不見的氣流緩慢流動，游標會攪動氣流

- 元件 Component: 背景・氛圍 (`bg`)
- 時機 Timing: 循環待機、懸停・點擊
- 技術 Tech: Canvas
- 情境 Uses: 背景裝飾、標題・Hero
- 風格／關鍵字 Style: 流場 氣流 線條 生成藝術 有機 Flow Field Generative Art Perlin Noise Lines Canvas 粒子 particles requestAnimationFrame 互動背景
- 標籤 Tag: Canvas trails
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「流場線條（Flow Field）」動態效果：背景佈滿數百個看不見的小粒子，每個粒子依照所在位置的「流向」（由平滑變化的雜訊或三角函數決定，且隨時間緩慢改變）前進並留下很細的軌跡，軌跡慢慢淡出，整體像風或水流的紋理不斷流動；游標附近的流向會被扭轉，形成被攪動的漩渦。（Canvas 2D：每幀先用低透明度的底色覆蓋畫面製造拖尾，再讓每個粒子依 angle = f(x, y, t) 前進一小段並畫線；粒子壽命到了或出界就重生；可用 simplex noise 讓流場更自然）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx173">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「流場線條」.

### JavaScript — `FX[173]` from `site/fx.js`

```js
173(s,x,card){cfx(s,card,{init:(c,W,H)=>{c.fillStyle=`rgb(${BGD})`;c.fillRect(0,0,W,H);return{P:[...Array(700)].map(()=>({x:rnd(0,W),y:rnd(0,H),l:rnd(0,200)})),c:accRGB(s)}},
  frame:(c,W,H,t,dt,m,o)=>{c.fillStyle=`rgba(${BGD},.06)`;c.fillRect(0,0,W,H);c.lineWidth=1;const [mx,my]=demoPt(t,W,H,m),R=W*.18;
    o.P.forEach((p,i)=>{let a=(Math.sin(p.x*.012+t*.25)+Math.cos(p.y*.014-t*.18)+Math.sin((p.x+p.y)*.006))*Math.PI*.8;const dx=p.x-mx,dy=p.y-my,d=Math.hypot(dx,dy);if(d<R)a+=(1-d/R)*Math.PI*.9;
      const nx=p.x+Math.cos(a)*W*.0025,ny=p.y+Math.sin(a)*W*.0025;c.strokeStyle=i%3?`rgba(${o.c},.55)`:'rgba(255,255,255,.35)';c.beginPath();c.moveTo(p.x,p.y);c.lineTo(nx,ny);c.stroke();p.x=nx;p.y=ny;
      if(--p.l<0||p.x<0||p.x>W||p.y<0||p.y>H){p.x=rnd(0,W);p.y=rnd(0,H);p.l=rnd(100,260)}})}})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx173` rules from `site/fx.css`

_No dedicated `.fx173` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #173
