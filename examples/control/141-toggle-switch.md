# 141 · 開關切換 — Toggle Switch

圓鈕滑到另一側時略微拉長，軌道跟著切換狀態

- 元件 Component: 表單・控制項 (`control`)
- 時機 Timing: 懸停・點擊、切換
- 技術 Tech: CSS
- 情境 Uses: 介面互動、App 介面
- 風格／關鍵字 Style: 開關 切換 switch toggle 設定 iOS 圓鈕 App 手機 行動裝置 微互動 Mobile App Micro-interaction
- 標籤 Tag: CSS switch
- 範例文字 Example text: 「通知提醒」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「開關切換（Toggle Switch）」動態效果：App 設定頁的開關：點擊時圓鈕從一側滑到另一側，滑動過程中圓鈕會先橫向拉長再縮回（像有彈性的果凍），抵達時略微過衝後定位；軌道同時切換成開啟狀態的強調色，關閉時回到低對比的狀態。約 0.35 秒。（CSS：button role="switch"，圓鈕用 left 的 transition 搭配 cubic-bezier(.5,1.4,.5,1) 做過衝，另用 keyframes 在 50% 時加寬；記得更新 aria-checked）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx141">`, preview text 「通知提醒」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「開關切換」.

### JavaScript — `FX[141]` from `site/fx.js`

```js
141(s,x,card){const w=el('div','tgw');w.innerHTML='<span class="tgl"></span><button class="tg" role="switch" aria-checked="false"><i></i></button>';w.querySelector('.tgl').textContent=x;s.append(w);const b=w.querySelector('.tg');let real=0;
  const tog=()=>{const on=!b.classList.contains('on');b.classList.toggle('on',on);b.setAttribute('aria-checked',on)};b.onclick=()=>{real=Date.now();tog()};card._timers.push(setInterval(()=>{if(Date.now()-real>3000)tog()},1400))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx141` rules from `site/fx.css`

_No dedicated `.fx141` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #141
