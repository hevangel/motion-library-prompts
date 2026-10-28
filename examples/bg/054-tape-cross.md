# 054 · 封鎖膠帶 — Tape Cross

寫著字的膠帶交叉成 X

- 元件 Component: 背景・氛圍 (`bg`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 強調重點、背景裝飾
- 風格／關鍵字 Style: 流動背景
- 標籤 Tag: 警告・街頭
- 範例文字 Example text: 「禁止進入」（預覽底色：dark）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「封鎖膠帶（Tape Cross）」動態效果：兩條上下有粗邊的警示膠帶交叉成 X 形，膠帶上的重複文字往相反方向滑動，帶陰影。約 6–8 秒一輪，警告封鎖感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx54">`, preview text 「禁止進入」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「封鎖膠帶」.

### JavaScript — `FX[54]` from `site/fx.js`

```js
54(s,x){const st='background:repeating-linear-gradient(90deg,#ffd400 0 100%);color:#111;border-block:.6cqw solid #111';const a=mqRow(rep(x+'・',8),6.5,8,false,st);a.className+=' band';a.style.top='36%';a.style.transform='rotate(-15deg)';const b=mqRow(rep(x+'・',8),6.5,6,true,st);b.className+=' band';b.style.top='38%';b.style.transform='rotate(13deg)';s.append(b,a)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx54` rules from `site/fx.css`

_No dedicated `.fx54` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #54
