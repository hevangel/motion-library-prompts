# 266 · 滑過預覽影片 — Hover to Play Video

影片縮圖平常靜止，滑過時播放鍵縮小消失、畫面開始播放、進度條前進

- 元件 Component: 圖片・媒體 (`media`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動
- 風格／關鍵字 Style: 影片 預覽 自動播放 縮圖 播放鍵 YouTube Video Preview Hover Play Thumbnail 圖片 媒體
- 標籤 Tag: CSS hover
- 範例文字 Example text: 「旅行紀錄」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「滑過預覽影片（Hover to Play Video）」動態效果：影片縮圖卡片：平常畫面稍暗、靜止，中間有一個圓形播放鍵，右下角顯示片長；滑鼠滑過時，播放鍵縮小淡出，畫面變亮並開始播放（示意中以緩慢推鏡代替），底部出現一條進度條開始前進；滑開時暫停並回到靜止狀態。（實作：hover 時呼叫 video.play()、離開時 pause() 並把 currentTime 歸零；播放鍵用 scale 與 opacity 過渡；video 設 muted、playsinline 才能自動播放）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx266">`, preview text 「旅行紀錄」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「滑過預覽影片」.

### JavaScript — `FX[266]` from `site/fx.js`

```js
266(s,x,card){const f=el('div','md-vd');f.innerHTML=mdImg(3,'kb')+'<div class="md-pl"><svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg></div><div class="md-vb"><i></i></div><span class="md-du">0:42</span><b class="md-vt"></b>';f.querySelector('.md-vt').textContent=x;s.append(f);autoHover(f,[f],card,2400)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx266` rules from `site/fx.css`

_No dedicated `.fx266` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #266
