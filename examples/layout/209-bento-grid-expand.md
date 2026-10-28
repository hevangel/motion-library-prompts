# 209 · Bento 格局展開 — Bento Grid Expand

滑過便當盒格局的某一格，那一格變大、其他格同步讓位

- 元件 Component: 版面・頁面 (`layout`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動、標題・Hero
- 風格／關鍵字 Style: Bento 便當盒 格局 網格 展開 放大 特色介紹 Bento Grid Expand Hover Feature 版面 頁面 網頁結構
- 標籤 Tag: CSS grid
- 範例文字 Example text: 「設計 開發 策略 品牌 數據 社群」（預覽底色：dark）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「Bento 格局展開（Bento Grid Expand）」動態效果：Bento（便當盒）式的 3×2 格局，滑鼠移到某一格時，該格所在的欄與列放大（欄寬約 2.4 倍、列高約 1.8 倍），其他格同步縮小讓位，整個格局平滑重新分配，放大那一格的標題也同步變大；滑鼠離開後恢復平均。約 0.55 秒、緩入緩出。（CSS：容器 grid-template-columns / rows 用 fr 值，hover 時以 JS 改寫目標欄列的 fr，並對 grid-template-columns 與 grid-template-rows 加 transition）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx209">`, preview text 「設計 開發 策略 品牌 數據 社群」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「Bento 格局展開」.

### JavaScript — `FX[209]` from `site/fx.js`

```js
209(s,x,card){const w=el('div','ly-bn');const ws=words(x);const L=[[0,0],[1,0],[2,0],[0,1],[1,1],[2,1]];const tiles=L.map(([c,r],i)=>{const t=el('div','ly-bt');t.style.gridArea=`${r+1}/${c+1}`;t.style.background=i%2?'#22242b':`linear-gradient(140deg,${GC[i%5]},${GC[(i+1)%5]})`;t.innerHTML='<b></b>';t.querySelector('b').textContent=ws[i%ws.length];w.append(t);return t});s.append(w);let real=false,k=0;
  const big=i=>{const c=['1fr','1fr','1fr'],r=['1fr','1fr'];if(i!=null){c[L[i][0]]='2.4fr';r[L[i][1]]='1.8fr'}w.style.gridTemplateColumns=c.join(' ');w.style.gridTemplateRows=r.join(' ');tiles.forEach((t,j)=>t.classList.toggle('on',j===i))};
  tiles.forEach((t,i)=>t.addEventListener('pointerenter',()=>{real=true;big(i)}));w.addEventListener('pointerleave',()=>{real=false;big(null)});card._timers.push(setInterval(()=>{if(!real)big(k++%7<6?(k-1)%7:null)},1400))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx209` rules from `site/fx.css`

_No dedicated `.fx209` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #209
