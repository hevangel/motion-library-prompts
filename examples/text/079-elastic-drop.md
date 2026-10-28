# 079 · 彈性落下 — Elastic Drop

字從天而降並彈性晃動

- 元件 Component: 文字 (`text`)
- 時機 Timing: 進場
- 技術 Tech: GSAP
- 情境 Uses: 標題・Hero、強調重點
- 風格／關鍵字 Style: Canva 風格 Canva Bounce 彈跳
- 標籤 Tag: Stagger・Elastic
- 範例文字 Example text: 「彈跳落下」（預覽底色：acc）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「彈性落下（Elastic Drop）」動態效果：每個字從畫面上方隨機順序掉下，帶隨機旋轉，落地時像果凍一樣彈性晃動後定位，停留後一起往下掉出並淡出。（GSAP：SplitText chars，ease elastic.out(1,0.35)，stagger from random）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage acc fx79">`, preview text 「彈跳落下」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「彈性落下」.

### JavaScript — `FX[79]` from `site/fx.js`

```js
79(s,x){const t=T(x);s.append(t);const sp=SplitText.create(t,{type:'chars'});
  gsap.timeline({repeat:-1,repeatDelay:.3}).from(sp.chars,{yPercent:-420,rotation:'random(-50,50)',duration:1.3,ease:'elastic.out(1,0.35)',stagger:{each:.07,from:'random'}}).to(sp.chars,{yPercent:420,rotation:'random(-40,40)',opacity:0,duration:.6,ease:'power2.in',stagger:.04},'+=1')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx79` rules from `site/fx.css`

_No dedicated `.fx79` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #79
