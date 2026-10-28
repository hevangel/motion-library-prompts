# 159 · 捲動橫移大字 — Scroll Marquee Text

三行大字隨捲動左右反向移動，中間一行空心

- 元件 Component: 文字 (`text`)
- 時機 Timing: 捲動觸發
- 技術 Tech: GSAP
- 情境 Uses: 背景裝飾、捲動效果、標題・Hero
- 風格／關鍵字 Style: 大字 橫移 跑馬燈 反向 標題 Scroll Marquee Big Type Horizontal Text Kinetic 捲動 滾動 scroll ScrollTrigger scrub 捲動觸發
- 標籤 Tag: ScrollTrigger scrub
- 範例文字 Example text: 「MOTION LIBRARY」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「捲動橫移大字（Scroll Marquee Text）」動態效果：畫面中有三行超大字級的重複文字（中間那行是空心描邊），捲動時第一、三行往左移、第二行往右移，移動距離完全跟著捲動進度（停止捲動就停住），形成有張力的版面節奏。（GSAP：timeline 綁 ScrollTrigger scrub:0.6，各行 fromTo xPercent 0↔-40；區塊 pin 或 sticky）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx159">`, preview text 「MOTION LIBRARY」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「捲動橫移大字」.

### JavaScript — `FX[159]` from `site/fx.js`

```js
159(s,x){const{sc,wrap,view}=scrollBox(s);view.classList.add('smq');const U=rep(x+' ',5);const rows=[0,1,2].map(i=>{const r=el('div','smr2'+(i===1?' o':''));r.textContent=U;view.append(r);return r});
  const tl=gsap.timeline({scrollTrigger:{trigger:wrap,scroller:sc,start:'top top',end:'bottom bottom',scrub:.6}});rows.forEach((r,i)=>tl.fromTo(r,{xPercent:i%2?-40:0},{xPercent:i%2?0:-40,ease:'none'},0));autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx159` rules from `site/fx.css`

_No dedicated `.fx159` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #159
