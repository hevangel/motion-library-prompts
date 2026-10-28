# 008 · 倒數砸落 — Number Slam

倒數數字重重砸下

- 元件 Component: 文字 (`text`)
- 時機 Timing: 進場
- 技術 Tech: CSS
- 情境 Uses: 數字資訊、標題・Hero
- 風格／關鍵字 Style: 衝擊登場
- 標籤 Tag: 開場・倒數
- 範例文字 Example text: 「3,2,1,GO!」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「倒數砸落（Number Slam）」動態效果：倒數「3、2、1、GO!」依序出現，每個數字從 3 倍大猛力砸下、回彈到原尺寸，每個數字約 0.75 秒，GO! 用強調色凸顯。粗黑體，開場感強烈。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx8">`, preview text 「3,2,1,GO!」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「倒數砸落」.

### JavaScript — `FX[8]` from `site/fx.js`

```js
8(s,x,card){const seq=['3','2','1','GO!'];let i=0;const show=()=>{s.querySelector('.n')?.remove();const n=el('div','n'+(seq[i]==='GO!'?' go':''),seq[i]);s.append(n);i=(i+1)%seq.length};show();card._timers.push(setInterval(show,750))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx8` rules from `site/fx.css`

```css
.fx8 .n{font-weight:900;font-size:24cqw;line-height:1;animation:slam .7s both cubic-bezier(.2,1.4,.4,1)}
.fx8 .n.go{color:var(--a)}
@keyframes slam{0%{transform:scale(3);opacity:0}35%{transform:scale(.9);opacity:1}55%{transform:scale(1.05)}100%{transform:scale(1)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #8
