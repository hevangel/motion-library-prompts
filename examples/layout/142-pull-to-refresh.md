# 142 · 下拉重新整理 — Pull to Refresh

往下拉列表，轉圈圖示出現，放開後載入並彈回

- 元件 Component: 版面・頁面 (`layout`)
- 時機 Timing: 拖曳手勢
- 技術 Tech: GSAP
- 情境 Uses: App 介面、介面互動
- 風格／關鍵字 Style: 下拉 重新整理 刷新 列表 手勢 Pull Refresh Spinner Gesture App 手機 行動裝置 微互動 Mobile App Micro-interaction
- 標籤 Tag: Pull to refresh
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「下拉重新整理（Pull to Refresh）」動態效果：手機列表頁頂端往下拉時，列表跟著手指往下移（越拉阻力越大），上方露出一個圓形載入圖示，圖示的旋轉角度跟著下拉距離增加；放開後圖示持續旋轉表示載入中，完成後列表平滑彈回頂端，最新一筆資料短暫高亮後淡回。（GSAP：手勢用 Draggable 或 Observer 取得下拉距離並乘上阻尼係數；放開後 timeline：spinner 旋轉 → 列表 y 回 0（power3.out）→ 新項目背景淡出）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx142">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「下拉重新整理」.

### JavaScript — `FX[142]` from `site/fx.js`

```js
142(s){const ph=phone(s);const sp=el('i','ptr');const fg=el('i','tap');const list=el('div','pl');for(let i=0;i<7;i++)list.append(mrow(i));ph.append(sp,list,fg);const H=()=>ph.offsetHeight;
  gsap.timeline({repeat:-1,repeatDelay:.6}).set([sp,fg],{opacity:0},0).set(fg,{y:()=>H()*.3},0).to(fg,{opacity:.7,duration:.2},.2)
    .to([list,fg],{y:i=>i?H()*.48:H()*.17,duration:.7,ease:'power2.out'},.3).fromTo(sp,{opacity:0,rotation:0},{opacity:1,rotation:240,duration:.7,ease:'power2.out'},.3).to(fg,{opacity:0,duration:.2})
    .to(sp,{rotation:'+=720',duration:1.2,ease:'none'}).to(list,{y:0,duration:.5,ease:'power3.out'}).to(sp,{opacity:0,duration:.2},'<').fromTo(list.firstChild,{backgroundColor:'rgba(255,255,255,.12)'},{backgroundColor:'rgba(255,255,255,0)',duration:1})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx142` rules from `site/fx.css`

_No dedicated `.fx142` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #142
