# 308 · 數據儀表卡片 — Stat Cards

三張數據卡片依序浮上來，數字累加、迷你折線圖畫出、成長率淡入

- 元件 Component: 卡片・群組 (`card`)
- 時機 Timing: 進場
- 技術 Tech: GSAP
- 情境 Uses: 數字資訊、介面互動
- 風格／關鍵字 Style: 儀表板 數據 統計 KPI 折線 sparkline 後台 Dashboard Stat Cards KPI Sparkline Count Up 卡片 群組
- 標籤 Tag: GSAP timeline
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-20

**AI 提示詞（網站複製格式）:**

```text
「數據儀表卡片（Stat Cards）」動態效果：後台儀表板的三張數據卡片（營收、訂單、轉換率）：進場時依序從下方浮上淡入（間隔約 0.12 秒），每張卡片中的大數字從 0 累加到目標值（含千分位與小數），下方的迷你折線圖從左到右畫出，最後成長百分比從左側淡入。（GSAP timeline：卡片 from y:30、opacity:0、stagger；數字用物件 tween + onUpdate 格式化；折線 polyline 用 DrawSVG 0% → 100%（或 stroke-dashoffset））
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx308">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「數據儀表卡片」.

### JavaScript — `FX[308]` from `site/fx.js`

```js
308(s,x){const D=[['營收','128,400',[3,5,4,7,6,9,8,11]],['訂單','1,286',[6,5,7,6,8,7,9,10]],['轉換率','4.8%',[4,6,5,5,7,6,8,7]]];const w=el('div','cg-db');const cs=D.map(([l,v,p],i)=>{const c=el('div','cg-dc');const mx=Math.max(...p),pts=p.map((y,j)=>`${j*100/(p.length-1)},${36-y/mx*30}`).join(' ');
  c.innerHTML=`<small>${l}</small><b>${v}</b><em>▲ ${[12,8,3][i]}%</em><svg viewBox="0 0 100 40" preserveAspectRatio="none"><polyline points="${pts}"/></svg>`;w.append(c);return c});s.append(w);
  const tl=gsap.timeline({repeat:-1,repeatDelay:2});tl.from(cs,{y:30,opacity:0,duration:.6,ease:'power3.out',stagger:.12});cs.forEach((c,i)=>{const b=c.querySelector('b'),v=b.textContent,num=parseFloat(v.replace(/,/g,'')),dec=v.includes('.')?1:0,suf=v.replace(/[\d,.]/g,'');const o={n:0};
    tl.to(o,{n:num,duration:1.2,ease:'power2.out',onUpdate:()=>b.textContent=(dec?o.n.toFixed(1):Math.round(o.n).toLocaleString())+suf},.2+i*.12).fromTo(c.querySelector('polyline'),{drawSVG:'0%'},{drawSVG:'100%',duration:1,ease:'power2.inOut'},.35+i*.12).from(c.querySelector('em'),{opacity:0,x:-6,duration:.4},.9+i*.12)})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx308` rules from `site/fx.css`

_No dedicated `.fx308` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #308
