# 098 · 發牌展開 — Card Deal

卡片從底部發牌成扇形

- 元件 Component: 卡片・群組 (`card`)
- 時機 Timing: 進場、退場
- 技術 Tech: GSAP
- 情境 Uses: 轉場切換、介面互動
- 風格／關鍵字 Style: 
- 標籤 Tag: Timeline・Stagger
- 範例文字 Example text: 「春夏秋冬雪」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「發牌展開（Card Deal）」動態效果：5 張卡片從畫面底部依序發牌，展開成帶角度的扇形並略帶回彈，停留後從最後一張開始收回底部。（GSAP：timeline + stagger，xPercent / rotation 用函式值 (i)=>(i-2)*115）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx98">`, preview text 「春夏秋冬雪」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「發牌展開」.

### JavaScript — `FX[98]` from `site/fx.js`

```js
98(s,x){const w=el('div','deal');const cs=chars(x);const cds=[...Array(5)].map((_,i)=>{const c=el('div','dc');c.textContent=cs[i%cs.length];w.append(c);return c});s.append(w);
  gsap.timeline({repeat:-1,repeatDelay:.2}).fromTo(cds,{xPercent:0,yPercent:170,rotation:0},{xPercent:i=>(i-2)*115,yPercent:0,rotation:i=>(i-2)*6,duration:.7,ease:'back.out(1.4)',stagger:.1}).to(cds,{xPercent:0,yPercent:170,rotation:0,duration:.5,ease:'power3.in',stagger:{each:.06,from:'end'}},'+=1.3')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx98` rules from `site/fx.css`

_No dedicated `.fx98` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #98
