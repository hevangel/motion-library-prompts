# 290 · 連結預覽卡 — Link Preview Popover

滑過文章中的連結時，上方彈出一張小卡，預覽連結頁面的圖片與標題

- 元件 Component: 文字 (`text`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動
- 風格／關鍵字 Style: 連結 預覽 彈出 小卡 popover tooltip 超連結 Link Preview Hover Card Wiki hover 懸停 滑過
- 標籤 Tag: :has()
- 範例文字 Example text: 「Hannah」（預覽底色：dark）
- 收錄日期 Added: 2026-10-20

**AI 提示詞（網站複製格式）:**

```text
「連結預覽卡（Link Preview Popover）」動態效果：文章段落中的一個帶底線的連結：滑鼠滑過（或鍵盤聚焦）時，連結正上方以小彈性彈出一張預覽小卡，卡片內有連結頁面的縮圖、標題與網址，從略小、略低、透明的狀態放大上移出現；滑開時縮回淡出。適合部落格、維基或作品集的外部連結。（CSS：預覽卡絕對定位在連結上方 transform-origin 底部中央，scale .9 + translateY → none，transition 用 cubic-bezier(.3,1.4,.5,1)；用 :has(a:hover) 或 :focus-within 觸發）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx290">`, preview text 「Hannah」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「連結預覽卡」.

### JavaScript — `FX[290]` from `site/fx.js`

```js
290(s,x,card){const p=el('p','ho-lp');p.innerHTML='推薦你看看 <a class="ho-a" href="https://hannahchao-portfolio.vercel.app/" target="_blank" rel="noopener"></a> 的作品，<br>每一件都很細緻。<span class="ho-pv">'+mdImg(3)+'<b></b><small>hannahchao-portfolio.vercel.app</small></span>';p.querySelector('.ho-a').textContent=x;p.querySelector('.ho-pv b').textContent=x+' 作品集';s.append(p);autoHover(p,[p.querySelector('.ho-a')],card,1700)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx290` rules from `site/fx.css`

_No dedicated `.fx290` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #290
