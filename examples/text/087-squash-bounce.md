# 087 · 壓扁彈跳 — Squash Bounce

落地壓扁、回彈伸展

- 元件 Component: 文字 (`text`)
- 時機 Timing: 進場
- 技術 Tech: GSAP
- 情境 Uses: 強調重點
- 風格／關鍵字 Style: 
- 標籤 Tag: CustomBounce
- 範例文字 Example text: 「彈彈彈」（預覽底色：acc）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「壓扁彈跳（Squash Bounce）」動態效果：文字從上方掉落，落地時像橡皮一樣壓扁、反彈時拉長，連續彈跳幾下停住，地面陰影跟著高度縮放。（GSAP：CustomBounce.create 產生 bounce 與 squash 兩條 ease，分別套在 y 與 scaleX/scaleY）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage acc fx87">`, preview text 「彈彈彈」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「壓扁彈跳」.

### JavaScript — `FX[87]` from `site/fx.js`

```js
87(s,x){const w=el('div','bn');const t=T(x);const sh=el('div','sh');w.append(t,sh);s.append(w);
  gsap.timeline({repeat:-1,repeatDelay:.3}).fromTo(w,{opacity:0},{opacity:1,duration:.2}).fromTo(t,{yPercent:-260},{yPercent:0,duration:1.8,ease:'tmBounce'},0).fromTo(t,{scaleX:1,scaleY:1},{scaleX:1.35,scaleY:.7,duration:1.8,ease:'tmBounce-squash',transformOrigin:'50% 100%'},0).fromTo(sh,{scaleX:.2,opacity:.1},{scaleX:1,opacity:.45,duration:1.8,ease:'tmBounce'},0).to(w,{opacity:0,duration:.3},'+=.8')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx87` rules from `site/fx.css`

_No dedicated `.fx87` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #87
