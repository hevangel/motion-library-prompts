# 297 · 劃掉改寫 — Strike & Rewrite

一個詞被一筆劃掉，上面再用手寫字一個字一個字寫出新的詞

- 元件 Component: 文字 (`text`)
- 時機 Timing: 切換
- 技術 Tech: GSAP
- 情境 Uses: 強調重點、標題・Hero
- 風格／關鍵字 Style: 劃掉 刪除線 改寫 修正 手寫 文案 Strikethrough Rewrite Correction Copywriting 文字 標題 動態文字
- 標籤 Tag: GSAP timeline
- 範例文字 Example text: 「便宜 實惠」（預覽底色：dark）
- 收錄日期 Added: 2026-10-20

**AI 提示詞（網站複製格式）:**

```text
「劃掉改寫（Strike & Rewrite）」動態效果：文案中原本的一個詞（例如「便宜」），先被一條略微傾斜的粗線從左到右一筆劃掉，原詞變淡；接著在它下方用手寫風格的字體、以強調色一個字一個字彈出新的詞（例如「實惠」），像有人親手修改文案，用來強調更好的說法。（GSAP timeline：刪除線元素 scaleX 0 → 1、transform-origin:left；原詞 opacity 降到 0.4；新詞用 SplitText 拆字，依序從下方 back.out 彈出）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx297">`, preview text 「便宜 實惠」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「劃掉改寫」.

### JavaScript — `FX[297]` from `site/fx.js`

```js
297(s,x){const ws=words(x);const a=ws[0]||'便宜',bw=ws[1]||'實惠';const w=el('div','tx-rw');w.innerHTML='<span class="tx-o"><b></b><i class="tx-st"></i></span><span class="tx-n"></span>';w.querySelector('.tx-o b').textContent=a;const nw=w.querySelector('.tx-n');nw.textContent=bw;w.style.fontSize=Math.min(12,50/Math.max(chars(a).length,chars(bw).length))+'cqw';s.append(w);
  const sp=SplitText.create(nw,{type:'chars'});const st=w.querySelector('.tx-st'),ob=w.querySelector('.tx-o b');
  gsap.timeline({repeat:-1,repeatDelay:.6}).set([st,sp.chars,ob],{clearProps:'all'}).set(st,{scaleX:0}).set(sp.chars,{opacity:0,y:'.3em'}).to(st,{scaleX:1,duration:.45,ease:'power2.inOut'},.6).to(ob,{opacity:.4,duration:.3},'<.2').to(sp.chars,{opacity:1,y:0,duration:.25,stagger:.12,ease:'back.out(3)'}).to(w,{opacity:0,duration:.4},'+=1.6').set(w,{opacity:1})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx297` rules from `site/fx.css`

_No dedicated `.fx297` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #297
