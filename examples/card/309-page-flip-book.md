# 309 · 翻頁書 — Page Flip Book

點一下書頁就以書脊為軸立體翻到左邊，翻完再一起翻回第一頁

- 元件 Component: 卡片・群組 (`card`)
- 時機 Timing: 切換
- 技術 Tech: GSAP
- 情境 Uses: 介面互動、標題・Hero
- 風格／關鍵字 Style: 翻頁 書本 書頁 雜誌 型錄 電子書 Page Flip Book Magazine Catalog 3D 卡片 群組
- 標籤 Tag: GSAP 3D
- 範例文字 Example text: 「序章 旅程 相遇 尾聲」（預覽底色：dark）
- 收錄日期 Added: 2026-10-20

**AI 提示詞（網站複製格式）:**

```text
「翻頁書（Page Flip Book）」動態效果：像一本書：右側是一疊書頁，每頁正面有圖片與頁碼；點擊時最上面那頁以左側書脊為軸，在 3D 空間中翻到左邊（約 0.9 秒、緩入緩出），翻到一半時可以看到書頁的立體角度，翻過去後顯示該頁的背面；一頁一頁翻完後，所有書頁依序快速翻回第一頁。（CSS 3D：每頁 transform-origin:left、transform-style:preserve-3d，正反兩面 backface-visibility:hidden、背面 rotateY(180deg)；GSAP tween rotationY 0 → −180，並在翻頁時調整 z-index 讓翻過去的頁疊在最上面）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx309">`, preview text 「序章 旅程 相遇 尾聲」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「翻頁書」.

### JavaScript — `FX[309]` from `site/fx.js`

```js
309(s,x,card){const ws=words(x);const bk=el('div','cg-bk');const P=4;bk.innerHTML='<div class="cg-pg base"></div>';const pgs=[];for(let i=P-1;i>=0;i--){const p=el('div','cg-pg');p.innerHTML='<div class="fr">'+mdImg(i)+'<b></b></div><div class="bk">'+mdImg(i+1)+'</div>';p.querySelector('b').textContent=ws[i%ws.length]+'　'+(i+1)+' / '+P;p.style.zIndex=P-i;bk.append(p);pgs.unshift(p)}s.append(bk);let k=0,real=0,busy=false;
  bk.querySelector('.base').innerHTML=mdImg(P)+'<b>THE END</b>';
  const next=()=>{if(busy)return;busy=true;if(k<P){const p=pgs[k++];gsap.to(p,{rotationY:-180,duration:.9,ease:'power2.inOut',onStart:()=>{p.style.zIndex=10+k},onComplete:()=>busy=false})}else{gsap.to(pgs.slice().reverse(),{rotationY:0,duration:.6,stagger:.1,ease:'power2.inOut',onComplete:()=>{pgs.forEach((p,i)=>p.style.zIndex=P-i);k=0;busy=false}})}};
  bk.onclick=()=>{real=Date.now();next()};card._timers.push(setInterval(()=>{if(Date.now()-real>5000)next()},1700))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx309` rules from `site/fx.css`

_No dedicated `.fx309` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #309
