# 291 · 表格十字高亮 — Table Crosshair Highlight

滑過表格某一格時，整列與整欄淡淡亮起，該格放大突顯

- 元件 Component: 表單・控制項 (`control`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 數字資訊、介面互動
- 風格／關鍵字 Style: 表格 資料 列 欄 高亮 十字 Table Row Column Highlight Crosshair Hover Data hover 懸停 滑過
- 標籤 Tag: JS + CSS
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-20

**AI 提示詞（網站複製格式）:**

```text
「表格十字高亮（Table Crosshair Highlight）」動態效果：資料表格：滑鼠滑過某一格時，該格所在的整列與整欄都淡淡亮起形成十字，被指到的那一格填滿強調底色、文字加粗並微微放大，讓人快速對照列標題與欄標題；移動到其他格時十字跟著移動，離開表格時全部恢復。（JS：pointerover 時找出 td 的 cellIndex 與所在的 tr，分別加上 class；CSS：.row 與 .col 用很淡的半透明底色，被指到的格子用強調底色 + scale(1.12)，transition 0.25 秒）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx291">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「表格十字高亮」.

### JavaScript — `FX[291]` from `site/fx.js`

```js
291(s,x,card){const t=el('table','ho-tb');const H=['','一月','二月','三月','四月'],R=[['網站',42,58,61,77],['App',31,36,52,49],['商店',18,24,29,41]];t.innerHTML='<thead><tr>'+H.map(h=>`<th>${h}</th>`).join('')+'</tr></thead><tbody>'+R.map(r=>'<tr>'+r.map((v,i)=>i?`<td>${v}</td>`:`<th>${v}</th>`).join('')+'</tr>').join('')+'</tbody>';s.append(t);
  const cells=[...t.querySelectorAll('td')];const set=td=>{t.querySelectorAll('.r,.c,.x').forEach(e=>e.classList.remove('r','c','x'));if(!td)return;const ci=td.cellIndex;td.parentElement.classList.add('r');t.querySelectorAll('tr').forEach(tr=>tr.children[ci]&&tr.children[ci].classList.add('c'));td.classList.add('x')};
  let real=false,k=0;t.addEventListener('pointerover',e=>{real=true;set(e.target.closest('td'))});t.addEventListener('pointerleave',()=>{real=false;set(null)});card._timers.push(setInterval(()=>{if(!real)set(cells[(k=(k+5)%cells.length)])},900))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx291` rules from `site/fx.css`

_No dedicated `.fx291` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #291
