# 076 · 逐字升起 — Split Rise

每個字從遮罩下方滑上來

- 元件 Component: 文字 (`text`)
- 時機 Timing: 進場、退場
- 技術 Tech: GSAP
- 情境 Uses: 標題・Hero
- 風格／關鍵字 Style: Canva 風格 Canva Ascend Rise 上升
- 標籤 Tag: SplitText
- 範例文字 Example text: 「一字一字升起」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「逐字升起（Split Rise）」動態效果：文字拆成單字，每個字放在裁切遮罩內，依序從遮罩下方滑上來（每字間隔約 0.06 秒、強烈減速），停留後再往上滑出。（GSAP：SplitText type chars + mask，from yPercent:110，ease power4.out，stagger）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx76">`, preview text 「一字一字升起」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「逐字升起」.

### JavaScript — `FX[76]` from `site/fx.js`

```js
76(s,x){const t=T(x);s.append(t);const sp=SplitText.create(t,{type:'chars',mask:'chars'});
  gsap.timeline({repeat:-1,repeatDelay:.5}).from(sp.chars,{yPercent:110,duration:.8,ease:'power4.out',stagger:.06}).to(sp.chars,{yPercent:-110,duration:.5,ease:'power3.in',stagger:.04},'+=1.3')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx76` rules from `site/fx.css`

_No dedicated `.fx76` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #76
