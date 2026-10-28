# 255 · 情境標籤游標 — Contextual Cursor

游標移到不同內容上，變成對應動作的大圓圈加文字，例如播放、查看、拖曳

- 元件 Component: 游標 (`cursor`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動、標題・Hero
- 風格／關鍵字 Style: 情境 標籤 游標 播放 查看 拖曳 作品集 Contextual Label Cursor View Play Drag Portfolio 游標 滑鼠
- 標籤 Tag: JS + CSS
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「情境標籤游標（Contextual Cursor）」動態效果：作品集的卡片區，平常游標是一個小圓點；移到不同類型的內容上時，小圓點彈性放大成一個實心大圓，中間顯示對應的圖示，下方浮出動作文字，例如影片顯示「▶ 播放」、作品顯示「↗ 查看」、輪播顯示「⇆ 拖曳」；離開內容時縮回小圓點。（JS：每個區塊用 data-cursor 屬性設定文字與圖示，mousemove 偵測目前所在區塊並更新游標內容；CSS：大圓 scale 0 → 1 用 cubic-bezier(.3,1.5,.5,1)、文字淡入上移）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx255">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「情境標籤游標」.

### JavaScript — `FX[255]` from `site/fx.js`

```js
255(s,x,card){const l=el('div','abs gl cr-ct');const g=el('div','cr-cg');const K=[['播放','▶'],['查看','↗'],['拖曳','⇆']];const it=K.map(([lb,ic],i)=>{const d=el('div','cr-ci');d.dataset.lb=lb;d.dataset.ic=ic;d.style.background=`linear-gradient(135deg,${GC[i]},${GC[(i+2)%5]})`;g.append(d);return d});
  const c=el('div','cr-cc');c.innerHTML='<b></b><span></span>';l.append(g,c);s.append(l);const [ib,sp]=[c.querySelector('b'),c.querySelector('span')];
  vpointer(l,card,(px,py)=>{const r=l.getBoundingClientRect();c.style.transform=`translate(${px}px,${py}px)`;let hit=null;it.forEach(d=>{const q=d.getBoundingClientRect();if(px>q.left-r.left&&px<q.right-r.left&&py>q.top-r.top&&py<q.bottom-r.top)hit=d});
    c.classList.toggle('on',!!hit);if(hit&&sp.textContent!==hit.dataset.lb){sp.textContent=hit.dataset.lb;ib.textContent=hit.dataset.ic}})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx255` rules from `site/fx.css`

_No dedicated `.fx255` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #255
