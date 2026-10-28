# 217 · 無限捲動卡片牆 — Infinite Card Wall

兩排卡片朝相反方向無限移動，滑鼠移上去就暫停

- 元件 Component: 卡片・群組 (`card`)
- 時機 Timing: 循環待機、懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 背景裝飾、數字資訊
- 風格／關鍵字 Style: 跑馬燈 卡片牆 評價 客戶 Logo 牆 無限 Infinite Marquee Testimonials Logo Wall 卡片 群組
- 標籤 Tag: CSS marquee
- 範例文字 Example text: 「設計師 工程師 行銷 創辦人」（預覽底色：dark）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「無限捲動卡片牆（Infinite Card Wall）」動態效果：兩排評價或客戶卡片橫向無限循環移動，上排往左、下排往右，速度緩慢穩定；滑鼠移到卡片牆上時兩排都暫停，方便閱讀，移開後繼續。適合客戶評價、合作夥伴 Logo 牆。（CSS：每排內容複製兩份放在同一條軌道，keyframes translateX(0 → -50%) linear infinite 達成無縫循環，反向那排用 animation-direction:reverse；:hover 時 animation-play-state:paused）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx217">`, preview text 「設計師 工程師 行銷 創辦人」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「無限捲動卡片牆」.

### JavaScript — `FX[217]` from `site/fx.js`

```js
217(s,x){const ws=words(x);const w=el('div','kd-wall');for(let r=0;r<2;r++){const row=el('div','kd-row'+(r?' kd-rv':''));const tr=el('div','kd-tr');const mk=()=>ws.map((v,i)=>{const c=el('div','kd-wc');c.innerHTML='<i></i><span><b></b><em></em><em class="s"></em></span>';c.querySelector('i').style.background=GC[(i+r*2)%5];c.querySelector('b').textContent=v;return c});[...mk(),...mk()].forEach(c=>tr.append(c));row.append(tr);w.append(row)}s.append(w)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx217` rules from `site/fx.css`

_No dedicated `.fx217` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #217
