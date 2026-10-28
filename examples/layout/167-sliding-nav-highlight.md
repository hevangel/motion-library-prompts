# 167 · 選單滑塊跟隨 — Sliding Nav Highlight

滑過選單項目時，背景膠囊滑塊跟著移到該項目

- 元件 Component: 版面・頁面 (`layout`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動、App 介面
- 風格／關鍵字 Style: 選單 導覽 滑塊 膠囊 highlight 跟隨 nav pill hover indicator tabs hover 懸停 滑鼠移入 滑過 互動
- 標籤 Tag: CSS + JS
- 範例文字 Example text: 「首頁 作品 服務 文章 聯絡」（預覽底色：dark）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「選單滑塊跟隨（Sliding Nav Highlight）」動態效果：膠囊形導覽列，滑鼠移到某個項目時，一顆膠囊背景滑塊從原本位置平滑滑過去並改變寬度貼合該項目，文字同時切換成與滑塊反差的顏色；滑鼠離開整個選單時滑塊回到目前所在的頁面項目。約 0.4 秒，帶一點點過衝。（做法：pointerenter 時讀取項目的 offsetLeft 與 offsetWidth，設定滑塊的 translateX 與 width，transition cubic-bezier(.2,.9,.3,1.1)）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx167">`, preview text 「首頁 作品 服務 文章 聯絡」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「選單滑塊跟隨」.

### JavaScript — `FX[167]` from `site/fx.js`

```js
167(s,x,card){const n=el('nav','npw');const pill=el('i','npl');n.append(pill);const its=words(x).slice(0,5).map(v=>{const a=el('span','npi');a.textContent=v;n.append(a);return a});s.append(n);let real=false,k=0;
  const go=i=>{const a=its[i];pill.style.width=a.offsetWidth+'px';pill.style.transform=`translateX(${a.offsetLeft}px)`;its.forEach(o=>o.classList.toggle('on',o===a))};
  its.forEach((a,i)=>a.addEventListener('pointerenter',()=>{real=true;go(i)}));n.addEventListener('pointerleave',()=>{real=false;go(0)});requestAnimationFrame(()=>go(0));card._timers.push(setInterval(()=>{if(!real)go(++k%its.length)},1000))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx167` rules from `site/fx.css`

_No dedicated `.fx167` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #167
