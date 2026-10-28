# 181 · 煙火 — Fireworks

點擊的位置升起煙火並炸開，沒操作時自動施放

- 元件 Component: 背景・氛圍 (`bg`)
- 時機 Timing: 懸停・點擊、循環待機
- 技術 Tech: Canvas
- 情境 Uses: 強調重點、背景裝飾
- 風格／關鍵字 Style: 煙火 慶祝 爆炸 粒子 活動 節慶 Fireworks Celebration Particles Explosion Click Canvas 粒子 particles requestAnimationFrame 互動背景
- 標籤 Tag: Canvas particles
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「煙火（Fireworks）」動態效果：夜空背景，點擊任一位置時，從畫面底部發射一枚煙火往上升到點擊處，抵達後炸開成數十顆火花，火花向四周散開、受重力下墜、阻力減速並逐漸淡出，留下短暫拖尾；沒有操作時會隨機自動施放。適合活動頁、完成慶祝。（Canvas 2D：火箭用 ease-out 插值上升，爆炸時產生粒子陣列，每幀更新速度（×阻力、+重力）與壽命；畫面每幀用半透明底色覆蓋做拖尾）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx181">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「煙火」.

### JavaScript — `FX[181]` from `site/fx.js`

```js
181(s,x,card){let auto=0;cfx(s,card,{init:(c,W,H,m)=>{c.fillStyle=`rgb(${BGD})`;c.fillRect(0,0,W,H);const o={R:[],P:[]};m.click=(px,py)=>{auto=Date.now();launch(o,W,H,px,py)};return o},
  frame:(c,W,H,t,dt,m,o)=>{c.fillStyle=`rgba(${BGD},.2)`;c.fillRect(0,0,W,H);if(Date.now()-auto>2500&&Math.random()<dt*1.3)launch(o,W,H,rnd(.2,.8)*W,rnd(.15,.5)*H);
    o.R=o.R.filter(r=>{r.t+=dt/.7;const k=Math.min(1,r.t),e=1-(1-k)**3,y=r.sy+(r.ty-r.sy)*e,xx=r.sx+(r.tx-r.sx)*e;c.fillStyle=`hsl(${r.h},100%,80%)`;c.beginPath();c.arc(xx,y,2,0,7);c.fill();
      if(k>=1){for(let i=0;i<70;i++){const a=rnd(0,6.3),v=rnd(.5,1)*W*.006;o.P.push({x:r.tx,y:r.ty,vx:Math.cos(a)*v,vy:Math.sin(a)*v,l:1,h:r.h+rnd(-20,20)})}return false}return true});
    o.P=o.P.filter(p=>{p.vx*=.97;p.vy=p.vy*.97+W*.00009;p.x+=p.vx;p.y+=p.vy;p.l-=dt*.7;c.fillStyle=`hsla(${p.h},100%,65%,${p.l})`;c.beginPath();c.arc(p.x,p.y,1.8,0,7);c.fill();return p.l>0})}});
  function launch(o,W,H,tx,ty){o.R.push({sx:tx+rnd(-W*.05,W*.05),sy:H,tx,ty,t:0,h:rnd(0,360)})}}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx181` rules from `site/fx.css`

_No dedicated `.fx181` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #181
