# 002 · 雷射切斷 — Laser Cut

雷射把文字一刀兩斷

- 元件 Component: 文字 (`text`)
- 時機 Timing: 退場
- 技術 Tech: CSS
- 情境 Uses: 轉場切換、標題・Hero
- 風格／關鍵字 Style: 消散退場
- 標籤 Tag: SF・切斷
- 範例文字 Example text: 「切断」（預覽底色：acc）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「雷射切斷（Laser Cut）」動態效果：一道帶光暈的雷射線由左往右快速橫切文字中線，切過後文字上半部往左上、下半部往右下錯開並微微傾斜，停留片刻再合回。約 2.6 秒一輪，俐落科幻感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage acc fx2">`, preview text 「切断」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「雷射切斷」.

### JavaScript — `FX[2]` from `site/fx.js`

```js
2(s,x){const w=el('div','w');const a=T(x);a.classList.add('top');const b=T(x);b.classList.add('bot');w.append(a,b,el('div','laser'));s.append(w)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx2` rules from `site/fx.css`

```css
.fx2 .w{position:relative}
.fx2 .top{clip-path:inset(0 0 50% 0);animation:lzT 2.6s infinite}
.fx2 .bot{position:absolute;left:0;top:0;clip-path:inset(50% 0 0 0);animation:lzB 2.6s infinite}
.fx2 .laser{position:absolute;left:-6%;top:50%;height:3px;margin-top:-1.5px;background:#fff;box-shadow:0 0 6px #f22,0 0 16px #f22,0 0 30px #f44;animation:lzL 2.6s infinite;z-index:3}
@keyframes lzB{0%,38%{transform:none}48%,85%{transform:translate(5%,10%) rotate(2deg)}100%{transform:none}}
@keyframes lzL{0%{width:0;opacity:1}35%{width:112%;opacity:1}45%,100%{width:112%;opacity:0}}
@keyframes lzT{0%,38%{transform:none}48%,85%{transform:translate(-5%,-10%) rotate(-3deg)}100%{transform:none}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #2
