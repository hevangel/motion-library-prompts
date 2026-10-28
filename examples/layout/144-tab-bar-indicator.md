# 144 · 底部導覽列切換 — Tab Bar Indicator

點選分頁時，膠囊指示器拉長滑到新位置，圖示輕彈

- 元件 Component: 版面・頁面 (`layout`)
- 時機 Timing: 切換、懸停・點擊
- 技術 Tech: GSAP
- 情境 Uses: App 介面、介面互動
- 風格／關鍵字 Style: 底部導覽列 分頁 tab bar 導覽 指示器 切換 Bottom Navigation Indicator Gooey App 手機 行動裝置 微互動 Mobile App Micro-interaction
- 標籤 Tag: Tab bar
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「底部導覽列切換（Tab Bar Indicator）」動態效果：App 底部的膠囊形導覽列有 4 個圖示，目前分頁底下有一顆膠囊指示器；點選另一個分頁時，指示器先往目標方向拉長、同時覆蓋新舊兩個位置（約 0.18 秒），再收縮到新分頁（約 0.34 秒、減速），像液體一樣流過去；新分頁的圖示同時從 0.7 倍彈回原尺寸，圖示與指示器形成反差。（GSAP：兩段 timeline 改變指示器的 x 與 width；圖示 scale 用 back.out(3)）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx144">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「底部導覽列切換」.

### JavaScript — `FX[144]` from `site/fx.js`

```js
144(s,x,card){const IC=['<path d="M3 11l9-8 9 8"/><path d="M5 10v10h14V10"/>','<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/>','<path d="M12 20s-7-4.5-9-9a5 5 0 0 1 9-3 5 5 0 0 1 9 3c-2 4.5-9 9-9 9z"/>','<circle cx="12" cy="8" r="4"/><path d="M4 21c1-4 4.5-6 8-6s7 2 8 6"/>'];
  const bar=el('div','tbar');const ind=el('i','tind');bar.append(ind);const tabs=IC.map((d,i)=>{const t=el('button','tab');t.innerHTML=`<svg viewBox="0 0 24 24">${d}</svg>`;bar.append(t);return t});s.append(bar);let cur=0,real=0;
  const go=(j,first)=>{const a=tabs[cur],b=tabs[j];tabs.forEach((t,k)=>t.classList.toggle('on',k===j));if(first||!b.offsetWidth){gsap.set(ind,{x:b.offsetLeft,width:b.offsetWidth});cur=j;return}
    const L=Math.min(a.offsetLeft,b.offsetLeft),R=Math.max(a.offsetLeft+a.offsetWidth,b.offsetLeft+b.offsetWidth);
    gsap.timeline().to(ind,{x:L,width:R-L,duration:.18,ease:'power2.in'}).to(ind,{x:b.offsetLeft,width:b.offsetWidth,duration:.34,ease:'power3.out'});gsap.fromTo(b.querySelector('svg'),{scale:.7},{scale:1,duration:.45,ease:'back.out(3)'});cur=j};
  tabs.forEach((t,i)=>t.onclick=()=>{real=Date.now();go(i)});go(0,true);card._timers.push(setInterval(()=>{if(Date.now()-real>3000)go((cur+1)%4)},1300))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx144` rules from `site/fx.css`

_No dedicated `.fx144` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #144
