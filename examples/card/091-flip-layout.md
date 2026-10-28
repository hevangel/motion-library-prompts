# 091 · 版面重排 — Flip Layout

格狀與橫排之間平滑重排

- 元件 Component: 卡片・群組 (`card`)
- 時機 Timing: 切換
- 技術 Tech: GSAP
- 情境 Uses: 介面互動、轉場切換
- 風格／關鍵字 Style: 
- 標籤 Tag: Flip
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「版面重排（Flip Layout）」動態效果：8 個方塊在「4×2 格狀」與「一整排」兩種版面之間切換，同時隨機打亂順序，每個方塊平滑滑到新位置與新尺寸。（GSAP：Flip.getState 記錄 → 改 class 與 DOM 順序 → Flip.from 補間）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx91">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「版面重排」.

### JavaScript — `FX[91]` from `site/fx.js`

```js
91(s,x,card){const g=el('div','fg');for(let i=0;i<8;i++){const e=el('div','ft');e.textContent=i+1;e.style.background=GC[i%4];g.append(e)}s.append(g);let k=0;
  card._timers.push(setInterval(()=>{const ts=[...g.children];const st=Flip.getState(ts);g.classList.toggle('alt',++k%2===1);gsap.utils.shuffle(ts).forEach(e=>g.append(e));Flip.from(st,{duration:.8,ease:'power3.inOut',stagger:.03})},1900))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx91` rules from `site/fx.css`

_No dedicated `.fx91` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #91
