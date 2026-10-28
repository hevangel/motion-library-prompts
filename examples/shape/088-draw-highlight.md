# 088 · 手繪圈重點 — Draw Highlight

手繪圓圈與底線畫出來

- 元件 Component: 圖形・SVG (`shape`)
- 時機 Timing: 進場
- 技術 Tech: GSAP
- 情境 Uses: 強調重點
- 風格／關鍵字 Style: 
- 標籤 Tag: DrawSVG
- 範例文字 Example text: 「重點在這」（預覽底色：cream）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「手繪圈重點（Draw Highlight）」動態效果：重點文字外圍用像手繪的線條畫出一個圓圈，接著在下方畫一條底線，停留後線條從起點方向收掉，圓頭線端。（GSAP：DrawSVGPlugin，drawSVG "0%"→"100%"，再到 "100% 100%"）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage cream fx88">`, preview text 「重點在這」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「手繪圈重點」.

### JavaScript — `FX[88]` from `site/fx.js`

```js
88(s,x){const w=el('div','dr');w.append(T(x,Math.min(13,56/chars(x).length)));w.insertAdjacentHTML('beforeend','<svg viewBox="0 0 200 100" preserveAspectRatio="none"><path d="M150,20 C120,4 48,6 24,30 C2,54 30,88 100,90 C172,92 198,66 188,42 C180,22 142,10 104,12"/><path d="M34,104 C74,98 130,100 172,103"/></svg>');s.append(w);const ps=w.querySelectorAll('path');
  gsap.timeline({repeat:-1,repeatDelay:.4}).fromTo(ps,{drawSVG:'0%'},{drawSVG:'100%',duration:1,ease:'power2.inOut',stagger:.6}).to(ps,{drawSVG:'100% 100%',duration:.6,ease:'power2.in',stagger:.1},'+=1.3')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx88` rules from `site/fx.css`

_No dedicated `.fx88` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #88
