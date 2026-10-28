# 163 · 空心字填滿 — Outline Text Fill

滑過空心大字時，從左到右被填滿成實心

- 元件 Component: 文字 (`text`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 標題・Hero、介面互動
- 風格／關鍵字 Style: 空心字 描邊 填滿 大標 outline stroke text fill hover hover 懸停 滑鼠移入 滑過 互動
- 標籤 Tag: background-clip
- 範例文字 Example text: 「DESIGN MOTION PLAY」（預覽底色：dark）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「空心字填滿（Outline Text Fill）」動態效果：幾行超大字級的空心描邊文字，滑鼠移到某一行時，那一行從左到右被填滿成實心（像墨水灌進去），移開時再從右往左退回空心；約 0.6 秒、緩入緩出，適合作品集標題或選單。（CSS：文字 -webkit-text-stroke 描邊、color:transparent；背景用單色 linear-gradient，background-clip:text，hover 時 background-size 0%→100% 加 transition）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx163">`, preview text 「DESIGN MOTION PLAY」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「空心字填滿」.

### JavaScript — `FX[163]` from `site/fx.js`

```js
163(s,x,card){const w=el('div','ofw');const its=words(x).slice(0,3).map(v=>{const d=el('div','ofl');d.textContent=v;w.append(d);return d});w.style.fontSize=Math.min(12,64/Math.max(...words(x).slice(0,3).map(v=>chars(v).length)))+'cqw';s.append(w);autoHover(w,its,card,1100)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx163` rules from `site/fx.css`

_No dedicated `.fx163` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #163
