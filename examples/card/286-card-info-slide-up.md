# 286 · 資訊面板滑上 — Card Info Slide Up

圖片卡片平常只露出標題，滑過時資訊面板從底部滑上來，圖片同時上移放大

- 元件 Component: 卡片・群組 (`card`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動
- 風格／關鍵字 Style: 卡片 資訊 面板 滑上 說明 作品 Card Info Slide Up Overlay Details Hover hover 懸停 滑過
- 標籤 Tag: CSS hover
- 範例文字 Example text: 「海邊 山林 夜空」（預覽底色：dark）
- 收錄日期 Added: 2026-10-20

**AI 提示詞（網站複製格式）:**

```text
「資訊面板滑上（Card Info Slide Up）」動態效果：一排直式圖片卡片，平常卡片底部只露出一條標題列；滑鼠滑過時，底部的半透明霧面資訊面板整個滑上來，顯示標題、簡短說明與「查看 →」連結，同時背後的圖片微微上移並放大；滑開時面板滑回只剩標題。約 0.5 秒。（CSS：面板 transform: translateY(calc(100% − 標題列高度))，:hover 時 translateY(0)；面板用半透明底色 + backdrop-filter:blur；圖片 scale 1.08 + translateY）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx286">`, preview text 「海邊 山林 夜空」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「資訊面板滑上」.

### JavaScript — `FX[286]` from `site/fx.js`

```js
286(s,x,card){const ws=words(x);const w=el('div','ho-cg');const its=[0,1,2].map(i=>{const c=el('div','ho-cd');c.innerHTML=mdImg(i)+'<div class="ho-in"><b></b><p>滑過時資訊面板從底部滑上來</p><span>查看 →</span></div>';c.querySelector('b').textContent=ws[i%ws.length];w.append(c);return c});s.append(w);autoHover(w,its,card,1300)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx286` rules from `site/fx.css`

_No dedicated `.fx286` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #286
