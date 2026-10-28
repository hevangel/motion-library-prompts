# 276 · 散落文字聚合 — Scattered Assemble

散落在四處、翻轉縮放的字母，隨著捲動飛回原位組成標題

- 元件 Component: 文字 (`text`)
- 時機 Timing: 捲動觸發
- 技術 Tech: GSAP
- 情境 Uses: 捲動效果、標題・Hero、Logo・品牌
- 風格／關鍵字 Style: 散落 聚合 組合 字母 飛回 拼湊 Scattered Letters Assemble Scroll 捲動觸發 ScrollTrigger
- 標籤 Tag: ScrollTrigger
- 範例文字 Example text: 「ASSEMBLE」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「散落文字聚合（Scattered Assemble）」動態效果：標題的每個字母一開始隨機散落在畫面各處，各自帶著不同的旋轉角度、縮放大小並且透明；使用者往下捲動時，字母以隨機順序依序飛回原本的位置、轉正、恢復大小與不透明度，組合成完整的標題；往回捲又會散開。（GSAP ScrollTrigger scrub：SplitText 拆字，timeline.from(字母, { x/y/rotation/scale 用函式回傳隨機值, opacity:0, stagger:{each:.02, from:"random"} })）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx276">`, preview text 「ASSEMBLE」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「散落文字聚合」.

### JavaScript — `FX[276]` from `site/fx.js`

```js
276(s,x){const{sc,wrap,view}=scrollBox(s);view.classList.add('cen');const t=el('div','sx-as');const ch=chars(x).map(c=>{const sp=el('span');sp.textContent=c===' '?' ':c;t.append(sp);return sp});t.style.fontSize=Math.min(14,64/ch.length)+'cqw';view.append(t);
  gsap.timeline({scrollTrigger:{trigger:wrap,scroller:sc,start:'top top',end:'bottom bottom',scrub:.6}}).from(ch,{x:()=>gsap.utils.random(-160,160),y:()=>gsap.utils.random(-90,90),rotation:()=>gsap.utils.random(-180,180),scale:()=>gsap.utils.random(.3,2),opacity:0,ease:'power2.out',stagger:{each:.02,from:'random'}});autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx276` rules from `site/fx.css`

_No dedicated `.fx276` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #276
