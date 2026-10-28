# 328 · 心電圖線條 — ECG Heartbeat Line

心電圖的波形由左往右畫出，發光的游標點沿線前進，旁邊心跳數字跳動

- 元件 Component: 圖形・SVG (`shape`)
- 時機 Timing: 循環待機
- 技術 Tech: GSAP
- 情境 Uses: 數字資訊、App 介面
- 風格／關鍵字 Style: 心電圖 心跳 波形 健康 醫療 監測 ECG Heartbeat Pulse Monitor Health 圖形 SVG
- 標籤 Tag: DrawSVG
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-21

**AI 提示詞（網站複製格式）:**

```text
「心電圖線條（ECG Heartbeat Line）」動態效果：醫療或健康 App 的心電圖顯示：深色帶細格線的螢幕上，一條發光的心電圖波形（平線、小波、尖銳的 QRS 波、T 波重複）由左往右畫出，一顆發光的游標點跟著畫線的前端前進，畫到底後線條從左側開始消失再重畫；右上角顯示心跳數字（偶爾小幅變動）與一顆規律跳動的愛心。（GSAP：DrawSVG "0% 0%" → "0% 100%" 畫出、再到 "100% 100%" 消失；游標點用 MotionPathPlugin 沿同一條路徑；愛心 scale yoyo）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx328">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「心電圖線條」.

### JavaScript — `FX[328]` from `site/fx.js`

```js
328(s,x){const id='ecg'+Math.random().toString(36).slice(2);const seg=o=>`L${o+20},50 L${o+26},46 L${o+30},50 L${o+36},50 L${o+39},56 L${o+43},18 L${o+47},68 L${o+51},50 L${o+60},50 L${o+66},43 L${o+74},50 L${o+80},50`;let d='M0,50 ';for(let o=0;o<320;o+=80)d+=seg(o)+' ';
  s.insertAdjacentHTML('beforeend',`<div class="sv-ecg"><svg viewBox="0 0 320 100" preserveAspectRatio="none"><defs><pattern id="${id}g" width="16" height="16" patternUnits="userSpaceOnUse"><path d="M16,0 H0 V16" fill="none"/></pattern></defs><rect width="320" height="100" fill="url(#${id}g)" class="gr"/><path id="${id}" class="tr" d="${d}"/><circle class="hd" r="2.6"/></svg><div class="sv-bpm"><b>72</b><small>BPM</small><span class="hrt">♥</span></div></div>`);
  const w=s.querySelector('.sv-ecg'),tr=w.querySelector('.tr'),hd=w.querySelector('.hd'),bpm=w.querySelector('.sv-bpm b'),hrt=w.querySelector('.hrt');
  gsap.timeline({repeat:-1}).fromTo(tr,{drawSVG:'0% 0%'},{drawSVG:'0% 100%',duration:3,ease:'none'}).to(hd,{motionPath:{path:'#'+id,align:'#'+id,alignOrigin:[.5,.5]},duration:3,ease:'none'},0).to(tr,{drawSVG:'100% 100%',duration:.6,ease:'none'});
  gsap.to(hrt,{scale:1.35,duration:.12,yoyo:true,repeat:-1,repeatDelay:.6,ease:'power2.out'});gsap.to({},{duration:1.5,repeat:-1,onRepeat:()=>bpm.textContent=70+Math.round(Math.random()*6)})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx328` rules from `site/fx.css`

_No dedicated `.fx328` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #328
