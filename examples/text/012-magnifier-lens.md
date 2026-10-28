# 012 · 放大鏡 — Magnifier Lens

用放大鏡放大文字

- 元件 Component: 文字 (`text`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 強調重點
- 風格／關鍵字 Style: 質感填色
- 標籤 Tag: 解說・發現
- 範例文字 Example text: 「虫眼鏡で拡大」（預覽底色：dark）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「放大鏡（Magnifier Lens）」動態效果：一個圓形放大鏡在文字上左右來回移動，鏡片範圍內的文字放大約 1.5 倍並改用強調色，鏡片外的文字較淡，放大鏡附手把。來回約 6 秒，解說／發現感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx12">`, preview text 「虫眼鏡で拡大」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「放大鏡」.

### JavaScript — `FX[12]` from `site/fx.js`

```js
12(s,x,card){const w=el('div','w');const b=T(x);b.classList.add('base');const o=T(x);o.classList.add('ov');const l=el('div','lens');w.append(b,o,l);s.append(w);
  ticks.set(card,t=>{const W=w.offsetWidth,H=w.offsetHeight;if(!W)return;const px=W*(.5+.42*Math.sin(t*1.1));const r=H*.62;o.style.transformOrigin=`${px}px 50%`;o.style.transform='scale(1.55)';o.style.clipPath=`circle(${r}px at ${px}px 50%)`;l.style.left=px+'px';l.style.width=l.style.height=(r*2*1.55)+'px'})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx12` rules from `site/fx.css`

```css
.fx12 .w{position:relative}
.fx12 .base{color:#666}
.fx12 .ov{position:absolute;left:0;top:0;color:var(--a);text-shadow:0 0 1px #fff}
.fx12 .lens{position:absolute;top:50%;border:.7cqw solid #fff;border-radius:50%;transform:translate(-50%,-50%);box-shadow:0 0 0 2px #0003,inset 0 0 12px #fff4;pointer-events:none}
.fx12 .lens::after{content:"";position:absolute;width:.9cqw;height:7cqw;background:#fff;border-radius:4px;right:-3.3cqw;bottom:-6.2cqw;transform:rotate(-45deg)}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #12
