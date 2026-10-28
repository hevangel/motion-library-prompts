# 136 · 圖示描邊 hover — Icon Stroke Redraw

滑過線條圖示時，筆畫重新描一次並微微上浮

- 元件 Component: 圖形・SVG (`shape`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: GSAP
- 情境 Uses: 介面互動
- 風格／關鍵字 Style: 圖示 icon 線條圖示 hover 重繪 描邊 選單 導覽 Icon Stroke Draw Hover Menu
- 標籤 Tag: DrawSVG hover
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「圖示描邊 hover（Icon Stroke Redraw）」動態效果：一排線條圖示（首頁、搜尋、愛心、通知），每個放在圓角方框內；滑鼠移到某個圖示上時，該圖示的線條從頭重新描繪一次（約 0.7 秒，多筆畫依序錯開 0.12 秒），方框邊框與線條同時切換成強調色，圖示微微上浮 6px 再回來。（GSAP：pointerenter 時對該圖示的 path / circle fromTo drawSVG "0%"→"100%"，加 overwrite:true 避免快速滑過時打架）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx136">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「圖示描邊 hover」.

### JavaScript — `FX[136]` from `site/fx.js`

```js
136(s,x,card){const IC=['<path d="M3 11l9-8 9 8"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/>','<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/>','<path d="M12 20s-7-4.5-9-9a5 5 0 0 1 9-3 5 5 0 0 1 9 3c-2 4.5-9 9-9 9z"/>','<path d="M6 16v-5a6 6 0 0 1 12 0v5l2 2H4z"/><path d="M10 20a2 2 0 0 0 4 0"/>'];
  const w=el('div','icr');const tiles=IC.map(d=>{const t=el('div','ict');t.innerHTML=`<svg viewBox="0 0 24 24">${d}</svg>`;w.append(t);return t});s.append(w);
  const run=t=>{gsap.fromTo(t.querySelectorAll('path,circle'),{drawSVG:'0%'},{drawSVG:'100%',duration:.7,ease:'power2.inOut',stagger:.12,overwrite:true});gsap.fromTo(t,{y:0},{y:-6,duration:.3,yoyo:true,repeat:1,ease:'power2.out',overwrite:true});tiles.forEach(o=>o.classList.toggle('on',o===t))};
  let real=false,k=0;tiles.forEach(t=>t.addEventListener('pointerenter',()=>{real=true;run(t)}));w.addEventListener('pointerleave',()=>real=false);card._timers.push(setInterval(()=>{if(!real)run(tiles[k++%4])},1200))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx136` rules from `site/fx.css`

_No dedicated `.fx136` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #136
