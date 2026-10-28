# 150 · 啟動頁轉場 — Splash to Home

啟動 Logo 彈出呼吸，再放大穿過畫面進入首頁

- 元件 Component: 版面・頁面 (`layout`)
- 時機 Timing: 進場
- 技術 Tech: GSAP
- 情境 Uses: App 介面、轉場切換、Logo・品牌
- 風格／關鍵字 Style: 啟動頁 開場 splash 載入 Logo 首頁 轉場 Launch Screen Intro Zoom Through App 手機 行動裝置 微互動 Mobile App Micro-interaction
- 標籤 Tag: Splash
- 範例文字 Example text: 「M」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「啟動頁轉場（Splash to Home）」動態效果：App 開啟時，畫面中央的 Logo 從小彈出（back.out），輕輕呼吸一次；接著 Logo 加速放大到充滿整個螢幕並淡出，像穿過 Logo 進入 App，底下的首頁內容（主視覺卡片、列表）同時由上到下依序淡入上浮。整段約 2 秒，結束後停在首頁。（GSAP：timeline：logo scale 0.6→1 → yoyo 1.06 → scale 14（power3.in）＋啟動層 opacity 0 → 首頁元素 stagger fromTo y:10 / opacity:0）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx150">`, preview text 「M」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「啟動頁轉場」.

### JavaScript — `FX[150]` from `site/fx.js`

```js
150(s,x){const ph=phone(s);const home=el('div','home');home.innerHTML='<i class="hb"></i>';for(let i=0;i<4;i++)home.append(mrow(i));const sp=el('div','spl');const lg=el('i');lg.textContent=chars(x)[0]||'M';sp.append(lg);ph.append(home,sp);
  gsap.timeline({repeat:-1,repeatDelay:.6}).set(sp,{opacity:1},0).fromTo(lg,{scale:.6,opacity:0},{scale:1,opacity:1,duration:.6,ease:'back.out(1.7)'},.2).to(lg,{scale:1.06,duration:.35,yoyo:true,repeat:1,ease:'sine.inOut'})
    .to(lg,{scale:14,duration:.6,ease:'power3.in'},'+=.2').to(sp,{opacity:0,duration:.3},'-=.25').fromTo(home.children,{y:10,opacity:0},{y:0,opacity:1,duration:.5,stagger:.07,ease:'power2.out'},'-=.15').to({},{duration:1.6})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx150` rules from `site/fx.css`

_No dedicated `.fx150` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #150
