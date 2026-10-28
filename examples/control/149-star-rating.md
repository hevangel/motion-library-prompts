# 149 · 星星評分 — Star Rating

點選評分時，星星由左到右依序點亮並彈跳

- 元件 Component: 表單・控制項 (`control`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: App 介面、介面互動
- 風格／關鍵字 Style: 評分 星星 評價 回饋 Rating Stars Review Feedback App 手機 行動裝置 微互動 Mobile App Micro-interaction
- 標籤 Tag: Rating
- 範例文字 Example text: 「幫這次體驗評分」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「星星評分（Star Rating）」動態效果：五顆空心星星，使用者點選第 N 顆時，第 1 到第 N 顆從左到右依序填滿並各自從小彈跳放大（每顆間隔約 0.08 秒），其餘維持空心；下方同步顯示對應的文字回饋（例如「很好」「超讚！」）。點選較少的星數時，多出來的星星變回空心。（CSS：切換 .on 填色與 .pop 彈跳 keyframes，用 setTimeout 或 transition-delay 依索引錯開；每顆星是 button 並附 aria-label）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx149">`, preview text 「幫這次體驗評分」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「星星評分」.

### JavaScript — `FX[149]` from `site/fx.js`

```js
149(s,x,card){const c=el('div','rtc');const w=el('div','rtw');const lb=el('div','rtl');lb.textContent=x;const rs=el('div','rts');c.append(w,lb,rs);s.append(c);let real=0;const T2=['','很差','普通','不錯','很好','超讚！'];
  const st=[...Array(5)].map((_,i)=>{const b=el('button','star');b.setAttribute('aria-label',(i+1)+' 顆星');b.innerHTML='<svg viewBox="0 0 24 24"><path d="M12 2.8l2.8 5.8 6.3.9-4.6 4.4 1.1 6.3L12 17.3l-5.6 2.9 1.1-6.3L2.9 9.5l6.3-.9z"/></svg>';b.onclick=()=>{real=Date.now();rate(i+1)};w.append(b);return b});
  let gen=0;const rate=n=>{const g=++gen;st.forEach((b,k)=>{b.classList.remove('pop');if(k<n)setTimeout(()=>{if(g===gen)b.classList.add('on','pop')},k*80);else b.classList.remove('on')});rs.textContent=T2[n]};
  const demo=()=>{if(Date.now()-real<4000)return;rate(0);setTimeout(()=>{if(Date.now()-real>=4000)rate(3+Math.floor(Math.random()*3))},500)};demo();card._timers.push(setInterval(demo,2600))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx149` rules from `site/fx.css`

_No dedicated `.fx149` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #149
