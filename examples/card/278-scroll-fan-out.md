# 278 · 捲動扇形展開 — Scroll Fan Out

疊在一起的卡片隨捲動展開成一把扇子

- 元件 Component: 卡片・群組 (`card`)
- 時機 Timing: 捲動觸發
- 技術 Tech: GSAP
- 情境 Uses: 捲動效果、標題・Hero
- 風格／關鍵字 Style: 扇形 展開 卡片 疊卡 作品 捲動 Scroll Fan Out Cards Spread 捲動觸發 ScrollTrigger
- 標籤 Tag: ScrollTrigger
- 範例文字 Example text: 「海邊 山林 夜空 午後 城市」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「捲動扇形展開（Scroll Fan Out）」動態效果：五張圖片卡片一開始整齊疊成一疊；使用者往下捲動時，卡片以底部下方的一點為軸，像打開一把扇子一樣向左右兩側展開：中間那張不動，越外側旋轉角度越大（每張約相差 14 度），同時往兩側與下方位移；往回捲則收回成一疊。（GSAP ScrollTrigger scrub：卡片 transform-origin: 50% 120%，fromTo rotation / x / y 用函式依索引 (i − 中間索引) 計算）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx278">`, preview text 「海邊 山林 夜空 午後 城市」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「捲動扇形展開」.

### JavaScript — `FX[278]` from `site/fx.js`

```js
278(s,x){const{sc,wrap,view}=scrollBox(s);view.classList.add('cen');const ws=words(x);const fan=el('div','sx-fn');const cs=[0,1,2,3,4].map(i=>{const c=el('div','sx-fk');c.innerHTML=mdImg(i)+'<b></b>';c.querySelector('b').textContent=ws[i%ws.length];fan.append(c);return c});view.append(fan);
  gsap.timeline({scrollTrigger:{trigger:wrap,scroller:sc,start:'top top',end:'bottom bottom',scrub:.6}}).fromTo(cs,{rotation:0,x:0,y:0},{rotation:i=>(i-2)*14,x:i=>(i-2)*58+'%',y:i=>Math.abs(i-2)*9+'%',ease:'power2.out'});autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx278` rules from `site/fx.css`

_No dedicated `.fx278` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #278
