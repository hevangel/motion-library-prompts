# 214 · 疊卡散開 — Stack Fan Out

一疊微歪的卡片，滑過時向兩側散開成一排

- 元件 Component: 卡片・群組 (`card`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動、標題・Hero
- 風格／關鍵字 Style: 疊卡 散開 扇形 展開 作品集 Stack Spread Fan Cards Hover 卡片 群組
- 標籤 Tag: CSS hover
- 範例文字 Example text: 「企劃 設計 開發 測試 上線」（預覽底色：dark）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「疊卡散開（Stack Fan Out）」動態效果：五張卡片疊成一疊，每張略微不同角度歪斜；滑鼠移到這疊卡片上時，卡片以中間那張為軸向左右兩側散開成扇形一排（越外側角度越大、略往下垂），帶一點彈性回彈；滑鼠離開時收回成一疊。約 0.6 秒。（CSS：每張用 CSS 變數 --i（-2 到 2）計算 translateX、rotate、translateY，hover 時改用較大的係數，transition cubic-bezier(.3,1.3,.5,1)）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx214">`, preview text 「企劃 設計 開發 測試 上線」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「疊卡散開」.

### JavaScript — `FX[214]` from `site/fx.js`

```js
214(s,x,card){const ws=words(x);const w=el('div','kd-st');const cs=[...Array(5)].map((_,i)=>{const c=el('div','kd-sk');c.style.setProperty('--i',i-2);c.style.background=`linear-gradient(160deg,${GC[i%5]},${GC[(i+2)%5]})`;c.innerHTML='<b></b>';c.querySelector('b').textContent=ws[i%ws.length];w.append(c);return c});s.append(w);autoHover(w,[w],card,1500)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx214` rules from `site/fx.css`

_No dedicated `.fx214` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #214
