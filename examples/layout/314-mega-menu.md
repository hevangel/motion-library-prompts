# 314 · 大型下拉選單 — Mega Menu

滑過導覽列項目時，下方展開一大塊多欄選單，各欄依序滑入

- 元件 Component: 版面・頁面 (`layout`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動
- 風格／關鍵字 Style: 大型選單 下拉 導覽列 多欄 mega menu Dropdown Navigation Header 版面 頁面
- 標籤 Tag: CSS transition
- 範例文字 Example text: 「品牌設計 網站開發 動態影像 社群經營 案例分享 設計指南」（預覽底色：dark）
- 收錄日期 Added: 2026-10-21

**AI 提示詞（網站複製格式）:**

```text
「大型下拉選單（Mega Menu）」動態效果：網站導覽列：滑鼠滑到「產品」時，下方展開一整塊寬版的大型選單面板（從略高處滑下並淡入），面板內分成三欄：兩欄是帶小圖示的連結清單，一欄是精選圖片卡；三欄依序（間隔約 0.06 秒）往上滑入；滑鼠離開導覽區時面板收起。（CSS：面板預設 opacity 0、translateY(−8px)、pointer-events:none，父層 :hover 或 .open 時恢復；每欄設 transition-delay 形成依序出現）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx314">`, preview text 「品牌設計 網站開發 動態影像 社群經營 案例分享 設計指南」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「大型下拉選單」.

### JavaScript — `FX[314]` from `site/fx.js`

```js
314(s,x,card){const f=lyPage(s,true);const ws=words(x);const nav=el('div','pg-mn');nav.innerHTML='<span class="pg-mi">產品 ▾</span><span>方案</span><span>關於</span>';const pn=el('div','pg-mp');pn.innerHTML=[0,1,2].map(c=>'<div class="pg-mc"><small>'+['服務','資源','精選'][c]+'</small>'+(c<2?[0,1,2].map(r=>'<p><i></i><b></b></p>').join(''):'<div class="pg-mf">'+mdImg(1)+'</div>')+'</div>').join('');pn.querySelectorAll('p b').forEach((b,i)=>b.textContent=ws[i%ws.length]);f.querySelector('.ly-bar').append(nav);f.append(pn);
  const mi=nav.querySelector('.pg-mi');let real=0;const open=o=>f.classList.toggle('pg-open',o);mi.addEventListener('pointerenter',()=>{real=Date.now();open(true)});f.addEventListener('pointerleave',()=>open(false));pn.addEventListener('pointerenter',()=>real=Date.now());
  card._timers.push(setInterval(()=>{if(Date.now()-real>5000)open(!f.classList.contains('pg-open'))},1800))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx314` rules from `site/fx.css`

_No dedicated `.fx314` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #314
