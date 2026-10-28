# 317 · Cookie 同意橫幅 — Cookie Banner

底部彈出 Cookie 同意卡片，餅乾圖示晃一下；按下按鈕後縮回滑走

- 元件 Component: 版面・頁面 (`layout`)
- 時機 Timing: 進場、退場
- 技術 Tech: GSAP
- 情境 Uses: 介面互動
- 風格／關鍵字 Style: Cookie 同意 橫幅 隱私 GDPR 提示 Consent Banner Privacy Notice 版面 頁面
- 標籤 Tag: GSAP
- 範例文字 Example text: 「這個網站使用 Cookie」（預覽底色：dark）
- 收錄日期 Added: 2026-10-21

**AI 提示詞（網站複製格式）:**

```text
「Cookie 同意橫幅（Cookie Banner）」動態效果：網站底部的 Cookie 同意卡片：進入頁面時卡片從下方帶回彈滑上來，左側的餅乾圖示從小、歪斜的狀態彈性轉正放大；卡片內有標題、簡短說明與兩個按鈕（只用必要／全部接受）；按下任一按鈕時按鈕輕壓一下，卡片隨即往下滑出並淡出。（GSAP：卡片 fromTo yPercent 140 → 0、ease back.out(1.4)；圖示 rotation −40 → 0、scale .4 → 1、ease elastic.out；關閉時 yPercent → 140、power3.in）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx317">`, preview text 「這個網站使用 Cookie」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「Cookie 同意橫幅」.

### JavaScript — `FX[317]` from `site/fx.js`

```js
317(s,x,card){const f=lyPage(s);f.insertAdjacentHTML('beforeend','<div class="pg-pc"><b>首頁</b><i class="ly-bl"></i><i class="ly-bl s"></i><i class="ly-bl"></i></div><div class="pg-ck"><span class="pg-cki">🍪</span><p><b></b><br><small>我們使用 Cookie 改善瀏覽體驗。</small></p><div><button class="no">只用必要</button><button class="ok">全部接受</button></div></div>');f.querySelector('.pg-ck b').textContent=x;const ck=f.querySelector('.pg-ck');let real=0;
  const show=()=>{gsap.fromTo(ck,{yPercent:140,opacity:0},{yPercent:0,opacity:1,duration:.6,ease:'back.out(1.4)'});gsap.fromTo(ck.querySelector('.pg-cki'),{rotation:-40,scale:.4},{rotation:0,scale:1,duration:.7,ease:'elastic.out(1,.5)',delay:.25})};
  const hide=b=>{gsap.timeline().to(b,{scale:.92,duration:.08}).to(b,{scale:1,duration:.15}).to(ck,{yPercent:140,opacity:0,duration:.4,ease:'power3.in'})};
  ck.querySelectorAll('button').forEach(b=>b.onclick=()=>{real=Date.now();hide(b);setTimeout(show,1800)});show();card._timers.push(setInterval(()=>{if(Date.now()-real<5000)return;hide(ck.querySelector('.ok'));setTimeout(show,1400)},3600))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx317` rules from `site/fx.css`

_No dedicated `.fx317` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #317
