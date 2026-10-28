# 126 · 逐行淡入 — Soft Line Fade

段落一行一行從微模糊變清楚，帶出閱讀節奏

- 元件 Component: 文字 (`text`)
- 時機 Timing: 進場
- 技術 Tech: GSAP
- 情境 Uses: 標題・Hero
- 風格／關鍵字 Style: 段落 內文 逐行 模糊 文案 溫和 柔和 輕柔 引導 動線 視線 閱讀順序 低調 Subtle Gentle Soft Entrance Visual Flow Hierarchy Canva 風格 Canva Fade Clarify 淡入 清晰
- 標籤 Tag: Line fade
- 範例文字 Example text: 「好的動態 不是搶走目光 而是輕輕帶著視線 往下一步走」（預覽底色：cream）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「逐行淡入（Soft Line Fade）」動態效果：一段多行文案進場時，每一行依序從下方約 10px、略帶模糊且透明的狀態，慢慢變清楚並淡入，行與行之間間隔約 0.28 秒（比一般 stagger 慢，接近閱讀速度），每行約 1.1 秒、平順減速，整體安靜、有呼吸感，適合品牌理念或引言段落。（GSAP：每行一個元素或用 SplitText type lines，fromTo y:10 / opacity:0 / filter:blur(4px) → 清晰，stagger 0.28，ease power2.out）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage cream fx126">`, preview text 「好的動態 不是搶走目光 而是輕輕帶著視線 往下一步走」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「逐行淡入」.

### JavaScript — `FX[126]` from `site/fx.js`

```js
126(s,x){const w=el('div','sl');words(x).forEach(v=>{const d=el('div');d.textContent=v;w.append(d)});s.append(w);const it=w.children;
  gsap.timeline({repeat:-1,repeatDelay:.3}).fromTo(it,{y:10,opacity:0,filter:'blur(4px)'},{y:0,opacity:1,filter:'blur(0px)',duration:1.1,ease:'power2.out',stagger:.28}).to(it,{opacity:0,duration:.6},'+=1.6')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx126` rules from `site/fx.css`

_No dedicated `.fx126` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #126
