# 228 · 閃爍星空 — Twinkling Sky

滿天星星各自閃爍，偶爾劃過一道流星，游標移動時星空微微視差

- 元件 Component: 背景・氛圍 (`bg`)
- 時機 Timing: 循環待機、懸停・點擊
- 技術 Tech: Canvas
- 情境 Uses: 標題・Hero、背景裝飾
- 風格／關鍵字 Style: 星空 星星 閃爍 流星 夜空 宇宙 視差 Twinkling Stars Night Sky Shooting Star Canvas particles requestAnimationFrame 互動背景 背景 氛圍
- 標籤 Tag: Canvas 2D
- 範例文字 Example text: 「晚安」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「閃爍星空（Twinkling Sky）」動態效果：夜空背景：上方深、往下帶一點柔和光暈，佈滿兩百多顆大小與亮度不同的星星，每顆以各自的速度與相位緩慢閃爍，最亮的幾顆閃爍到最亮時會出現細小的十字星芒；每隔幾秒有一道流星從右上斜向左下劃過並拖出漸淡的尾巴；游標移動時星空依星星的遠近做不同幅度的反向視差。（Canvas 2D：每顆星記錄位置、半徑、深度、閃爍頻率與相位，亮度 = sin(時間 × 頻率 + 相位)；流星用 createLinearGradient 畫線段；視差位移以 lerp 平滑）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx228">`, preview text 「晚安」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「閃爍星空」.

### JavaScript — `FX[228]` from `site/fx.js`

```js
228(s,x,card){cfx(s,card,{init:(c,W,H)=>({S:[...Array(220)].map(()=>({x:rnd(0,W),y:rnd(0,H),r:rnd(.3,1.5),z:rnd(.2,1),p:rnd(0,6.3),f:rnd(.6,2.4)})),sh:null,next:1,c:accRGB(s),ox:0,oy:0}),
  frame:(c,W,H,t,dt,m,o)=>{const g=c.createLinearGradient(0,0,0,H);g.addColorStop(0,`rgb(${BGD})`);g.addColorStop(1,`rgba(${o.c},.18)`);c.fillStyle=`rgb(${BGD})`;c.fillRect(0,0,W,H);c.fillStyle=g;c.fillRect(0,0,W,H);
    const tx=m.in?(m.x/W-.5)*-W*.04:0,ty=m.in?(m.y/H-.5)*-H*.04:0;o.ox+=(tx-o.ox)*.06;o.oy+=(ty-o.oy)*.06;
    o.S.forEach(p=>{const a=.35+.65*(.5+.5*Math.sin(t*p.f+p.p));const X=(p.x+o.ox*p.z+W)%W,Y=(p.y+o.oy*p.z+H)%H;c.fillStyle=`rgba(255,255,255,${a*p.z})`;c.beginPath();c.arc(X,Y,p.r*(.7+p.z*.6),0,7);c.fill();
      if(p.r>1.35&&a>.9){c.strokeStyle=`rgba(255,255,255,${(a-.9)*4*p.z})`;c.lineWidth=.6;c.beginPath();c.moveTo(X-p.r*4,Y);c.lineTo(X+p.r*4,Y);c.moveTo(X,Y-p.r*4);c.lineTo(X,Y+p.r*4);c.stroke()}});
    o.next-=dt;if(!o.sh&&o.next<0)o.sh={x:rnd(W*.2,W),y:rnd(0,H*.4),l:0};
    if(o.sh){const q=o.sh;q.l+=dt*1.6;const L=W*.22,px=q.x-q.l*W*.5,py=q.y+q.l*W*.25;const gr=c.createLinearGradient(px,py,px+L,py-L/2);gr.addColorStop(0,`rgba(${o.c},${Math.max(0,1-q.l)})`);gr.addColorStop(1,'rgba(255,255,255,0)');c.strokeStyle=gr;c.lineWidth=1.6;c.beginPath();c.moveTo(px,py);c.lineTo(px+L,py-L/2);c.stroke();if(q.l>1){o.sh=null;o.next=rnd(1.5,3.5)}}}});
  const tx=T(x,Math.min(11,52/chars(x).length));tx.classList.add('cvt');s.append(tx)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx228` rules from `site/fx.css`

_No dedicated `.fx228` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #228
