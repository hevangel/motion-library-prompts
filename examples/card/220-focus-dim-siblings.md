# 220 · 聚焦淡化其他 — Focus Dim Siblings

滑過某張卡片時它浮起，其他卡片變淡、縮小

- 元件 Component: 卡片・群組 (`card`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動
- 風格／關鍵字 Style: 聚焦 淡化 其他卡片 hover 突顯 Focus Dim Siblings Highlight Spotlight 卡片 群組
- 標籤 Tag: :has()
- 範例文字 Example text: 「入門 進階 大師 團隊」（預覽底色：dark）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「聚焦淡化其他（Focus Dim Siblings）」動態效果：一排卡片，滑鼠移到其中一張時，那張微微上浮並放大到 1.04 倍，其他卡片同時變淡、輕微模糊、降低飽和並縮小到 95%，讓視線集中在目前這張；滑鼠離開整排時全部恢復。約 0.45 秒、減速。（CSS：容器 :hover 時對 .card:not(:hover) 降低 opacity、加 filter:blur(1px) saturate(.6)、scale(.95)；被 hover 的卡片 translateY + scale；可用 :has() 支援鍵盤焦點）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx220">`, preview text 「入門 進階 大師 團隊」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「聚焦淡化其他」.

### JavaScript — `FX[220]` from `site/fx.js`

```js
220(s,x,card){const ws=words(x);const w=el('div','kd-fd');const cs=[...Array(4)].map((_,i)=>{const c=el('div','kd-fc');c.innerHTML='<i></i><b></b><em></em>';c.querySelector('i').style.background=`linear-gradient(140deg,${GC[i%5]},${GC[(i+2)%5]})`;c.querySelector('b').textContent=ws[i%ws.length];w.append(c);return c});s.append(w);autoHover(w,cs,card,1300)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx220` rules from `site/fx.css`

_No dedicated `.fx220` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #220
