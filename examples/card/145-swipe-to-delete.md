# 145 · 滑動刪除 — Swipe to Delete

列表項目往左滑露出刪除，滑到底就收合移除

- 元件 Component: 卡片・群組 (`card`)
- 時機 Timing: 拖曳手勢、退場
- 技術 Tech: GSAP
- 情境 Uses: App 介面、介面互動
- 風格／關鍵字 Style: 滑動 刪除 左滑 列表 手勢 收合 Swipe Delete Gesture List Dismiss App 手機 行動裝置 微互動 Mobile App Micro-interaction
- 標籤 Tag: Draggable
- 範例文字 Example text: 「會議提醒 帳單通知 新訊息」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「滑動刪除（Swipe to Delete）」動態效果：列表項目可以用手指往左滑，項目後方露出警示色的「刪除」按鈕；滑動距離小於一半時放開會彈回原位，超過門檻（約 30%）放開時，項目整個往左滑出畫面，接著這一列高度收合為 0，下面的項目平滑補上。（GSAP：Draggable type:"x" 並限制只能往左、edgeResistance 0.8；onRelease 判斷門檻後 xPercent:-100，再 tween height 到 0；手機上設定 touch-action:pan-y 讓上下捲動不受影響）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx145">`, preview text 「會議提醒 帳單通知 新訊息」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「滑動刪除」.

### JavaScript — `FX[145]` from `site/fx.js`

```js
145(s,x,card){const ws=words(x);const l=el('div','swl');const rows=[0,1,2].map(i=>{const r=el('div','swr');r.innerHTML='<div class="del">刪除</div><div class="fr"><i></i><span><b></b><em></em></span></div>';r.querySelector('i').style.background=GC[i];r.querySelector('b').textContent=ws[i%ws.length];l.append(r);return r});s.append(l);let idle=0;
  const kill=r=>{const f=r.querySelector('.fr');gsap.timeline().to(f,{xPercent:-100,duration:.3,ease:'power2.in'}).to(r,{height:0,opacity:0,duration:.3,ease:'power2.inOut'}).set(f,{x:0,xPercent:0},'+=.9').to(r,{height:'auto',opacity:1,duration:.4,ease:'power2.out'})};
  const ds=rows.map(r=>Draggable.create(r.querySelector('.fr'),{type:'x',bounds:{minX:-r.offsetWidth*.6,maxX:0},edgeResistance:.8,onPress(){idle=Date.now()+4000},onRelease(){if(this.x<-r.offsetWidth*.3)kill(r);else gsap.to(this.target,{x:0,duration:.3,ease:'power3.out'})}})[0]);card._kill.push(()=>ds.forEach(d=>d.kill()));
  let k=0;card._timers.push(setInterval(()=>{if(Date.now()<idle)return;const r=rows[k++%3],f=r.querySelector('.fr');gsap.timeline().to(f,{x:-r.offsetWidth*.24,duration:.45,ease:'power2.out'}).add(()=>kill(r),'+=.7')},3200))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx145` rules from `site/fx.css`

_No dedicated `.fx145` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #145
