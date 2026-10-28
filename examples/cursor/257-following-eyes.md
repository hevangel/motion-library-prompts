# 257 · 眼睛跟隨 — Following Eyes

一對大眼睛的眼珠一直盯著游標轉，偶爾眨眼

- 元件 Component: 游標 (`cursor`)
- 時機 Timing: 懸停・點擊、循環待機
- 技術 Tech: CSS
- 情境 Uses: 介面互動、Logo・品牌
- 風格／關鍵字 Style: 眼睛 眼珠 跟隨 盯著 可愛 吉祥物 404 Googly Eyes Follow Cursor Mascot 游標 滑鼠
- 標籤 Tag: JS atan2
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「眼睛跟隨（Following Eyes）」動態效果：一對大眼睛（眼白 + 眼珠，眼珠帶一個小反光點），眼珠一直朝游標的方向轉動：游標越遠，眼珠越靠近眼眶邊緣，游標在眼睛正前方時眼珠回到中間；每隔幾秒兩眼一起快速眨眼一次（眼睛垂直壓扁再恢復，約 0.15 秒）。適合吉祥物、404 頁面或趣味互動。（JS：每隻眼睛以中心點計算 atan2 角度，距離取 min(1, 距離 / 範圍) × 最大偏移，用 transform 移動眼珠；眨眼用 scaleY 的 class 切換）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx257">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「眼睛跟隨」.

### JavaScript — `FX[257]` from `site/fx.js`

```js
257(s,x,card){const l=el('div','abs gl cr-ey');const f=el('div','cr-ef');f.innerHTML='<div class="cr-e"><i></i></div><div class="cr-e"><i></i></div><span class="cr-m"></span>';l.append(f);s.append(l);const es=[...f.querySelectorAll('.cr-e')];let blink=0;
  vpointer(l,card,(px,py)=>{const r=l.getBoundingClientRect();es.forEach(e=>{const q=e.getBoundingClientRect(),cx=q.left-r.left+q.width/2,cy=q.top-r.top+q.height/2,a=Math.atan2(py-cy,px-cx),d=Math.min(1,Math.hypot(px-cx,py-cy)/(q.width*1.5))*q.width*.26;e.firstChild.style.transform=`translate(${Math.cos(a)*d}px,${Math.sin(a)*d}px)`})});
  card._timers.push(setInterval(()=>{f.classList.add('bk');setTimeout(()=>f.classList.remove('bk'),160)},2600))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx257` rules from `site/fx.css`

_No dedicated `.fx257` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #257
