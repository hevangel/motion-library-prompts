# 231 · 漂浮幾何 — Floating Shapes

圓形、方塊、三角形、圓環等幾何圖形在背景隨機緩慢漂浮旋轉

- 元件 Component: 背景・氛圍 (`bg`)
- 時機 Timing: 循環待機、進場
- 技術 Tech: GSAP
- 情境 Uses: 背景裝飾、標題・Hero
- 風格／關鍵字 Style: 漂浮 幾何 圖形 隨機 裝飾 背景 Floating Shapes Geometric Random Decoration 背景 氛圍
- 標籤 Tag: repeatRefresh
- 範例文字 Example text: 「Shapes」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「漂浮幾何（Floating Shapes）」動態效果：背景散佈十多個簡單的幾何圖形：實心圓、圓角方塊、三角形、空心圓環與十字，大小不一；進場時各自以彈性放大依序出現，之後每個圖形持續朝隨機方向緩慢漂移並旋轉，每次來回都換一個新的隨機目標，看起來自然不重複；標題位於中間。（GSAP：每個圖形 gsap.to x / y / rotation 用 "random(-40,40)" 字串，duration random(3,6)、ease sine.inOut、repeat:-1、yoyo:true、repeatRefresh:true；進場 gsap.from scale:0 搭配 back.out）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx231">`, preview text 「Shapes」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「漂浮幾何」.

### JavaScript — `FX[231]` from `site/fx.js`

```js
231(s,x){const w=el('div','abs bga-fs');const K=['c','q','t','ring','c','q','t','ring','c','plus','q','plus'];const es=K.map((k,i)=>{const e=el('i','bga-'+k);e.style.cssText=`left:${rnd(4,90)}%;top:${rnd(6,82)}%;--z:${rnd(3,7)}cqw;color:${i%3?'var(--a)':GC[i%5]}`;w.append(e);return e});s.append(w,T(x,Math.min(12,56/chars(x).length)));
  es.forEach(e=>{gsap.to(e,{x:'random(-40,40)',y:'random(-30,30)',rotation:'random(-120,120)',duration:'random(3,6)',ease:'sine.inOut',repeat:-1,yoyo:true,repeatRefresh:true});gsap.from(e,{scale:0,opacity:0,duration:.8,ease:'back.out(2)',delay:rnd(0,.8)})})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx231` rules from `site/fx.css`

```css
.fx222 .t,.fx224 .t,.fx227 .t,.fx231 .t{color:#fff;z-index:1;text-shadow:0 .4cqw 2cqw #0006}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #231
