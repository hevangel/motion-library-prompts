# 080 · 3D 翻字 — 3D Char Flip

每個字沿 X 軸翻轉登場

- 元件 Component: 文字 (`text`)
- 時機 Timing: 進場
- 技術 Tech: GSAP
- 情境 Uses: 轉場切換、標題・Hero
- 風格／關鍵字 Style: 
- 標籤 Tag: SplitText・3D
- 範例文字 Example text: 「翻轉登場」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「3D 翻字（3D Char Flip）」動態效果：每個字以 X 軸 3D 翻轉登場（從背面翻到正面、略帶回彈），依序間隔 0.07 秒，停留後再往前翻走消失。（GSAP：SplitText chars，rotationX、transformOrigin 帶 Z 深度，ease back.out）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx80">`, preview text 「翻轉登場」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「3D 翻字」.

### JavaScript — `FX[80]` from `site/fx.js`

```js
80(s,x){const t=T(x);s.append(t);const sp=SplitText.create(t,{type:'chars'});const o={transformOrigin:'50% 50% -30'};
  gsap.timeline({repeat:-1,repeatDelay:.3}).from(sp.chars,{...o,rotationX:-95,opacity:0,duration:.9,ease:'back.out(1.8)',stagger:.07}).to(sp.chars,{...o,rotationX:95,opacity:0,duration:.6,ease:'power2.in',stagger:.05},'+=1.2')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx80` rules from `site/fx.css`

_No dedicated `.fx80` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #80
