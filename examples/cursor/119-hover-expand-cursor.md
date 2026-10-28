# 119 · 懸停放大游標 — Hover Expand Cursor

小圓點游標移到作品上時放大成寫著文字的圓

- 元件 Component: 游標 (`cursor`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動
- 風格／關鍵字 Style: 游標 自訂游標 放大 懸停 VIEW 查看 Custom Cursor Hover Expand Portfolio
- 標籤 Tag: Custom cursor
- 範例文字 Example text: 「VIEW」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「懸停放大游標（Hover Expand Cursor）」動態效果：隱藏系統游標，改用一顆小圓點跟著滑鼠移動（帶一點延遲感）；當游標移到作品縮圖上時，小圓點平滑放大成約 3 倍大的圓，圓中央出現「VIEW」之類的提示文字，作品本身也微微縮小回應；離開作品時再縮回小圓點、文字淡出。放大約 0.35 秒、緩出。（做法：容器設 cursor:none；自訂游標用 position:fixed + transform 跟隨 mousemove；hover 目標時加 class，讓內層圓 scale(0.16→1)、文字 opacity 0→1；觸控裝置上應關閉此效果）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx119">`, preview text 「VIEW」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「懸停放大游標」.

### JavaScript — `FX[119]` from `site/fx.js`

```js
119(s,x,card){const l=el('div','abs gl cz');const row=el('div','czr');const ts=[0,1,2].map(i=>{const t=el('div','czt');t.style.background=`linear-gradient(135deg,${GC[i]},${GC[i+1]})`;row.append(t);return t});
  const c=el('div','cx');const cb=el('div','cb');const lb=el('span');lb.textContent=x;cb.append(lb);c.append(cb);l.append(row,c);s.append(l);
  vpointer(l,card,(px,py)=>{c.style.transform=`translate(${px}px,${py}px)`;let on=false;ts.forEach(t=>{const h=px>=t.offsetLeft&&px<=t.offsetLeft+t.offsetWidth&&py>=t.offsetTop&&py<=t.offsetTop+t.offsetHeight;t.classList.toggle('hv',h);on=on||h});c.classList.toggle('big',on)})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx119` rules from `site/fx.css`

_No dedicated `.fx119` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #119
