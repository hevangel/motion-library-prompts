# 103 · 游標擴散填滿按鈕 — Direction-aware Fill Button

從滑鼠進入的位置擴散填滿，離開時往出口收回

- 元件 Component: 按鈕 (`button`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動、強調重點
- 風格／關鍵字 Style: 按鈕 hover 方向感知 擴散 填色 漣漪 從滑鼠位置 Direction Aware Hover Fill Ripple Button CTA
- 標籤 Tag: CSS + JS
- 範例文字 Example text: 「立即聯絡」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「游標擴散填滿按鈕（Direction-aware Fill Button）」動態效果：描邊膠囊按鈕。滑鼠移入時，一個強調色圓形從「游標進入按鈕的那一點」開始放大，擴散到填滿整顆按鈕，文字顏色同時切換成與填色有反差的顏色；滑鼠移出時，圓形改以「游標離開的那一點」為中心縮小消失，所以從哪邊出去、顏色就往哪邊收。約 0.55 秒、緩入緩出。（做法：按鈕 overflow:hidden；pointerenter / pointerleave 時用 getBoundingClientRect 算出游標在按鈕內的座標，寫進 CSS 變數 --x、--y，圓的直徑取「到最遠角距離 × 2」確保蓋滿；圓用 transform:scale(0→1) 做 transition）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx103">`, preview text 「立即聯絡」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「游標擴散填滿按鈕」.

### JavaScript — `FX[103]` from `site/fx.js`

```js
103(s,x,card){const b=el('button','fbtn');b.setAttribute('aria-label',x);b.style.fontSize=Math.min(5,40/chars(x).length)+'cqw';const f=el('span','fl');const t=el('span','ft2');t.textContent=x;b.append(f,t);
  const cur=el('div','vcur');cur.style.transition='transform .35s ease,opacity .2s';cur.innerHTML='<svg viewBox="0 0 24 24"><path d="M3 2l17 9-7.5 2L9 20z" fill="#fff" stroke="#111" stroke-width="1.6" stroke-linejoin="round"/></svg>';s.append(b,cur);
  // 把圓心設在進入（或離開）的位置，半徑取到最遠的角，保證能蓋滿整顆按鈕
  const at=(px,py,on)=>{const W=b.offsetWidth,H=b.offsetHeight,r=Math.hypot(Math.max(px,W-px),Math.max(py,H-py));b.style.setProperty('--x',px+'px');b.style.setProperty('--y',py+'px');b.style.setProperty('--r',r*2+'px');b.classList.toggle('on',on)};
  const rel=e=>{const r=b.getBoundingClientRect();return[e.clientX-r.left,e.clientY-r.top]};let real=false,on=false;
  b.addEventListener('pointerenter',e=>{real=true;cur.style.opacity=0;at(...rel(e),true)});b.addEventListener('pointerleave',e=>{at(...rel(e),false);real=false;on=false;cur.style.opacity=''});
  // 示範：游標從按鈕隨機一邊進來、再從另一邊出去
  const edge=()=>{const W=b.offsetWidth,H=b.offsetHeight,k=Math.floor(Math.random()*4),r=Math.random();return[[0,r*H],[W,r*H],[r*W,0],[r*W,H]][k]};
  card._timers.push(setInterval(()=>{if(real)return;const[px,py]=edge();on=!on;cur.style.transform=`translate(${b.offsetLeft+px}px,${b.offsetTop+py}px)`;setTimeout(()=>{if(!real)at(px,py,on)},350)},1400))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx103` rules from `site/fx.css`

_No dedicated `.fx103` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #103
