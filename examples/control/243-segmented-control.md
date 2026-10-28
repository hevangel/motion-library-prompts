# 243 · 分段控制器 — Segmented Control

一排選項底下有一塊滑塊，點哪個就帶點彈性滑過去並改變寬度

- 元件 Component: 表單・控制項 (`control`)
- 時機 Timing: 切換
- 技術 Tech: CSS
- 情境 Uses: 介面互動、App 介面
- 風格／關鍵字 Style: 分段控制 切換 頁籤 tabs 滑塊 Segmented Control Tabs Pill Switcher iOS 表單 控制項
- 標籤 Tag: CSS transition
- 範例文字 Example text: 「日 週 月 年」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「分段控制器（Segmented Control）」動態效果：膠囊形的分段控制器，例如「日／週／月／年」；目前選項底下有一塊實心滑塊，點擊其他選項時滑塊帶一點回彈地滑到新位置，並同時改變寬度貼合新選項的文字長度；選中的文字變成與滑塊對比的顏色。約 0.45 秒。（CSS：滑塊絕對定位，JS 讀取被點按鈕的 offsetLeft 與 offsetWidth 寫進 CSS 變數，transform:translateX(var(--x)) 與 width 用 cubic-bezier(.5,1.5,.5,1) 過渡）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx243">`, preview text 「日 週 月 年」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「分段控制器」.

### JavaScript — `FX[243]` from `site/fx.js`

```js
243(s,x,card){const ws=words(x).slice(0,4);const w=el('div','fm-seg');w.innerHTML='<i class="fm-ind"></i>';const bs=ws.map((t,i)=>{const b=el('button');b.textContent=t;b.onclick=()=>{real=Date.now();go(i)};w.append(b);return b});s.append(w);let cur=0,real=0;
  const go=i=>{cur=i;const b=bs[i];w.style.setProperty('--x',b.offsetLeft+'px');w.style.setProperty('--w',b.offsetWidth+'px');bs.forEach((o,j)=>o.classList.toggle('on',j===i))};requestAnimationFrame(()=>go(0));
  card._timers.push(setInterval(()=>{if(Date.now()-real>5000)go((cur+1)%bs.length)},1500))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx243` rules from `site/fx.css`

_No dedicated `.fx243` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #243
