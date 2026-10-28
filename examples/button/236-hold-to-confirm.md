# 236 · 長按確認 — Hold to Confirm

按住不放時進度慢慢填滿，放開就退回，填滿才執行，適合刪除等危險操作

- 元件 Component: 按鈕 (`button`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動、App 介面
- 風格／關鍵字 Style: 長按 按住 確認 刪除 危險操作 進度 Hold To Confirm Long Press Delete Destructive 按鈕
- 標籤 Tag: CSS transition
- 範例文字 Example text: 「按住刪除」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「長按確認（Hold to Confirm）」動態效果：危險操作（例如刪除）用的按鈕：外框樣式，使用者按住不放時，一層填滿從左往右以約 1.2 秒等速填滿整顆按鈕、按鈕微微縮小；中途放開則填滿快速退回、不執行；填滿後按鈕輕微彈一下、文字變成「已刪除 ✓」。可避免誤觸。（CSS：填滿層 transform:scaleX(0)，按住時加 class 改成 scaleX(1) 並設 transition 1.2s linear，放開時移除 class 用較短的 transition 退回；JS 在 pointerdown 開 1.2 秒計時器，pointerup / pointerleave 取消）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx236">`, preview text 「按住刪除」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「長按確認」.

### JavaScript — `FX[236]` from `site/fx.js`

```js
236(s,x,card){const b=bxBtn('bx-hd',x);b.insertAdjacentHTML('afterbegin','<i class="bx-hf"></i>');const lb=b.querySelector('span');s.append(b);const hint=el('div','bx-hint','按住不放');s.append(hint);let tm=0,real=0;
  const down=()=>{if(b.classList.contains('ok'))return;b.classList.add('hold');tm=setTimeout(()=>{b.classList.remove('hold');b.classList.add('ok');lb.textContent='已刪除 ✓';setTimeout(()=>{b.classList.remove('ok');lb.textContent=x},1500)},1200)};
  const up=()=>{clearTimeout(tm);b.classList.remove('hold')};
  b.addEventListener('pointerdown',()=>{real=Date.now();down()});['pointerup','pointerleave'].forEach(ev=>b.addEventListener(ev,up));card._kill.push(()=>clearTimeout(tm));
  let k=0;card._timers.push(setInterval(()=>{if(Date.now()-real<5000)return;k++;down();setTimeout(()=>{if(Date.now()-real>5000&&k%2)up()},500)},3200))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx236` rules from `site/fx.css`

_No dedicated `.fx236` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #236
