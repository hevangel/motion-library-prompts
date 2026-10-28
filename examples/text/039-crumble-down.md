# 039 · 崩落 — Crumble Down

文字崩塌掉落

- 元件 Component: 文字 (`text`)
- 時機 Timing: 退場
- 技術 Tech: CSS
- 情境 Uses: 轉場切換
- 風格／關鍵字 Style: 消散退場
- 標籤 Tag: 結尾・翻轉
- 範例文字 Example text: 「崩れ落ちる」（預覽底色：cream）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「崩落（Crumble Down）」動態效果：每個字先微微歪斜，接著依序像崩塌一樣受重力加速往下掉並旋轉淡出，之後從上方落回原位重組。約 3.4 秒一輪，結尾感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage cream fx39">`, preview text 「崩れ落ちる」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「崩落」.

### JavaScript — `FX[39]` from `site/fx.js`

```js
39(s,x){const t=split(x);t.querySelectorAll('.c').forEach(c=>{c.style.setProperty('--r0',rnd(-12,12)+'deg');c.style.setProperty('--r',rnd(-90,90)+'deg')});s.append(t)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx39` rules from `site/fx.css`

```css
.fx39 .c{animation:crm 3.4s calc(var(--i)*.16s) infinite}
.fx39 .c:nth-child(even){color:#c08a00}
@keyframes crm{0%,22%{transform:none;opacity:1}27%{transform:rotate(var(--r0))}30%{transform:rotate(var(--r0));animation-timing-function:cubic-bezier(.5,0,1,.5)}62%{transform:translateY(170%) rotate(var(--r));opacity:0}80%{transform:translateY(-50%);opacity:0;animation-timing-function:ease-out}92%,100%{transform:none;opacity:1}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #39
