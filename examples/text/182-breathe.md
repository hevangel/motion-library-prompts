# 182 · 呼吸 — Breathe

元素緩慢放大縮小，像在呼吸一樣循環

- 元件 Component: 文字 (`text`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 強調重點、Logo・品牌
- 風格／關鍵字 Style: 呼吸 脈動 放大縮小 待機 Pulse Breathing Idle Canva 風格 Canva Breathe 呼吸 簡報 社群貼文 動畫
- 標籤 Tag: CSS keyframes
- 範例文字 Example text: 「深呼吸」（預覽底色：cream）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「呼吸（Breathe）」動態效果：文字或元素持續緩慢地放大到約 1.07 倍再縮回，同時透明度在 0.82 與 1 之間輕微起伏，一個循環約 3.2 秒、前後都緩入緩出，像在呼吸，適合強調重點或待機狀態。（CSS：keyframes 0%/100% scale(1)、50% scale(1.07)，ease-in-out，infinite）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage cream fx182">`, preview text 「深呼吸」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「呼吸」.

### JavaScript — `FX[182]` from `site/fx.js`

```js
182(s,x){const w=el('div','brw');w.append(T(x,Math.min(12,52/chars(x).length)));s.append(w)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx182` rules from `site/fx.css`

_No dedicated `.fx182` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #182
