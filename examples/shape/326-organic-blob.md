# 326 · 有機流動色塊 — Organic Blob

一團不規則的柔軟色塊持續緩慢變形，後面還有一層淡淡的影子

- 元件 Component: 圖形・SVG (`shape`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 背景裝飾、標題・Hero、強調重點
- 風格／關鍵字 Style: 有機 色塊 斑點 流動 變形 液態 Blob Organic Shape Morph Liquid 圖形 SVG
- 標籤 Tag: JS + SVG
- 範例文字 Example text: 「Blob」（預覽底色：dark）
- 收錄日期 Added: 2026-10-21

**AI 提示詞（網站複製格式）:**

```text
「有機流動色塊（Organic Blob）」動態效果：一團有機的不規則色塊（像軟軟的液體或果凍），邊緣以多組不同頻率的正弦波驅動，持續緩慢地變形、永不重複；後方還有一層稍大、較淡的同色影子以不同節奏變形，增加層次；文字放在色塊中央。（JS requestAnimationFrame：取 8 個繞圓分布的控制點，半徑 = 基準 + 多個 sin(時間 + 索引 × 相位) 的和，用 Catmull-Rom 轉成平滑的三次貝茲曲線寫入 path 的 d）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx326">`, preview text 「Blob」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「有機流動色塊」.

### JavaScript — `FX[326]` from `site/fx.js`

```js
326(s,x,card){const w=el('div','sv-blw');w.innerHTML='<svg viewBox="-60 -60 120 120"><path class="b2"/><path class="b1"/></svg>';const t=T(x,Math.min(11,50/chars(x).length));t.classList.add('sv-blt');w.append(t);s.append(w);const [p2,p1]=w.querySelectorAll('path');
  const shape=(t,R,seed)=>{const N=8,pts=[];for(let i=0;i<N;i++){const a=i/N*Math.PI*2,r=R+R*.16*Math.sin(t*1.1+i*1.7+seed)+R*.1*Math.sin(t*.7+i*2.9+seed*2);pts.push([Math.cos(a)*r,Math.sin(a)*r])}
    let d='';for(let i=0;i<N;i++){const p0=pts[(i-1+N)%N],a=pts[i],b=pts[(i+1)%N],c=pts[(i+2)%N];if(!i)d+=`M${a[0].toFixed(1)},${a[1].toFixed(1)}`;d+=`C${(a[0]+(b[0]-p0[0])/6).toFixed(1)},${(a[1]+(b[1]-p0[1])/6).toFixed(1)} ${(b[0]-(c[0]-a[0])/6).toFixed(1)},${(b[1]-(c[1]-a[1])/6).toFixed(1)} ${b[0].toFixed(1)},${b[1].toFixed(1)}`}return d+'Z'};
  ticks.set(card,t=>{p1.setAttribute('d',shape(t,40,0));p2.setAttribute('d',shape(t*.8,46,3))})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx326` rules from `site/fx.css`

_No dedicated `.fx326` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #326
