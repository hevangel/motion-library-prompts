# 084 · 數字累加 — Number Counter

數字滾動累加並同步進度條

- 元件 Component: 文字 (`text`)
- 時機 Timing: 進場
- 技術 Tech: GSAP
- 情境 Uses: 數字資訊
- 風格／關鍵字 Style: 
- 標籤 Tag: Tween 數值
- 範例文字 Example text: 「下載次數」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「數字累加（Number Counter）」動態效果：標籤下方的大數字從 0 快速累加到 128,450，越接近終點越慢，下方進度條同步填滿，停留後淡出重來，數字用等寬數字。（GSAP：tween 一個物件數值 + onUpdate 寫入 toLocaleString，ease power3.out）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx84">`, preview text 「下載次數」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「數字累加」.

### JavaScript — `FX[84]` from `site/fx.js`

```js
84(s,x){const w=el('div','ctr');w.innerHTML='<div class="lb"></div><div class="num">0</div><div class="bar"><i></i></div>';w.querySelector('.lb').textContent=x;s.append(w);const n=w.querySelector('.num'),b=w.querySelector('.bar i'),o={v:0};
  gsap.timeline({repeat:-1,repeatDelay:.3}).fromTo(w,{opacity:0},{opacity:1,duration:.3}).fromTo(o,{v:0},{v:128450,duration:2.4,ease:'power3.out',onUpdate:()=>n.textContent=Math.round(o.v).toLocaleString()},0).fromTo(b,{scaleX:0},{scaleX:1,duration:2.4,ease:'power3.out'},0).to(w,{opacity:0,duration:.4},'+=1.4')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx84` rules from `site/fx.css`

_No dedicated `.fx84` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #84
