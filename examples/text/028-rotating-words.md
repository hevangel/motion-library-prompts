# 028 · 圓環換字 — Rotating Words

在圓環中切換單字

- 元件 Component: 文字 (`text`)
- 時機 Timing: 切換
- 技術 Tech: CSS
- 情境 Uses: 數字資訊、Logo・品牌
- 風格／關鍵字 Style: 文字切換
- 標籤 Tag: 時間・季節
- 範例文字 Example text: 「春夏秋冬」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「圓環換字（Rotating Words）」動態效果：中央圓角方塊內的字依序切換（例：春→夏→秋→冬），每次切換有上下翻轉的動作，周圍有一圈文字環持續慢轉。約 1.3 秒切換一次。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx28">`, preview text 「春夏秋冬」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「圓環換字」.

### JavaScript — `FX[28]` from `site/fx.js`

```js
28(s,x,card){s.append(ringOf('はる・なつ・あき・ふゆ・','17','3.6','cw'));const c=el('div','center');s.append(c);const cs=chars(x);let i=0;const show=()=>{c.textContent=cs[i];c.classList.remove('flip');void c.offsetWidth;c.classList.add('flip');i=(i+1)%cs.length};show();card._timers.push(setInterval(show,1300))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx28` rules from `site/fx.css`

```css
.fx28 .center{position:relative;font-weight:900;font-size:13cqw;background:#fff;color:#111;padding:0 1.5cqw;border-radius:2cqw;line-height:1.2;z-index:2}
.fx28 .center.flip{animation:flp .5s}
@keyframes flp{0%{transform:rotateX(90deg)}100%{transform:none}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #28
