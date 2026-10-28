# 247 · 展開搜尋框 — Expanding Search

平常只有一個放大鏡圓鈕，點下後向左展開成搜尋框

- 元件 Component: 表單・控制項 (`control`)
- 時機 Timing: 切換
- 技術 Tech: CSS
- 情境 Uses: 介面互動、App 介面
- 風格／關鍵字 Style: 搜尋 放大鏡 展開 收合 導覽列 Expanding Search Bar Icon Input Header 表單 控制項
- 標籤 Tag: CSS transition
- 範例文字 Example text: 「搜尋作品…」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「展開搜尋框（Expanding Search）」動態效果：導覽列上的搜尋：平常只是一顆圓形放大鏡按鈕，點擊後按鈕向左平滑展開成長條搜尋框（約 0.5 秒），輸入框內的文字在展開一半後才淡入，放大鏡旋轉 90 度並外圍亮起一圈框線；輸入框失去焦點且沒有內容時收回成圓鈕。（CSS：容器 overflow:hidden，width 從圓鈕寬度過渡到展開寬度，cubic-bezier(.6,0,.2,1)；input opacity 搭配 transition-delay；JS 切換 class 並 focus 輸入框）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx247">`, preview text 「搜尋作品…」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「展開搜尋框」.

### JavaScript — `FX[247]` from `site/fx.js`

```js
247(s,x,card){const w=el('div','fm-sr');w.innerHTML='<input type="search" aria-label="搜尋"><button type="button" aria-label="搜尋"><svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="6.5"/><path d="M16 16l4.5 4.5"/></svg></button>';const inp=w.querySelector('input');inp.placeholder=x;s.append(w);
  w.querySelector('button').onclick=()=>{real=Date.now();if(w.classList.contains('open')&&!inp.value){w.classList.remove('open');inp.blur()}else{w.classList.add('open');inp.focus()}};inp.addEventListener('blur',()=>{if(!inp.value)w.classList.remove('open')});let real=0;
  card._timers.push(setInterval(()=>{if(Date.now()-real<6000||document.activeElement===inp)return;w.classList.toggle('open')},1800))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx247` rules from `site/fx.css`

_No dedicated `.fx247` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #247
