# 319 · 無限捲動載入 — Infinite Scroll

捲到底時出現轉圈的「載入更多」，新內容接著一張張浮上來

- 元件 Component: 版面・頁面 (`layout`)
- 時機 Timing: 捲動觸發
- 技術 Tech: GSAP
- 情境 Uses: 介面互動、App 介面、捲動效果
- 風格／關鍵字 Style: 無限捲動 載入更多 分頁 動態牆 Infinite Scroll Load More Feed Pagination 版面 頁面
- 標籤 Tag: GSAP
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-21

**AI 提示詞（網站複製格式）:**

```text
「無限捲動載入（Infinite Scroll）」動態效果：社群動態牆或文章列表的無限捲動：使用者捲到清單底部時，底部出現一個轉圈的載入指示與「載入更多…」，約一秒後新的一批卡片接在清單後面，從下方依序（間隔約 0.12 秒）淡入浮上，使用者可以繼續往下捲。（實作：IntersectionObserver 觀察清單底部的哨兵元素，進入畫面時顯示載入指示並請求下一頁；新卡片插入後用 GSAP from y:24、opacity:0、stagger 進場）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx319">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「無限捲動載入」.

### JavaScript — `FX[319]` from `site/fx.js`

```js
319(s,x){const sc=el('div','scr pg-is');const list=el('div','pg-il2');const sp=el('div','pg-ld','<i></i><span>載入更多…</span>');sc.append(list,sp);s.append(sc);let n=0;
  const add=k=>{const items=[];for(let i=0;i<k;i++){const c=el('div','pg-it');c.innerHTML=mdImg(n++)+'<b>貼文 #'+n+'</b>';list.append(c);items.push(c)}return items};add(4);let loading=false;
  const step=()=>{const max=sc.scrollHeight-sc.clientHeight;gsap.to(sc,{scrollTop:max,duration:1.4,ease:'power1.inOut',onComplete:()=>{sp.classList.add('on');gsap.delayedCall(.9,()=>{sp.classList.remove('on');const it=add(2);gsap.from(it,{y:24,opacity:0,duration:.5,stagger:.12,ease:'power3.out'});if(n>=12){gsap.delayedCall(1.2,()=>{gsap.to(sc,{scrollTop:0,duration:.6,onComplete:()=>{list.innerHTML='';n=0;add(4);gsap.delayedCall(.6,step)}})})}else gsap.delayedCall(.9,step)})}})};
  gsap.delayedCall(.6,step)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx319` rules from `site/fx.css`

_No dedicated `.fx319` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #319
