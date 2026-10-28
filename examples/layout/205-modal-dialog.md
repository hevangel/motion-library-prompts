# 205 · 彈出視窗 — Modal Dialog

背景模糊變暗，視窗從稍小稍低的位置彈性浮出

- 元件 Component: 版面・頁面 (`layout`)
- 時機 Timing: 進場、退場
- 技術 Tech: CSS
- 情境 Uses: 介面互動、App 介面
- 風格／關鍵字 Style: 彈窗 對話框 視窗 確認 modal dialog popup 背景模糊 Overlay 版面 頁面 網頁結構
- 標籤 Tag: CSS transition
- 範例文字 Example text: 「確定要送出嗎？」（預覽底色：dark）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「彈出視窗（Modal Dialog）」動態效果：點擊按鈕後，背景加上一層半透明遮罩並輕微模糊（約 0.35 秒淡入），對話框從 90% 大小、略低於中心的位置以帶一點過衝的彈性浮到正中央，內容包含標題、說明與取消／確定兩顆按鈕；點擊遮罩或任一按鈕時，對話框淡出縮回、遮罩淡出。（CSS：開關一個 open class；遮罩 opacity + backdrop-filter:blur；對話框 transform:translate(-50%,-40%) scale(.9) → translate(-50%,-50%) scale(1)，transition cubic-bezier(.3,1.4,.5,1)；記得處理焦點與 Esc 鍵關閉）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx205">`, preview text 「確定要送出嗎？」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「彈出視窗」.

### JavaScript — `FX[205]` from `site/fx.js`

```js
205(s,x,card){const f=lyPage(s);f.insertAdjacentHTML('beforeend','<div class="ly-pg"><b>商品頁</b><i class="ly-bl"></i><i class="ly-bl s"></i><button class="ly-ob">開啟視窗</button></div><div class="ly-bd"></div><div class="ly-md"><b></b><i class="ly-bl"></i><i class="ly-bl s"></i><div class="ly-mb"><span>取消</span><span class="p">確定</span></div></div>');f.querySelector('.ly-md b').textContent=x;
  let real=0;const ob=f.querySelector('.ly-ob');const tog=()=>f.classList.toggle('ly-open');ob.onclick=()=>{real=Date.now();tog()};f.querySelector('.ly-bd').onclick=()=>{real=Date.now();f.classList.remove('ly-open')};f.querySelectorAll('.ly-mb span').forEach(e=>e.onclick=()=>{real=Date.now();f.classList.remove('ly-open')});
  card._timers.push(setInterval(()=>{if(Date.now()-real>4000){if(!f.classList.contains('ly-open')){ob.classList.add('pr');setTimeout(()=>ob.classList.remove('pr'),160)}tog()}},1800))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx205` rules from `site/fx.css`

_No dedicated `.fx205` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #205
