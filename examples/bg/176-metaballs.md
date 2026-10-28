# 176 · 融合球 — Metaballs

幾顆圓球漂浮移動，靠近時像液體一樣黏在一起

- 元件 Component: 背景・氛圍 (`bg`)
- 時機 Timing: 循環待機、懸停・點擊
- 技術 Tech: Canvas
- 情境 Uses: 背景裝飾、標題・Hero
- 風格／關鍵字 Style: 融合球 液體 黏液 有機 熔岩燈 Metaballs Liquid Blob Gooey Lava Lamp Canvas 粒子 particles requestAnimationFrame 互動背景
- 標籤 Tag: Canvas field
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「融合球（Metaballs）」動態效果：背景有幾顆大小不一的圓球緩慢漂浮、碰到邊界反彈，當兩顆球靠近時邊緣會像液體一樣平滑地黏在一起、拉出連接的頸部，分開時再斷開；其中一顆會跟著游標移動，可以去「黏」其他球。像熔岩燈的有機感。（Canvas：在低解析度格子上計算每格的場強 Σ r²/d²，大於門檻就填色、邊緣做柔和過渡，再放大繪製到畫布；或用 CSS filter blur + contrast 的 gooey 技巧）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx176">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「融合球」.

### JavaScript — `FX[176]` from `site/fx.js`

```js
176(s,x,card){cfx(s,card,{init:(c,W,H,m)=>{const g=4,gw=Math.ceil(W/g),gh=Math.ceil(H/g),off=document.createElement('canvas');off.width=gw;off.height=gh;const oc=off.getContext('2d');
    return{g,gw,gh,off,oc,img:oc.createImageData(gw,gh),c:accRGB(s),B:[...Array(5)].map(()=>({x:rnd(.2,.8)*gw,y:rnd(.2,.8)*gh,vx:rnd(-12,12),vy:rnd(-9,9),r:rnd(.09,.14)*gh}))}},
  frame:(c,W,H,t,dt,m,o)=>{const{gw,gh,img,B}=o,d=img.data,[mx,my]=demoPt(t,W,H,m);B.forEach(b=>{b.x+=b.vx*dt;b.y+=b.vy*dt;if(b.x<b.r||b.x>gw-b.r)b.vx*=-1;if(b.y<b.r||b.y>gh-b.r)b.vy*=-1});
    const all=[...B,{x:mx/o.g,y:my/o.g,r:gh*.13}];const[R,G,Bc]=o.c;
    for(let y=0;y<gh;y++)for(let x=0;x<gw;x++){let f=0;for(const b of all){const dx=x-b.x,dy=y-b.y;f+=b.r*b.r/(dx*dx+dy*dy+1)}const i=(y*gw+x)*4,k=Math.max(0,Math.min(1,(f-.9)*6));
      d[i]=21+(R-21)*k;d[i+1]=22+(G-22)*k;d[i+2]=26+(Bc-26)*k;d[i+3]=255}
    o.oc.putImageData(img,0,0);c.imageSmoothingEnabled=true;c.drawImage(o.off,0,0,W,H)}})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx176` rules from `site/fx.css`

_No dedicated `.fx176` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #176
