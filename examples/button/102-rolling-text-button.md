# 102 · 文字翻滾按鈕 — Rolling Text Button

hover 時字逐一往上翻滾、按鈕反轉、箭頭轉向

- 元件 Component: 按鈕 (`button`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動、強調重點
- 風格／關鍵字 Style: 按鈕 hover 懸停 文字翻滾 Roll Text Button Hover Stagger CTA
- 標籤 Tag: CSS hover
- 範例文字 Example text: 「查看作品」（預覽底色：cream）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「文字翻滾按鈕（Rolling Text Button）」動態效果：膠囊形按鈕，左邊文字、右邊一顆圓形箭頭。滑鼠移上去時，按鈕文字的每個字依序往上翻滾（每字延遲約 0.035 秒），下方一模一樣的文字從底下補上來；同時按鈕底色與文字色互換成強調配色，右側圓圈也跟著反轉配色，並把箭頭轉成往右上 45 度；滑鼠離開時全部反向翻回。整體約 0.55 秒、緩入緩出（cubic-bezier(.7,0,.2,1)）。（CSS：每個字包 span，用 ::after{content:attr(data-t);top:100%} 做第二份文字，外層 overflow:hidden，:hover 時 translateY(-100%)，transition-delay 用 calc(var(--i)*.035s) 做逐字錯開）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage cream fx102">`, preview text 「查看作品」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「文字翻滾按鈕」.

### JavaScript — `FX[102]` from `site/fx.js`

```js
102(s,x,card){const b=el('button','rbtn');b.setAttribute('aria-label',x);const lab=el('span','rl');b.style.fontSize=Math.min(5,40/chars(x).length)+'cqw';
  chars(x).forEach((ch,i)=>{const c=el('span','rc');c.style.setProperty('--i',i);c.textContent=c.dataset.t=ch===' '?'\u00a0':ch;lab.append(c)});
  const ar=el('i','ra');ar.textContent='→';b.append(lab,ar);s.append(b);
  // 沒人操作時自動示範 hover；滑鼠移上去就交給真正的 :hover
  let real=false;b.addEventListener('pointerenter',()=>{real=true;b.classList.remove('hv')});b.addEventListener('pointerleave',()=>real=false);
  card._timers.push(setInterval(()=>{if(!real)b.classList.toggle('hv')},1500))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx102` rules from `site/fx.css`

_No dedicated `.fx102` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #102
