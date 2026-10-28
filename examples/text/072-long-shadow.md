# 072 · 長陰影 — Long Shadow

長長的影子轉一圈

- 元件 Component: 文字 (`text`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: Logo・品牌
- 風格／關鍵字 Style: 質感填色
- 標籤 Tag: 扁平風
- 範例文字 Example text: 「光與影」（預覽底色：dark）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「長陰影（Long Shadow）」動態效果：文字後方拖著一條很長的扁平陰影，陰影方向持續繞著文字旋轉一整圈。約 7 秒轉一圈，扁平設計風。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx72">`, preview text 「光與影」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「長陰影」.

### JavaScript — `FX[72]` from `site/fx.js`

```js
72(s,x,card){const t=T(x);s.append(t);ticks.set(card,tt=>{const a=tt*.9;const fs=parseFloat(getComputedStyle(t).fontSize)||40;const st=fs/40;let sh=[];for(let k=1;k<=34;k++)sh.push(`${(Math.cos(a)*k*st).toFixed(1)}px ${(Math.sin(a)*k*st).toFixed(1)}px 0 ${k<3?'#f47fae':'#c4527f'}`);t.style.textShadow=sh.join(',')})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx72` rules from `site/fx.css`

```css
.fx72 .t{color:#fff}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #72
