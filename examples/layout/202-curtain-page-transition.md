# 202 · 頁面轉場簾幕 — Curtain Page Transition

切換頁面時三片簾幕依序落下蓋住，再往下收走露出新頁

- 元件 Component: 版面・頁面 (`layout`)
- 時機 Timing: 切換
- 技術 Tech: GSAP
- 情境 Uses: 轉場切換
- 風格／關鍵字 Style: 頁面轉場 換頁 簾幕 遮罩 SPA 路由 Page Transition Curtain Wipe Router 版面 頁面 網頁結構
- 標籤 Tag: Timeline
- 範例文字 Example text: 「首頁 作品 關於」（預覽底色：dark）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「頁面轉場簾幕（Curtain Page Transition）」動態效果：點擊導覽切換頁面時，三片直條狀的簾幕從上方依序（間隔約 0.08 秒）落下蓋住整個畫面，此時在背後替換成新頁面，接著三片簾幕再依序往下收走，新頁面的標題與內容區塊由上到下淡入上浮。整段約 1.4 秒，讓換頁有完整的節奏感。（GSAP：簾幕 yPercent -101→0→101，stagger 0.08，ease power3.inOut；在兩段之間的 callback 切換內容；SPA 可搭配 Barba.js 或框架的路由轉場 hook）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx202">`, preview text 「首頁 作品 關於」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「頁面轉場簾幕」.

### JavaScript — `FX[202]` from `site/fx.js`

```js
202(s,x){const ws=words(x);const f=lyPage(s);const pg=el('div','ly-pg');f.append(pg);const cur=el('div','ly-cur');for(let i=0;i<3;i++)cur.append(el('i'));f.append(cur);const bars=cur.children;let k=0;
  const paint=()=>{pg.innerHTML='<b></b><i class="ly-bl"></i><i class="ly-bl s"></i><div class="ly-gr"><i></i><i></i><i></i></div>';pg.querySelector('b').textContent=ws[k%ws.length];pg.querySelectorAll('.ly-gr i').forEach((e,i)=>e.style.background=GC[(k+i)%5])};paint();
  gsap.timeline({repeat:-1,repeatDelay:1.2,onRepeat:()=>{}}).fromTo(bars,{yPercent:-101},{yPercent:0,duration:.55,ease:'power3.inOut',stagger:.08},1.2).add(()=>{k++;paint()}).fromTo(bars,{yPercent:0},{yPercent:101,duration:.55,ease:'power3.inOut',stagger:.08},'+=.1').fromTo(pg.children,{y:12,opacity:0},{y:0,opacity:1,duration:.5,stagger:.06,ease:'power2.out'},'-=.3')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx202` rules from `site/fx.css`

_No dedicated `.fx202` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #202
