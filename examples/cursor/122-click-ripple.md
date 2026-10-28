# 122 · 點擊漣漪 — Click Ripple

在畫面任何位置點擊，都會從點擊處擴散出波紋

- 元件 Component: 游標 (`cursor`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動
- 風格／關鍵字 Style: 游標 點擊 漣漪 波紋 回饋 Click Ripple Wave Feedback Material
- 標籤 Tag: Click ripple
- 範例文字 Example text: 「點任何地方」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「點擊漣漪（Click Ripple）」動態效果：在區塊內任何位置點擊時，從點擊處同時擴散出一個半透明實心圓與一圈外框環（外框稍晚 0.12 秒），兩者從 0 放大到約一個拇指大小的數倍並淡出，約 0.85 秒、強烈減速，給使用者清楚的點擊回饋；可以快速連點，波紋會重疊。（做法：pointerdown 時在點擊座標建立圓形元素，CSS keyframes 做 scale(0→1) + opacity(1→0)，動畫結束後移除元素）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx122">`, preview text 「點任何地方」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「點擊漣漪」.

### JavaScript — `FX[122]` from `site/fx.js`

```js
122(s,x,card){const l=el('div','abs gl rp');l.append(T(x,Math.min(9,50/chars(x).length)));const cur=el('div','vcur');cur.style.transition='transform .35s ease,opacity .2s';cur.innerHTML=ARROW;l.append(cur);s.append(l);let real=0;
  const ripple=(px,py)=>{for(let k=0;k<2;k++){const r=el('i','rpl'+(k?'':' f'));r.style.left=px+'px';r.style.top=py+'px';r.style.animationDelay=k*.12+'s';l.append(r);setTimeout(()=>r.remove(),1100)}};
  l.addEventListener('pointerdown',e=>{const r=l.getBoundingClientRect();real=Date.now();cur.style.opacity=0;ripple(e.clientX-r.left,e.clientY-r.top)});l.addEventListener('pointerleave',()=>cur.style.opacity='');
  card._timers.push(setInterval(()=>{if(Date.now()-real<3000)return;cur.style.opacity='';const W=l.offsetWidth,H=l.offsetHeight,px=W*(.2+Math.random()*.6),py=H*(.25+Math.random()*.5);cur.style.transform=`translate(${px}px,${py}px)`;setTimeout(()=>ripple(px,py),380)},1100))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx122` rules from `site/fx.css`

_No dedicated `.fx122` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #122
