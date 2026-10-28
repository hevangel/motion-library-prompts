# 203 · 漢堡選單展開 — Hamburger Menu Reveal

三條線變成叉叉，全螢幕選單從按鈕處圓形擴散展開

- 元件 Component: 版面・頁面 (`layout`)
- 時機 Timing: 懸停・點擊、切換
- 技術 Tech: CSS
- 情境 Uses: 介面互動、App 介面
- 風格／關鍵字 Style: 漢堡選單 選單 全螢幕 導覽 手機版 叉叉 Hamburger Menu Overlay Fullscreen Nav Toggle 版面 頁面 網頁結構
- 標籤 Tag: clip-path
- 範例文字 Example text: 「首頁 作品 服務 聯絡」（預覽底色：dark）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「漢堡選單展開（Hamburger Menu Reveal）」動態效果：點擊右上角的漢堡選單按鈕時，三條線變形成叉叉（上下兩條旋轉 ±45 度並移到中間、中間那條縮短淡出），同時全螢幕選單以按鈕位置為圓心用圓形遮罩擴散展開，選單項目由上到下依序從下方滑入淡出現（間隔約 0.07 秒）；再點一次則反向收合。約 0.6 秒、緩入緩出。（CSS：切換一個 open class；選單層 clip-path:circle(0% at 按鈕位置) → circle(150%)；線條用 top 與 rotate 的 transition；項目 transition-delay 依索引遞增）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx203">`, preview text 「首頁 作品 服務 聯絡」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「漢堡選單展開」.

### JavaScript — `FX[203]` from `site/fx.js`

```js
203(s,x,card){const f=lyPage(s,true);const bt=el('button','ly-hb');bt.setAttribute('aria-label','選單');bt.innerHTML='<i></i><i></i><i></i>';const ov=el('nav','ly-ov');words(x).slice(0,4).forEach((v,i)=>{const a=el('span');a.textContent=v;a.style.setProperty('--i',i);ov.append(a)});f.append(ov,bt);
  let real=0;const tog=()=>f.classList.toggle('ly-open');bt.onclick=()=>{real=Date.now();tog()};card._timers.push(setInterval(()=>{if(Date.now()-real>4000)tog()},2200))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx203` rules from `site/fx.css`

_No dedicated `.fx203` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #203
