# 100 · 滾輪加速跑馬燈 — Velocity Marquee

滾輪或拖曳讓跑馬燈加速傾斜

- 元件 Component: 背景・氛圍 (`bg`)
- 時機 Timing: 捲動觸發、拖曳手勢
- 技術 Tech: GSAP
- 情境 Uses: 背景裝飾、介面互動
- 風格／關鍵字 Style: 
- 標籤 Tag: Observer
- 範例文字 Example text: 「滾輪加速」（預覽底色：acc）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「滾輪加速跑馬燈（Velocity Marquee）」動態效果：兩行無限跑馬燈（一行實心、一行空心描邊，方向相反），使用者滾動滾輪或拖曳時加速並依方向傾斜，停下後慢慢恢復原速。（GSAP：Observer 取得 velocityY，調整 tween.timeScale 與 skewX）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage acc fx100">`, preview text 「滾輪加速」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「滾輪加速跑馬燈」.

### JavaScript — `FX[100]` from `site/fx.js`

```js
100(s,x,card){const l=layer(s);l.classList.add('vm');const U=rep(x+' ✦ ',6);const inns=[0,1].map(()=>{const r=el('div','vr');const i=el('div','vi');i.textContent=U+U;r.append(i);l.append(r);return i});
  const tws=inns.map((e,i)=>gsap.fromTo(e,{xPercent:i?-50:0},{xPercent:i?0:-50,duration:16,ease:'none',repeat:-1}));let st,busy=0;
  const boost=v=>{v=gsap.utils.clamp(-8,8,v);tws.forEach(tw=>gsap.to(tw,{timeScale:Math.max(1,Math.abs(v)),duration:.25,overwrite:true}));gsap.to(inns,{skewX:-v*2,duration:.25,overwrite:true});clearTimeout(st);
    st=setTimeout(()=>{tws.forEach(tw=>gsap.to(tw,{timeScale:1,duration:1.4,overwrite:true}));gsap.to(inns,{skewX:0,duration:1.2,ease:'elastic.out(1,.5)',overwrite:true})},180)};
  const ob=Observer.create({target:l,type:'wheel,touch,pointer',onChangeY:self=>{busy=Date.now();boost(self.velocityY/150)}});card._kill.push(()=>ob.kill());
  card._timers.push(setInterval(()=>{if(Date.now()-busy>3000)boost(gsap.utils.random([7,-6,8]))},3200))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx100` rules from `site/fx.css`

_No dedicated `.fx100` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #100
