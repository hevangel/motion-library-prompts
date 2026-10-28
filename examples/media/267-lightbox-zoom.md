# 267 · 點圖放大燈箱 — Lightbox Zoom

點一下縮圖，它從原位置平滑放大到畫面中央，背景變暗；再點縮回

- 元件 Component: 圖片・媒體 (`media`)
- 時機 Timing: 切換
- 技術 Tech: GSAP
- 情境 Uses: 介面互動、轉場切換
- 風格／關鍵字 Style: 燈箱 lightbox 放大 圖片檢視 相簿 Modal Zoom Gallery Photo Viewer Flip 圖片 媒體
- 標籤 Tag: Flip
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「點圖放大燈箱（Lightbox Zoom）」動態效果：一排正方形縮圖，點擊任一張時，那張圖從原本的位置與大小平滑放大到畫面中央的大尺寸（約 0.55 秒、緩入緩出），同時背後鋪上一層半透明遮罩讓其他內容變暗；點擊大圖或遮罩時，圖片平滑縮回原本在縮圖列中的位置，遮罩淡出。（GSAP Flip：Flip.getState 記錄縮圖 → 加上「放大」的 class（改為絕對定位置中、較大尺寸）→ Flip.from 補間；收回時反向；遮罩用 opacity transition）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx267">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「點圖放大燈箱」.

### JavaScript — `FX[267]` from `site/fx.js`

```js
267(s,x,card){const w=el('div','md-lb');const ths=[0,1,2,3].map(i=>{const t=el('button','md-th');t.setAttribute('aria-label','放大圖片 '+(i+1));t.innerHTML=mdImg(i);w.append(t);return t});const bd=el('div','md-bd');w.append(bd);s.append(w);let open=null,real=0;
  const close=()=>{if(!open)return;const t=open;open=null;const st=Flip.getState(t);t.classList.remove('big');Flip.from(st,{duration:.5,ease:'power3.inOut',zIndex:5});bd.classList.remove('on')};
  const show=t=>{if(open)return close();open=t;const st=Flip.getState(t);t.classList.add('big');Flip.from(st,{duration:.55,ease:'power3.inOut',zIndex:5});bd.classList.add('on')};
  ths.forEach(t=>t.onclick=()=>{real=Date.now();open===t?close():show(t)});bd.onclick=()=>{real=Date.now();close()};let k=0;
  card._timers.push(setInterval(()=>{if(Date.now()-real<5000)return;open?close():show(ths[k++%4])},1700))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx267` rules from `site/fx.css`

_No dedicated `.fx267` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #267
