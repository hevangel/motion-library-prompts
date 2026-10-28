# 329 · 樹枝生長 — Growing Plant

樹幹先長出來，再分出枝條，最後葉子一片片冒出

- 元件 Component: 圖形・SVG (`shape`)
- 時機 Timing: 進場
- 技術 Tech: GSAP
- 情境 Uses: 標題・Hero、Logo・品牌
- 風格／關鍵字 Style: 樹 生長 植物 枝條 葉子 成長 永續 Growing Tree Plant Branches Leaves Growth 圖形 SVG
- 標籤 Tag: DrawSVG
- 範例文字 Example text: 「慢慢長大」（預覽底色：dark）
- 收錄日期 Added: 2026-10-21

**AI 提示詞（網站複製格式）:**

```text
「樹枝生長（Growing Plant）」動態效果：一棵樹由下往上生長：先畫出地面線與主幹（約 0.8 秒），接著左右分枝依序長出，再長出更細的小枝；枝條畫完後，葉子以隨機順序一片片從枝條末端彈出（從 0 放大到 1，帶回彈）；最後下方文字浮現。適合品牌故事、成長或永續主題。（GSAP timeline：每條枝條是 SVG path，用 DrawSVG 0% → 100% 依序畫出；葉子 scale 0 → 1、transform-origin 在葉柄、stagger from:"random"）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx329">`, preview text 「慢慢長大」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「樹枝生長」.

### JavaScript — `FX[329]` from `site/fx.js`

```js
329(s,x){const w=el('div','sv-tree');const B=[['M80,118 C80,95 78,80 80,60','t'],['M80,92 C70,86 60,80 54,70',''],['M80,82 C92,76 102,68 108,56',''],['M80,66 C74,58 70,50 70,40',''],['M80,62 C86,54 92,48 96,38',''],['M54,70 C48,66 44,60 42,54','s'],['M108,56 C114,52 118,46 120,40','s']];const LV=[[54,70],[42,54],[108,56],[120,40],[70,40],[96,38],[80,60],[62,78],[100,66]];
  w.innerHTML=`<svg viewBox="0 0 160 125"><path class="gd" d="M30,118 H130"/>${B.map(([d,c])=>`<path class="br ${c}" d="${d}"/>`).join('')}${LV.map(([cx,cy],i)=>`<g class="lf" transform="translate(${cx},${cy}) rotate(${(i*47)%360})"><path d="M0,0 C4,-5 10,-5 13,0 C10,5 4,5 0,0Z"/></g>`).join('')}</svg><b></b>`;w.querySelector('b').textContent=x;s.append(w);
  const br=w.querySelectorAll('.br'),lf=w.querySelectorAll('.lf path');
  gsap.timeline({repeat:-1,repeatDelay:1}).set(lf,{scale:0,transformOrigin:'0% 50%'}).fromTo(br[0],{drawSVG:'0%'},{drawSVG:'100%',duration:.8,ease:'power2.out'}).fromTo([...br].slice(1,5),{drawSVG:'0%'},{drawSVG:'100%',duration:.6,stagger:.12,ease:'power2.out'},'-=.3').fromTo([...br].slice(5),{drawSVG:'0%'},{drawSVG:'100%',duration:.4,stagger:.1},'-=.2').to(lf,{scale:1,duration:.5,ease:'back.out(2.5)',stagger:{each:.07,from:'random'}},'-=.2').from(w.querySelector('b'),{y:8,opacity:0,duration:.4},'-=.2').to(w,{opacity:0,duration:.5},'+=1.6').set(w,{opacity:1})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx329` rules from `site/fx.css`

_No dedicated `.fx329` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #329
