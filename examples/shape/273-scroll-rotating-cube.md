# 273 · 捲動旋轉立方體 — Scroll Rotating Cube

一個 3D 立方體隨捲動旋轉，每一面寫著不同的關鍵字

- 元件 Component: 圖形・SVG (`shape`)
- 時機 Timing: 捲動觸發
- 技術 Tech: GSAP
- 情境 Uses: 捲動效果、標題・Hero
- 風格／關鍵字 Style: 立方體 3D 旋轉 方塊 cube 捲動 Scroll Rotate Cube Faces 捲動觸發 ScrollTrigger
- 標籤 Tag: ScrollTrigger
- 範例文字 Example text: 「設計 開發 動態 品牌 策略 測試」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「捲動旋轉立方體（Scroll Rotating Cube）」動態效果：畫面中央一個 3D 立方體，六個面各寫一個關鍵字並使用不同的主題色：隨著使用者往下捲動，立方體略微俯視（rotateX −20 度）並繞垂直軸旋轉，依捲動進度轉過 270 度，讓各面依序轉到正前方。（GSAP ScrollTrigger scrub：立方體 transform-style:preserve-3d，六個面以 rotateY / rotateX ± 90 度加 translateZ(邊長的一半) 組成；捲動時 tween rotationY）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx273">`, preview text 「設計 開發 動態 品牌 策略 測試」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「捲動旋轉立方體」.

### JavaScript — `FX[273]` from `site/fx.js`

```js
273(s,x){const{sc,wrap,view}=scrollBox(s);view.classList.add('cen','sx-pv');const ws=words(x);const c=el('div','sx-cb');['f','r','b','l','t','d'].forEach((k,i)=>{const f=el('div','sx-cf '+k);f.textContent=ws[i%ws.length];f.style.background=i%2?'var(--a)':GC[i%5];c.append(f)});view.append(c);
  gsap.fromTo(c,{rotationX:-20,rotationY:0},{rotationX:-20,rotationY:-270,ease:'none',scrollTrigger:{trigger:wrap,scroller:sc,start:'top top',end:'bottom bottom',scrub:.6}});autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx273` rules from `site/fx.css`

_No dedicated `.fx273` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #273
