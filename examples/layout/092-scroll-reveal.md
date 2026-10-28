# 092 · 捲動揭示 — Scroll Reveal

捲到時淡入、進度條同步

- 元件 Component: 版面・頁面 (`layout`)
- 時機 Timing: 捲動觸發
- 技術 Tech: GSAP
- 情境 Uses: 捲動效果
- 風格／關鍵字 Style: 
- 標籤 Tag: ScrollTrigger
- 範例文字 Example text: 「捲動揭示」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「捲動揭示（Scroll Reveal）」動態效果：在可捲動的區塊中，頂端進度條隨捲動比例填滿，每段文字捲到畫面 85% 處時從左側淡入，往回捲時再淡出。（GSAP：ScrollTrigger toggleActions "play none none reverse"，進度條用 scrub:true）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx92">`, preview text 「捲動揭示」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「捲動揭示」.

### JavaScript — `FX[92]` from `site/fx.js`

```js
92(s,x){const sc=el('div','scr');const bar=el('div','pbar');const bi=el('i');bar.append(bi);sc.append(bar);s.append(sc);
  [x,'元素依序淡入','進度條跟著捲動','到底了 ✓'].forEach(v=>{const b=el('div','blk');b.textContent=v;sc.append(b);gsap.from(b,{opacity:0,x:-40,duration:.6,ease:'power3.out',scrollTrigger:{trigger:b,scroller:sc,start:'top 85%',toggleActions:'play none none reverse'}})});
  gsap.fromTo(bi,{scaleX:0},{scaleX:1,ease:'none',scrollTrigger:{scroller:sc,start:0,end:'max',scrub:true}});autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx92` rules from `site/fx.css`

_No dedicated `.fx92` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #92
