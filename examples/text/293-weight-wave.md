# 293 · 字重波浪 — Weight Wave

每個字的粗細輪流變化，像一道波浪從左掃到右

- 元件 Component: 文字 (`text`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 標題・Hero、強調重點
- 風格／關鍵字 Style: 字重 粗細 可變字體 波浪 呼吸 Variable Font Weight Wave Breathing 文字 標題 動態文字
- 標籤 Tag: variable font
- 範例文字 Example text: 「WEIGHT」（預覽底色：dark）
- 收錄日期 Added: 2026-10-20

**AI 提示詞（網站複製格式）:**

```text
「字重波浪（Weight Wave）」動態效果：標題的每個字的字重在最細與最粗之間來回變化，相鄰的字依序延遲，看起來像一道粗細的波浪從左往右不斷掃過，最粗的時候字同時變成強調色。（CSS：使用支援可變字重的字體，每個字拆成獨立元素，共用一個 keyframes 在 font-weight 100 ↔ 900 之間變化，animation-delay 依索引遞增）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx293">`, preview text 「WEIGHT」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「字重波浪」.

### JavaScript — `FX[293]` from `site/fx.js`

```js
293(s,x){const t=T(x,Math.min(15,64/chars(x).length));t.classList.add('tx-ww');s.append(t);const sp=SplitText.create(t,{type:'chars'});sp.chars.forEach((c,i)=>c.style.animationDelay=(i*.09-3)+'s')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx293` rules from `site/fx.css`

_No dedicated `.fx293` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #293
