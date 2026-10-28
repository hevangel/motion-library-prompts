# 233 · 果凍彈跳按鈕 — Jelly Button

滑過或點擊時按鈕像果凍一樣被壓扁、拉長再彈回

- 元件 Component: 按鈕 (`button`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動、強調重點、App 介面
- 風格／關鍵字 Style: 果凍 彈跳 Q彈 壓扁 拉長 Jelly Rubber Squash Stretch Bounce Button 按鈕
- 標籤 Tag: CSS keyframes
- 範例文字 Example text: 「點我試試」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「果凍彈跳按鈕（Jelly Button）」動態效果：滑鼠滑過或點擊時，按鈕像果凍一樣先被橫向壓扁（寬 1.18、高 0.82），再縱向拉長（寬 0.85、高 1.15），之後幅度遞減地來回晃動幾次回到原狀，整段約 0.7 秒，Q 彈可愛。（CSS keyframes：依序 scale(1.18,.82) → (.85,1.15) → (1.08,.92) → (.97,1.03) → (1,1)；點擊觸發時先移除 class、強制 reflow 再加回，才能重播）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx233">`, preview text 「點我試試」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「果凍彈跳按鈕」.

### JavaScript — `FX[233]` from `site/fx.js`

```js
233(s,x,card){const b=bxBtn('bx-jl',x);s.append(b);const go=()=>{b.classList.remove('go');void b.offsetWidth;b.classList.add('go')};b.addEventListener('click',go);b.addEventListener('animationend',()=>b.classList.remove('go'));bxDemo(b,card,go,1800)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx233` rules from `site/fx.css`

_No dedicated `.fx233` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #233
