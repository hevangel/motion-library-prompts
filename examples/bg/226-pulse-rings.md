# 226 · 同心圓擴散 — Pulse Rings

中心點規律脈動，一圈圈圓環向外擴散後淡出

- 元件 Component: 背景・氛圍 (`bg`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 背景裝飾、強調重點、App 介面
- 風格／關鍵字 Style: 同心圓 擴散 脈動 雷達 聲波 直播 定位 訊號 Pulse Rings Ripple Radar Signal Live 背景 氛圍
- 標籤 Tag: CSS keyframes
- 範例文字 Example text: 「Live」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「同心圓擴散（Pulse Rings）」動態效果：畫面中心有一個實心圓點規律地輕輕脈動，從它的位置不斷有細圓環一圈圈向外擴散放大並逐漸變淡消失，多個圓環錯開時間形成連續的波紋，像雷達、聲波或「直播中」的訊號；中心圓點上可放短標籤。（CSS：3–4 個圓環共用同一個 keyframes：scale 0.15 → 1.25、opacity 0.9 → 0，用負的 animation-delay 均分錯開；中心點用另一個 scale 的 keyframes）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx226">`, preview text 「Live」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「同心圓擴散」.

### JavaScript — `FX[226]` from `site/fx.js`

```js
226(s,x){const w=el('div','abs bga-pr');for(let i=0;i<4;i++){const r=el('i');r.style.animationDelay=(-i).toFixed(1)+'s';w.append(r)}w.append(el('b'));s.append(w);const t=T(x,Math.min(9,44/chars(x).length));t.classList.add('bga-pt');s.append(t)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx226` rules from `site/fx.css`

_No dedicated `.fx226` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #226
