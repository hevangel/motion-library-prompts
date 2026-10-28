# 327 · 成就徽章解鎖 — Badge Unlock

六角形徽章描邊畫出、星星從大縮小蓋上去、四周光芒放射

- 元件 Component: 圖形・SVG (`shape`)
- 時機 Timing: 進場
- 技術 Tech: GSAP
- 情境 Uses: 強調重點、App 介面
- 風格／關鍵字 Style: 徽章 成就 解鎖 獎勵 遊戲化 Badge Achievement Unlock Reward Gamification 圖形 SVG
- 標籤 Tag: DrawSVG
- 範例文字 Example text: 「連續登入 7 天」（預覽底色：dark）
- 收錄日期 Added: 2026-10-21

**AI 提示詞（網站複製格式）:**

```text
「成就徽章解鎖（Badge Unlock）」動態效果：達成成就時的徽章動畫：六角形徽章的外框先沿著邊一筆畫出，接著內部淡入填滿；一顆星星從很大、旋轉、透明的狀態快速縮小落到徽章中央並帶回彈，像蓋章一樣；同時徽章四周的一圈短光芒由內往外快速射出後消失，徽章整體輕彈一下；下方的成就名稱與「成就解鎖」字樣依序浮現。（GSAP timeline：DrawSVG 畫外框 → fillOpacity → 星星 fromTo scale 3 → 1、rotation −60 → 0、back.out → 光芒 DrawSVG "0% 0%" → "0% 100%" → "100% 100%"）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx327">`, preview text 「連續登入 7 天」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「成就徽章解鎖」.

### JavaScript — `FX[327]` from `site/fx.js`

```js
327(s,x){const w=el('div','sv-bdg');w.innerHTML='<svg viewBox="-60 -60 120 120"><g class="sv-rays">'+[...Array(12)].map((_,i)=>`<line y1="-40" y2="-52" transform="rotate(${i*30})"/>`).join('')+'</g><path class="sv-hex" d="M0,-36 L31,-18 L31,18 L0,36 L-31,18 L-31,-18Z"/><path class="sv-star" d="M0,-16 L4.7,-6.5 L15.2,-4.9 L7.6,2.5 L9.4,12.9 L0,8 L-9.4,12.9 L-7.6,2.5 L-15.2,-4.9 L-4.7,-6.5Z"/></svg><b></b><small>成就解鎖</small>';w.querySelector('b').textContent=x;s.append(w);
  const hex=w.querySelector('.sv-hex'),st=w.querySelector('.sv-star'),rays=w.querySelectorAll('.sv-rays line');
  gsap.timeline({repeat:-1,repeatDelay:1.4}).set(hex,{fillOpacity:0}).fromTo(hex,{drawSVG:'0%'},{drawSVG:'100%',duration:.8,ease:'power2.inOut'}).to(hex,{fillOpacity:1,duration:.3}).fromTo(st,{scale:3,opacity:0,rotation:-60,transformOrigin:'50% 50%'},{scale:1,opacity:1,rotation:0,duration:.45,ease:'back.out(2.2)'},'-=.1').fromTo(rays,{drawSVG:'0% 0%'},{keyframes:[{drawSVG:'0% 100%',duration:.25},{drawSVG:'100% 100%',duration:.3}],stagger:.015,ease:'power2.out'},'-=.15').from(w.querySelectorAll('b,small'),{y:10,opacity:0,duration:.4,stagger:.08},'<').to(w.querySelector('svg'),{scale:1.06,duration:.15,yoyo:true,repeat:1,transformOrigin:'50% 50%'},'<').to(w,{opacity:0,duration:.4},'+=2.2').set(w,{opacity:1})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx327` rules from `site/fx.css`

_No dedicated `.fx327` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #327
