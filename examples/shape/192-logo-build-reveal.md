# 192 · Logo 組合登場 — Logo Build Reveal

標誌的圓、方塊、圓點依序畫出組合，再滑出品牌名

- 元件 Component: 圖形・SVG (`shape`)
- 時機 Timing: 進場
- 技術 Tech: GSAP
- 情境 Uses: Logo・品牌、標題・Hero
- 風格／關鍵字 Style: Logo 標誌 品牌 開場 組合 描繪 Logo Reveal Brand Intro Build SVG 圖形
- 標籤 Tag: DrawSVG
- 範例文字 Example text: 「STUDIO」（預覽底色：dark）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「Logo 組合登場（Logo Build Reveal）」動態效果：品牌標誌依序組合登場：外圈的圓先被描出來（約 0.9 秒），接著中間旋轉 45 度的方塊描邊並填入強調色，中心圓點從 0 彈出放大，最後品牌名稱從左側 12px 滑入淡出現；停留後整體淡出。適合網站開場或影片片頭。（GSAP：DrawSVGPlugin 依序描繪 circle 與 rect，fill-opacity 0→1；圓點 scale 用 back.out(3)；文字 fromTo x:-12 / opacity:0）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx192">`, preview text 「STUDIO」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「Logo 組合登場」.

### JavaScript — `FX[192]` from `site/fx.js`

```js
192(s,x){const w=el('div','lgw');w.innerHTML='<svg viewBox="0 0 60 60" class="lgm"><circle class="o" cx="30" cy="30" r="26"/><rect class="q" x="19" y="19" width="22" height="22" rx="3" transform="rotate(45 30 30)"/><circle class="d" cx="30" cy="30" r="4"/></svg>';const t=T(x,Math.min(8,44/chars(x).length));t.classList.add('lgt');w.append(t);s.append(w);const q=c=>w.querySelector(c);
  gsap.timeline({repeat:-1,repeatDelay:.4}).set(w,{opacity:1},0).fromTo(q('.o'),{drawSVG:'0%'},{drawSVG:'100%',duration:.9,ease:'power2.inOut'},0).fromTo(q('.q'),{drawSVG:'0%',fillOpacity:0},{drawSVG:'100%',duration:.7,ease:'power2.inOut'},.35)
    .fromTo(q('.d'),{scale:0,transformOrigin:'50% 50%'},{scale:1,duration:.5,ease:'back.out(3)'},'-=.1').to(q('.q'),{fillOpacity:1,duration:.4},'<').fromTo(t,{x:-12,opacity:0},{x:0,opacity:1,duration:.6,ease:'power3.out'},'-=.2').to(w,{opacity:0,duration:.5},'+=1.6')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx192` rules from `site/fx.css`

_No dedicated `.fx192` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #192
