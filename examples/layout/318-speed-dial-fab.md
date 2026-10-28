# 318 · 浮動按鈕展開選單 — Speed Dial FAB

右下角的「+」按鈕點開時轉成「×」，上方依序彈出幾個小動作按鈕和標籤

- 元件 Component: 版面・頁面 (`layout`)
- 時機 Timing: 切換
- 技術 Tech: CSS
- 情境 Uses: 介面互動、App 介面
- 風格／關鍵字 Style: 浮動按鈕 FAB 展開 快捷 動作 Speed Dial Floating Action Button Menu 版面 頁面
- 標籤 Tag: CSS transition
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-21

**AI 提示詞（網站複製格式）:**

```text
「浮動按鈕展開選單（Speed Dial FAB）」動態效果：畫面右下角的圓形浮動按鈕（+）：點擊時按鈕旋轉 135 度變成 ×，背景鋪上一層半透明遮罩，上方由下往上依序彈出三個小圓形動作按鈕，每個左側帶一個文字標籤（例如新增筆記、拍照、分享連結），出現時從小、略低的位置帶回彈放大；再點一次或點遮罩則依相反順序收回。（CSS：.open 時主按鈕 rotate(135deg)；每個動作項設 --i，transform: translateY + scale 過渡，transition-delay 依索引計算，收合時順序相反）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx318">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「浮動按鈕展開選單」.

### JavaScript — `FX[318]` from `site/fx.js`

```js
318(s,x,card){const f=lyPage(s);f.insertAdjacentHTML('beforeend','<div class="pg-pc"><b>文件</b><i class="ly-bl"></i><i class="ly-bl s"></i><i class="ly-bl"></i></div><div class="pg-bd"></div>');const dial=el('div','pg-dl');const A=[['✎','新增筆記'],['📷','拍照'],['🔗','分享連結']];dial.innerHTML=A.map(([i,l],k)=>`<div class="pg-da" style="--i:${k}"><span></span><button aria-label="${l}">${i}</button></div>`).join('')+'<button class="pg-fab" aria-label="更多">+</button>';dial.querySelectorAll('.pg-da span').forEach((sp,k)=>sp.textContent=A[k][1]);f.append(dial);
  let real=0;const tog=o=>f.classList.toggle('pg-dopen',o);dial.querySelector('.pg-fab').onclick=()=>{real=Date.now();tog(!f.classList.contains('pg-dopen'))};f.querySelector('.pg-bd').onclick=()=>{real=Date.now();tog(false)};
  card._timers.push(setInterval(()=>{if(Date.now()-real>5000)tog(!f.classList.contains('pg-dopen'))},1700))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx318` rules from `site/fx.css`

_No dedicated `.fx318` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #318
