# 063 · 翻卡 — Flip Cards

一張張翻面換字

- 元件 Component: 文字 (`text`)
- 時機 Timing: 切換
- 技術 Tech: CSS
- 情境 Uses: 轉場切換
- 風格／關鍵字 Style: 文字切換
- 標籤 Tag: 切換・公告
- 範例文字 Example text: 「夜未眠」（預覽底色：acc）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「翻卡（Flip Cards）」動態效果：每個字是一張卡片，依序以 Y 軸翻面，正反兩面用對比的配色，翻成另一組字後停留，再翻回來。約 3.4 秒一輪，切換公告感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage acc fx63">`, preview text 「夜未眠」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「翻卡」.

### JavaScript — `FX[63]` from `site/fx.js`

```js
63(s,x){const w=el('div','w');const a=chars(x).slice(0,4);const b=x==='夜未眠'?[...'月光下']:[...a].reverse();a.forEach((c,i)=>{const d=el('div','cd');d.style.setProperty('--i',i);d.innerHTML=`<b>${c}</b><b>${b[i]}</b>`;w.append(d)});s.append(w)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx63` rules from `site/fx.css`

```css
.fx63 .w{display:flex;gap:2cqw}
.fx63 .cd{width:16cqw;height:19cqw;position:relative;transform-style:preserve-3d;animation:fc 3.4s calc(var(--i)*.16s) infinite}
.fx63 .cd b{position:absolute;inset:0;display:grid;place-items:center;font-weight:900;font-size:12cqw;background:#fff;color:#111;border-radius:1.4cqw;backface-visibility:hidden;box-shadow:0 .6cqw 1.4cqw #0003}
.fx63 .cd b+b{transform:rotateY(180deg);background:#111;color:var(--a)}
@keyframes fc{0%,25%{transform:rotateY(0)}42%,75%{transform:rotateY(180deg)}92%,100%{transform:rotateY(360deg)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #63
