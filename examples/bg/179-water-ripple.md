# 179 · 水波漣漪 — Water Ripple

游標滑過或點擊的地方，畫面像水面一樣泛起漣漪

- 元件 Component: 背景・氛圍 (`bg`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: Canvas
- 情境 Uses: 背景裝飾、標題・Hero
- 風格／關鍵字 Style: 水波 漣漪 水面 波紋 折射 Water Ripple Wave Refraction Liquid Canvas 粒子 particles requestAnimationFrame 互動背景
- 標籤 Tag: Canvas pixels
- 範例文字 Example text: 「水面」（預覽底色：dark）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「水波漣漪（Water Ripple）」動態效果：整個區塊像一面水，游標滑過時沿路產生細小波紋，點擊時產生較大的漣漪，波紋會向外擴散、互相干涉並逐漸平息，水面下的圖文會跟著波紋折射扭曲；沒有互動時偶爾自動滴下一滴水。（Canvas：在低解析度上用兩個高度緩衝區做經典水波演算法 next = (四鄰平均×2 − prev) × 阻尼；繪製時依高度梯度偏移取樣底圖的像素，再放大到畫布）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx179">`, preview text 「水面」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「水波漣漪」.

### JavaScript — `FX[179]` from `site/fx.js`

```js
179(s,x,card){cfx(s,card,{init:(c,W,H,m)=>{const g=2,gw=Math.ceil(W/g),gh=Math.ceil(H/g),base=document.createElement('canvas');base.width=gw;base.height=gh;const b=base.getContext('2d');
    const gr=b.createLinearGradient(0,0,gw,gh);gr.addColorStop(0,'#0f3d4c');gr.addColorStop(1,'#1d8a8a');b.fillStyle=gr;b.fillRect(0,0,gw,gh);b.strokeStyle='rgba(255,255,255,.08)';for(let i=0;i<gw;i+=8){b.beginPath();b.moveTo(i,0);b.lineTo(i,gh);b.stroke()}
    b.fillStyle='#fff';b.font=`900 ${Math.min(gh*.4,gw*1.4/Math.max(2,chars(x).length))}px "Noto Sans JP",sans-serif`;b.textAlign='center';b.textBaseline='middle';b.fillText(x,gw/2,gh/2);
    const out=document.createElement('canvas');out.width=gw;out.height=gh;const ocx=out.getContext('2d');
    const o={g,gw,gh,src:b.getImageData(0,0,gw,gh).data,out,ocx,img:ocx.createImageData(gw,gh),a:new Float32Array(gw*gh),b:new Float32Array(gw*gh),drop:0};
    m.click=(px,py)=>drop(o,px/g,py/g,90);return o},
  frame:(c,W,H,t,dt,m,o)=>{const{gw,gh}=o;if(m.in&&Math.hypot(m.x-m.px,m.y-m.py)>1)drop(o,m.x/o.g,m.y/o.g,40);else if(!m.in){o.drop+=dt;if(o.drop>.7){o.drop=0;drop(o,rnd(.15,.85)*gw,rnd(.2,.8)*gh,110)}}
    const A=o.a,B=o.b;for(let y=1;y<gh-1;y++)for(let x=1;x<gw-1;x++){const i=y*gw+x;B[i]=((A[i-1]+A[i+1]+A[i-gw]+A[i+gw])/2-B[i])*.965}o.a=B;o.b=A;
    const d=o.img.data,S=o.src,C=o.a;for(let y=1;y<gh-1;y++)for(let x=1;x<gw-1;x++){const i=y*gw+x,dx=(C[i-1]-C[i+1])*.12,dy=(C[i-gw]-C[i+gw])*.12;const sx=Math.min(gw-1,Math.max(0,x+dx|0)),sy=Math.min(gh-1,Math.max(0,y+dy|0)),j=(sy*gw+sx)*4,k=i*4,sh=dx*2;
      d[k]=S[j]+sh;d[k+1]=S[j+1]+sh;d[k+2]=S[j+2]+sh;d[k+3]=255}o.ocx.putImageData(o.img,0,0);c.drawImage(o.out,0,0,W,H)}});
  function drop(o,x,y,v){x|=0;y|=0;for(let j=-2;j<=2;j++)for(let i=-2;i<=2;i++){const xx=x+i,yy=y+j;if(xx>0&&yy>0&&xx<o.gw-1&&yy<o.gh-1)o.a[yy*o.gw+xx]+=v*(1-Math.hypot(i,j)/3)}}}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx179` rules from `site/fx.css`

_No dedicated `.fx179` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #179
