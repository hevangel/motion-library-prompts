# 211 · 回到頂部進度環 — Back to Top Progress

捲動後右下角浮出按鈕，外圈顯示閱讀進度，點了回到頂部

- 元件 Component: 版面・頁面 (`layout`)
- 時機 Timing: 捲動觸發、懸停・點擊
- 技術 Tech: GSAP
- 情境 Uses: 介面互動、捲動效果
- 風格／關鍵字 Style: 回到頂部 頂端 進度環 閱讀進度 捲動進度 Back To Top Scroll Progress Ring Button 版面 頁面 網頁結構
- 標籤 Tag: DrawSVG scrub
- 範例文字 Example text: 「閱讀進度」（預覽底色：dark）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「回到頂部進度環（Back to Top Progress）」動態效果：長文章頁面往下捲超過一小段後，右下角的圓形按鈕從 0 彈性放大出現，按鈕外圈是一條隨整頁捲動比例畫滿的進度環（從正上方順時針），中間是向上箭頭；點擊時頁面平滑捲回頂部，回到頂端附近時按鈕縮小消失。（GSAP：DrawSVGPlugin 綁 ScrollTrigger scrub 畫進度環，onUpdate 依 progress 切換顯示；點擊用 gsap.to(window,{scrollTo:0}) 或 window.scrollTo({top:0,behavior:"smooth"})）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx211">`, preview text 「閱讀進度」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「回到頂部進度環」.

### JavaScript — `FX[211]` from `site/fx.js`

```js
211(s,x){const sc=el('div','scr nopad');const c=el('div','ly-art');c.innerHTML='<b></b>'+[...Array(14)].map((_,i)=>`<i class="ly-bl${i%3===2?' s':''}"></i>`).join('');c.querySelector('b').textContent=x;sc.append(c);s.append(sc);
  const btn=el('button','ly-top');btn.setAttribute('aria-label','回到頂部');btn.innerHTML='<svg viewBox="0 0 40 40"><circle class="tr" cx="20" cy="20" r="17"/><circle class="pr" cx="20" cy="20" r="17"/></svg><span>↑</span>';s.append(btn);
  gsap.fromTo(btn.querySelector('.pr'),{drawSVG:'0%'},{drawSVG:'100%',ease:'none',scrollTrigger:{scroller:sc,start:0,end:'max',scrub:true,onUpdate:t=>btn.classList.toggle('on',t.progress>.12)}});
  btn.onclick=()=>gsap.to(sc,{scrollTop:0,duration:.8,ease:'power3.inOut'});autoScroll(sc,btn)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx211` rules from `site/fx.css`

_No dedicated `.fx211` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #211
