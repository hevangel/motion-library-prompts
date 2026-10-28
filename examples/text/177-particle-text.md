# 177 · 文字粒子化 — Particle Text

文字由許多小點組成，游標靠近會被吹散，離開後聚回

- 元件 Component: 文字 (`text`)
- 時機 Timing: 懸停・點擊、進場
- 技術 Tech: Canvas
- 情境 Uses: 標題・Hero、Logo・品牌
- 風格／關鍵字 Style: 文字 粒子 點陣 吹散 聚合 互動標題 Particle Text Interactive Typography Scatter Canvas 粒子 particles requestAnimationFrame 互動背景
- 標籤 Tag: Canvas particles
- 範例文字 Example text: 「HELLO」（預覽底色：dark）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「文字粒子化（Particle Text）」動態效果：大標題由上千個小方點組成：進場時點從畫面各處飛來聚合成文字；游標靠近時，附近的點被推開散落，離開後像彈簧一樣聚回原位，被推離原位的點暫時改用強調色。適合作品集首頁的互動標題。（Canvas 2D：先把文字畫在離屏畫布，每隔數個像素取樣不透明的點當目標位置；每個粒子以彈簧力回到目標、受游標距離產生排斥力並加阻尼）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx177">`, preview text 「HELLO」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「文字粒子化」.

### JavaScript — `FX[177]` from `site/fx.js`

```js
177(s,x,card){cfx(s,card,{init:(c,W,H)=>{const off=document.createElement('canvas');off.width=W;off.height=H;const oc=off.getContext('2d');const fs=Math.min(H*.42,W*1.5/Math.max(2,chars(x).length));
    oc.font=`900 ${fs}px "Noto Sans JP",sans-serif`;oc.textAlign='center';oc.textBaseline='middle';oc.fillText(x,W/2,H/2);const px=oc.getImageData(0,0,W,H).data,gap=Math.max(3,Math.round(W/150)),P=[];
    for(let y=0;y<H;y+=gap)for(let xx=0;xx<W;xx+=gap)if(px[(y*W+xx)*4+3]>128)P.push({tx:xx,ty:y,x:rnd(0,W),y:rnd(0,H),vx:0,vy:0});return{P,gap,c:accRGB(s)}},
  frame:(c,W,H,t,dt,m,o)=>{c.clearRect(0,0,W,H);const [mx,my]=demoPt(t,W,H,m),R=W*.12,sz=o.gap*.7;
    o.P.forEach((p,i)=>{const dx=p.x-mx,dy=p.y-my,d=Math.hypot(dx,dy)||1;if(d<R){const f=(1-d/R)*6;p.vx+=dx/d*f;p.vy+=dy/d*f}p.vx+=(p.tx-p.x)*.06;p.vy+=(p.ty-p.y)*.06;p.vx*=.82;p.vy*=.82;p.x+=p.vx;p.y+=p.vy;
      const off=Math.min(1,Math.hypot(p.x-p.tx,p.y-p.ty)/(W*.05));c.fillStyle=off>.15?`rgb(${o.c})`:'#fff';c.fillRect(p.x-sz/2,p.y-sz/2,sz,sz)})}})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx177` rules from `site/fx.css`

_No dedicated `.fx177` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #177
