# 316 · 空狀態插畫 — Empty State

沒有搜尋結果時，空箱子彈跳落下、蓋子掀開冒出問號，文字與按鈕依序出現

- 元件 Component: 版面・頁面 (`layout`)
- 時機 Timing: 進場
- 技術 Tech: GSAP
- 情境 Uses: 介面互動、App 介面
- 風格／關鍵字 Style: 空狀態 無結果 找不到 404 插畫 Empty State No Results Illustration 版面 頁面
- 標籤 Tag: GSAP timeline
- 範例文字 Example text: 「找不到相關效果」（預覽底色：dark）
- 收錄日期 Added: 2026-10-21

**AI 提示詞（網站複製格式）:**

```text
「空狀態插畫（Empty State）」動態效果：搜尋沒有結果或清單為空時的空狀態：一個簡單的箱子插畫從上方落下並彈跳停住，接著箱子的蓋子以一角為軸掀開，裡面冒出一個問號並上下輕輕漂浮；下方的標題、說明文字與「瀏覽全部」按鈕依序淡入上移；之後蓋子闔上、問號消失。讓空白畫面不冷冰冰並引導下一步。（GSAP timeline：插畫 from y:-20 ease bounce.out → 蓋子 rotation −28 back.out → 問號 from scale 0 → 文字 stagger 淡入 → 問號 yoyo 漂浮）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx316">`, preview text 「找不到相關效果」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「空狀態插畫」.

### JavaScript — `FX[316]` from `site/fx.js`

```js
316(s,x,card){const w=el('div','pg-em');w.innerHTML='<div class="pg-il"><i class="pg-box"></i><i class="pg-lid"></i><i class="pg-q">?</i><i class="pg-sh"></i></div><b></b><p>試試換個關鍵字，或看看熱門效果</p><button>瀏覽全部</button>';w.querySelector('b').textContent=x;s.append(w);
  gsap.timeline({repeat:-1,repeatDelay:1.2}).from(w.querySelector('.pg-il'),{y:-20,opacity:0,duration:.6,ease:'bounce.out'}).to(w.querySelector('.pg-lid'),{rotation:-28,y:-6,duration:.35,ease:'back.out(3)'}).from(w.querySelector('.pg-q'),{y:14,scale:0,opacity:0,duration:.45,ease:'back.out(3)'},'-=.1').from(w.querySelectorAll('b,p,button'),{y:12,opacity:0,duration:.4,stagger:.08},'-=.2').to(w.querySelector('.pg-q'),{y:-4,duration:.6,yoyo:true,repeat:3,ease:'sine.inOut'}).to(w.querySelector('.pg-lid'),{rotation:0,y:0,duration:.3},'+=.2').to(w.querySelector('.pg-q'),{opacity:0,duration:.2},'<')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx316` rules from `site/fx.css`

_No dedicated `.fx316` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #316
