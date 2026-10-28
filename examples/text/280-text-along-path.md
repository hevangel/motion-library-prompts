# 280 · 沿曲線跑的文字 — Text Along Path

一行文字沿著彎曲的線條移動，捲動決定它跑到哪裡

- 元件 Component: 文字 (`text`)
- 時機 Timing: 捲動觸發
- 技術 Tech: GSAP
- 情境 Uses: 捲動效果、背景裝飾、強調重點
- 風格／關鍵字 Style: 曲線 路徑 文字 跑馬燈 textPath 波浪 捲動 Text On Path Curve Scroll 捲動觸發 ScrollTrigger
- 標籤 Tag: SVG textPath
- 範例文字 Example text: 「Follow the curve」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「沿曲線跑的文字（Text Along Path）」動態效果：畫面中有一條橫跨的彎曲波浪線（淡淡的細線），一行文字貼著這條曲線排列；使用者往下捲動時，文字沿著曲線從右邊流向左邊，彎曲的地方文字跟著轉彎，捲動速度決定文字移動速度，往回捲則倒退。（SVG：<path id> + <text><textPath href="#id">；GSAP ScrollTrigger scrub tween textPath 的 startOffset 屬性從 100% → −100%）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx280">`, preview text 「Follow the curve」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「沿曲線跑的文字」.

### JavaScript — `FX[280]` from `site/fx.js`

```js
280(s,x){const{sc,wrap,view}=scrollBox(s);const id='tp'+Math.random().toString(36).slice(2);view.innerHTML=`<svg class="sx-tp" viewBox="0 0 400 225"><path id="${id}" d="M-20,170 C80,40 160,40 200,112 S320,190 420,60"/><text><textPath href="#${id}" startOffset="100%"></textPath></text></svg>`;
  const tp=view.querySelector('textPath');tp.textContent=rep(x+' · ',3);gsap.fromTo(tp,{attr:{startOffset:'100%'}},{attr:{startOffset:'-100%'},ease:'none',scrollTrigger:{trigger:wrap,scroller:sc,start:'top top',end:'bottom bottom',scrub:.5}});autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx280` rules from `site/fx.css`

_No dedicated `.fx280` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #280
