# 304 · 多選卡片 — Selectable Cards

點卡片選取時出現框線與打勾，底部彈出「已選 N 項」的操作列

- 元件 Component: 卡片・群組 (`card`)
- 時機 Timing: 切換
- 技術 Tech: CSS
- 情境 Uses: 介面互動、App 介面
- 風格／關鍵字 Style: 選取 多選 勾選 卡片 操作列 Selectable Cards Multi Select Checkbox Action Bar 卡片 群組
- 標籤 Tag: JS + CSS
- 範例文字 Example text: 「海邊 山林 夜空 午後」（預覽底色：dark）
- 收錄日期 Added: 2026-10-20

**AI 提示詞（網站複製格式）:**

```text
「多選卡片（Selectable Cards）」動態效果：一排可多選的圖片卡片：點擊卡片時，卡片外圍出現強調色框線並輕微縮小，圖片在框內微放大，右上角的圓形勾選框填滿並畫出勾勾（帶回彈）；只要有選取，畫面底部就從下方彈出一條膠囊形操作列，顯示「已選 N 項」（數字變動時上下滾動）與「下一步 →」按鈕；全部取消時操作列滑回隱藏。（JS 切換 aria-pressed，CSS 依 [aria-pressed=true] 改變框線、scale 與勾勾的 stroke-dashoffset；操作列 translateY 與 opacity transition）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx304">`, preview text 「海邊 山林 夜空 午後」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「多選卡片」.

### JavaScript — `FX[304]` from `site/fx.js`

```js
304(s,x,card){const ws=words(x);const w=el('div','cg-sw');w.innerHTML='<div class="cg-sg"></div><div class="cg-bar"><b>已選 <span>0</span> 項</b><button>下一步 →</button></div>';const sg=w.querySelector('.cg-sg'),bar=w.querySelector('.cg-bar'),cnt=bar.querySelector('span');
  const cs=[0,1,2,3].map(i=>{const c=el('button','cg-sc');c.setAttribute('aria-pressed','false');c.innerHTML=mdImg(i)+'<i class="cg-ck"><svg viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7"/></svg></i><b></b>';c.querySelector('b').textContent=ws[i%ws.length];c.onclick=()=>{real=Date.now();tog(c)};sg.append(c);return c});s.append(w);let real=0;
  const tog=c=>{const on=c.getAttribute('aria-pressed')!=='true';c.setAttribute('aria-pressed',on);const n=cs.filter(x=>x.getAttribute('aria-pressed')==='true').length;cnt.textContent=n;bar.classList.toggle('on',n>0);gsap.fromTo(cnt,{y:on?'-60%':'60%',opacity:0},{y:0,opacity:1,duration:.3,ease:'back.out(3)'})};
  card._timers.push(setInterval(()=>{if(Date.now()-real<5000)return;tog(cs[Math.floor(Math.random()*4)])},1100))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx304` rules from `site/fx.css`

_No dedicated `.fx304` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #304
