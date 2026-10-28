# 187 · 剪貼簿 — Scrapbook

照片、膠帶、貼紙和標題一個個歪歪地貼上來

- 元件 Component: 卡片・群組 (`card`)
- 時機 Timing: 進場
- 技術 Tech: CSS
- 情境 Uses: 標題・Hero、強調重點
- 風格／關鍵字 Style: 剪貼簿 拼貼 手帳 照片 貼紙 膠帶 Scrapbook Collage Sticker Photo Journal Canva 風格 Canva Scrapbook 剪貼簿 簡報 社群貼文 動畫
- 標籤 Tag: CSS keyframes
- 範例文字 Example text: 「我的夏天」（預覽底色：cream）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「剪貼簿（Scrapbook）」動態效果：像手帳拼貼的版面：兩張拍立得照片、一段紙膠帶、一個圓形貼紙和手寫感標題，依序一個個「貼」上來——每個元素從稍大、略高的位置快速落下，帶各自的小角度歪斜，落定時輕微彈一下（約 0.5 秒，間隔約 0.28 秒），停留後一起淡出。溫暖、手作感。（CSS：每個元素用 CSS 變數設定自己的旋轉角度與延遲，keyframes translateY(-30%) scale(1.25) → scale(.95) → 1，保持 rotate(var(--r))）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage cream fx187">`, preview text 「我的夏天」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「剪貼簿」.

### JavaScript — `FX[187]` from `site/fx.js`

```js
187(s,x){const w=el('div','scb');w.innerHTML=`<div class="pc ph1" style="--r:-7deg;--d:0s">${scene('#9fd3ff','#ffe1b0','#4f7a6a','#264a3f','#fff6d8')}</div><div class="pc ph2" style="--r:6deg;--d:.28s">${scene('#ffd9c2','#c9b6ff','#7b6ca8','#3f3566','#fff6e6')}</div><i class="pc tape" style="--r:-14deg;--d:.56s"></i><i class="pc stk" style="--r:8deg;--d:.76s">★</i><b class="pc ttl" style="--r:-3deg;--d:.96s"></b>`;w.querySelector('.ttl').textContent=x;s.append(w)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx187` rules from `site/fx.css`

_No dedicated `.fx187` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #187
