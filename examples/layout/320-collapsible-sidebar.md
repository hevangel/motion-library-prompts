# 320 · 側欄收合 — Collapsible Sidebar

後台側邊欄按一下收成只剩圖示，文字淡出，主內容區同步變寬

- 元件 Component: 版面・頁面 (`layout`)
- 時機 Timing: 切換
- 技術 Tech: CSS
- 情境 Uses: 介面互動、App 介面
- 風格／關鍵字 Style: 側邊欄 收合 展開 後台 儀表板 Collapsible Sidebar Nav Dashboard Admin 版面 頁面
- 標籤 Tag: CSS transition
- 範例文字 Example text: 「首頁 報表 訊息 設定」（預覽底色：dark）
- 收錄日期 Added: 2026-10-21

**AI 提示詞（網站複製格式）:**

```text
「側欄收合（Collapsible Sidebar）」動態效果：後台介面左側的側邊欄：點擊側欄頂端的收合按鈕時，側欄寬度平滑縮窄到只容得下圖示（約 0.45 秒），每個項目的文字同時往左淡出，右側主內容區同步變寬；再點一次展開時文字淡入回來；目前所在的項目有淡淡的強調底色。（CSS：側欄 width transition，cubic-bezier(.6,0,.2,1)；項目文字 opacity 與 translateX 過渡，white-space:nowrap + overflow:hidden 避免換行；主內容 flex:1 自動填滿）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx320">`, preview text 「首頁 報表 訊息 設定」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「側欄收合」.

### JavaScript — `FX[320]` from `site/fx.js`

```js
320(s,x,card){const ws=words(x);const w=el('div','pg-sbw');w.innerHTML='<aside class="pg-side"><button class="pg-tg" aria-label="收合側欄">«</button>'+['⌂','▦','✉','⚙'].map((ic,i)=>`<a class="${i?'':'on'}"><i>${ic}</i><span></span></a>`).join('')+'</aside><main class="pg-main"><b>儀表板</b><div class="pg-cards"><i></i><i></i><i></i></div><i class="ly-bl"></i><i class="ly-bl s"></i></main>';w.querySelectorAll('.pg-side span').forEach((sp,i)=>sp.textContent=ws[i%ws.length]);s.append(w);
  let real=0;const tg=w.querySelector('.pg-tg');const tog=()=>{const c=w.classList.toggle('mini');tg.textContent=c?'»':'«';tg.setAttribute('aria-label',c?'展開側欄':'收合側欄')};tg.onclick=()=>{real=Date.now();tog()};card._timers.push(setInterval(()=>{if(Date.now()-real>5000)tog()},2000))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx320` rules from `site/fx.css`

_No dedicated `.fx320` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #320
