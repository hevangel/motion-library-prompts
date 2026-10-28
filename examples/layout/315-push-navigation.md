# 315 · 推入換頁 — Push Navigation

點清單項目，新頁面從右邊推進來、舊頁面往左退並變暗；按返回則反向

- 元件 Component: 版面・頁面 (`layout`)
- 時機 Timing: 切換
- 技術 Tech: GSAP
- 情境 Uses: 轉場切換、App 介面
- 風格／關鍵字 Style: 推入 換頁 返回 導覽 iOS 堆疊 Push Pop Navigation Stack Page Transition App 版面 頁面
- 標籤 Tag: GSAP
- 範例文字 Example text: 「設定 通知 隱私 關於」（預覽底色：dark）
- 收錄日期 Added: 2026-10-21

**AI 提示詞（網站複製格式）:**

```text
「推入換頁（Push Navigation）」動態效果：模擬 App 的頁面堆疊導覽：點擊清單中的某一項時，詳細頁面從右側整頁推入（帶左側陰影），原本的清單頁同時往左移動約 30% 並變暗，像被新頁面蓋過去；點左上角「‹ 返回」時反向：詳細頁往右退出，清單頁移回原位並恢復亮度。約 0.5 秒、緩入緩出。（GSAP：新頁 xPercent 100 → 0，舊頁 xPercent 0 → −30 並 filter: brightness(.6)；返回時相反）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx315">`, preview text 「設定 通知 隱私 關於」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「推入換頁」.

### JavaScript — `FX[315]` from `site/fx.js`

```js
315(s,x,card){const f=lyPage(s);const ws=words(x);const vw=el('div','pg-vw');vw.innerHTML='<div class="pg-p a"><ul></ul></div><div class="pg-p b"><button class="pg-back">‹ 返回</button><div class="pg-hero">'+mdImg(2)+'</div><b></b><i class="ly-bl"></i><i class="ly-bl s"></i></div>';const ul=vw.querySelector('ul');ws.slice(0,4).forEach((t,i)=>{const li=el('li');li.innerHTML='<i></i><b></b><span>›</span>';li.querySelector('b').textContent=t;ul.append(li)});f.append(vw);
  const A=vw.querySelector('.a'),B=vw.querySelector('.b'),bt=B.querySelector('b');let inB=false,busy=false,real=0;gsap.set(B,{xPercent:100});
  const push=t=>{if(busy||inB)return;busy=true;inB=true;bt.textContent=t;gsap.timeline({onComplete:()=>busy=false}).to(A,{xPercent:-30,filter:'brightness(.6)',duration:.5,ease:'power3.inOut'},0).to(B,{xPercent:0,duration:.5,ease:'power3.inOut'},0)};
  const pop=()=>{if(busy||!inB)return;busy=true;inB=false;gsap.timeline({onComplete:()=>busy=false}).to(A,{xPercent:0,filter:'brightness(1)',duration:.45,ease:'power3.inOut'},0).to(B,{xPercent:100,duration:.45,ease:'power3.inOut'},0)};
  ul.querySelectorAll('li').forEach(li=>li.onclick=()=>{real=Date.now();push(li.querySelector('b').textContent)});B.querySelector('.pg-back').onclick=()=>{real=Date.now();pop()};let k=0;
  card._timers.push(setInterval(()=>{if(Date.now()-real<5000)return;inB?pop():push(ws[k++%ws.length])},1700))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx315` rules from `site/fx.css`

_No dedicated `.fx315` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #315
