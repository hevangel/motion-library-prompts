# 053 · 直書三層 — Parallax Columns

三層直排文字一起流動

- 元件 Component: 背景・氛圍 (`bg`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 背景裝飾
- 風格／關鍵字 Style: 流動背景
- 標籤 Tag: 夜・東方
- 範例文字 Example text: 「雨街燈夜」（預覽底色：cream）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「直書三層（Parallax Columns）」動態效果：三層直排文字直向流動：最後層字小、很淡、速度快；中間層半透明、中速；最前層字大、不透明、速度慢，形成景深視差，明體字。夜晚東方感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage cream fx53">`, preview text 「雨街燈夜」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「直書三層」.

### JavaScript — `FX[53]` from `site/fx.js`

```js
53(s,x){[[9,'#0001',6,5],[6,'#0004',10,8],[3,'#111',16,13]].forEach(([n,c,d,f])=>{const l=el('div','lay');for(let i=0;i<n;i++){const e=el('div','col');e.innerHTML=chars(rep(x,6)).join('<br>');e.style.cssText+=`;color:${c};font-size:${f}cqw;--dur:${d+i%3}s`;if(i%2)e.style.animationDirection='reverse';l.append(e)}s.append(l)})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx53` rules from `site/fx.css`

```css
.fx53 .lay{position:absolute;inset:0;display:flex;justify-content:space-around;overflow:hidden}
.fx53 .col{align-self:flex-start;text-align:center;font-family:"Noto Serif JP",serif;font-weight:900;line-height:1;animation:mqv var(--dur) linear infinite}
@keyframes mqv{to{transform:translateY(-50%)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #53
