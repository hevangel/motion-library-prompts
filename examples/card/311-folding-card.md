# 311 · 對折邀請卡 — Folding Card

像實體卡片一樣，封面以左邊為軸立體打開，露出裡面的圖片和文字

- 元件 Component: 卡片・群組 (`card`)
- 時機 Timing: 切換
- 技術 Tech: GSAP
- 情境 Uses: 介面互動、標題・Hero
- 風格／關鍵字 Style: 卡片 對折 邀請卡 賀卡 打開 3D Folding Greeting Invitation Card Open 卡片 群組
- 標籤 Tag: GSAP 3D
- 範例文字 Example text: 「YOU ARE INVITED」（預覽底色：dark）
- 收錄日期 Added: 2026-10-20

**AI 提示詞（網站複製格式）:**

```text
「對折邀請卡（Folding Card）」動態效果：一張對折的邀請卡：一開始只看到封面（強調色底、大標題與「點一下打開」），點擊時封面以左側為軸，在 3D 空間中往左翻開 180 度（約 0.9 秒），封面背面是一張圖片，右側露出卡片內頁的邀請文字與日期；整張卡片同時往右平移，讓打開後的整體保持置中；再點一次則闔上。（CSS 3D：容器 perspective；封面 transform-origin:left、preserve-3d，正面與背面 backface-visibility:hidden、背面 rotateY(180deg)；GSAP timeline 同時 tween 封面 rotationY 0 → −180 與卡片 xPercent 0 → 50，play / reverse 切換）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx311">`, preview text 「YOU ARE INVITED」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「對折邀請卡」.

### JavaScript — `FX[311]` from `site/fx.js`

```js
311(s,x,card){const w=el('div','cg-fo');w.innerHTML='<div class="cg-ins"><p>邀請你參加<br>我們的週年派對 🎉</p><small>11 / 08 · 19:00</small></div><div class="cg-cv"><div class="fr"><b></b><small>點一下打開</small></div><div class="bk">'+mdImg(1)+'</div></div>';w.querySelector('.fr b').textContent=x;s.append(w);
  const cv=w.querySelector('.cg-cv');let open=false,real=0;const tl=gsap.timeline({paused:true}).to(cv,{rotationY:-180,duration:.9,ease:'power2.inOut'}).to(w,{xPercent:50,duration:.9,ease:'power2.inOut'},0);
  const tog=()=>{open=!open;open?tl.play():tl.reverse()};w.onclick=()=>{real=Date.now();tog()};card._timers.push(setInterval(()=>{if(Date.now()-real>5000)tog()},2600))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx311` rules from `site/fx.css`

_No dedicated `.fx311` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #311
