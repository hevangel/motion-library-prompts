# 206 · 手風琴問答 — Accordion FAQ

點開問題時答案區平滑展開，加號轉成叉叉，同時收起其他題

- 元件 Component: 版面・頁面 (`layout`)
- 時機 Timing: 懸停・點擊、切換
- 技術 Tech: CSS
- 情境 Uses: 介面互動、數字資訊
- 風格／關鍵字 Style: 手風琴 常見問題 FAQ 展開 收合 摺疊 Accordion Collapse Expand Details 版面 頁面 網頁結構
- 標籤 Tag: grid-template-rows
- 範例文字 Example text: 「如何下單？ 運費怎麼算？ 可以退貨嗎？」（預覽底色：dark）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「手風琴問答（Accordion FAQ）」動態效果：常見問題列表，每題右側有一個加號；點開某一題時，答案區的高度從 0 平滑展開到內容高度（不是瞬間跳出），加號同時旋轉 135 度變成叉叉，其他已展開的題目同步收起，一次只開一題。約 0.45 秒、緩入緩出。（CSS：答案外層 display:grid + grid-template-rows:0fr → 1fr 的 transition，內層 overflow:hidden；加號用兩條線組成並 rotate；也可用 details/summary 搭配 JS）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx206">`, preview text 「如何下單？ 運費怎麼算？ 可以退貨嗎？」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「手風琴問答」.

### JavaScript — `FX[206]` from `site/fx.js`

```js
206(s,x,card){const ws=words(x);const w=el('div','ly-acc');const its=ws.slice(0,3).map(v=>{const it=el('div','ly-ai');it.innerHTML='<button><span></span><i></i></button><div class="ly-ab"><div><em></em><em class="s"></em></div></div>';it.querySelector('span').textContent=v;w.append(it);return it});s.append(w);let real=0,k=0;
  const open=i=>its.forEach((it,j)=>it.classList.toggle('on',j===i&&!it.classList.contains('on')));its.forEach((it,i)=>it.querySelector('button').onclick=()=>{real=Date.now();open(i)});
  card._timers.push(setInterval(()=>{if(Date.now()-real>4000)open(k++%3)},1600))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx206` rules from `site/fx.css`

_No dedicated `.fx206` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #206
