# 296 · 逐字模糊浮現 — Blur In Letters

每個字從模糊、略大的狀態依序變清楚並落定

- 元件 Component: 文字 (`text`)
- 時機 Timing: 進場
- 技術 Tech: GSAP
- 情境 Uses: 標題・Hero
- 風格／關鍵字 Style: 模糊 浮現 逐字 柔和 進場 Blur In Letters Soft Reveal Stagger 文字 標題 動態文字
- 標籤 Tag: SplitText
- 範例文字 Example text: 「慢慢浮現」（預覽底色：dark）
- 收錄日期 Added: 2026-10-20

**AI 提示詞（網站複製格式）:**

```text
「逐字模糊浮現（Blur In Letters）」動態效果：標題的每個字依序從「模糊、透明、略大、略低」的狀態變成清楚並落到定位，每個字間隔約 0.07 秒，整體柔和、有質感；停留一段時間後依序模糊淡出再重播。（GSAP + SplitText：fromTo 字元 {opacity:0, filter:"blur(10px)", y:".25em", scale:1.15} → {opacity:1, filter:"blur(0px)", y:0, scale:1}，ease power2.out、stagger 0.07）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx296">`, preview text 「慢慢浮現」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「逐字模糊浮現」.

### JavaScript — `FX[296]` from `site/fx.js`

```js
296(s,x){const t=T(x);s.append(t);const sp=SplitText.create(t,{type:'chars'});gsap.timeline({repeat:-1,repeatDelay:.4}).fromTo(sp.chars,{opacity:0,filter:'blur(10px)',y:'.25em',scale:1.15},{opacity:1,filter:'blur(0px)',y:0,scale:1,duration:.9,ease:'power2.out',stagger:.07}).to(sp.chars,{opacity:0,filter:'blur(10px)',duration:.6,stagger:.03,ease:'power1.in'},'+=1.6')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx296` rules from `site/fx.css`

_No dedicated `.fx296` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #296
