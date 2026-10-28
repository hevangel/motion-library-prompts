# 129 · 步驟依序連接 — Connected Steps

步驟卡之間的連接線畫過去後，下一步才出現

- 元件 Component: 卡片・群組 (`card`)
- 時機 Timing: 進場
- 技術 Tech: GSAP
- 情境 Uses: 介面互動、數字資訊
- 風格／關鍵字 Style: 步驟 流程 1 2 3 連接線 教學 結帳 Onboarding 溫和 柔和 輕柔 引導 動線 視線 閱讀順序 低調 Subtle Gentle Soft Entrance Visual Flow Hierarchy
- 標籤 Tag: Steps
- 範例文字 Example text: 「選擇方案 填寫資料 完成付款」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「步驟依序連接（Connected Steps）」動態效果：三張橫向排列的步驟卡（編號 01、02、03＋標題＋一條說明文字列），進場時第一張先從下方約 14px 淡入，接著一條細連接線由左往右畫到第二張，第二張才淡入，再畫線到第三張，第三張淡入；節奏平穩，讓使用者清楚理解「先做什麼、再做什麼」。（GSAP：timeline 依序串接，卡片 fromTo y:14 / opacity:0，連接線 scaleX 0→1、transform-origin 左側，ease power1.inOut / power2.out）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx129">`, preview text 「選擇方案 填寫資料 完成付款」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「步驟依序連接」.

### JavaScript — `FX[129]` from `site/fx.js`

```js
129(s,x){const w=el('div','stp');const parts=[];words(x).slice(0,3).forEach((v,i)=>{if(i){const c=el('i','cn');w.append(c);parts.push(['c',c])}const c=el('div','sc');c.innerHTML=`<em>0${i+1}</em><b></b><span></span>`;c.querySelector('b').textContent=v;w.append(c);parts.push(['s',c])});s.append(w);
  const tl=gsap.timeline({repeat:-1,repeatDelay:.3}).set(w,{opacity:1},0);let t=0;
  parts.forEach(([k,e])=>{if(k==='s'){tl.fromTo(e,{opacity:0,y:14},{opacity:1,y:0,duration:.8,ease:'power2.out'},t);t+=.45}else{tl.fromTo(e,{scaleX:0},{scaleX:1,duration:.6,ease:'power1.inOut'},t);t+=.55}});tl.to(w,{opacity:0,duration:.5},'+=1.6')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx129` rules from `site/fx.css`

_No dedicated `.fx129` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #129
