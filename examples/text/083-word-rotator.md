# 083 · 遮罩換詞 — Word Rotator

固定前綴、後面的詞輪播替換

- 元件 Component: 文字 (`text`)
- 時機 Timing: 切換
- 技術 Tech: GSAP
- 情境 Uses: 標題・Hero、轉場切換
- 風格／關鍵字 Style: 
- 標籤 Tag: SplitText mask
- 範例文字 Example text: 「設計 動畫 互動 體驗」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「遮罩換詞（Word Rotator）」動態效果：固定前綴「我們做」，後面的詞放在遮罩內輪播：新詞逐字從下方滑上，停留後往上滑出，接著換下一個詞，輪播的詞用強調色。（GSAP：SplitText chars + mask，timeline 依序串接每個詞）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx83">`, preview text 「設計 動畫 互動 體驗」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「遮罩換詞」.

### JavaScript — `FX[83]` from `site/fx.js`

```js
83(s,x){const ws=words(x);const w=el('div','wm');const pre=el('span');pre.textContent='我們做';const box=el('span','box');w.append(pre,box);w.style.fontSize=Math.min(11,62/(3+Math.max(...ws.map(v=>chars(v).length))))+'cqw';s.append(w);
  const tl=gsap.timeline({repeat:-1});ws.forEach(v=>{const e=el('span','it');e.textContent=v;box.append(e);const sp=SplitText.create(e,{type:'chars',mask:'chars'});tl.fromTo(sp.chars,{yPercent:110},{yPercent:0,duration:.6,ease:'power3.out',stagger:.04}).to(sp.chars,{yPercent:-110,duration:.45,ease:'power3.in',stagger:.03},'+=1')})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx83` rules from `site/fx.css`

_No dedicated `.fx83` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #83
