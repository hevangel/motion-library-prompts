# 246 · 驗證碼輸入 — OTP Input

四格驗證碼，輸入一格自動跳下一格；正確時依序跳起，錯誤時整排抖動

- 元件 Component: 表單・控制項 (`control`)
- 時機 Timing: 切換
- 技術 Tech: CSS
- 情境 Uses: 介面互動、App 介面
- 風格／關鍵字 Style: 驗證碼 OTP 一次性密碼 簡訊 登入 PIN Code Input Verification Auto Focus 表單 控制項
- 標籤 Tag: JS + CSS
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「驗證碼輸入（OTP Input）」動態效果：四格驗證碼輸入框：每格只能輸入一個數字，輸入後該格輕彈一下並自動跳到下一格，在空格按倒退鍵會回到上一格並清除；四格填滿後自動驗證：正確時每格依序向上跳起並填滿底色，錯誤時整排左右抖動、外框變成警示樣式。（JS：每格 maxLength=1、inputMode="numeric"，input 事件後 focus 下一格，keydown Backspace 處理倒退；結果用 class 觸發 CSS keyframes，跳起用 animation-delay 錯開；手機上字級至少 16px 避免自動放大）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx246">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「驗證碼輸入」.

### JavaScript — `FX[246]` from `site/fx.js`

```js
246(s,x,card){const w=el('div','fm-otp');w.innerHTML='<p>輸入驗證碼</p><div class="fm-ob"></div>';const ob=w.querySelector('.fm-ob');const ins=[...Array(4)].map(()=>{const i=el('input');i.inputMode='numeric';i.maxLength=1;i.autocomplete='one-time-code';ob.append(i);return i});s.append(w);let real=0;
  const check=()=>{const v=ins.map(i=>i.value).join('');w.classList.remove('ok','bad');if(v.length===4){void w.offsetWidth;w.classList.add(v==='2026'?'ok':'bad')}};
  ins.forEach((i,k)=>{i.addEventListener('input',()=>{real=Date.now();i.value=i.value.replace(/\D/g,'').slice(-1);i.classList.toggle('f',!!i.value);if(i.value&&ins[k+1])ins[k+1].focus();check()});
    i.addEventListener('keydown',e=>{if(e.key==='Backspace'&&!i.value&&ins[k-1]){ins[k-1].focus();ins[k-1].value='';ins[k-1].classList.remove('f');check()}});i.addEventListener('focus',()=>{if(Date.now()-real>6000){ins.forEach(x=>{x.value='';x.classList.remove('f')});n=0;check();real=Date.now();if(i!==ins[0])return ins[0].focus()}real=Date.now();i.select()})});
  let n=0;card._timers.push(setInterval(()=>{if(Date.now()-real<6000||ins.includes(document.activeElement))return;if(n<4){ins[n].value='2026'[n];ins[n].classList.add('f')}else if(n===7){ins.forEach(i=>{i.value='';i.classList.remove('f')})}n=(n+1)%9;check()},380))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx246` rules from `site/fx.css`

_No dedicated `.fx246` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #246
