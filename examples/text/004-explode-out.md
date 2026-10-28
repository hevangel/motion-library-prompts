# 004 · 爆炸四散 — Explode Out

文字向四面八方炸飛

- 元件 Component: 文字 (`text`)
- 時機 Timing: 退場
- 技術 Tech: CSS
- 情境 Uses: 轉場切換、強調重點
- 風格／關鍵字 Style: 消散退場
- 標籤 Tag: 衝擊・副歌
- 範例文字 Example text: 「爆発四散」（預覽底色：dark）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「爆炸四散（Explode Out）」動態效果：文字先微微放大蓄力，接著每個字往不同方向隨機炸飛、旋轉並縮小淡出，停頓後再飛回原位組成文字，字與字可用主色與強調色交錯。約 2.8 秒一輪，衝擊感強。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx4">`, preview text 「爆発四散」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「爆炸四散」.

### JavaScript — `FX[4]` from `site/fx.js`

```js
4(s,x){const t=split(x);t.querySelectorAll('.c').forEach(c=>{c.style.setProperty('--dx',rnd(-40,40)+'cqw');c.style.setProperty('--dy',rnd(-30,30)+'cqw');c.style.setProperty('--r',rnd(-200,200)+'deg')});s.append(t)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx4` rules from `site/fx.css`

```css
.fx4 .c{animation:exp 2.8s calc(var(--i)*.03s) infinite cubic-bezier(.2,.7,.3,1)}
.fx4 .c:nth-child(even){color:var(--a)}
@keyframes exp{0%,22%{transform:none;opacity:1}26%{transform:scale(1.15)}50%,72%{transform:translate(var(--dx),var(--dy)) rotate(var(--r)) scale(.5);opacity:0}90%,100%{transform:none;opacity:1}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #4
