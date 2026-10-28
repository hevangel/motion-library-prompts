# 090 · 路徑飛行 — Path Flight

紙飛機沿曲線飛行並轉向

- 元件 Component: 圖形・SVG (`shape`)
- 時機 Timing: 循環待機
- 技術 Tech: GSAP
- 情境 Uses: 背景裝飾
- 風格／關鍵字 Style: 
- 標籤 Tag: MotionPath
- 範例文字 Example text: 「」（預覽底色：acc，固定文字）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「路徑飛行（Path Flight）」動態效果：一架紙飛機沿著帶迴圈的虛線曲線飛過畫面，機頭會跟著路徑方向轉彎，飛出畫面後重新開始。（GSAP：MotionPathPlugin，path/align 指定 SVG 路徑，autoRotate:true）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage acc fx90">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「路徑飛行」.

### JavaScript — `FX[90]` from `site/fx.js`

```js
90(s){const id='mp'+Math.random().toString(36).slice(2);s.insertAdjacentHTML('beforeend',`<svg class="mpth" viewBox="0 0 320 180"><path id="${id}" d="M-30,130 C40,130 60,40 115,58 C160,74 130,132 100,112 C72,92 112,36 175,58 C235,80 255,135 350,95" fill="none" stroke="#111" stroke-opacity=".35" stroke-width="2" stroke-dasharray="4 7" stroke-linecap="round"/><g class="pl"><path d="M-11,-9 L13,0 L-11,9 L-6,0 Z" fill="#111"/></g></svg>`);
  gsap.to(s.querySelector('.pl'),{motionPath:{path:'#'+id,align:'#'+id,alignOrigin:[.5,.5],autoRotate:true},duration:4.2,repeat:-1,repeatDelay:.3,ease:'power1.inOut'})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx90` rules from `site/fx.css`

_No dedicated `.fx90` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #90
