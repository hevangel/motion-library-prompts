# 156 · 往下捲隱藏導覽列 — Hide Header on Scroll

往下捲時導覽列收起，往回捲時立刻滑出

- 元件 Component: 版面・頁面 (`layout`)
- 時機 Timing: 捲動觸發
- 技術 Tech: GSAP
- 情境 Uses: 介面互動、捲動效果、App 介面
- 風格／關鍵字 Style: 導覽列 頁首 選單 header navbar 隱藏 顯示 方向 Headroom Hide On Scroll Down Show On Scroll Up 捲動 滾動 scroll ScrollTrigger scrub 捲動觸發
- 標籤 Tag: ScrollTrigger direction
- 範例文字 Example text: 「LOGO」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「往下捲隱藏導覽列（Hide Header on Scroll）」動態效果：頁首導覽列固定在頂端；使用者往下捲動（閱讀內容）時導覽列往上滑出畫面讓出空間，一旦往上捲（想找選單）就立刻從頂端滑回來，在最頂端時一定顯示；約 0.35 秒、減速。手機版很常用。（做法：比較目前與上一次的 scrollY 判斷方向，或用 ScrollTrigger 的 self.direction；切換 class 讓 header translateY(-100%)，加 transition）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx156">`, preview text 「LOGO」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「往下捲隱藏導覽列」.

### JavaScript — `FX[156]` from `site/fx.js`

```js
156(s,x){const sc=el('div','scr nopad');const h=el('header','hh');h.innerHTML='<b></b><nav><i></i><i></i><i></i></nav>';h.querySelector('b').textContent=x;const c=el('div','shc');for(let i=0;i<10;i++)c.append(el('i'));sc.append(h,c);s.append(sc);
  ScrollTrigger.create({scroller:sc,start:0,end:'max',onUpdate:t=>h.classList.toggle('hide',t.direction===1&&t.scroll()>30)});autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx156` rules from `site/fx.css`

_No dedicated `.fx156` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #156
