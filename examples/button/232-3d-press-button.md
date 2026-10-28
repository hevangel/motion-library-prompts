# 232 · 立體按壓按鈕 — 3D Press Button

按鈕下方有一層厚度，按下時整顆往下壓、厚度消失，像實體按鍵

- 元件 Component: 按鈕 (`button`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動、App 介面
- 風格／關鍵字 Style: 立體 按壓 實體 按鍵 3D Pressable Button Push Tactile 遊戲 按鈕
- 標籤 Tag: CSS :active
- 範例文字 Example text: 「立即開始」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「立體按壓按鈕（3D Press Button）」動態效果：實體按鍵感的按鈕：按鈕本體下方有一層同色系但較深的「厚度」（用不模糊的下方陰影做出），外圍再有一層柔和投影；滑鼠滑過時按鈕微微浮起、厚度增加；按下時整顆往下壓到幾乎貼平、厚度與投影縮小，放開彈回。約 0.12 秒、反應俐落。（CSS：box-shadow: 0 6px 0 較深色, 0 10px 20px 半透明；:active 時 translateY(5px) 並把第一層陰影縮成 1px）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx232">`, preview text 「立即開始」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「立體按壓按鈕」.

### JavaScript — `FX[232]` from `site/fx.js`

```js
232(s,x,card){const b=bxBtn('bx-3d',x);s.append(b);bxDemo(b,card,()=>{b.classList.add('dn');setTimeout(()=>b.classList.remove('dn'),180)},1600)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx232` rules from `site/fx.css`

_No dedicated `.fx232` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #232
