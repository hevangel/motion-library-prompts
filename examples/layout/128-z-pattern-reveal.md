# 128 · Z 字閱讀動線 — Z-pattern Reveal

首頁版面依 Z 字閱讀順序依序出現

- 元件 Component: 版面・頁面 (`layout`)
- 時機 Timing: 進場
- 技術 Tech: GSAP
- 情境 Uses: 標題・Hero
- 風格／關鍵字 Style: 首頁 Hero 版面 Z 字 F 字 閱讀模式 Logo 導覽 圖片 行動按鈕 溫和 柔和 輕柔 引導 動線 視線 閱讀順序 低調 Subtle Gentle Soft Entrance Visual Flow Hierarchy
- 標籤 Tag: Z-pattern
- 範例文字 Example text: 「讓動線自然發生」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「Z 字閱讀動線（Z-pattern Reveal）」動態效果：首頁 Hero 進場時，元素依照 Z 字閱讀動線依序淡入上浮：左上 Logo → 右上導覽選單 → 左側主標題與內文 → 右側主視覺圖片 → 左下行動按鈕 → 右下次要連結，每個元素間隔約 0.4 秒、從下方約 12px 輕輕浮現，節奏平均、沒有誇張位移，讓使用者的視線照著設計好的順序移動。（預覽中的細線只是示意 Z 字路徑，實際網站不需要。GSAP：依閱讀順序排列元素陣列，fromTo y:12 / opacity:0，stagger 0.42，ease power2.out）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx128">`, preview text 「讓動線自然發生」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「Z 字閱讀動線」.

### JavaScript — `FX[128]` from `site/fx.js`

```js
128(s,x){const w=el('div','abs zp');w.innerHTML='<svg viewBox="0 0 100 56" preserveAspectRatio="none"><path d="M10,7 L90,7 L12,47 L90,47"/></svg><i class="lg"></i><div class="nv"><i></i><i></i><i></i></div><b class="hd2"></b><i class="ph"></i><i class="im2"></i><span class="cta">開始</span><i class="lk"></i>';
  w.querySelector('.hd2').textContent=x;s.append(w);const q=c=>w.querySelector(c),path=q('path');
  gsap.timeline({repeat:-1,repeatDelay:.3}).set(w,{opacity:1},0).set(path,{opacity:1},0).fromTo(path,{drawSVG:'0%'},{drawSVG:'100%',duration:3,ease:'power1.inOut'},0)
    .fromTo(['.lg','.nv','.hd2','.ph','.im2','.cta','.lk'].map(q),{opacity:0,y:12},{opacity:1,y:0,duration:.8,ease:'power2.out',stagger:.42},.1)
    .to(path,{opacity:0,duration:.6},'-=.2').to(w,{opacity:0,duration:.5},'+=1.4')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx128` rules from `site/fx.css`

_No dedicated `.fx128` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #128
