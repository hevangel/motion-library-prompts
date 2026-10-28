# 152 · 捲動逐字點亮 — Scroll Text Reveal

段落的字隨著捲動一個個由淡轉亮

- 元件 Component: 文字 (`text`)
- 時機 Timing: 捲動觸發
- 技術 Tech: GSAP
- 情境 Uses: 標題・Hero、捲動效果
- 風格／關鍵字 Style: 逐字 點亮 段落 文案 Apple 官網 Text Reveal Highlight On Scroll 捲動 滾動 scroll ScrollTrigger scrub 捲動觸發
- 標籤 Tag: ScrollTrigger scrub
- 範例文字 Example text: 「好的動態設計會在你捲動時一個字一個字亮起來，帶著視線往下讀完這段話。」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「捲動逐字點亮（Scroll Text Reveal）」動態效果：一段大字級的文案固定在畫面中央，一開始所有字都很淡；使用者往下捲動時，字從第一個開始依序變清楚，捲動進度＝已點亮的比例，往回捲時再依序變淡，像 Apple 官網的文案呈現。（GSAP：SplitText 拆字，fromTo opacity 0.15→1、stagger 0.1、ease none，綁 ScrollTrigger scrub:true；區塊用 pin 或 position:sticky 固定，外層高度約 3–4 個視窗）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx152">`, preview text 「好的動態設計會在你捲動時一個字一個字亮起來，帶著視線往下讀完這段話。」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「捲動逐字點亮」.

### JavaScript — `FX[152]` from `site/fx.js`

```js
152(s,x){const{sc,wrap,view}=scrollBox(s);view.classList.add('cen');const p=el('div','sfill');p.textContent=x;view.append(p);const sp=SplitText.create(p,{type:'chars'});
  gsap.fromTo(sp.chars,{opacity:.15},{opacity:1,stagger:.1,ease:'none',scrollTrigger:{trigger:wrap,scroller:sc,start:'top top',end:'bottom bottom',scrub:true}});autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx152` rules from `site/fx.css`

_No dedicated `.fx152` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #152
