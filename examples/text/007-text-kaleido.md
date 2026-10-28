# 007 · 文字萬花筒 — Text Kaleido

文字萬花筒旋轉

- 元件 Component: 文字 (`text`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 背景裝飾、Logo・品牌
- 風格／關鍵字 Style: 3D 空間旋轉
- 標籤 Tag: 迷幻・MV
- 範例文字 Example text: 「万華鏡」（預覽底色：cream）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「文字萬花筒（Text Kaleido）」動態效果：同一個詞複製 12 份，以中心點放射狀排列成花朵形，整體持續慢速旋轉，每份文字同時往外伸縮呼吸，形成萬花筒效果，相鄰的複本用深淺兩種色調交錯。旋轉一圈約 7 秒。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage cream fx7">`, preview text 「万華鏡」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「文字萬花筒」.

### JavaScript — `FX[7]` from `site/fx.js`

```js
7(s,x){const k=el('div','k');for(let i=0;i<12;i++){const sp=el('span');sp.innerHTML=`<span class="in">${x}</span>`;sp.style.transform=`rotate(${i*30}deg) translateY(-50%)`;k.append(sp)}s.append(k)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx7` rules from `site/fx.css`

```css
.fx7 .k{position:relative;width:1px;height:1px;animation:spin 7s linear infinite}
.fx7 .k span{position:absolute;left:0;top:0;font-weight:900;font-size:6cqw;transform-origin:0 0;white-space:nowrap;color:#2a3a12}
.fx7 .k span:nth-child(odd){color:#7a9a1c}
.fx7 .k .in{display:inline-block;animation:kpulse 2.4s ease-in-out infinite}
@keyframes kpulse{0%,100%{transform:translateX(2cqw)}50%{transform:translateX(8cqw)}}
@keyframes spin{to{transform:rotate(360deg)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #7
