# 061 · 立體字 — Extrude Text

立體字的厚度方向轉一圈

- 元件 Component: 文字 (`text`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: Logo・品牌、標題・Hero
- 風格／關鍵字 Style: 3D 空間旋轉
- 標籤 Tag: 標題
- 範例文字 Example text: 「立體」（預覽底色：dark）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「立體字（Extrude Text）」動態效果：有厚度的 3D 立體字，正面較亮、側面由多層由深到淺的色階堆疊出厚度，整組字以垂直軸緩慢旋轉一整圈，能看到側面厚度。約 5 秒轉一圈。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx61">`, preview text 「立體」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「立體字」.

### JavaScript — `FX[61]` from `site/fx.js`

```js
61(s,x){const e=el('div','ex');for(let i=14;i>=1;i--){const l=T(x,20);l.classList.add('l');l.style.transform=`translateZ(${-i*.45}cqw)`;l.style.color=`hsl(15 60% ${12+i*.6}%)`;e.append(l)}const f=T(x,20);f.style.color='#fff';e.append(f);s.append(e)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx61` rules from `site/fx.css`

```css
.fx61 .ex{position:relative;transform-style:preserve-3d;animation:exr 5s linear infinite}
.fx61 .ex .t{color:var(--a)}
.fx61 .ex .t.l{position:absolute;left:0;top:0}
@keyframes exr{from{transform:rotateX(12deg) rotateY(0)}to{transform:rotateX(12deg) rotateY(360deg)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #61
