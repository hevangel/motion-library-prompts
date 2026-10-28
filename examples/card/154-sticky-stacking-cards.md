# 154 · 黏著堆疊卡片 — Sticky Stacking Cards

卡片一張張捲上來疊住，下面那張縮小變暗

- 元件 Component: 卡片・群組 (`card`)
- 時機 Timing: 捲動觸發
- 技術 Tech: GSAP
- 情境 Uses: 介面互動、捲動效果
- 風格／關鍵字 Style: 卡片 堆疊 黏著 sticky 疊起來 服務介紹 Stacking Cards Sticky Stack Deck 捲動 滾動 scroll ScrollTrigger scrub 捲動觸發
- 標籤 Tag: Sticky・scrub
- 範例文字 Example text: 「研究 設計 開發 上線」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「黏著堆疊卡片（Sticky Stacking Cards）」動態效果：一組大卡片依序往下排，每張卡片捲到畫面頂端附近時會黏住（每張的停留位置往下錯開一點，看得到前一張的邊緣），下一張卡片捲上來疊在上面時，被蓋住的那張同步縮小到約 90% 並變暗，形成一疊卡片的景深；往回捲時恢復。（CSS position:sticky + top 依索引遞增；GSAP 每張卡片一個 ScrollTrigger，以「下一張卡片進入畫面到抵達頂端」為範圍 scrub scale 與 brightness）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx154">`, preview text 「研究 設計 開發 上線」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「黏著堆疊卡片」.

### JavaScript — `FX[154]` from `site/fx.js`

```js
154(s,x){const sc=el('div','scr nopad');const c=el('div','stk');const ws=words(x);const cs=ws.slice(0,4).map((v,i)=>{const k=el('div','skc2');k.style.setProperty('--i',i);k.style.background=GC[i%5];k.innerHTML=`<small>0${i+1}</small><b></b>`;k.querySelector('b').textContent=v;c.append(k);return k});sc.append(c);s.append(sc);
  cs.forEach((k,i)=>{if(i<cs.length-1)gsap.to(k,{scale:.9,filter:'brightness(.55)',ease:'none',scrollTrigger:{trigger:cs[i+1],scroller:sc,start:'top bottom',end:'top top+=8%',scrub:true}})});autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx154` rules from `site/fx.css`

_No dedicated `.fx154` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #154
