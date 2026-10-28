# 219 · 瀑布流依序落下 — Masonry Cascade

高低不一的瀑布流卡片，一排排帶微微旋轉落下就位

- 元件 Component: 卡片・群組 (`card`)
- 時機 Timing: 進場
- 技術 Tech: GSAP
- 情境 Uses: 介面互動、標題・Hero
- 風格／關鍵字 Style: 瀑布流 masonry Pinterest 圖庫 進場 落下 Masonry Grid Cascade Gallery 卡片 群組
- 標籤 Tag: Stagger
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「瀑布流依序落下（Masonry Cascade）」動態效果：瀑布流（Masonry）圖庫進場：三欄高低不一的卡片，依照由上到下、由左到右的閱讀順序，一張張從上方約 30px 帶著輕微隨機旋轉落下並淡入，就位時略微回彈（間隔約 0.09 秒），整面圖庫像被逐一擺上去。（GSAP：依每張卡片的列、欄索引排序後 stagger 0.09，fromTo y:-30 / opacity:0 / rotation:random(-6,6) → 歸零，ease back.out(1.4)；實際網站可用 CSS columns 或 masonry 函式庫排版）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx219">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「瀑布流依序落下」.

### JavaScript — `FX[219]` from `site/fx.js`

```js
219(s){const H=[[14,9,12],[10,13,8],[12,8,11]];const w=el('div','kd-ms');const items=[];H.forEach((col,ci)=>{const c=el('div','kd-mc');col.forEach((h,ri)=>{const it=el('i');it.style.height=h+'cqw';it.style.background=`linear-gradient(150deg,${GC[(ci+ri)%5]},${GC[(ci+ri+2)%5]})`;c.append(it);items.push([it,ri,ci])});w.append(c)});s.append(w);
  const ord=items.sort((a,b)=>a[1]-b[1]||a[2]-b[2]).map(a=>a[0]);gsap.timeline({repeat:-1,repeatDelay:.4}).fromTo(ord,{y:-30,opacity:0,rotation:()=>gsap.utils.random(-6,6)},{y:0,opacity:1,rotation:0,duration:.6,ease:'back.out(1.4)',stagger:.09}).to(ord,{opacity:0,y:10,duration:.4,stagger:.03},'+=1.6')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx219` rules from `site/fx.css`

_No dedicated `.fx219` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #219
