# 081 · 隨機散聚 — Random Scatter

字從四處飛來再散開

- 元件 Component: 文字 (`text`)
- 時機 Timing: 進場、退場
- 技術 Tech: GSAP
- 情境 Uses: 標題・Hero
- 風格／關鍵字 Style: 
- 標籤 Tag: Stagger random
- 範例文字 Example text: 「四散再聚合」（預覽底色：cream）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「隨機散聚（Random Scatter）」動態效果：每個字從畫面四處隨機位置、隨機旋轉與大小飛進來，強烈減速聚合成文字，停留後再爆散到隨機位置。（GSAP：SplitText chars，"random(-400,400)" 函式值，ease expo，stagger from random）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage cream fx81">`, preview text 「四散再聚合」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「隨機散聚」.

### JavaScript — `FX[81]` from `site/fx.js`

```js
81(s,x){const t=T(x);s.append(t);const sp=SplitText.create(t,{type:'chars'});const v={xPercent:'random(-400,400)',yPercent:'random(-300,300)',rotation:'random(-200,200)',scale:'random(0,2)',opacity:0};
  gsap.timeline({repeat:-1,repeatDelay:.2}).from(sp.chars,{...v,duration:1.3,ease:'expo.out',stagger:{each:.05,from:'random'}}).to(sp.chars,{...v,duration:.9,ease:'expo.in',stagger:{each:.03,from:'random'}},'+=1.1')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx81` rules from `site/fx.css`

_No dedicated `.fx81` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #81
