# 213 · 左右滑卡 — Swipe Card Stack

最上面的卡片可以拖曳甩出，下一張補上來

- 元件 Component: 卡片・群組 (`card`)
- 時機 Timing: 拖曳手勢、退場
- 技術 Tech: GSAP
- 情境 Uses: 介面互動、App 介面
- 風格／關鍵字 Style: 滑卡 左滑右滑 交友 Tinder 卡片堆疊 甩出 Swipe Cards Stack Like Dislike 卡片 群組
- 標籤 Tag: Draggable
- 範例文字 Example text: 「東京 京都 首爾 台南」（預覽底色：dark）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「左右滑卡（Swipe Card Stack）」動態效果：一疊卡片，最上面那張可以用手指或滑鼠拖曳，拖曳時卡片會依水平位移跟著傾斜，往右拖時左上角浮出「喜歡」印章、往左拖時右上角浮出「略過」；放開時若超過門檻就加速往該方向甩出畫面，下面的卡片依序往上補位並放大；未超過門檻則彈回原位。（GSAP Draggable：onDrag 依 x 設定 rotation 與印章透明度，onRelease 判斷門檻後 tween 出畫面，再把那張移到最底層並重新排列整疊）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx213">`, preview text 「東京 京都 首爾 台南」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「左右滑卡」.

### JavaScript — `FX[213]` from `site/fx.js`

```js
213(s,x,card){const ws=words(x);const w=el('div','kd-sw');let order=[...Array(4)].map((_,i)=>{const c=el('div','kd-sc');c.style.background=`linear-gradient(160deg,${GC[i%5]},${GC[(i+3)%5]})`;c.innerHTML='<em class="y">喜歡</em><em class="n">略過</em><b></b>';c.querySelector('b').textContent=ws[i%ws.length];w.append(c);return c});s.append(w);let idle=0,dr;
  const stack=()=>{order.forEach((c,i)=>{const k=order.length-1-i;gsap.to(c,{x:0,y:k*-2.4+'%',scale:1-k*.05,rotation:0,duration:.4,ease:'power3.out',overwrite:true});c.style.zIndex=i;gsap.set(c.querySelectorAll('em'),{opacity:0})});bind()};
  const fly=(c,dir)=>{gsap.to(c,{x:dir*w.offsetWidth*1.4,rotation:dir*25,duration:.45,ease:'power2.in',onComplete:()=>{order=[c,...order.filter(o=>o!==c)];w.prepend(c);gsap.set(c,{x:0,rotation:0});stack()}})};
  const bind=()=>{dr&&dr.kill();const top=order[order.length-1];dr=Draggable.create(top,{type:'x,y',onPress(){idle=Date.now()+4000},onDrag(){gsap.set(top,{rotation:this.x*.06});gsap.set(top.querySelector('.y'),{opacity:Math.max(0,this.x/80)});gsap.set(top.querySelector('.n'),{opacity:Math.max(0,-this.x/80)})},onRelease(){if(Math.abs(this.x)>w.offsetWidth*.25)fly(top,Math.sign(this.x));else stack()}})[0]};
  card._kill.push(()=>dr&&dr.kill());stack();let dir=1;card._timers.push(setInterval(()=>{if(Date.now()<idle)return;const top=order[order.length-1];gsap.timeline().to(top,{x:dir*w.offsetWidth*.18,rotation:dir*8,duration:.35,ease:'power2.out'}).to(top.querySelector(dir>0?'.y':'.n'),{opacity:1,duration:.2},'<').add(()=>fly(top,dir),'+=.25');dir*=-1},2300))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx213` rules from `site/fx.css`

_No dedicated `.fx213` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #213
