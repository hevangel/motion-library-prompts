# 174 · 飄落花瓣 — Falling Petals

花瓣緩緩旋轉飄落，游標經過會把花瓣吹開

- 元件 Component: 背景・氛圍 (`bg`)
- 時機 Timing: 循環待機、懸停・點擊
- 技術 Tech: Canvas
- 情境 Uses: 背景裝飾、標題・Hero
- 風格／關鍵字 Style: 花瓣 櫻花 飄落 下雪 天氣 季節 Petals Sakura Snow Weather Falling Particles Canvas 粒子 particles requestAnimationFrame 互動背景
- 標籤 Tag: Canvas particles
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「飄落花瓣（Falling Petals）」動態效果：背景有數十片花瓣從上方緩緩飄落，每片都會左右擺盪、翻轉（用縮放模擬翻面）並各自旋轉，速度大小略有差異；游標經過時會依移動方向與速度把附近的花瓣吹開，之後花瓣慢慢回到自然飄落。也可以換成雪花、雨滴等天氣粒子。（Canvas 2D：每片花瓣有位置、速度、角度與擺盪相位；游標速度 = 本幀與上一幀座標差，距離內的花瓣依距離加上推力，再逐漸衰減；落出畫面底部就回到頂端重生）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx174">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「飄落花瓣」.

### JavaScript — `FX[174]` from `site/fx.js`

```js
174(s,x,card){cfx(s,card,{init:(c,W,H)=>({P:[...Array(90)].map(()=>({x:rnd(0,W),y:rnd(-H,H),vx:0,vy:rnd(.3,.8),r:rnd(.006,.013)*W,a:rnd(0,6.3),va:rnd(-1.5,1.5),ph:rnd(0,6.3)}))}),
  frame:(c,W,H,t,dt,m,o)=>{c.clearRect(0,0,W,H);const [mx,my]=demoPt(t,W,H,m);const wx=m.in?(m.x-m.px):Math.cos(t*.8)*2.2,wy=m.in?(m.y-m.py):Math.sin(t*1.6)*1.2;
    o.P.forEach(p=>{const d=Math.hypot(p.x-mx,p.y-my);if(d<W*.15){const k=1-d/(W*.15);p.vx+=wx*k*.08;p.vy+=wy*k*.05}p.vx*=.96;p.vy+=(.55-p.vy)*.02;
      p.x+=p.vx+Math.sin(t*1.3+p.ph)*.35;p.y+=p.vy*H*.004;p.a+=p.va*dt;if(p.y>H+20){p.y=-20;p.x=rnd(0,W)}if(p.x<-20)p.x=W+20;if(p.x>W+20)p.x=-20;
      c.save();c.translate(p.x,p.y);c.rotate(p.a);c.scale(1,.6+.4*Math.sin(t*2+p.ph));c.fillStyle='rgba(255,183,213,.9)';c.beginPath();c.ellipse(0,0,p.r,p.r*.62,0,0,7);c.fill();c.fillStyle='rgba(255,140,190,.9)';c.beginPath();c.ellipse(p.r*.35,0,p.r*.3,p.r*.2,0,0,7);c.fill();c.restore()})}})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx174` rules from `site/fx.css`

_No dedicated `.fx174` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #174
