# 279 · 模糊對焦 — Blur to Focus

段落標題捲進畫面時由模糊變清楚，捲出時又慢慢糊掉

- 元件 Component: 文字 (`text`)
- 時機 Timing: 捲動觸發
- 技術 Tech: GSAP
- 情境 Uses: 捲動效果、標題・Hero
- 風格／關鍵字 Style: 模糊 對焦 清晰 blur 景深 捲動 Blur To Focus Scroll Depth 捲動觸發 ScrollTrigger
- 標籤 Tag: ScrollTrigger
- 範例文字 Example text: 「慢慢 看清楚 再離開」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「模糊對焦（Blur to Focus）」動態效果：一段長頁面中的幾個大標題：每個標題從畫面下方捲進來時是模糊、透明、略小的，越接近畫面中央越清楚，在中央時完全清晰；繼續往上捲出畫面時又逐漸模糊、淡出並略微放大，像相機對焦掃過，引導視線停在目前的段落。（GSAP ScrollTrigger scrub：每個標題 start "top bottom"、end "bottom top"，timeline 先 fromTo filter blur(12px) → blur(0)、opacity 0 → 1、scale .92 → 1，再 to blur(12px)、opacity 0、scale 1.06）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx279">`, preview text 「慢慢 看清楚 再離開」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「模糊對焦」.

### JavaScript — `FX[279]` from `site/fx.js`

```js
279(s,x){const sc=el('div','scr');const box=el('div','sx-bf');box.innerHTML='<div class="sx-sp"></div>';words(x).slice(0,3).forEach(t=>{const h=T(t,Math.min(12,52/chars(t).length));h.classList.add('sx-bl');box.append(h)});box.insertAdjacentHTML('beforeend','<div class="sx-sp"></div>');sc.append(box);s.append(sc);
  box.querySelectorAll('.sx-bl').forEach(h=>gsap.timeline({scrollTrigger:{trigger:h,scroller:sc,start:'top bottom',end:'bottom top',scrub:true}}).fromTo(h,{filter:'blur(12px)',opacity:0,scale:.92},{filter:'blur(0px)',opacity:1,scale:1,ease:'power1.out'}).to(h,{filter:'blur(12px)',opacity:0,scale:1.06,ease:'power1.in'}));autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx279` rules from `site/fx.css`

_No dedicated `.fx279` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #279
