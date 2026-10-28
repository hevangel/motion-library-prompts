# 261 · 點擊噴出小物 — Click Confetti Pop

在畫面任何地方點擊，就從那裡噴出愛心星星等小圖案再落下

- 元件 Component: 游標 (`cursor`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: GSAP
- 情境 Uses: 強調重點、介面互動
- 風格／關鍵字 Style: 點擊 噴出 愛心 星星 彩紙 回饋 可愛 Click Burst Hearts Confetti Pop Particles 游標 滑鼠
- 標籤 Tag: GSAP keyframes
- 範例文字 Example text: 「Click!」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「點擊噴出小物（Click Confetti Pop）」動態效果：在區塊內任何地方點擊時，從點擊位置噴出約 7 個小圖案（愛心、星星、小花），各自往上方扇形範圍飛出、大小與角度隨機，飛到最高點後一邊往下掉一邊淡出；同時點擊處有一圈細圓環擴散消失。適合可愛風格的網站或按讚回饋。（GSAP：每個小圖案 fromTo 從點擊點 scale 0，keyframes 第一段往隨機角度與距離飛出 power3.out，第二段往下並 opacity 0；動畫結束移除元素）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx261">`, preview text 「Click!」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「點擊噴出小物」.

### JavaScript — `FX[261]` from `site/fx.js`

```js
261(s,x,card){const l=el('div','abs gl cr-ck');const t=T(x,Math.min(12,52/chars(x).length));l.append(t,el('div','cr-hint','點一下試試'));s.append(l);const E=['❤','✦','★','✿','♥'];let real=0;
  const pop=(px,py)=>{for(let i=0;i<7;i++){const p=el('span','cr-pp');p.textContent=E[i%E.length];p.style.color=i%2?'var(--a)':GC[i%5];l.append(p);const a=rnd(-Math.PI*.95,-Math.PI*.05),d=rnd(30,70);
    gsap.fromTo(p,{x:px,y:py,xPercent:-50,yPercent:-50,scale:0,rotation:rnd(-40,40)},{keyframes:[{x:px+Math.cos(a)*d,y:py+Math.sin(a)*d,scale:rnd(.8,1.3),duration:.45,ease:'power3.out'},{y:`+=${rnd(20,40)}`,opacity:0,duration:.6,ease:'power1.in'}],onComplete:()=>p.remove()})}
    const r=el('i','cr-cr');r.style.transform=`translate(${px}px,${py}px)`;l.append(r);r.addEventListener('animationend',()=>r.remove())};
  l.addEventListener('pointerdown',e=>{real=Date.now();const q=l.getBoundingClientRect();pop(e.clientX-q.left,e.clientY-q.top)});
  card._timers.push(setInterval(()=>{if(Date.now()-real<5000)return;pop(rnd(.2,.8)*l.offsetWidth,rnd(.3,.75)*l.offsetHeight)},1300))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx261` rules from `site/fx.css`

_No dedicated `.fx261` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #261
