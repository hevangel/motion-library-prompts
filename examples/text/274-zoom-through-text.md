# 274 · 穿越大字轉場 — Zoom Through Text

巨大的標題隨捲動不斷放大，鏡頭像穿過字母進入下一個畫面

- 元件 Component: 文字 (`text`)
- 時機 Timing: 捲動觸發
- 技術 Tech: GSAP
- 情境 Uses: 捲動效果、轉場切換、標題・Hero
- 風格／關鍵字 Style: 放大 穿越 大字 鏡頭 轉場 Zoom Through Text Scale Scroll Transition 捲動觸發 ScrollTrigger
- 標籤 Tag: ScrollTrigger
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「穿越大字轉場（Zoom Through Text）」動態效果：一個巨大的英文標題（例如 ZOOM）在畫面中央，使用者往下捲動時標題開始放大，越捲放大越快（加速曲線），最後放大到數十倍，鏡頭像是穿過字母中間的空隙，畫面被字母填滿後轉成下一段內容（下一段在後方淡入並從 0.8 倍放大到 1 倍）。（GSAP ScrollTrigger scrub：sticky 區塊內 fromTo scale 1 → 38，ease power2.in，transform-origin 對準要穿過的字母空隙；下一段內容在進度 70% 後淡入）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx274">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「穿越大字轉場」.

### JavaScript — `FX[274]` from `site/fx.js`

```js
274(s,x){const{sc,wrap,view}=scrollBox(s);view.classList.add('cen');const nx=el('div','abs gl sx-nx');nx.append(T('WELCOME',9));const big=el('div','sx-zt');big.textContent='ZOOM';view.append(big,nx);
  // 放大中心對準第一個 O 的中空處，穿過去後下一段淡入
  gsap.timeline({scrollTrigger:{trigger:wrap,scroller:sc,start:'top top',end:'bottom bottom',scrub:.5}}).fromTo(big,{scale:1},{scale:40,ease:'power2.in',duration:.8},0).fromTo(nx,{opacity:0,scale:.85},{opacity:1,scale:1,ease:'power1.out',duration:.25},.65).to({},{duration:.2});autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx274` rules from `site/fx.css`

_No dedicated `.fx274` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #274
