# 041 · 文字爆開 — Word Burst

單字咚一聲彈出來

- 元件 Component: 文字 (`text`)
- 時機 Timing: 進場
- 技術 Tech: CSS
- 情境 Uses: 強調重點
- 風格／關鍵字 Style: 衝擊登場 Canva 風格 Canva Pop 跳出
- 標籤 Tag: 強調・亮點
- 範例文字 Example text: 「衝擊」（預覽底色：dark）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「文字爆開（Word Burst）」動態效果：文字從 0 迅速彈出放大到 1.25 倍再回到原尺寸，同時從中心放射出一圈短線條往外飛散消失。約 1.8 秒一輪，強調亮點。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx41">`, preview text 「衝擊」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「文字爆開」.

### JavaScript — `FX[41]` from `site/fx.js`

```js
41(s,x){const r=el('div','rays');for(let i=0;i<14;i++){const e=el('i');e.style.setProperty('--r',i*360/14+'deg');r.append(e)}s.append(r,T(x,Math.min(20,74/chars(x).length)))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx41` rules from `site/fx.css`

```css
.fx41 .t{color:var(--a);animation:burst 1.8s infinite cubic-bezier(.2,1.6,.4,1)}
.fx41 .rays{position:absolute;left:50%;top:50%}
.fx41 .rays i{position:absolute;left:-.4cqw;top:0;width:.8cqw;height:6cqw;background:var(--a);transform-origin:50% 0;opacity:0;animation:ray 1.8s infinite}
@keyframes burst{0%{transform:scale(0);opacity:0}25%{transform:scale(1.25);opacity:1}35%,85%{transform:scale(1);opacity:1}100%{transform:scale(1);opacity:0}}
@keyframes ray{0%,12%{opacity:0;transform:rotate(var(--r)) translateY(9cqw) scaleY(.2)}24%{opacity:1;transform:rotate(var(--r)) translateY(14cqw) scaleY(1)}45%,100%{opacity:0;transform:rotate(var(--r)) translateY(24cqw) scaleY(.3)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #41
