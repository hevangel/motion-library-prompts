# 089 · 形狀變形 — Shape Morph

圓、星、心、雲朵互相變形

- 元件 Component: 圖形・SVG (`shape`)
- 時機 Timing: 切換
- 技術 Tech: GSAP
- 情境 Uses: Logo・品牌、轉場切換
- 風格／關鍵字 Style: 
- 標籤 Tag: MorphSVG
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「形狀變形（Shape Morph）」動態效果：一個色塊在圓形、星形、愛心、雲朵之間平滑變形，每次變形同時換一個顏色，整體緩慢旋轉。（GSAP：MorphSVGPlugin，morphSVG 切換路徑，ease expo.inOut）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx89">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「形狀變形」.

### JavaScript — `FX[89]` from `site/fx.js`

```js
89(s){s.insertAdjacentHTML('beforeend',`<svg class="mo" viewBox="0 0 100 100"><path d="${SH[0]}" fill="${GC[2]}"/></svg>`);const p=s.querySelector('.mo path');const tl=gsap.timeline({repeat:-1});
  [1,2,3,0].forEach(k=>tl.to(p,{morphSVG:SH[k],fill:[GC[1],GC[4],GC[3],GC[2]][k===0?3:k-1],duration:.9,ease:'expo.inOut'},'+=.6'));gsap.to(s.querySelector('.mo'),{rotation:360,duration:14,repeat:-1,ease:'none'})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx89` rules from `site/fx.css`

_No dedicated `.fx89` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #89
