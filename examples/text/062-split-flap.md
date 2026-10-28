# 062 · 翻牌 — Split Flap

像車站時刻表一樣翻到定位

- 元件 Component: 文字 (`text`)
- 時機 Timing: 切換
- 技術 Tech: CSS
- 情境 Uses: 數字資訊
- 風格／關鍵字 Style: 文字切換
- 標籤 Tag: 復古・車站
- 範例文字 Example text: 「準時」（預覽底色：dark）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「翻牌（Split Flap）」動態效果：每個字放在翻牌格內（中間有分隔線），像車站時刻表一樣快速翻過許多隨機字，由左到右依序停在正確的字上，停留後重新翻。翻動很快、全部停定約 1.5 秒。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx62">`, preview text 「準時」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「翻牌」.

### JavaScript — `FX[62]` from `site/fx.js`

```js
62(s,x,card){const tg=chars(x).slice(0,6);const w=el('div','w');const cells=tg.map(()=>{const c=el('div','fl');c.innerHTML='<span></span>';w.append(c);return c});s.append(w);const pool=[...'準時延誤出發抵達東西南北甲乙丙丁一二三四五ABC0123'];let f=0;
  card._timers.push(setInterval(()=>{f=(f+1)%70;cells.forEach((c,i)=>{const stop=12+i*7;if(f<stop){c.firstChild.textContent=pool[Math.floor(Math.random()*pool.length)];c.classList.remove('f');void c.offsetWidth;c.classList.add('f')}else c.firstChild.textContent=tg[i]})},85))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx62` rules from `site/fx.css`

```css
.fx62 .w{display:flex;gap:1.2cqw}
.fx62 .fl{position:relative;width:15cqw;height:18cqw;background:#f4f4f0;color:#111;border-radius:1.2cqw;display:grid;place-items:center;font-weight:900;font-size:12cqw;line-height:1;overflow:hidden}
.fx62 .fl::after{content:"";position:absolute;left:0;right:0;top:50%;height:.3cqw;background:#2b2b2b}
.fx62 .fl.f span{animation:flap .09s}
@keyframes flap{from{transform:rotateX(70deg) scaleY(.6)}to{transform:none}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #62
