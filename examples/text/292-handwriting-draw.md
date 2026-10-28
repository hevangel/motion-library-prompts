# 292 · 手寫描繪 — Handwriting Draw

文字的筆畫像用筆一筆一筆寫出來，寫完後填滿

- 元件 Component: 文字 (`text`)
- 時機 Timing: 進場、循環待機
- 技術 Tech: GSAP
- 情境 Uses: 標題・Hero、Logo・品牌
- 風格／關鍵字 Style: 手寫 簽名 筆畫 描繪 書寫 Handwriting Signature Stroke Draw Text SVG 文字 標題 動態文字
- 標籤 Tag: stroke-dashoffset
- 範例文字 Example text: 「Thank you」（預覽底色：dark）
- 收錄日期 Added: 2026-10-20

**AI 提示詞（網站複製格式）:**

```text
「手寫描繪（Handwriting Draw）」動態效果：一段文字（例如簽名或 Thank you）用手寫風格字體呈現，一開始只看到空白，接著文字的輪廓筆畫沿著字形一筆一筆被描繪出來（約 2.4 秒），像有人正在用筆書寫；筆畫描完後，字的內部再淡入填滿。（SVG：<text> 設 stroke 與 fill；用 stroke-dasharray 等於大於路徑總長的值，stroke-dashoffset 從總長補間到 0；描完後 fill-opacity 0 → 1。若要更精準可把文字轉成 path 再用 DrawSVG）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx292">`, preview text 「Thank you」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「手寫描繪」.

### JavaScript — `FX[292]` from `site/fx.js`

```js
292(s,x){const w=el('div','tx-hw');const fs=Math.min(30,130/chars(x).length);w.innerHTML=`<svg viewBox="0 0 200 70"><text x="100" y="50" text-anchor="middle" style="font-size:${fs*1.9}px"></text></svg>`;w.querySelector('text').textContent=x;s.append(w);
  const tx=w.querySelector('text');const L=600;gsap.timeline({repeat:-1,repeatDelay:.6}).set(tx,{strokeDasharray:L,strokeDashoffset:L,fillOpacity:0}).to(tx,{strokeDashoffset:0,duration:2.4,ease:'power1.inOut'}).to(tx,{fillOpacity:1,duration:.6},'-=.4').to(tx,{opacity:0,duration:.4},'+=1.4').set(tx,{opacity:1})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx292` rules from `site/fx.css`

_No dedicated `.fx292` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #292
