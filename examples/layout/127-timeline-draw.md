# 127 · 時間軸延伸 — Timeline Draw

一條線往下延伸，碰到哪個步驟就出現哪一步

- 元件 Component: 版面・頁面 (`layout`)
- 時機 Timing: 進場、捲動觸發
- 技術 Tech: GSAP
- 情境 Uses: 介面互動、數字資訊
- 風格／關鍵字 Style: 時間軸 流程 步驟 歷程 線條 延伸 溫和 柔和 輕柔 引導 動線 視線 閱讀順序 低調 Subtle Gentle Soft Entrance Visual Flow Hierarchy
- 標籤 Tag: Timeline
- 範例文字 Example text: 「需求訪談 概念發想 設計製作 上線交付」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「時間軸延伸（Timeline Draw）」動態效果：垂直時間軸：左側一條細線從頂端慢慢往下延伸（約 2.4 秒、緩入緩出），每當線延伸到某個節點，該節點的圓點、標題與說明文字列就從左側約 10px 輕輕滑入淡出現，讓視線跟著線一路往下讀完流程。（GSAP：線條 scaleY 0→1、transform-origin 頂端；各節點依序在對應時間點 fromTo x:-10 / opacity:0；實際網站可用 ScrollTrigger scrub 讓線條長度跟著捲動進度）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx127">`, preview text 「需求訪談 概念發想 設計製作 上線交付」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「時間軸延伸」.

### JavaScript — `FX[127]` from `site/fx.js`

```js
127(s,x){const w=el('div','vt');w.innerHTML='<i class="rail"></i>';const its=words(x).slice(0,4).map(v=>{const r=el('div','vi2');r.innerHTML='<i class="dot"></i><b></b><span></span>';r.querySelector('b').textContent=v;w.append(r);return r});s.append(w);
  const tl=gsap.timeline({repeat:-1,repeatDelay:.3}).set(w,{opacity:1},0).fromTo(w.querySelector('.rail'),{scaleY:0},{scaleY:1,duration:2.4,ease:'power1.inOut'},0);
  its.forEach((r,i)=>tl.fromTo(r.children,{x:-10,opacity:0},{x:0,opacity:1,duration:.7,ease:'power2.out',stagger:.08},.2+i*.6));tl.to(w,{opacity:0,duration:.5},'+=1.6')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx127` rules from `site/fx.css`

_No dedicated `.fx127` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #127
