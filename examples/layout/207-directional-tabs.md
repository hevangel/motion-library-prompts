# 207 · 分頁標籤切換 — Directional Tabs

底線指示器滑到新分頁，內容依切換方向左右滑動交替

- 元件 Component: 版面・頁面 (`layout`)
- 時機 Timing: 切換
- 技術 Tech: GSAP
- 情境 Uses: 介面互動、App 介面
- 風格／關鍵字 Style: 分頁 頁籤 標籤 tab 切換 方向 內容 Tabs Directional Slide Indicator 版面 頁面 網頁結構
- 標籤 Tag: GSAP
- 範例文字 Example text: 「設計 開發 行銷」（預覽底色：dark）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「分頁標籤切換（Directional Tabs）」動態效果：一組分頁標籤，點選其他分頁時，標籤下方的底線指示器平滑滑到新標籤並調整成它的寬度；內容區依切換方向滑動——往右邊的分頁切時，舊內容往左滑出淡出、新內容從右側滑入淡入，往左切則相反，讓使用者感受到分頁的前後順序。約 0.45 秒。（GSAP：比較新舊索引決定方向 d，舊內容 xPercent → -30×d 並淡出後移除，新內容從 xPercent 30×d 進來；指示器用 offsetLeft / offsetWidth 設定 transform 與 width）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx207">`, preview text 「設計 開發 行銷」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「分頁標籤切換」.

### JavaScript — `FX[207]` from `site/fx.js`

```js
207(s,x,card){const ws=words(x).slice(0,3);const w=el('div','ly-tabs');w.innerHTML='<div class="ly-th"><i class="ly-ti"></i></div><div class="ly-tp"></div>';const th=w.firstChild,tp=w.lastChild;const hs=ws.map(v=>{const b=el('button');b.textContent=v;th.append(b);return b});s.append(w);let cur=0,real=0;
  const panel=i=>{const p=el('div','ly-pn');p.innerHTML='<b></b><i class="ly-bl"></i><i class="ly-bl s"></i><div class="ly-gr"><i></i><i></i><i></i></div>';p.querySelector('b').textContent=ws[i]+' 的內容';p.querySelectorAll('.ly-gr i').forEach((e,j)=>e.style.background=GC[(i+j)%5]);return p};
  tp.append(panel(0));const ind=th.querySelector('.ly-ti');const mv=i=>{ind.style.width=hs[i].offsetWidth+'px';ind.style.transform=`translateX(${hs[i].offsetLeft}px)`;hs.forEach((h,j)=>h.classList.toggle('on',j===i))};requestAnimationFrame(()=>mv(0));
  const go=i=>{if(i===cur)return;const d=i>cur?1:-1;const old=tp.firstChild,nw=panel(i);tp.append(nw);gsap.to(old,{xPercent:-30*d,opacity:0,duration:.35,ease:'power2.in',onComplete:()=>old.remove()});gsap.fromTo(nw,{xPercent:30*d,opacity:0},{xPercent:0,opacity:1,duration:.45,ease:'power3.out',delay:.15});mv(i);cur=i};
  hs.forEach((h,i)=>h.onclick=()=>{real=Date.now();go(i)});card._timers.push(setInterval(()=>{if(Date.now()-real>4000)go((cur+1)%hs.length)},1700))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx207` rules from `site/fx.css`

_No dedicated `.fx207` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #207
