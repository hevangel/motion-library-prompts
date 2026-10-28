# 043 · 印章 — Text Stamp

像蓋章一樣一個個蓋上去

- 元件 Component: 文字 (`text`)
- 時機 Timing: 進場
- 技術 Tech: CSS
- 情境 Uses: 強調重點
- 風格／關鍵字 Style: 衝擊登場 Canva 風格 Canva Stomp 重擊
- 標籤 Tag: 公告・決定
- 範例文字 Example text: 「確定」（預覽底色：cream）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「印章（Text Stamp）」動態效果：兩個帶粗框的印章字樣，從 2.4 倍大斜斜地「啪」一聲蓋上去，略微回縮後停住，印面帶一點斑駁質感，兩枚依序蓋下。約 2.8 秒一輪。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage cream fx43">`, preview text 「確定」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「印章」.

### JavaScript — `FX[43]` from `site/fx.js`

```js
43(s,x){[[x,'-9deg','18%','24%','0s'],['核准','7deg','55%','46%','.55s']].forEach(([w,r,l,t,d])=>{const e=el('div','st');e.textContent=w;e.style.cssText+=`;left:${l};top:${t};--r:${r};--d:${d}`;s.append(e)})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx43` rules from `site/fx.css`

```css
.fx43 .st{position:absolute;font-weight:900;color:var(--a);border:.7cqw solid var(--a);border-radius:1.4cqw;padding:.4cqw 2.4cqw;font-size:8cqw;animation:stamp 2.8s var(--d) infinite both;-webkit-mask:repeating-radial-gradient(circle at 30% 40%,#000 0 3px,#000c 3px 4px)}
@keyframes stamp{0%{opacity:0;transform:rotate(var(--r)) scale(2.4)}9%{opacity:1;transform:rotate(var(--r)) scale(.93)}13%,82%{opacity:1;transform:rotate(var(--r)) scale(1)}95%,100%{opacity:0;transform:rotate(var(--r))}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #43
