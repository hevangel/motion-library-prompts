# 198 · 長條圖成長 — Bar Chart Grow

長條依序由下往上長出並略微回彈，數值同步累加

- 元件 Component: 圖形・SVG (`shape`)
- 時機 Timing: 進場、捲動觸發
- 技術 Tech: GSAP
- 情境 Uses: 數字資訊
- 風格／關鍵字 Style: 長條圖 柱狀圖 圖表 數據 統計 Dashboard Bar Chart Column Graph Data SVG 圖形
- 標籤 Tag: Stagger
- 範例文字 Example text: 「每月瀏覽次數」（預覽底色：dark）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「長條圖成長（Bar Chart Grow）」動態效果：長條圖進場：每根長條依序（間隔 0.1 秒）從底線往上長出並略微過衝回彈，長條頂端的數值同時從 0 累加到實際數字，下方顯示月份標籤。適合報表、成果頁。（GSAP：長條 transform-origin 底部、fromTo scaleY 0→1、ease back.out(1.6)；數值 tween 物件數值 + onUpdate；可搭配 ScrollTrigger 捲到時播放）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx198">`, preview text 「每月瀏覽次數」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「長條圖成長」.

### JavaScript — `FX[198]` from `site/fx.js`

```js
198(s,x){const V=[42,65,38,80,58,92],L=['1月','2月','3月','4月','5月','6月'];const w=el('div','bcw');w.innerHTML='<b></b><div class="bars">'+V.map((v,i)=>`<div class="bc"><span>0</span><i style="height:${v}%"></i><em>${L[i]}</em></div>`).join('')+'</div>';w.querySelector('b').textContent=x;s.append(w);
  const tl=gsap.timeline({repeat:-1,repeatDelay:.4}).set(w,{opacity:1},0);w.querySelectorAll('.bc').forEach((c,i)=>{const o={v:0},sp=c.querySelector('span');tl.fromTo(c.querySelector('i'),{scaleY:0},{scaleY:1,duration:.8,ease:'back.out(1.6)'},i*.1).fromTo(o,{v:0},{v:V[i],duration:.8,ease:'power2.out',onUpdate:()=>sp.textContent=Math.round(o.v)},i*.1)});tl.to(w,{opacity:0,duration:.5},'+=1.8')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx198` rules from `site/fx.css`

_No dedicated `.fx198` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #198
