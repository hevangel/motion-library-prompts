# 212 · 焦點卡片輪播 — Focus Carousel

中間的卡片放大清楚，兩側縮小變淡，左右切換

- 元件 Component: 卡片・群組 (`card`)
- 時機 Timing: 切換、循環待機
- 技術 Tech: CSS
- 情境 Uses: 介面互動、標題・Hero
- 風格／關鍵字 Style: 輪播 carousel slider 焦點 中間放大 coverflow 作品 輪播圖 卡片 群組
- 標籤 Tag: CSS transition
- 範例文字 Example text: 「品牌 網站 插畫 包裝 攝影」（預覽底色：dark）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「焦點卡片輪播（Focus Carousel）」動態效果：一組卡片橫向排列成輪播，目前這張置中、最大、完全清楚，左右相鄰的卡片縮小到約 82% 並變半透明，再外側的更小更淡；切換時所有卡片一起平滑滑到新位置並改變大小（約 0.6 秒、緩入緩出），下方有左右箭頭與圓點指示器（目前那點拉長），可自動播放，點兩側卡片也能直接切到它。（CSS：每張卡片依「與目前索引的距離」設定 translateX、scale、opacity、z-index，加 transition；超出範圍時取最近的循環方向）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx212">`, preview text 「品牌 網站 插畫 包裝 攝影」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「焦點卡片輪播」.

### JavaScript — `FX[212]` from `site/fx.js`

```js
212(s,x,card){const ws=words(x);const w=el('div','kd-car');const cs=[...Array(5)].map((_,i)=>{const c=el('div','kd-cc');c.style.background=`linear-gradient(150deg,${GC[i%5]},${GC[(i+2)%5]})`;c.innerHTML='<small>0'+(i+1)+'</small><b></b>';c.querySelector('b').textContent=ws[i%ws.length];w.append(c);return c});
  const nav=el('div','kd-nav');nav.innerHTML='<button aria-label="上一張">‹</button><span></span><button aria-label="下一張">›</button>';const dots=nav.querySelector('span');cs.forEach(()=>dots.append(el('i')));s.append(w,nav);let cur=0,real=0;
  const lay=()=>cs.forEach((c,i)=>{let o=i-cur;if(o>2)o-=5;if(o<-2)o+=5;c.style.transform=`translateX(${o*58}%) scale(${1-Math.abs(o)*.18})`;c.style.zIndex=10-Math.abs(o);c.style.opacity=Math.abs(o)>1?.25:Math.abs(o)?.6:1;dots.children[i].classList.toggle('on',i===cur)});
  const go=d=>{cur=(cur+d+5)%5;lay()};const [pv,nx]=nav.querySelectorAll('button');pv.onclick=()=>{real=Date.now();go(-1)};nx.onclick=()=>{real=Date.now();go(1)};cs.forEach((c,i)=>c.onclick=()=>{real=Date.now();cur=i;lay()});lay();
  card._timers.push(setInterval(()=>{if(Date.now()-real>4000)go(1)},1700))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx212` rules from `site/fx.css`

_No dedicated `.fx212` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #212
