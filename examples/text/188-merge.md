# 188 · 合併 — Merge

文字上下兩半分別從左右滑入，合成完整的字

- 元件 Component: 文字 (`text`)
- 時機 Timing: 進場
- 技術 Tech: CSS
- 情境 Uses: 標題・Hero、轉場切換
- 風格／關鍵字 Style: 合併 拼合 上下 切半 左右 滑入 Merge Split Halves Join Canva 風格 Canva Merge 合併 簡報 社群貼文 動畫
- 標籤 Tag: clip-path
- 範例文字 Example text: 「合而為一」（預覽底色：dark）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「合併（Merge）」動態效果：標題被水平切成上下兩半：上半部從左側、下半部從右側同時滑入並淡入，在中間精準對齊合成完整的文字（約 0.9 秒、強烈減速），停留後淡出。（CSS：同一段文字放兩份，分別用 clip-path:inset(0 0 50% 0) 與 inset(50% 0 0 0) 只顯示上半與下半，各自用 translateX(∓35%) → 0 的 keyframes）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx188">`, preview text 「合而為一」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「合併」.

### JavaScript — `FX[188]` from `site/fx.js`

```js
188(s,x){const w=el('div','mg');const sz=Math.min(13,60/chars(x).length);const a=T(x,sz),b=T(x,sz);a.classList.add('a');b.classList.add('b');w.append(a,b);s.append(w)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx188` rules from `site/fx.css`

_No dedicated `.fx188` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #188
