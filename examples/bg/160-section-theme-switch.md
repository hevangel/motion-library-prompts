# 160 · 章節主題切換 — Section Theme Switch

捲到不同章節時，整個頁面背景與文字配置跟著切換

- 元件 Component: 背景・氛圍 (`bg`)
- 時機 Timing: 捲動觸發、切換
- 技術 Tech: GSAP
- 情境 Uses: 背景裝飾、捲動效果、轉場切換
- 風格／關鍵字 Style: 背景 主題 切換 章節 區塊 Section Theme Background Change On Scroll Chapters 捲動 滾動 scroll ScrollTrigger scrub 捲動觸發
- 標籤 Tag: ScrollTrigger toggle
- 範例文字 Example text: 「序章 理念 作品 聯絡」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「章節主題切換（Section Theme Switch）」動態效果：頁面分成幾個章節，每個章節有自己的背景與文字配色主題；當某個章節捲到畫面中線時，整個頁面的背景與文字在約 0.6 秒內平滑過渡到該章節的主題，往回捲時切回前一個，讓每一章有明確的氛圍轉換。（GSAP：每個章節一個 ScrollTrigger，start "top 50%"、end "bottom 50%"，onToggle 時切換 CSS 變數或 class；CSS 對 background / color 加 transition）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx160">`, preview text 「序章 理念 作品 聯絡」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「章節主題切換」.

### JavaScript — `FX[160]` from `site/fx.js`

```js
160(s,x){const sc=el('div','scr nopad thm');const TH=[['#15161a','#fff'],['#f4f1e8','#111'],['#ff7a2f','#111'],['#7c5cff','#fff']];const ws=words(x);
  const secs=ws.slice(0,4).map((v,i)=>{const e=el('section','ths');e.innerHTML=`<small>CHAPTER 0${i+1}</small><b></b><i></i><i class="s"></i>`;e.querySelector('b').textContent=v;sc.append(e);return e});s.append(sc);
  const set=i=>{sc.style.background=TH[i][0];sc.style.color=TH[i][1]};set(0);secs.forEach((e,i)=>ScrollTrigger.create({trigger:e,scroller:sc,start:'top 50%',end:'bottom 50%',onToggle:t=>{if(t.isActive)set(i)}}));autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx160` rules from `site/fx.css`

_No dedicated `.fx160` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #160
