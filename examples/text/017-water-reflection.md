# 017 · 水面倒影 — Water Reflection

在水面搖曳的倒影

- 元件 Component: 文字 (`text`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 標題・Hero
- 風格／關鍵字 Style: 質感填色
- 標籤 Tag: 夜景・沉靜
- 範例文字 Example text: 「水面」（預覽底色：dark）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「水面倒影（Water Reflection）」動態效果：文字下方有一條細水平線，線下是上下顛倒的倒影，倒影半透明、往下漸淡，持續左右傾斜搖晃像水波，上方文字也輕微浮動。夜景沉靜感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx17">`, preview text 「水面」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「水面倒影」.

### JavaScript — `FX[17]` from `site/fx.js`

```js
17(s,x){const w=el('div','w');const a=T(x,18);const r=T(x,18);r.classList.add('ref');w.append(a,el('div','line'),r);s.append(w)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx17` rules from `site/fx.css`

```css
.fx17 .w{display:flex;flex-direction:column;align-items:center}
.fx17 .t{color:#fff;animation:bob 3s ease-in-out infinite}
.fx17 .line{width:70cqw;height:1px;background:linear-gradient(90deg,transparent,#fff8,transparent)}
.fx17 .ref{transform:scaleY(-1);opacity:.45;color:var(--a);-webkit-mask:linear-gradient(transparent 20%,#000);mask:linear-gradient(transparent 20%,#000);animation:rip 2.2s ease-in-out infinite;filter:blur(.6px)}
@keyframes bob{0%,100%{transform:none}50%{transform:translateY(-3%)}}
@keyframes rip{0%,100%{transform:scaleY(-1) skewX(0)}25%{transform:scaleY(-.92) skewX(7deg) translateX(1%)}75%{transform:scaleY(-1.04) skewX(-7deg) translateX(-1%)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #17
