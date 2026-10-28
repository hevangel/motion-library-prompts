# 050 · 斜線帶 — Diagonal Text Bands

斜斜的帶子，文字反向跑

- 元件 Component: 背景・氛圍 (`bg`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 背景裝飾、轉場切換
- 風格／關鍵字 Style: 流動背景
- 標籤 Tag: 轉場・俏皮
- 範例文字 Example text: 「天亮以前」（預覽底色：dark）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「斜線帶（Diagonal Text Bands）」動態效果：兩條斜放的文字帶子交錯穿過畫面，兩條帶子用不同底色區分，帶上的重複文字往相反方向持續滑動，帶子有陰影。約 7–9 秒一輪，俏皮轉場感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx50">`, preview text 「天亮以前」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「斜線帶」.

### JavaScript — `FX[50]` from `site/fx.js`

```js
50(s,x){const a=mqRow(rep(x+'・',8),7,9,false,'background:var(--a);color:#111');a.className+=' band';a.style.top='22%';a.style.transform='rotate(-9deg)';const b=mqRow(rep(x+'・',8),7,7,true,'background:#fff;color:#111');b.className+=' band';b.style.top='56%';b.style.transform='rotate(6deg)';s.append(a,b)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx50` rules from `site/fx.css`

_No dedicated `.fx50` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #50
