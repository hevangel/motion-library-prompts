# 324 · 天氣圖示動畫 — Animated Weather Icons

晴天太陽緩轉、雲朵飄動、雨滴落下、閃電閃一下

- 元件 Component: 圖形・SVG (`shape`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 介面互動、App 介面、數字資訊
- 風格／關鍵字 Style: 天氣 圖示 太陽 雲 雨 閃電 icon Weather Icons Animated Sun Cloud Rain Thunder 圖形 SVG
- 標籤 Tag: CSS keyframes
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-21

**AI 提示詞（網站複製格式）:**

```text
「天氣圖示動畫（Animated Weather Icons）」動態效果：一組天氣圖示卡片：晴天的太陽與光芒緩慢自轉；多雲的雲朵左右輕輕飄移；雨天的雨滴從雲下方錯開時間持續落下並淡出；雷雨的閃電大部分時間暗淡，偶爾快速閃兩下。圖示下方標示天氣名稱。（SVG + CSS keyframes：太陽 rotate 10 秒一圈；雲 translateX 來回；雨滴 translateY + opacity，animation-delay 錯開；閃電用 steps(1) 的 keyframes 做閃爍）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx324">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「天氣圖示動畫」.

### JavaScript — `FX[324]` from `site/fx.js`

```js
324(s,x){const w=el('div','sv-wx');const L=[['晴','<g class="sun"><circle r="9"/>'+[...Array(8)].map((_,i)=>`<line x1="0" y1="-14" x2="0" y2="-19" transform="rotate(${i*45})"/>`).join('')+'</g>'],['多雲','<g class="sun s2"><circle cx="-6" cy="-6" r="7"/></g><path class="cl" d="M-14,8 A7,7 0 0 1 -9,-4 A9,9 0 0 1 8,-6 A7,7 0 0 1 14,8 Z"/>'],['雨','<path class="cl" d="M-14,2 A7,7 0 0 1 -9,-10 A9,9 0 0 1 8,-12 A7,7 0 0 1 14,2 Z"/>'+[-8,0,8].map((xx,i)=>`<line class="rd" style="--i:${i}" x1="${xx}" y1="7" x2="${xx-2}" y2="13"/>`).join('')],['雷','<path class="cl" d="M-14,0 A7,7 0 0 1 -9,-12 A9,9 0 0 1 8,-14 A7,7 0 0 1 14,0 Z"/><path class="bolt" d="M2,2 L-4,11 L1,11 L-3,19 L6,8 L1,8 L4,2Z"/>']];
  w.innerHTML=L.map(([l,g])=>`<div class="sv-wi"><svg viewBox="-22 -22 44 44">${g}</svg><span>${l}</span></div>`).join('');s.append(w)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx324` rules from `site/fx.css`

_No dedicated `.fx324` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #324
