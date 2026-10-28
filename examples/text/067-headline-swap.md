# 067 · 標題切換 — Headline Swap

新聞標題一個換一個

- 元件 Component: 文字 (`text`)
- 時機 Timing: 切換
- 技術 Tech: CSS
- 情境 Uses: 數字資訊、轉場切換
- 風格／關鍵字 Style: 文字切換
- 標籤 Tag: 快訊・解說
- 範例文字 Example text: 「全面免費 今晚上線 限時三天」（預覽底色：acc）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「標題切換（Headline Swap）」動態效果：左側「快訊」標籤固定，右側框內的新聞標題由下往上滑入，舊標題往上滑出，一則換一則。約 1.6 秒換一則。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage acc fx67">`, preview text 「全面免費 今晚上線 限時三天」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「標題切換」.

### JavaScript — `FX[67]` from `site/fx.js`

```js
67(s,x,card){const w=el('div','w');w.innerHTML='<div class="lab">快訊</div>';const box=el('div','box');w.append(box);s.append(w);const ws=words(x);let i=0;const show=()=>{box.querySelector('.hl:not(.out)')?.classList.add('out');const h=el('div','hl');h.textContent=ws[i++%ws.length];box.append(h);setTimeout(()=>{box.querySelectorAll('.out').forEach(o=>o.remove())},500)};show();card._timers.push(setInterval(show,1600))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx67` rules from `site/fx.css`

```css
.fx67 .w{display:flex;align-items:stretch;width:84%;height:22cqw}
.fx67 .lab{background:#fff;color:#111;font-weight:900;font-size:8cqw;display:grid;place-items:center;padding:0 3cqw}
.fx67 .box{flex:1;background:#2b2b2b;position:relative;overflow:hidden}
.fx67 .hl{position:absolute;inset:0;display:flex;align-items:center;padding-left:3cqw;font-weight:900;font-size:8.5cqw;color:var(--a);animation:hl .55s both cubic-bezier(.2,.9,.3,1)}
.fx67 .hl.out{animation:hlo .4s both}
@keyframes hl{from{transform:translateY(100%)}to{transform:none}}
@keyframes hlo{to{transform:translateY(-100%)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #67
