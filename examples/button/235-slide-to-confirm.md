# 235 · 滑動確認 — Slide to Confirm

拖曳圓鈕滑到底才確認，未到底會彈回，文字有流光提示

- 元件 Component: 按鈕 (`button`)
- 時機 Timing: 拖曳手勢
- 技術 Tech: GSAP
- 情境 Uses: 介面互動、App 介面
- 風格／關鍵字 Style: 滑動 確認 解鎖 付款 拖曳 Slide To Unlock Confirm Swipe Button Payment 按鈕
- 標籤 Tag: Draggable
- 範例文字 Example text: 「滑動以付款」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「滑動確認（Slide to Confirm）」動態效果：膠囊形滑軌，左側是一顆圓形把手（內有向右箭頭），中間的提示文字有一道光從左往右掃過；使用者拖曳把手時，把手經過的軌道被填滿、提示文字逐漸淡出；拖到接近最右側放開才算確認，軌道整個填滿、文字變成「完成 ✓」；未拖到底放開時把手帶彈性彈回起點。（GSAP Draggable type:"x"、bounds 限制在軌道內，onDrag 更新填滿寬度，onRelease 判斷是否超過 85%；流光用 background-clip:text 加移動的漸層）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx235">`, preview text 「滑動以付款」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「滑動確認」.

### JavaScript — `FX[235]` from `site/fx.js`

```js
235(s,x,card){const w=el('div','bx-sl');w.innerHTML='<span class="bx-st"></span><i class="bx-sf"></i><b class="bx-kn">'+'<svg viewBox="0 0 24 24"><path d="M5 12h13M13 6l6 6-6 6"/></svg></b>';w.querySelector('.bx-st').textContent=x;w.style.fontSize=Math.min(4.2,36/chars(x).length)+'cqw';s.append(w);
  const kn=w.querySelector('.bx-kn'),fill=w.querySelector('.bx-sf'),st=w.querySelector('.bx-st');let idle=0,done=false;const max=()=>w.offsetWidth-kn.offsetWidth-w.offsetHeight*.16;
  const upd=v=>{fill.style.width=v+kn.offsetWidth+'px';st.style.opacity=1-v/max()*1.4};
  const finish=()=>{done=true;w.classList.add('ok');st.textContent='完成 ✓';st.style.opacity=1;setTimeout(()=>{w.classList.remove('ok');st.textContent=x;gsap.to(kn,{x:0,duration:.5,ease:'power3.out',onUpdate:()=>upd(gsap.getProperty(kn,'x')),onComplete:()=>done=false})},1400)};
  const dr=Draggable.create(kn,{type:'x',bounds:{minX:0,maxX:max()},onPress(){idle=Date.now()+5000;if(!done)gsap.killTweensOf(kn);this.applyBounds({minX:0,maxX:max()})},onDrag(){upd(this.x)},onRelease(){if(this.x>max()*.85){gsap.to(kn,{x:max(),duration:.15,onUpdate:()=>upd(gsap.getProperty(kn,'x')),onComplete:finish})}else gsap.to(kn,{x:0,duration:.45,ease:'back.out(2)',onUpdate:()=>upd(gsap.getProperty(kn,'x'))})}})[0];card._kill.push(()=>dr.kill());
  card._timers.push(setInterval(()=>{if(done||Date.now()<idle)return;gsap.to(kn,{x:max(),duration:.9,ease:'power2.inOut',onUpdate:()=>upd(gsap.getProperty(kn,'x')),onComplete:finish})},3600))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx235` rules from `site/fx.css`

_No dedicated `.fx235` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #235
