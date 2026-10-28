# 302 · 拖曳排序清單 — Drag to Reorder

拖住某一列上下移動，其他列自動讓位，放開時彈回定位並更新編號

- 元件 Component: 卡片・群組 (`card`)
- 時機 Timing: 拖曳手勢
- 技術 Tech: GSAP
- 情境 Uses: 介面互動、App 介面
- 風格／關鍵字 Style: 拖曳 排序 重新排列 清單 待辦 sortable Drag Reorder List Sortable 卡片 群組
- 標籤 Tag: Draggable
- 範例文字 Example text: 「企劃 設計 開發 上線」（預覽底色：dark）
- 收錄日期 Added: 2026-10-20

**AI 提示詞（網站複製格式）:**

```text
「拖曳排序清單（Drag to Reorder）」動態效果：一份可以拖曳排序的清單，每列左側有拖曳把手、右側有順序編號：按住某一列時它微微放大並浮起（加深陰影與外框），可以上下拖動；拖過其他列的位置時，被經過的列自動平滑地往上或往下讓位；放開時被拖的列帶點彈性落到新位置，所有編號依新順序更新。（GSAP Draggable type:"y"：拖曳時依 y ÷ 列高算出目標索引，改變陣列順序並讓其他列 tween 到 索引 × 列高；放開時 back.out 對齊）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx302">`, preview text 「企劃 設計 開發 上線」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「拖曳排序清單」.

### JavaScript — `FX[302]` from `site/fx.js`

```js
302(s,x,card){const ws=words(x).slice(0,4);const l=el('ul','cg-dl');const items=ws.map((t,i)=>{const li=el('li');li.innerHTML='<span class="cg-hd" aria-hidden="true">⋮⋮</span><b></b><em>0'+(i+1)+'</em>';li.querySelector('b').textContent=t;l.append(li);return li});s.append(l);
  let order=[...items],H=0,real=0;const pos=(skip)=>order.forEach((li,i)=>{if(li!==skip)gsap.to(li,{y:i*H,duration:.3,ease:'power3.out'})});
  requestAnimationFrame(()=>{H=items[0].offsetHeight+6;l.style.height=H*items.length+'px';order.forEach((li,i)=>gsap.set(li,{y:i*H}));
    items.forEach(li=>Draggable.create(li,{type:'y',trigger:li,onPress(){real=Date.now()+1e9;li.classList.add('drag');gsap.to(li,{scale:1.04,duration:.2})},onDrag(){const ni=Math.max(0,Math.min(order.length-1,Math.round(this.y/H)));const oi=order.indexOf(li);if(ni!==oi){order.splice(oi,1);order.splice(ni,0,li);pos(li)}},
      onRelease(){real=Date.now();li.classList.remove('drag');gsap.to(li,{y:order.indexOf(li)*H,scale:1,duration:.35,ease:'back.out(2)'});order.forEach((o,i)=>o.querySelector('em').textContent='0'+(i+1))}}))});
  card._kill.push(()=>items.forEach(li=>{const d=Draggable.get(li);d&&d.kill()}));
  card._timers.push(setInterval(()=>{if(Date.now()-real<5000||!H)return;const a=order.pop();order.splice(Math.floor(Math.random()*order.length),0,a);order.forEach((li,i)=>{gsap.to(li,{y:i*H,duration:.5,ease:'power3.inOut'});li.querySelector('em').textContent='0'+(i+1)})},2200))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx302` rules from `site/fx.css`

_No dedicated `.fx302` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #302
