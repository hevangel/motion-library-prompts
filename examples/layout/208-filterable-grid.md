# 208 · 作品篩選重排 — Filterable Grid

切換分類時，不符合的作品縮小消失，其他作品平滑補位

- 元件 Component: 版面・頁面 (`layout`)
- 時機 Timing: 切換
- 技術 Tech: GSAP
- 情境 Uses: 介面互動
- 風格／關鍵字 Style: 篩選 分類 作品集 格狀 重排 補位 Filter Grid Portfolio Isotope Reflow Flip 版面 頁面 網頁結構
- 標籤 Tag: Flip
- 範例文字 Example text: 「品牌 網站 插畫」（預覽底色：dark）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「作品篩選重排（Filterable Grid）」動態效果：作品集上方有分類標籤（全部／品牌／網站／插畫），點選分類時，不符合的作品縮小淡出，符合的作品從原本位置平滑移動到新的排列位置補滿空位，重新出現的作品從小放大淡入；選中的分類標籤切換成強調狀態。約 0.6 秒。（GSAP：Flip.getState 記錄所有卡片 → 切換 display → Flip.from，設定 absolute:true、onEnter / onLeave 處理出現與消失的縮放淡入淡出）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx208">`, preview text 「品牌 網站 插畫」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「作品篩選重排」.

### JavaScript — `FX[208]` from `site/fx.js`

```js
208(s,x,card){const cats=words(x).slice(0,3);const w=el('div','ly-fw');w.innerHTML='<div class="ly-fc"></div><div class="ly-fg"></div>';const fc=w.firstChild,fg=w.lastChild;const all=['全部',...cats];const chs=all.map(v=>{const b=el('button');b.textContent=v;fc.append(b);return b});
  const tiles=[...Array(9)].map((_,i)=>{const t=el('div','ly-ft');t.dataset.c=cats[i%cats.length];t.style.background=`linear-gradient(140deg,${GC[i%3]},${GC[(i%3)+2]})`;t.innerHTML='<span></span>';t.querySelector('span').textContent=cats[i%cats.length];fg.append(t);return t});s.append(w);let k=0,real=0;
  const go=i=>{chs.forEach((b,j)=>b.classList.toggle('on',j===i));const st=Flip.getState(tiles);tiles.forEach(t=>t.style.display=(i===0||t.dataset.c===all[i])?'':'none');Flip.from(st,{duration:.6,ease:'power2.inOut',scale:true,absolute:true,onEnter:e=>gsap.fromTo(e,{opacity:0,scale:.6},{opacity:1,scale:1,duration:.5}),onLeave:e=>gsap.to(e,{opacity:0,scale:.6,duration:.4})})};
  chs.forEach((b,i)=>b.onclick=()=>{real=Date.now();go(i)});go(0);card._timers.push(setInterval(()=>{if(Date.now()-real>4000)go(++k%all.length)},1900))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx208` rules from `site/fx.css`

_No dedicated `.fx208` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #208
