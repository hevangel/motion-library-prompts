# 204 · 側邊抽屜推移 — Push Side Drawer

開啟選單時整個內容頁縮小推到右側，露出底下的選單

- 元件 Component: 版面・頁面 (`layout`)
- 時機 Timing: 懸停・點擊、切換
- 技術 Tech: CSS
- 情境 Uses: 介面互動、App 介面
- 風格／關鍵字 Style: 側邊選單 抽屜 推移 縮小 off-canvas 手機 Side Drawer Push Menu Off Canvas Scale 版面 頁面 網頁結構
- 標籤 Tag: CSS transform
- 範例文字 Example text: 「首頁 作品 服務 聯絡」（預覽底色：dark）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「側邊抽屜推移（Push Side Drawer）」動態效果：點擊漢堡圖示時，目前的內容頁整體往右推並縮小到約 86%、加上圓角與陰影，像卡片一樣被推開，露出藏在底下的選單，選單項目從左側依序滑入淡出現；再點一次內容頁滑回來蓋住選單。約 0.55 秒、緩入緩出。（CSS：內容層 transform:translateX(38%) scale(.86)、transform-origin 左側中間，border-radius 一起 transition；選單項目 transition-delay 錯開）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx204">`, preview text 「首頁 作品 服務 聯絡」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「側邊抽屜推移」.

### JavaScript — `FX[204]` from `site/fx.js`

```js
204(s,x,card){const w=el('div','ly-dw');w.innerHTML='<nav class="ly-dr"><b>MENU</b></nav><div class="ly-ct"><div class="ly-cb"><i class="ly-hm"></i></div><b></b><i class="ly-bl"></i><i class="ly-bl s"></i><div class="ly-gr"><i></i><i></i></div></div>';const dr=w.querySelector('.ly-dr');words(x).slice(0,4).forEach(v=>{const a=el('span');a.textContent=v;dr.append(a)});
  w.querySelector('.ly-ct b').textContent='首頁';w.querySelectorAll('.ly-gr i').forEach((e,i)=>e.style.background=GC[i+1]);s.append(w);let real=0;w.querySelector('.ly-hm').onclick=()=>{real=Date.now();w.classList.toggle('ly-open')};
  card._timers.push(setInterval(()=>{if(Date.now()-real>4000)w.classList.toggle('ly-open')},2000))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx204` rules from `site/fx.css`

_No dedicated `.fx204` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #204
