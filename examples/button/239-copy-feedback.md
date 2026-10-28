# 239 · 複製成功回饋 — Copy Feedback

按下複製後圖示旋轉變成打勾，上方彈出「已複製」小提示

- 元件 Component: 按鈕 (`button`)
- 時機 Timing: 切換
- 技術 Tech: CSS
- 情境 Uses: 介面互動、App 介面
- 風格／關鍵字 Style: 複製 剪貼簿 打勾 提示 tooltip 回饋 Copy To Clipboard Feedback Check Code 按鈕
- 標籤 Tag: CSS transition
- 範例文字 Example text: 「npm i gsap」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「複製成功回饋（Copy Feedback）」動態效果：一行程式碼（或文字）旁邊的複製按鈕：按下後，複製圖示旋轉縮小消失，打勾圖示帶彈性放大出現，按鈕底色變成強調色；同時按鈕上方彈出一個「已複製」的小提示框，約 1.5 秒後全部恢復原狀。（CSS：兩個 SVG 圖示疊在同一格，用 class 切換 transform 與 opacity，transition 用帶回彈的 cubic-bezier(.3,1.5,.5,1)；提示框用絕對定位在按鈕上方；JS 呼叫 navigator.clipboard.writeText 後加 class、setTimeout 移除）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx239">`, preview text 「npm i gsap」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「複製成功回饋」.

### JavaScript — `FX[239]` from `site/fx.js`

```js
239(s,x,card){const w=el('div','bx-cpw');w.innerHTML='<code></code><button class="bx-cp" aria-label="複製"><svg class="i1" viewBox="0 0 24 24"><rect x="8" y="8" width="12" height="12" rx="2"/><path d="M16 8V5a1 1 0 0 0-1-1H5a1 1 0 0 0-1 1v10a1 1 0 0 0 1 1h3"/></svg><svg class="i2" viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7"/></svg><em>已複製</em></button>';w.querySelector('code').textContent=x;w.style.fontSize=Math.min(4,34/chars(x).length)+'cqw';s.append(w);const b=w.querySelector('button');let tm;
  const go=()=>{b.classList.add('ok');clearTimeout(tm);tm=setTimeout(()=>b.classList.remove('ok'),1500)};b.addEventListener('click',go);card._kill.push(()=>clearTimeout(tm));bxDemo(b,card,go,2800)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx239` rules from `site/fx.css`

_No dedicated `.fx239` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #239
