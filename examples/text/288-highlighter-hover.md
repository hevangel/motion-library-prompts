# 288 · 螢光筆劃記 — Highlighter Hover

段落中的重點詞滑過時，背後像用螢光筆由左往右劃過一道

- 元件 Component: 文字 (`text`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 強調重點
- 風格／關鍵字 Style: 螢光筆 標記 劃重點 highlight 重點 Highlighter Marker Hover Emphasis Text hover 懸停 滑過
- 標籤 Tag: background-size
- 範例文字 Example text: 「好的 設計 是 讓人 一眼 看懂」（預覽底色：dark）
- 收錄日期 Added: 2026-10-20

**AI 提示詞（網站複製格式）:**

```text
「螢光筆劃記（Highlighter Hover）」動態效果：一段文字中的幾個重點詞，滑鼠滑過時，背後像用螢光筆從左往右快速劃過一道帶點斜角、略低於字中線的色塊，文字顏色同時反轉以保持可讀；滑開時色塊收回。約 0.55 秒。（CSS：mark 元素背景用 linear-gradient 畫出帶斜邊的色帶，background-size 從 0% 過渡到 100%，background-position 偏下讓它像手劃的螢光筆）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx288">`, preview text 「好的 設計 是 讓人 一眼 看懂」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「螢光筆劃記」.

### JavaScript — `FX[288]` from `site/fx.js`

```js
288(s,x,card){const p=el('p','ho-hl');const ws=words(x);p.innerHTML=ws.map((t,i)=>i%2?`<mark></mark>`:'<span></span>').join(' ');[...p.children].forEach((c,i)=>c.textContent=ws[i]);s.append(p);autoHover(p,[...p.querySelectorAll('mark')],card,1100)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx288` rules from `site/fx.css`

_No dedicated `.fx288` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #288
