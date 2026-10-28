# 093 · 橫向捲動 — Horizontal Scroll

往下捲、內容往左滑

- 元件 Component: 版面・頁面 (`layout`)
- 時機 Timing: 捲動觸發
- 技術 Tech: GSAP
- 情境 Uses: 捲動效果
- 風格／關鍵字 Style: 
- 標籤 Tag: ScrollTrigger scrub
- 範例文字 Example text: 「橫向 捲動 展示 作品」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「橫向捲動（Horizontal Scroll）」動態效果：往下捲動時，整排作品卡片改為往左橫向滑動，捲到底剛好看到最後一張，像橫向作品集展示。（GSAP：ScrollTrigger pin（或 sticky）+ scrub，x 移動距離 = 軌道寬 − 視窗寬）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx93">`, preview text 「橫向 捲動 展示 作品」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「橫向捲動」.

### JavaScript — `FX[93]` from `site/fx.js`

```js
93(s,x){const{sc,wrap,view}=scrollBox(s);const tr=el('div','htrack');words(x).forEach((v,i)=>{const p=el('div','hp');p.innerHTML=`<small>0${i+1}</small><b></b>`;p.querySelector('b').textContent=v;p.style.background=GC[i%4];tr.append(p)});view.append(tr);
  gsap.to(tr,{x:()=>-(tr.scrollWidth-view.clientWidth),ease:'none',scrollTrigger:{trigger:wrap,scroller:sc,start:'top top',end:'bottom bottom',scrub:.5,invalidateOnRefresh:true}});autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx93` rules from `site/fx.css`

_No dedicated `.fx93` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #93
