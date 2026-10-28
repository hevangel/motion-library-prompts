# 281 · 對開門轉場 — Split Doors Reveal

整個畫面從中間切開成左右兩扇門，隨捲動往兩側拉開，露出下一段

- 元件 Component: 版面・頁面 (`layout`)
- 時機 Timing: 捲動觸發
- 技術 Tech: GSAP
- 情境 Uses: 捲動效果、轉場切換
- 風格／關鍵字 Style: 對開 開門 拉開 分割 轉場 揭開 Split Doors Curtain Reveal Scroll Transition 捲動觸發 ScrollTrigger
- 標籤 Tag: ScrollTrigger
- 範例文字 Example text: 「歡迎光臨」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「對開門轉場（Split Doors Reveal）」動態效果：兩段內容之間的轉場：前一段是一整面強調色的畫面，中間有一個巨大的字；使用者往下捲動時，這個畫面從正中央垂直切開成左右兩扇門（大字也跟著被切成兩半），兩扇門隨捲動進度往左右兩側滑開，露出後面的下一段內容，下一段同時從 0.8 倍放大並變清楚。（GSAP ScrollTrigger scrub：左右兩個各寬 50%、overflow:hidden 的區塊，內部各放一份寬度 200% 的同一個大字（左邊靠左、右邊靠右對齊）讓它看起來是同一個字；timeline 讓兩扇門 xPercent −100 / 100）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx281">`, preview text 「歡迎光臨」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「對開門轉場」.

### JavaScript — `FX[281]` from `site/fx.js`

```js
281(s,x){const{sc,wrap,view}=scrollBox(s);const nx=el('div','abs gl sx-cn');nx.append(T(x,Math.min(11,50/chars(x).length)));const L=el('div','sx-ct l'),R=el('div','sx-ct r');L.innerHTML=R.innerHTML='<b>SCROLL</b>';view.append(nx,L,R);
  gsap.timeline({scrollTrigger:{trigger:wrap,scroller:sc,start:'top top',end:'bottom bottom',scrub:.6}}).to(L,{xPercent:-100,ease:'power2.inOut'},.15).to(R,{xPercent:100,ease:'power2.inOut'},.15).fromTo(nx,{scale:.8,opacity:.2},{scale:1,opacity:1,ease:'power2.out'},.15);autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx281` rules from `site/fx.css`

_No dedicated `.fx281` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #281
