# 197 · 折線圖繪製 — Line Chart Draw

折線由左到右畫出，資料點依序彈出，下方面積淡入

- 元件 Component: 圖形・SVG (`shape`)
- 時機 Timing: 進場、捲動觸發
- 技術 Tech: GSAP
- 情境 Uses: 數字資訊
- 風格／關鍵字 Style: 折線圖 圖表 數據 成長 趨勢 Dashboard Line Chart Graph Data Visualization SVG 圖形
- 標籤 Tag: DrawSVG
- 範例文字 Example text: 「月營收成長」（預覽底色：dark）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「折線圖繪製（Line Chart Draw）」動態效果：折線圖進場：背景有淡淡的水平格線，折線由左到右描繪出來（約 1.6 秒），每個資料點在線條經過時依序從 0 彈出，線條畫到後段時，線下方的面積以漸層淡入，最後在終點上方浮出成長數值標籤。（GSAP：DrawSVGPlugin 描繪折線 path；資料點 stagger 時間 = 描繪時間 ÷ 點數；面積用同樣路徑加上底邊封閉並填入由上到下漸淡的漸層；實際網站可搭配 ScrollTrigger 捲到時播放）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx197">`, preview text 「月營收成長」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「折線圖繪製」.

### JavaScript — `FX[197]` from `site/fx.js`

```js
197(s,x){const V=[22,34,28,46,40,58,52,72],N=V.length,pts=V.map((v,i)=>[10+i*(140/(N-1)),80-v]);const d='M'+pts.map(p=>p.join(',')).join(' L');const id='ag'+Math.random().toString(36).slice(2);
  s.insertAdjacentHTML('beforeend',`<div class="lcw"><b></b><svg viewBox="0 0 160 90"><defs><linearGradient id="${id}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" class="s1"/><stop offset="1" class="s2"/></linearGradient></defs>${[20,40,60,80].map(y=>`<path class="gd" d="M10,${y}H150"/>`).join('')}<path class="ar" d="${d} L150,80 L10,80 Z" fill="url(#${id})"/><path class="ln" d="${d}"/>${pts.map(([cx,cy])=>`<circle class="pt" cx="${cx}" cy="${cy}" r="2.4"/>`).join('')}<text class="vl" x="${pts[N-1][0]-2}" y="${pts[N-1][1]-6}">+72%</text></svg></div>`);
  const w=s.querySelector('.lcw');w.querySelector('b').textContent=x;const q=c=>w.querySelector(c);
  gsap.timeline({repeat:-1,repeatDelay:.4}).set(w,{opacity:1},0).fromTo(q('.ln'),{drawSVG:'0%'},{drawSVG:'100%',duration:1.6,ease:'power1.inOut'},0).fromTo(w.querySelectorAll('.pt'),{scale:0,transformOrigin:'50% 50%'},{scale:1,duration:.35,ease:'back.out(3)',stagger:1.6/N},.05)
    .fromTo(q('.ar'),{opacity:0},{opacity:1,duration:.6},1.2).fromTo(q('.vl'),{opacity:0,y:4},{opacity:1,y:0,duration:.4},1.5).to(w,{opacity:0,duration:.5},'+=1.8')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx197` rules from `site/fx.css`

_No dedicated `.fx197` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #197
