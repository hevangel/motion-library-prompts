# 086 · 逐行揭示 — Line Reveal

一行行從遮罩下翻上來

- 元件 Component: 文字 (`text`)
- 時機 Timing: 進場
- 技術 Tech: GSAP
- 情境 Uses: 標題・Hero
- 風格／關鍵字 Style: 
- 標籤 Tag: Mask・Stagger
- 範例文字 Example text: 「動畫 讓介面 有了生命」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「逐行揭示（Line Reveal）」動態效果：多行文字逐行從各自的遮罩下方帶一點旋轉翻上來，最後一行用強調色，下方一條細線由左往右畫出，停留後整段往上收走。（GSAP：每行包 overflow hidden，from yPercent:115，stagger 0.14）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx86">`, preview text 「動畫 讓介面 有了生命」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「逐行揭示」.

### JavaScript — `FX[86]` from `site/fx.js`

```js
86(s,x){const ws=words(x);const w=el('div','ln');w.style.fontSize=Math.min(10,62/Math.max(...ws.map(v=>chars(v).length)))+'cqw';const inn=ws.map((v,i)=>{const m=el('div','m');const e=el('div','i');e.textContent=v;if(i===ws.length-1)e.style.color='var(--a)';m.append(e);w.append(m);return e});const rule=el('div','rule');w.append(rule);s.append(w);
  gsap.timeline({repeat:-1,repeatDelay:.3}).from(inn,{yPercent:115,rotation:4,duration:.9,ease:'power4.out',stagger:.14}).fromTo(rule,{scaleX:0,transformOrigin:'0% 50%'},{scaleX:1,duration:.8,ease:'power3.inOut'},'-=.5').to(inn,{yPercent:-115,duration:.5,ease:'power3.in',stagger:.08},'+=1.4').to(rule,{scaleX:0,transformOrigin:'100% 50%',duration:.5,ease:'power3.in'},'<')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx86` rules from `site/fx.css`

_No dedicated `.fx86` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #86
