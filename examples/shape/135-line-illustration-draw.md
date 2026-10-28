# 135 · 線條插畫逐筆描繪 — Line Illustration Draw

線條插畫一筆一筆畫完，最後主體淡淡浮現

- 元件 Component: 圖形・SVG (`shape`)
- 時機 Timing: 進場
- 技術 Tech: GSAP
- 情境 Uses: 標題・Hero、背景裝飾
- 風格／關鍵字 Style: 插畫 線條插畫 逐筆 描繪 手繪 圖解 Line Art Illustration Draw Sketch
- 標籤 Tag: DrawSVG
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「線條插畫逐筆描繪（Line Illustration Draw）」動態效果：一張由多條線組成的線條插畫（例如一杯冒著熱氣的咖啡：杯碟、杯身、把手、三縷熱氣），依照由下往上、由主體到細節的順序一筆一筆描出來，每筆約 0.9 秒、間隔約 0.32 秒；全部畫完後，主體淡淡地補上一層半透明填色，熱氣線條輕輕上下飄動一次。整體安靜、有手作感。（GSAP：DrawSVGPlugin 對各路徑 stagger 描繪；填色用另一個相同形狀的 path 從 opacity 0 淡入）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx135">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「線條插畫逐筆描繪」.

### JavaScript — `FX[135]` from `site/fx.js`

```js
135(s){s.insertAdjacentHTML('beforeend','<svg class="ill" viewBox="0 0 120 90"><path class="fl2" d="M34,40 L38,70 C40,76 80,76 82,70 L86,40 Z"/><path d="M22,78 C40,84 80,84 98,78"/><path d="M34,40 L38,70 C40,76 80,76 82,70 L86,40 Z"/><path d="M86,46 C98,44 100,60 84,62"/><path class="st" d="M48,32 C44,26 52,22 48,14"/><path class="st" d="M60,32 C56,24 64,20 60,10"/><path class="st" d="M72,32 C68,26 76,22 72,14"/></svg>');
  const sv=s.querySelector('.ill'),ps=sv.querySelectorAll('path:not(.fl2)'),st=sv.querySelectorAll('.st');
  gsap.timeline({repeat:-1,repeatDelay:.4}).set(sv,{opacity:1},0).fromTo(ps,{drawSVG:'0%'},{drawSVG:'100%',duration:.9,ease:'power1.inOut',stagger:.32},0).fromTo(sv.querySelector('.fl2'),{opacity:0},{opacity:.28,duration:.8,ease:'power1.out'})
    .to(st,{y:-2,duration:.8,ease:'sine.inOut',yoyo:true,repeat:1,stagger:.15},'<').to(sv,{opacity:0,duration:.5},'+=.6')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx135` rules from `site/fx.css`

_No dedicated `.fx135` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #135
