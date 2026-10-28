# 277 · 捲動形狀變形 — Scroll Shape Morph

一個圖形隨捲動依序變形成星星、愛心、方塊，邊變邊轉

- 元件 Component: 圖形・SVG (`shape`)
- 時機 Timing: 捲動觸發
- 技術 Tech: GSAP
- 情境 Uses: 捲動效果、強調重點
- 風格／關鍵字 Style: 變形 形狀 morph 星星 愛心 SVG 捲動 Scroll Shape Morph 捲動觸發 ScrollTrigger
- 標籤 Tag: MorphSVG
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「捲動形狀變形（Scroll Shape Morph）」動態效果：畫面中央一個實心的圓形 SVG 圖形，隨著使用者往下捲動，依序平滑變形成五角星、愛心、圓角方塊，每次變形同時旋轉 90 度；變形進度完全由捲動控制，往回捲會反向變回去。（GSAP MorphSVGPlugin + ScrollTrigger scrub：timeline 依序 to(path, {morphSVG: 下一個形狀的 d, rotation:"+=90", transformOrigin:"50% 50%"})）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx277">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「捲動形狀變形」.

### JavaScript — `FX[277]` from `site/fx.js`

```js
277(s,x){const{sc,wrap,view}=scrollBox(s);view.classList.add('cen');view.innerHTML='<svg class="sx-mo" viewBox="0 0 100 100"><path d="M50 10 A40 40 0 1 1 49.9 10Z"/></svg>';const p=view.querySelector('path');
  const SH=['M50 6 L61 38 L95 38 L67 58 L78 92 L50 71 L22 92 L33 58 L5 38 L39 38Z','M50 88 C20 66 6 50 6 32 C6 18 17 8 30 8 C40 8 46 14 50 22 C54 14 60 8 70 8 C83 8 94 18 94 32 C94 50 80 66 50 88Z','M14 14 H86 V86 H14Z'];
  const tl=gsap.timeline({scrollTrigger:{trigger:wrap,scroller:sc,start:'top top',end:'bottom bottom',scrub:.6}});SH.forEach(d=>tl.to(p,{morphSVG:d,rotation:'+=90',transformOrigin:'50% 50%',ease:'power1.inOut'}));autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx277` rules from `site/fx.css`

_No dedicated `.fx277` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #277
