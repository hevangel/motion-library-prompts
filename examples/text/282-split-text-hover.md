# 282 · 上下切開文字 — Split Text Hover

滑過時標題沿水平中線切成上下兩半，往反方向錯開，中間露出一行小字

- 元件 Component: 文字 (`text`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 標題・Hero、強調重點
- 風格／關鍵字 Style: 切開 分割 上下 錯開 標題 clip-path Split Text Slice Hover Reveal hover 懸停 滑過
- 標籤 Tag: clip-path
- 範例文字 Example text: 「SPLIT」（預覽底色：dark）
- 收錄日期 Added: 2026-10-20

**AI 提示詞（網站複製格式）:**

```text
「上下切開文字（Split Text Hover）」動態效果：一個大標題，滑鼠滑過時沿著文字的水平中線被切成上下兩半：上半部往左上錯開、下半部往右下錯開（約 0.5 秒、緩入緩出），兩半之間裂開的縫隙中，一行小字（例如 OPEN）垂直展開淡入；滑開時兩半合回。（CSS：同一段文字疊兩層，一層 clip-path: inset(0 0 50% 0) 只露上半、另一層 inset(50% 0 0 0) 只露下半，:hover 時各自 transform 往反方向位移）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx282">`, preview text 「SPLIT」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「上下切開文字」.

### JavaScript — `FX[282]` from `site/fx.js`

```js
282(s,x,card){const w=el('div','ho-sp');w.style.fontSize=Math.min(15,64/chars(x).length)+'cqw';['up','dn','m'].forEach(k=>{const d=el('span','ho-'+k);d.textContent=k==='m'?'':x;w.append(d)});w.querySelector('.ho-m').textContent='OPEN';s.append(w);autoHover(w,[w],card,1500)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx282` rules from `site/fx.css`

_No dedicated `.fx282` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #282
