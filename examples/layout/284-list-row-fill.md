# 284 · 清單列滑入填滿 — List Row Fill

滑過清單某一列時，底色從左邊刷進來，文字往右讓位、箭頭滑出

- 元件 Component: 版面・頁面 (`layout`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動
- 風格／關鍵字 Style: 清單 列表 服務項目 選單 底色 填滿 箭頭 List Row Hover Fill Sweep Arrow Services Menu hover 懸停 滑過
- 標籤 Tag: CSS hover
- 範例文字 Example text: 「品牌識別 網站設計 動態影像 包裝設計」（預覽底色：dark）
- 收錄日期 Added: 2026-10-20

**AI 提示詞（網站複製格式）:**

```text
「清單列滑入填滿（List Row Fill）」動態效果：一份服務項目清單，每列有編號、項目名稱、右側箭頭，列與列之間有細分隔線：滑鼠滑過某一列時，一塊實心底色從左邊刷進來填滿整列，項目名稱往右移一點讓位，右側箭頭從左邊滑入出現，文字顏色反轉以保持可讀；滑開時底色往右收走。約 0.5 秒。（CSS：每列內一個絕對定位的底色層 transform:scaleX(0)，hover 時 scaleX(1) 且 transform-origin 從 left；離開時 transform-origin 改成 right，形成「左進右出」）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx284">`, preview text 「品牌識別 網站設計 動態影像 包裝設計」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「清單列滑入填滿」.

### JavaScript — `FX[284]` from `site/fx.js`

```js
284(s,x,card){const ws=words(x).slice(0,4);const w=el('ul','ho-rw');const its=ws.map((t,i)=>{const li=el('li');li.innerHTML='<i></i><em>0'+(i+1)+'</em><b></b><svg viewBox="0 0 24 24"><path d="M5 12h13M13 6l6 6-6 6"/></svg>';li.querySelector('b').textContent=t;w.append(li);return li});s.append(w);autoHover(w,its,card,1000)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx284` rules from `site/fx.css`

_No dedicated `.fx284` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #284
