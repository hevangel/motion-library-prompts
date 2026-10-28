# 275 · 捲動速度傾斜 — Scroll Velocity Skew

圖片列表在快速捲動時跟著速度歪斜，停下來就回正

- 元件 Component: 圖片・媒體 (`media`)
- 時機 Timing: 捲動觸發
- 技術 Tech: GSAP
- 情境 Uses: 捲動效果、介面互動
- 風格／關鍵字 Style: 傾斜 歪斜 速度 慣性 skew 捲動 Scroll Velocity Skew Images List 捲動觸發 ScrollTrigger
- 標籤 Tag: getVelocity
- 範例文字 Example text: 「山 海 城 林」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「捲動速度傾斜（Scroll Velocity Skew）」動態效果：一列可捲動的圖片卡片，平常排列整齊；當使用者快速捲動時，所有卡片依捲動速度沿垂直方向歪斜（skewY），捲得越快歪得越多，方向跟著捲動方向，最大約 12 度；捲動減速或停止時平滑回正，帶出慣性與速度感。（GSAP：ScrollTrigger.create 的 onUpdate 中取得 self.getVelocity()，換算成角度並 clamp，用 gsap.quickTo(元素, "skewY", {duration:.5, ease:"power3.out"}) 平滑設定）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx275">`, preview text 「山 海 城 林」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「捲動速度傾斜」.

### JavaScript — `FX[275]` from `site/fx.js`

```js
275(s,x){const sc=el('div','scr nopad');const ls=el('div','sx-sk');words(x).concat(words(x)).slice(0,8).forEach((t,i)=>{const r=el('div','sx-sr');r.innerHTML=mdImg(i)+'<b></b>';r.querySelector('b').textContent=t;ls.append(r)});sc.append(ls);s.append(sc);
  const rows=[...ls.children],set=gsap.quickTo(rows,'skewY',{duration:.5,ease:'power3.out'});let last=0,lt=0;
  ScrollTrigger.create({scroller:sc,trigger:ls,start:'top top',end:'bottom bottom',onUpdate:self=>{const v=self.getVelocity();set(gsap.utils.clamp(-12,12,v/-90))}});autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx275` rules from `site/fx.css`

_No dedicated `.fx275` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #275
