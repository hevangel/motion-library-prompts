# 046 · 穿越放大 — Text Zoom Through

衝進字裡，接到下一個詞

- 元件 Component: 文字 (`text`)
- 時機 Timing: 切換
- 技術 Tech: CSS
- 情境 Uses: 轉場切換
- 風格／關鍵字 Style: 文字切換
- 標籤 Tag: 轉場・速度感
- 範例文字 Example text: 「衝進 字裡 下一個」（預覽底色：cream）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「穿越放大（Text Zoom Through）」動態效果：詞彙從小放大到正常尺寸，接著加速放大到填滿畫面並淡出，像鏡頭衝進字裡，下一個詞隨即從遠處出現接上。每個詞約 1.2 秒。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage cream fx46">`, preview text 「衝進 字裡 下一個」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「穿越放大」.

### JavaScript — `FX[46]` from `site/fx.js`

```js
46(s,x,card){const ws=words(x);let i=0;const show=()=>{const e=el('div','zt');e.textContent=ws[i%ws.length];if(i%2)e.style.color='var(--a)';s.append(e);setTimeout(()=>e.remove(),1500);i++};show();card._timers.push(setInterval(show,1150))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx46` rules from `site/fx.css`

```css
.fx46 .zt{position:absolute;font-weight:900;font-size:15cqw;color:#111;animation:zt 1.5s both cubic-bezier(.6,0,.9,.5)}
@keyframes zt{0%{transform:scale(.2);opacity:0}22%{transform:scale(1);opacity:1;animation-timing-function:linear}60%{transform:scale(1.15);opacity:1;animation-timing-function:cubic-bezier(.7,0,1,.6)}100%{transform:scale(16);opacity:0}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #46
