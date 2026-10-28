# 069 · 空心字 — Outline Text

空心字一行一行被填滿

- 元件 Component: 背景・氛圍 (`bg`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 背景裝飾
- 風格／關鍵字 Style: 流動背景
- 標籤 Tag: 質感・MV
- 範例文字 Example text: 「疾風怒濤」（預覽底色：dark）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「空心字（Outline Text）」動態效果：畫面鋪滿多行重複的空心描邊文字，每行往不同方向緩慢橫移，並由上到下一行一行填滿顏色再退回空心。約 3.2 秒一輪，質感 MV。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx69">`, preview text 「疾風怒濤」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「空心字」.

### JavaScript — `FX[69]` from `site/fx.js`

```js
69(s,x){const r=el('div','rows');for(let i=0;i<5;i++){const m=mqRow(rep(x+'・',6),11,10+i*2,i%2);m.className+=' row';m.style.setProperty('--i',i);r.append(m)}s.append(r)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx69` rules from `site/fx.css`

```css
.fx69 .rows{position:absolute;inset:-4% 0;display:flex;flex-direction:column;justify-content:space-between}
.fx69 .row{font-weight:900;font-size:11cqw;line-height:1.05;-webkit-text-stroke:.25cqw var(--a);color:transparent;animation:ofill 3.2s calc(var(--i)*.35s) infinite}
@keyframes ofill{0%,8%{color:transparent}18%,60%{color:var(--a)}72%,100%{color:transparent}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #69
