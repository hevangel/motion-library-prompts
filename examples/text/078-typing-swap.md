# 078 · 打字換句 — Typing Swap

打字、刪除、換下一句

- 元件 Component: 文字 (`text`)
- 時機 Timing: 切換
- 技術 Tech: GSAP
- 情境 Uses: 標題・Hero
- 風格／關鍵字 Style: Canva 風格 Canva Typewriter 打字機
- 標籤 Tag: TextPlugin
- 範例文字 Example text: 「用 GSAP 打字」（預覽底色：cream）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「打字換句（Typing Swap）」動態效果：像打字機一樣逐字打出一句話，後方游標閃爍，停留約 1 秒後從尾端逐字刪除，再打下一句，三句輪播。（GSAP：TextPlugin 打字 + timeline 串接刪除）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage cream fx78">`, preview text 「用 GSAP 打字」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「打字換句」.

### JavaScript — `FX[78]` from `site/fx.js`

```js
78(s,x){const ph=[x,'讓介面動起來','換一句再打'];const w=el('div','tw2');const t=el('span');w.append(t,el('span','cur2'));w.style.fontSize=Math.min(9,64/Math.max(...ph.map(v=>chars(v).length)))+'cqw';s.append(w);
  const tl=gsap.timeline({repeat:-1});ph.forEach(v=>{const n=chars(v).length,o={n};tl.to(t,{duration:n*.1,text:{value:v},ease:'none'}).to(o,{n:0,duration:n*.05,ease:'none',onUpdate:()=>t.textContent=chars(v).slice(0,Math.round(o.n)).join('')},'+=1.1').set(o,{n})})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx78` rules from `site/fx.css`

_No dedicated `.fx78` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #78
