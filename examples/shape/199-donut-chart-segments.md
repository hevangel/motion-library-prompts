# 199 · 圓餅圖分段 — Donut Chart Segments

環圈圖一段接一段畫出，圖例依序滑入

- 元件 Component: 圖形・SVG (`shape`)
- 時機 Timing: 進場、捲動觸發
- 技術 Tech: GSAP
- 情境 Uses: 數字資訊
- 風格／關鍵字 Style: 圓餅圖 環圈圖 甜甜圈圖 比例 圖表 數據 Donut Pie Chart Segments Data SVG 圖形
- 標籤 Tag: DrawSVG
- 範例文字 Example text: 「流量來源」（預覽底色：dark）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「圓餅圖分段（Donut Chart Segments）」動態效果：環圈圖（甜甜圈圖）進場：從正上方開始，第一個分類的弧段順時針畫出，接著下一段從前一段的終點接續畫出，依序完成整圈，每段之間保留細小間隙，各段用不同的分類色；中央顯示總計與標題，右側圖例依序從右滑入。（GSAP：每段是一個完整圓圈，用 DrawSVGPlugin 的 drawSVG "起點% 起點%" → "起點% 終點%" 畫出指定區段；SVG rotate(-90deg) 讓起點在上方）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx199">`, preview text 「流量來源」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「圓餅圖分段」.

### JavaScript — `FX[199]` from `site/fx.js`

```js
199(s,x){const V=[42,28,18,12],Lb=['搜尋','社群','直接','其他'],C=['#ff7a2f','#7c5cff','#00c8ff','#ffd23f'];let acc=0;const seg=V.map((v,i)=>{const a=acc;acc+=v;return [a,acc,C[i]]});
  const w=el('div','dnw');w.innerHTML=`<div class="dn"><svg viewBox="0 0 100 100">${seg.map(([a,b,c])=>`<circle cx="50" cy="50" r="38" stroke="${c}"/>`).join('')}</svg><div class="dnc"><b>100%</b><span></span></div></div><ul>${V.map((v,i)=>`<li><i style="background:${C[i]}"></i>${Lb[i]}<em>${v}%</em></li>`).join('')}</ul>`;w.querySelector('.dnc span').textContent=x;s.append(w);
  const cs=w.querySelectorAll('circle'),tl=gsap.timeline({repeat:-1,repeatDelay:.4}).set(w,{opacity:1},0);seg.forEach(([a,b],i)=>tl.fromTo(cs[i],{drawSVG:`${a}% ${a}%`},{drawSVG:`${a+.6}% ${b-.6}%`,duration:.5+(b-a)/100,ease:'power2.inOut'},i?'-=.15':0));
  tl.fromTo(w.querySelectorAll('li'),{x:10,opacity:0},{x:0,opacity:1,stagger:.1,duration:.4},.4).to(w,{opacity:0,duration:.5},'+=1.8')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx199` rules from `site/fx.css`

_No dedicated `.fx199` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #199
