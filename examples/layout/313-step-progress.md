# 313 · 步驟進度條 — Step Progress

多步驟表單上方的步驟圓點，完成的打勾、目前這步放大，連接線跟著填滿

- 元件 Component: 版面・頁面 (`layout`)
- 時機 Timing: 切換
- 技術 Tech: CSS
- 情境 Uses: 介面互動、App 介面
- 風格／關鍵字 Style: 步驟 進度 多步驟 表單 結帳 精靈 Stepper Multi Step Form Wizard Progress Checkout 版面 頁面
- 標籤 Tag: CSS transition
- 範例文字 Example text: 「帳號 資料 付款 完成」（預覽底色：dark）
- 收錄日期 Added: 2026-10-21

**AI 提示詞（網站複製格式）:**

```text
「步驟進度條（Step Progress）」動態效果：多步驟表單（例如註冊或結帳）上方的步驟指示：一排圓形步驟編號以一條線連接，已完成的步驟圓點填滿並以回彈出現勾勾，目前這一步外圈亮起並略為放大，未到的步驟維持淡色；連接線的填滿長度跟著步驟平滑延伸；下方有「上一步／下一步」按鈕。（CSS：連接線內層 transform:scaleX(目前索引 / (總數 − 1))，transition 0.5 秒；步驟以 .done / .on class 切換樣式，勾勾用 scale 0 → 1 的 keyframes）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx313">`, preview text 「帳號 資料 付款 完成」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「步驟進度條」.

### JavaScript — `FX[313]` from `site/fx.js`

```js
313(s,x,card){const ws=words(x).slice(0,4);const w=el('div','pg-st');w.innerHTML='<div class="pg-sl"><i></i></div>'+ws.map((t,i)=>`<div class="pg-sp"><b>${i+1}</b><span></span></div>`).join('')+'<div class="pg-sb"><button class="pv">上一步</button><button class="nx">下一步</button></div>';w.querySelectorAll('.pg-sp span').forEach((sp,i)=>sp.textContent=ws[i]);s.append(w);
  const ps=[...w.querySelectorAll('.pg-sp')],fill=w.querySelector('.pg-sl i');let cur=0,real=0;const go=i=>{cur=Math.max(0,Math.min(ps.length-1,i));ps.forEach((p,j)=>{p.classList.toggle('done',j<cur);p.classList.toggle('on',j===cur)});fill.style.transform=`scaleX(${cur/(ps.length-1)})`};go(0);
  w.querySelector('.nx').onclick=()=>{real=Date.now();go(cur+1)};w.querySelector('.pv').onclick=()=>{real=Date.now();go(cur-1)};card._timers.push(setInterval(()=>{if(Date.now()-real>5000)go(cur===ps.length-1?0:cur+1)},1300))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx313` rules from `site/fx.css`

_No dedicated `.fx313` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #313
