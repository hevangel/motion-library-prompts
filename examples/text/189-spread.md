# 189 · 展開 — Spread

字疊在一起從模糊中往兩側展開成正常字距

- 元件 Component: 文字 (`text`)
- 時機 Timing: 進場
- 技術 Tech: CSS
- 情境 Uses: 標題・Hero、強調重點
- 風格／關鍵字 Style: 展開 字距 擴散 模糊 聚焦 Spread Letter Spacing Tracking Expand Canva 風格 Canva Spread 展開 簡報 社群貼文 動畫
- 標籤 Tag: letter-spacing
- 範例文字 Example text: 「展開」（預覽底色：cream）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「展開（Spread）」動態效果：文字一開始字距極度緊縮、所有字疊在一起並且模糊透明，接著字距平滑展開到正常寬度，同時變清晰、淡入（約 1.1 秒、減速），像從中心散開成形；停留後淡出。（CSS：keyframes letter-spacing:-0.55em → 0.06em，搭配 filter:blur(6px)→0 與 opacity）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage cream fx189">`, preview text 「展開」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「展開」.

### JavaScript — `FX[189]` from `site/fx.js`

```js
189(s,x){const t=T(x,Math.min(12,48/chars(x).length));t.classList.add('spr');s.append(t)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx189` rules from `site/fx.css`

_No dedicated `.fx189` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #189
