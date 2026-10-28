# 330 · 齒輪連動 — Gear Train

三個大小不同的齒輪咬合在一起，依齒數比例以不同速度互相帶動

- 元件 Component: 圖形・SVG (`shape`)
- 時機 Timing: 循環待機
- 技術 Tech: GSAP
- 情境 Uses: 背景裝飾、數字資訊
- 風格／關鍵字 Style: 齒輪 連動 機械 運轉 設定 系統 Gears Cogs Mechanism Rotation Settings 圖形 SVG
- 標籤 Tag: GSAP
- 範例文字 Example text: 「系統運作中」（預覽底色：dark）
- 收錄日期 Added: 2026-10-21

**AI 提示詞（網站複製格式）:**

```text
「齒輪連動（Gear Train）」動態效果：三個大小與齒數不同的齒輪彼此咬合：最大的齒輪以固定速度順時針轉動，與它咬合的兩個較小齒輪依照齒數比例以較快的速度逆時針轉動（齒數少的轉得快），齒與齒對準不會穿模，像機械系統正在運作；適合「處理中」、設定或系統狀態的畫面。（SVG：用程式依半徑與齒數產生齒輪輪廓 path；GSAP 讓每個齒輪 rotation 無限循環，小齒輪的角速度 = 大齒輪 × (大齒數 ÷ 小齒數)、方向相反，並設定初始相位讓齒對齊）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx330">`, preview text 「系統運作中」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「齒輪連動」.

### JavaScript — `FX[330]` from `site/fx.js`

```js
330(s,x){const gear=(r,n,d)=>{let p='';const st=Math.PI*2/n;for(let i=0;i<n;i++){const a=i*st;const pts=[[a,r-d],[a+st*.15,r],[a+st*.45,r],[a+st*.6,r-d]];pts.forEach(([aa,rr],k)=>p+=(i||k?'L':'M')+(Math.cos(aa)*rr).toFixed(2)+','+(Math.sin(aa)*rr).toFixed(2))}return p+'Z'};
  const G=[[0,0,34,16,'a'],[49,-8,20,10,'b'],[-40,22.6,16,8,'c']];
  s.insertAdjacentHTML('beforeend',`<div class="sv-gr"><svg viewBox="-90 -60 180 120">${G.map(([cx,cy,r,n,c])=>`<g transform="translate(${cx},${cy})"><g class="sv-g ${c}"><path d="${gear(r,n,r*.16)}"/><circle r="${r*.32}"/>${r>25?[0,1,2,3,4,5].map(i=>`<circle class="hl" r="${r*.1}" cx="${(Math.cos(i*Math.PI/3)*r*.58).toFixed(1)}" cy="${(Math.sin(i*Math.PI/3)*r*.58).toFixed(1)}"/>`).join(''):''}</g></g>`).join('')}</svg><b></b></div>`);
  const gr=s.querySelector('.sv-gr');gr.querySelector('b').textContent=x;const [a,b2,c]=gr.querySelectorAll('.sv-g');const T0=8;
  gsap.to(a,{rotation:360,duration:T0,ease:'none',repeat:-1,svgOrigin:'0 0'});gsap.fromTo(b2,{rotation:11},{rotation:11-360*16/10,duration:T0,ease:'none',repeat:-1,svgOrigin:'0 0'});gsap.fromTo(c,{rotation:6},{rotation:6-360*16/8,duration:T0,ease:'none',repeat:-1,svgOrigin:'0 0'})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx330` rules from `site/fx.css`

_No dedicated `.fx330` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #330
