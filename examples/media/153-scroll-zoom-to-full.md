# 153 · 捲動放大全幅圖片 — Scroll Zoom to Full

小圖隨捲動放大到充滿畫面，最後浮出標題

- 元件 Component: 圖片・媒體 (`media`)
- 時機 Timing: 捲動觸發
- 技術 Tech: GSAP
- 情境 Uses: 標題・Hero、捲動效果、轉場切換
- 風格／關鍵字 Style: 圖片 放大 全幅 全螢幕 展開 Zoom Image Expand Full Screen Fullbleed 捲動 滾動 scroll ScrollTrigger scrub 捲動觸發
- 標籤 Tag: ScrollTrigger scrub
- 範例文字 Example text: 「走進風景」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「捲動放大全幅圖片（Scroll Zoom to Full）」動態效果：畫面中央一張帶圓角的小圖（約 4 成寬），隨著往下捲動逐漸放大到充滿整個畫面，圓角同時縮成直角，圖片內容則從 1.3 倍慢慢縮回原尺寸（避免放大時看起來糊），放大到後段時標題從下方淡入疊在圖片上；往回捲時全部倒退。（GSAP：timeline 綁 ScrollTrigger scrub:true，區塊 pin 或 sticky；tween width / height / borderRadius 與內層 scale；也可改用 clip-path inset 做）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx153">`, preview text 「走進風景」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「捲動放大全幅圖片」.

### JavaScript — `FX[153]` from `site/fx.js`

```js
153(s,x){const{sc,wrap,view}=scrollBox(s);view.classList.add('cen');const f=el('div','zim');f.innerHTML=scene('#9fd3ff','#ffe1b0','#4f7a6a','#264a3f','#fff6d8');const cap=T(x,Math.min(10,50/chars(x).length));cap.classList.add('zcap');f.append(cap);view.append(f);
  gsap.timeline({scrollTrigger:{trigger:wrap,scroller:sc,start:'top top',end:'bottom bottom',scrub:true}}).fromTo(f,{width:'38%',height:'46%',borderRadius:'2cqw'},{width:'100%',height:'100%',borderRadius:'0cqw',ease:'none'},0)
    .fromTo(f.querySelector('svg'),{scale:1.3},{scale:1,ease:'none'},0).fromTo(cap,{opacity:0,y:20},{opacity:1,y:0,ease:'none',duration:.3},.7);autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx153` rules from `site/fx.css`

_No dedicated `.fx153` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #153
