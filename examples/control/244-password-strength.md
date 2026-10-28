# 244 · 密碼強度條 — Password Strength

輸入密碼時下方的強度條逐格長出，依強弱改變並顯示提示

- 元件 Component: 表單・控制項 (`control`)
- 時機 Timing: 切換
- 技術 Tech: CSS
- 情境 Uses: 介面互動、數字資訊
- 風格／關鍵字 Style: 密碼 強度 註冊 驗證 表單 Password Strength Meter Signup Validation 表單 控制項
- 標籤 Tag: JS + CSS
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「密碼強度條（Password Strength）」動態效果：密碼輸入框下方有四格強度條：使用者輸入時即時計算強度（長度是否達 8 字、有無大寫、數字、符號），符合越多條件就有越多格從左往右長出；強度越高，格子的視覺越強烈，下方文字依序顯示「太弱／普通／不錯／很強」；輸入框右側有顯示／隱藏密碼的眼睛按鈕；輸入框聚焦時外框亮起。（JS：input 事件計算分數 0–4，設定 data-level 與每格的 class；新亮起的格子用 scaleX 0→1 的 keyframes 長出）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx244">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「密碼強度條」.

### JavaScript — `FX[244]` from `site/fx.js`

```js
244(s,x,card){const w=el('div','fm-pw');w.innerHTML='<label>密碼</label><div class="fm-pf"><input type="text" spellcheck="false" autocomplete="off"><button type="button" aria-label="顯示密碼">👁</button></div><div class="fm-bar"><i></i><i></i><i></i><i></i></div><small></small>';s.append(w);
  const inp=w.querySelector('input'),bars=[...w.querySelectorAll('.fm-bar i')],tip=w.querySelector('small'),eye=w.querySelector('button');let show=false;const L=['','太弱','普通','不錯','很強'];
  const score=v=>!v?0:Math.min(4,(v.length>=8)+/[A-Z]/.test(v)+/\d/.test(v)+/[^\w]/.test(v)+(v.length>=4?0:-1)+1);
  const upd=()=>{const n=Math.max(0,score(inp.value));w.dataset.lv=n;bars.forEach((b,i)=>b.classList.toggle('on',i<n));tip.textContent=L[n]};
  const mask=()=>{inp.type=show?'text':'password'};eye.onclick=()=>{show=!show;mask()};show=false;mask();inp.addEventListener('input',()=>{real=Date.now();upd()});inp.addEventListener('focus',()=>real=Date.now());
  let real=0,i=0;const D=['m','mo','mot','moti','motio','motion','Motion','Motion2','Motion26','Motion26!'];upd();
  card._timers.push(setInterval(()=>{if(Date.now()-real<6000||document.activeElement===inp)return;inp.value=i<D.length?D[i]:'';i=(i+1)%(D.length+4);upd()},320))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx244` rules from `site/fx.css`

_No dedicated `.fx244` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #244
