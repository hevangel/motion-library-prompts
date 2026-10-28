# 151 · 錯誤震動提示 — Shake on Error

輸入錯誤時欄位左右震動，下方滑出錯誤訊息

- 元件 Component: 表單・控制項 (`control`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: App 介面、介面互動
- 風格／關鍵字 Style: 錯誤 震動 搖晃 驗證 密碼 登入 表單 Shake Error Validation Wrong Password Login App 手機 行動裝置 微互動 Mobile App Micro-interaction
- 標籤 Tag: CSS keyframes
- 範例文字 Example text: 「密碼錯誤，請再試一次」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「錯誤震動提示（Shake on Error）」動態效果：登入時密碼錯誤，輸入框左右快速震動幾下（像搖頭說不，約 0.45 秒，幅度由小到大再變小），邊框同時切換成錯誤提示色，下方的錯誤訊息從上方 4px 淡入滑出；修正輸入後邊框與訊息恢復。（CSS：keyframes 以 translateX 做 10%–90% 的左右來回，cubic-bezier(.36,.07,.19,.97)；重播前先移除 class 並觸發 reflow；可搭配手機震動 navigator.vibrate）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx151">`, preview text 「密碼錯誤，請再試一次」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「錯誤震動提示」.

### JavaScript — `FX[151]` from `site/fx.js`

```js
151(s,x,card){const f=el('div','shk');f.innerHTML='<div class="pw"><span>••••••</span></div><div class="er"></div>';f.querySelector('.er').textContent=x;s.append(f);
  const run=()=>{f.classList.remove('err');void f.offsetWidth;f.classList.add('err');setTimeout(()=>f.classList.remove('err'),2200)};run();card._timers.push(setInterval(run,3000))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx151` rules from `site/fx.css`

_No dedicated `.fx151` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #151
