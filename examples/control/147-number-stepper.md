# 147 · 數量步進器 — Number Stepper

按加減時按鈕回饋，數字往上或往下滾動切換

- 元件 Component: 表單・控制項 (`control`)
- 時機 Timing: 懸停・點擊、切換
- 技術 Tech: CSS
- 情境 Uses: App 介面、介面互動、數字資訊
- 風格／關鍵字 Style: 數量 加減 步進器 購物車 計數 Stepper Counter Quantity Plus Minus Cart App 手機 行動裝置 微互動 Mobile App Micro-interaction
- 標籤 Tag: Stepper
- 範例文字 Example text: 「數量」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「數量步進器（Number Stepper）」動態效果：購物車的數量選擇器：左右是減號與加號圓形按鈕，中間是數字；按下按鈕時按鈕縮小並切換成強調色作為回饋，數字依方向滾動切換——加的時候舊數字往上滑出、新數字從下方滑入，減的時候方向相反，約 0.3 秒；到達上下限時數字不再變化。（CSS：數字容器 overflow:hidden，新舊數字各用 keyframes translateY ±100% 進出，結束後移除舊元素）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx147">`, preview text 「數量」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「數量步進器」.

### JavaScript — `FX[147]` from `site/fx.js`

```js
147(s,x,card){const w=el('div','stw');w.innerHTML='<span class="sl2"></span><div class="stp2"><button aria-label="減少">−</button><div class="nv2"><b>1</b></div><button aria-label="增加">+</button></div>';w.querySelector('.sl2').textContent=x;s.append(w);
  const box=w.querySelector('.nv2'),[m,p]=w.querySelectorAll('button');let n=1,real=0,dir=1;
  const set=(d,btn)=>{btn.classList.add('pr');setTimeout(()=>btn.classList.remove('pr'),150);const nn=Math.max(0,Math.min(9,n+d));if(nn===n)return;const o=box.lastChild;const nb=el('b',d>0?'in-up':'in-dn');nb.textContent=nn;o.className=d>0?'out-up':'out-dn';box.append(nb);setTimeout(()=>o.remove(),300);n=nn};
  m.onclick=()=>{real=Date.now();set(-1,m)};p.onclick=()=>{real=Date.now();set(1,p)};card._timers.push(setInterval(()=>{if(Date.now()-real<3000)return;if(n>=4)dir=-1;if(n<=1)dir=1;set(dir,dir>0?p:m)},900))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx147` rules from `site/fx.css`

_No dedicated `.fx147` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #147
