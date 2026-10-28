# 322 · 地圖路線導航 — Map Route

地圖上的地標針依序落下，路線從起點畫到終點，小圓點沿路線前進

- 元件 Component: 圖形・SVG (`shape`)
- 時機 Timing: 進場、循環待機
- 技術 Tech: GSAP
- 情境 Uses: 數字資訊、標題・Hero
- 風格／關鍵字 Style: 地圖 路線 導航 地標 定位 旅程 外送 物流 Map Route Path Pin Delivery Journey 圖形 SVG
- 標籤 Tag: MotionPath
- 範例文字 Example text: 「台北 台中 高雄」（預覽底色：dark）
- 收錄日期 Added: 2026-10-21

**AI 提示詞（網站複製格式）:**

```text
「地圖路線導航（Map Route）」動態效果：一張簡化的地圖背景（淡淡的陸地輪廓與經緯格線），上面有三個地標針從上方依序落下並彈跳停住，每個地標下方標示地名；接著一條路線從起點沿著彎曲路徑一路畫到終點（約 2.2 秒），同時一個帶光圈的小圓點沿著路線前進；抵達終點時終點地標彈一下。（GSAP：地標 from y:-30 + bounce.out stagger；路線 DrawSVG 0% → 100%；小圓點用 MotionPathPlugin 沿同一條 path 移動，duration 與畫線一致；底下另有一條淡色虛線表示完整路線）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx322">`, preview text 「台北 台中 高雄」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「地圖路線導航」.

### JavaScript — `FX[322]` from `site/fx.js`

```js
322(s,x){const ws=words(x);const id='rt'+Math.random().toString(36).slice(2);s.insertAdjacentHTML('beforeend',`<svg class="sv-map" viewBox="0 0 320 180"><g class="sv-land"><path d="M20,40 C60,10 120,30 150,20 C190,8 230,30 270,22 C300,18 310,60 300,90 C292,120 310,150 270,160 C220,172 170,150 120,162 C80,172 30,160 22,128 C14,100 30,80 20,40Z"/></g><g class="sv-grid">${[...Array(7)].map((_,i)=>`<path d="M${i*50},0 V180"/>`).join('')}${[...Array(4)].map((_,i)=>`<path d="M0,${i*50+15} H320"/>`).join('')}</g><path id="${id}" class="sv-rt0" d="M60,130 C90,70 130,140 165,95 C200,50 230,110 262,58"/><path class="sv-rt" d="M60,130 C90,70 130,140 165,95 C200,50 230,110 262,58"/>${[[60,130],[165,95],[262,58]].map(([cx,cy],i)=>`<g class="sv-pin" transform="translate(${cx},${cy})"><path d="M0,0 C-7,-9 -9,-13 -9,-17 A9,9 0 1 1 9,-17 C9,-13 7,-9 0,0Z"/><circle cy="-17" r="3.4"/><text y="14" text-anchor="middle"></text></g>`).join('')}<g class="sv-car"><circle r="6"/><circle r="11" class="h"/></g></svg>`);
  const sv=s.querySelector('.sv-map');sv.querySelectorAll('.sv-pin text').forEach((t,i)=>t.textContent=ws[i%ws.length]);const pins=sv.querySelectorAll('.sv-pin'),car=sv.querySelector('.sv-car'),rt=sv.querySelector('.sv-rt');
  gsap.timeline({repeat:-1,repeatDelay:1}).set(car,{opacity:0}).from(pins,{y:'-=30',opacity:0,duration:.5,ease:'bounce.out',stagger:.15}).fromTo(rt,{drawSVG:'0%'},{drawSVG:'100%',duration:2.2,ease:'power1.inOut'},'+=.1').to(car,{opacity:1,duration:.2},'<').to(car,{motionPath:{path:'#'+id,align:'#'+id,alignOrigin:[.5,.5]},duration:2.2,ease:'power1.inOut'},'<').to(pins[2],{scale:1.3,transformOrigin:'50% 100%',duration:.2,yoyo:true,repeat:1}).to([rt,car],{opacity:0,duration:.5},'+=1')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx322` rules from `site/fx.css`

_No dedicated `.fx322` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #322
