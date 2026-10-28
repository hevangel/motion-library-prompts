# 139 · 圓環進度 — Circular Progress

圓環描到指定百分比，中間數字同步累加

- 元件 Component: 圖形・SVG (`shape`)
- 時機 Timing: 進場
- 技術 Tech: GSAP
- 情境 Uses: 數字資訊
- 風格／關鍵字 Style: 進度 圓環 百分比 儀表 數據 統計 Progress Ring Donut Percentage Gauge Stats
- 標籤 Tag: DrawSVG
- 範例文字 Example text: 「專案完成度」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「圓環進度（Circular Progress）」動態效果：一個圓環進度圖，底下有一圈低對比的軌道，進場時進度弧線從正上方開始順時針描到指定百分比（例如 78%），線端圓角；中間的百分比數字從 0 同步累加到 78%，下方小字標示項目名稱；約 1.8 秒、緩入緩出，停在結果。（GSAP：DrawSVGPlugin drawSVG "0%"→"0% 78%"，SVG 整體 rotate(-90deg) 讓起點在上方；數字 tween 一個物件數值 + onUpdate 寫入，與弧線同時間、同 ease）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx139">`, preview text 「專案完成度」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「圓環進度」.

### JavaScript — `FX[139]` from `site/fx.js`

```js
139(s,x){const w=el('div','cpg');w.innerHTML='<svg viewBox="0 0 100 100"><circle class="tr" cx="50" cy="50" r="40"/><circle class="br" cx="50" cy="50" r="40"/></svg><div class="cv"><b>0%</b><span></span></div>';w.querySelector('span').textContent=x;s.append(w);const b=w.querySelector('b'),o={v:0};
  gsap.timeline({repeat:-1,repeatDelay:.4}).set(w,{opacity:1},0).fromTo(w.querySelector('.br'),{drawSVG:'0%'},{drawSVG:'0% 78%',duration:1.8,ease:'power2.inOut'},0).fromTo(o,{v:0},{v:78,duration:1.8,ease:'power2.inOut',onUpdate:()=>b.textContent=Math.round(o.v)+'%'},0).to(w,{opacity:0,duration:.5},'+=1.6')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx139` rules from `site/fx.css`

_No dedicated `.fx139` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #139
