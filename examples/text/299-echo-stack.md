# 299 · 殘影堆疊 — Echo Stack

文字後面疊著好幾層空心的複製，依序往斜後方展開再收回

- 元件 Component: 文字 (`text`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 標題・Hero、強調重點
- 風格／關鍵字 Style: 殘影 堆疊 複製 空心 立體 迴聲 Echo Stack Outline Layers Repeat Text 文字 標題 動態文字
- 標籤 Tag: CSS keyframes
- 範例文字 Example text: 「ECHO」（預覽底色：dark）
- 收錄日期 Added: 2026-10-20

**AI 提示詞（網站複製格式）:**

```text
「殘影堆疊（Echo Stack）」動態效果：一個粗體大標題，後面疊著 5 層同樣文字的空心描邊複製，每層描邊越後面越淡；動畫時這些複製層依序（每層延遲約 0.06 秒）往右上方斜向展開，形成像回聲或立體階梯的殘影，停留一下再收回到與原字重疊，來回循環。（CSS：多個 span 疊在同一格 grid，用 CSS 變數 --i 計算 translate 距離、描邊透明度與 animation-delay；-webkit-text-stroke 做空心字）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx299">`, preview text 「ECHO」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「殘影堆疊」.

### JavaScript — `FX[299]` from `site/fx.js`

```js
299(s,x){const w=el('div','tx-ec');w.style.fontSize=Math.min(14,60/chars(x).length)+'cqw';for(let i=0;i<6;i++){const d=el('span');d.textContent=x;d.style.setProperty('--i',i);w.append(d)}s.append(w)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx299` rules from `site/fx.css`

_No dedicated `.fx299` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #299
