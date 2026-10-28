# 107 · 聚光網格 — Spotlight Grid

細格線背景，游標附近的格線被點亮並帶柔光

- 元件 Component: 背景・氛圍 (`bg`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 背景裝飾、介面互動
- 風格／關鍵字 Style: 背景 網格 格線 聚光 游標 光暈 Spotlight Grid Pattern Cursor Glow SaaS
- 標籤 Tag: CSS mask
- 範例文字 Example text: 「Spotlight」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「聚光網格（Spotlight Grid）」動態效果：整個區塊背景是淡淡的細格線，游標所在位置周圍一圈的格線會被點亮成強調色，並帶一團柔和光暈，亮區跟著游標移動、邊緣自然淡出；游標離開時亮區消失。（做法：兩層相同的格線背景，上層用強調色，再用 mask:radial-gradient(circle at var(--mx) var(--my)) 只露出游標附近；mousemove 時更新 CSS 變數 --mx、--my）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx107">`, preview text 「Spotlight」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「聚光網格」.

### JavaScript — `FX[107]` from `site/fx.js`

```js
107(s,x,card){const l=el('div','abs gl sgrid');l.append(el('div','spot'),T(x,Math.min(12,56/chars(x).length)));s.append(l);vpointer(l,card,(px,py)=>{l.style.setProperty('--mx',px+'px');l.style.setProperty('--my',py+'px')})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx107` rules from `site/fx.css`

_No dedicated `.fx107` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #107
