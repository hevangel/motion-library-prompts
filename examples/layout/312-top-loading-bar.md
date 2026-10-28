# 312 · 頂部載入進度條 — Top Loading Bar

換頁時頁面頂端一條細線快速跑到一半、慢慢爬，載完衝到底消失，內容再依序浮現

- 元件 Component: 版面・頁面 (`layout`)
- 時機 Timing: 進場、切換
- 技術 Tech: GSAP
- 情境 Uses: 轉場切換、介面互動
- 風格／關鍵字 Style: 載入 進度條 頂部 換頁 NProgress YouTube Loading Bar Page Load Progress 版面 頁面
- 標籤 Tag: GSAP
- 範例文字 Example text: 「文章標題」（預覽底色：dark）
- 收錄日期 Added: 2026-10-21

**AI 提示詞（網站複製格式）:**

```text
「頂部載入進度條（Top Loading Bar）」動態效果：網站換頁或載入內容時，頁面最頂端出現一條細細的強調色進度條（帶微光）：先快速跑到約 30%，接著慢慢爬到約 70%（給人「正在載入」的感覺），載入完成時迅速衝到 100% 並淡出；同時頁面內容（標題、段落、卡片）依序從下方淡入浮現。（GSAP timeline：進度條 transform-origin:left，scaleX 0 → .3（power2.out）→ .7（較慢）→ 1（快），再 opacity 0；內容 stagger 淡入）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx312">`, preview text 「文章標題」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「頂部載入進度條」.

### JavaScript — `FX[312]` from `site/fx.js`

```js
312(s,x,card){const f=lyPage(s);f.insertAdjacentHTML('beforeend','<i class="pg-lb"></i><div class="pg-ct"><b></b><i class="ly-bl"></i><i class="ly-bl s"></i><div class="pg-row"><i></i><i></i><i></i></div></div>');f.querySelector('.pg-ct b').textContent=x;const bar=f.querySelector('.pg-lb'),ct=f.querySelector('.pg-ct');
  gsap.timeline({repeat:-1,repeatDelay:.8}).set(ct.children,{opacity:0,y:10}).set(bar,{scaleX:0,opacity:1}).to(bar,{scaleX:.3,duration:.4,ease:'power2.out'}).to(bar,{scaleX:.7,duration:1.2,ease:'power1.inOut'}).to(bar,{scaleX:1,duration:.25,ease:'power1.in'}).to(bar,{opacity:0,duration:.3}).to(ct.children,{opacity:1,y:0,duration:.5,stagger:.08,ease:'power2.out'},'-=.2').to({},{duration:1.6})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx312` rules from `site/fx.css`

_No dedicated `.fx312` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #312
