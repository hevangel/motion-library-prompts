# 270 · 拍立得洗牌 — Photo Stack Shuffle

一疊微歪的拍立得照片，點一下最上面那張被抽走、塞回最底下

- 元件 Component: 圖片・媒體 (`media`)
- 時機 Timing: 切換
- 技術 Tech: GSAP
- 情境 Uses: 介面互動、標題・Hero
- 風格／關鍵字 Style: 拍立得 照片 堆疊 洗牌 相簿 Polaroid Photo Stack Shuffle Deck 圖片 媒體
- 標籤 Tag: GSAP timeline
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「拍立得洗牌（Photo Stack Shuffle）」動態效果：一疊拍立得風格的照片（四周帶寬邊框、下方較寬處寫小標題），每張以不同角度微微歪斜地疊在一起；點擊時最上面那張往右被抽出並旋轉，接著回到整疊的最底下，其他照片同時調整位置與角度補上，形成洗牌的效果，可以一直點下去。（GSAP timeline：最上面那張 x +120%、rotation 18 → 調整 z-index 排到最底 → 回到堆疊位置；每張依堆疊順序設定 rotation 與 x/y 的小偏移）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx270">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「拍立得洗牌」.

### JavaScript — `FX[270]` from `site/fx.js`

```js
270(s,x,card){const w=el('div','md-pd');const ps=[0,1,2,3].map(i=>{const d=el('div','md-pp');d.innerHTML=mdImg(i)+'<small></small>';d.querySelector('small').textContent=['夏日','旅行','夜晚','午後'][i];d.style.setProperty('--r',(i-1.5)*5+'deg');w.append(d);return d});s.append(w);let order=[...ps],busy=false,real=0;
  const lay=()=>order.forEach((d,k)=>{d.style.zIndex=k;gsap.to(d,{rotation:(k-1.5)*5+(k===3?0:0),x:(k-1.5)*3,y:-k*2,duration:.4,ease:'power2.out'})});lay();
  const shuffle=()=>{if(busy)return;busy=true;const t=order[3];gsap.timeline({onComplete:()=>{busy=false}}).to(t,{x:'+=120%',rotation:18,duration:.35,ease:'power2.in'}).add(()=>{order=[t,...order.slice(0,3)];lay()}).to(t,{x:-4.5,duration:.4,ease:'power3.out'})};
  w.onclick=()=>{real=Date.now();shuffle()};card._timers.push(setInterval(()=>{if(Date.now()-real>5000)shuffle()},2200))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx270` rules from `site/fx.css`

_No dedicated `.fx270` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #270
